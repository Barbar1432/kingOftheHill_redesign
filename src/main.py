# Initialize Pygame
import random
import sys
import pygame
import webbrowser
from board import Board
from visuals import BoardVisuals
from animations import Animation
from tests import FENtoBoard
import multiprocessing as mp
import numpy as np
import time
SCREEN_WIDTH = 480 * 2
SCREEN_HEIGHT = 480
SQUARE_SIZE = 60
DARK_GREEN = (79, 121, 66)
LIGHT_GREEN = (158, 194, 133)
FOG_GREY = (101, 89, 103)
BOARD_DISLOCATION_WIDTH = 120
BOARD_DISLOCATION_HEIGHT = 120
BORDER_BROWN_LIGHT = (164, 144, 124)
BORDER_BROWN_LIGHT_2 = (183, 159, 135)
BORDER_BROWN_DARK = (141, 123, 104)
color_green = (204, 212, 179)
DARK_GREY = (90, 90, 90)


def game_process(queue_game, queue_bot, queue_anim, queue_text, queue_textbool, queue_timer, queue_timertext):
    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Recommended Settings
    game_algorithm = "alphabeta"
    timer_count = "20"
    botchat_bool = "active"

    # Set up the start menu
    ui_handler = BoardVisuals()
    ui_handler.set_caption("King of the Hill")
    ui_handler.screen.fill((202, 206, 187))
    running = True
    while running:
        # Print the menu buttons
        if ui_handler.menu_status == "menu":
            ui_handler.draw_start_menu()
            ui_handler.draw_button_text("menu")
        elif ui_handler.menu_status == "settings":
            ui_handler.draw_settings_menu()
            ui_handler.draw_button_text("settings")
            ui_handler.draw_button_png("settings")
        elif ui_handler.menu_status == "about":
            ui_handler.draw_about_menu()
            ui_handler.draw_button_text("about")
        # Check for clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Signal other processors to quit
                queue_bot.put("quit")
                queue_anim.put("quit")
                queue_timer.put("quit")
                # Quit pygame
                pygame.quit()
                sys.exit()
            # If clicked on the buttons...
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Currently on the main menu
                if ui_handler.menu_status == "menu":
                    if ui_handler.start_button.collidepoint(mouse_pos):  # Start button clicked
                        running = False
                    elif ui_handler.setting_button.collidepoint(mouse_pos):  # Settings button clicked
                        ui_handler.menu_status = "settings"
                    elif ui_handler.about_button.collidepoint(mouse_pos):  # About button clicked
                        ui_handler.menu_status = "about"
                    elif ui_handler.quit_button.collidepoint(mouse_pos):  # Quit button clicked
                        queue_bot.put("quit")
                        queue_anim.put("quit")
                        queue_timer.put("quit")
                        # Quit pygame
                        pygame.quit()
                        sys.exit()
                # Currently on the settings menu
                elif ui_handler.menu_status == "settings":
                    if ui_handler.back_button.collidepoint(mouse_pos):
                        ui_handler.menu_status = "menu"
                    elif ui_handler.white_button.collidepoint(mouse_pos):
                        ui_handler.color_selected = 0
                    elif ui_handler.black_button.collidepoint(mouse_pos):
                        ui_handler.color_selected = 1
                    elif ui_handler.button_20.collidepoint(mouse_pos):
                        ui_handler.time_selected = 0
                        timer_count = "20"
                    elif ui_handler.button_30.collidepoint(mouse_pos):
                        ui_handler.time_selected = 1
                        timer_count = "30"
                    elif ui_handler.button_40.collidepoint(mouse_pos):
                        ui_handler.time_selected = 2
                        timer_count = "40"
                    elif ui_handler.button_alphabeta.collidepoint(mouse_pos):
                        ui_handler.algo_selected = 0
                        game_algorithm = "alphabeta"
                    elif ui_handler.button_montecarlo.collidepoint(mouse_pos):
                        ui_handler.algo_selected = 1
                        game_algorithm = "montecarlo"
                    elif ui_handler.button_bot_speak_on.collidepoint(mouse_pos):
                        ui_handler.bot_speak = 0
                        botchat_bool = "active"
                    elif ui_handler.button_bot_speak_off.collidepoint(mouse_pos):
                        ui_handler.bot_speak = 1
                        botchat_bool = "inactive"
                # Currently on the about menu
                elif ui_handler.menu_status == "about":
                    if ui_handler.back_button.collidepoint(mouse_pos):
                        ui_handler.menu_status = "menu"
                    elif ui_handler.button_link.collidepoint(mouse_pos):
                        webbrowser.open(r"https://www.chess.com/terms/king-of-the-hill")

        # If hovered over the buttons... Just for fun
        pos = pygame.mouse.get_pos()
        if ui_handler.menu_status == "menu":
            button_list = ui_handler.menu_buttons
        elif ui_handler.menu_status == "settings":
            button_list =ui_handler.setting_buttons
        else:
            button_list = ui_handler.about_buttons
        for button in button_list:
            if button.collidepoint(pos):
                pygame.draw.rect(ui_handler.screen, BORDER_BROWN_LIGHT, button)
                ui_handler.draw_button_text(ui_handler.menu_status)
                ui_handler.draw_button_png(ui_handler.menu_status)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    # Create an instance of the Board class
    chess_board = Board()
    """board, color, kingSideCastle_white, queenSideCastle_white, \
        kingSideCastle_black, queenSideCastle_black, \
        enPassent, halfMoveClock, fullMoveClock = FENtoBoard("rnb1kbnr/8/8/8/7p/8/8/RN1QKBNR w")
    chess_board.chessBoard = board
    chess_board.can_castle_black_right = kingSideCastle_black
    chess_board.can_castle_black_left = queenSideCastle_black
    chess_board.can_castle_white_right = kingSideCastle_white
    chess_board.can_castle_white_left = queenSideCastle_white
    if color == 'black':
        chess_board.isMax = False"""

    # Create the UI handler
    ui_handler.draw_screen(ui_handler.bot_speak)
    ui_handler.draw_board(chess_board)
    if ui_handler.color_selected == 0:
        ui_handler.animations('Portrait/Portrait_B.png')
    elif ui_handler.color_selected == 1:
        ui_handler.animations('Portrait/Portrait_W.png')
    queue_textbool.put(botchat_bool)
    queue_timer.put("start")
    queue_timer.put(timer_count)

    animator = Animation()
    start_time = time.time()
    boredom_timer = time.time()
    last_dialogue = time.time()
    idle_timer = time.time()
    delay = 12
    idle_dialogue_early = 12
    idle_dialogue_mid = 24
    boredom_time = 40

    AI = True
    bot_is_running = False
    game_over = False
    running = True
    while running:
        if chess_board.white_hill_win or chess_board.black_hill_win:
            ui_handler.set_caption("Game Over")
            game_over = True
            queue_bot.put("quit")
            queue_anim.put("quit")
            queue_timer.put("quit")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Signal other processors to quit
                queue_bot.put("quit")
                queue_anim.put("quit")
                queue_timer.put("quit")
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Not allowed to click if the game is over or not players turn
                if not chess_board.isMax or game_over:
                    break
                # Get the position of the mouse click
                # If clicked outside the board break
                mouse_pos_check = pygame.mouse.get_pos()
                if (((mouse_pos_check[0] - BOARD_DISLOCATION_WIDTH) // SQUARE_SIZE) > 7 or
                    ((mouse_pos_check[0] - BOARD_DISLOCATION_WIDTH) // SQUARE_SIZE) < 0) \
                        or (((mouse_pos_check[1] - BOARD_DISLOCATION_HEIGHT) // SQUARE_SIZE) > 7 or
                             ((mouse_pos_check[1] - BOARD_DISLOCATION_HEIGHT) // SQUARE_SIZE) < 0):
                    break
                mouse_pos = pygame.mouse.get_pos()
                # Convert the mouse position to board coordinates
                clicked_col = (mouse_pos[0] - BOARD_DISLOCATION_WIDTH) // SQUARE_SIZE
                clicked_row = (mouse_pos[1] - BOARD_DISLOCATION_HEIGHT) // SQUARE_SIZE
                print(clicked_col, clicked_row)

                # Check if a square is already selected
                if chess_board.selected_square is None:
                    # No square selected yet, store the clicked square as the selected square
                    chess_board.selected_square = (clicked_row, clicked_col)
                else:
                    # A square is already selected, move the piece to the new square
                    new_row, new_col = clicked_row, clicked_col
                    sqDest = (new_row, new_col)

                    # Perform the move operation in your chess engine or game logic
                    # ...
                    # Update the chess board accordingly

                    chess_board.move_piece(chess_board.selected_square, sqDest, chess_board.chessBoard)
                    if chess_board.last_condition != "move_invalid":
                        queue_timer.put("black")
                    if chess_board.white_hill_win is True:
                        game_over = True

                    # Draw played chess board

                    ui_handler.draw_board(chess_board)
                    pygame.display.flip()

                    # Reset the selected square
                    chess_board.selected_square = None

        # Play bots turn, send signal 'bot' to bot_process
        if chess_board.isMax is False and not bot_is_running and not game_over:
            bot_is_running = True
            queue_bot.put("bot")
            queue_bot.put(game_algorithm)
            queue_bot.put(chess_board)

        # Text condition analyser
        if chess_board.urgency:
            while not queue_anim.empty():
                queue_anim.get()
            dialogue = animator.dialogues(chess_board.last_condition)
            queue_anim.put("text")
            queue_anim.put(dialogue)
            start_time = time.time()
            last_dialogue = time.time()
            chess_board.urgency = False
            chess_board.last_condition = ""
        else:
            # If 30 seconds have passed print the boredom dialogue
            if time.time() - boredom_timer > boredom_time and not bot_is_running:
                dialogue = animator.dialogues("time_limit_exceeded")
                queue_anim.put("text")
                queue_anim.put(dialogue)
                boredom_timer = time.time()
            elif time.time() - start_time > delay:  # If 8 seconds have passed print the next dialogue
                if chess_board.last_condition != "":  # If there is a waiting dialogue
                    dialogue = animator.dialogues(chess_board.last_condition)
                    queue_anim.put("text")
                    queue_anim.put(dialogue)
                    start_time = time.time()
                    last_dialogue = time.time()
                    chess_board.last_condition = ""
                elif chess_board.last_condition == "":
                    if time.time() - last_dialogue > idle_dialogue_early and time.time() - idle_timer < 300:
                        # Early game idle dialogues
                        dialogue = animator.dialogues("idle_early_game")
                        queue_anim.put("text")
                        queue_anim.put(dialogue)
                    elif time.time() - last_dialogue > idle_dialogue_mid and 300 < time.time() - idle_timer < 600:
                        # Mid game idle dialogues
                        dialogue = animator.dialogues("idle_mid_game")
                        queue_anim.put("text")
                        queue_anim.put(dialogue)
                    elif time.time() - last_dialogue > idle_dialogue_mid and 600 < time.time() - idle_timer:
                        # Late game idle dialogues
                        dialogue = animator.dialogues("idle_late_game")
                        queue_anim.put("text")
                        queue_anim.put(dialogue)
                    last_dialogue = time.time()

        # Check if got any signals for board and anim
        if not queue_game.empty():
            item = queue_game.get()
            # Got Signal 'quit', game over
            if item == "quit":
                ui_handler.set_caption("Game Over")
                game_over = True
            # Got Signal 'update', bot successfully played update chess board
            elif item == "update" and game_over is False:
                print("Updated")
                chess_board = queue_game.get()
                ui_handler.draw_board(chess_board)
                pygame.display.flip()
                boredom_timer = time.time()
                bot_is_running = False
                queue_timer.put("white")
            else:
                queue_game.put(item)
        # Check if got any signals for text
        if not queue_text.empty():
            item = queue_text.get()
            # Got Signal 'startoftext', empty the chat box
            if item == "startoftext":
                pygame.draw.rect(ui_handler.screen, DARK_GREY, (615, 420, 235, 80))
                ui_handler.line = 0
                # Got Signal 'text', blit text animation
            elif item == "text":
                text_part = queue_text.get()
                ui_handler.draw_text(text_part)
                pygame.display.flip()
                # Got Signal 'endoftext', blit text animation successfully completed
            elif item == "endoftext":
                ui_handler.line = 0
            elif item == "line":
                ui_handler.line += 1
            else:
                queue_text.put(item)
        # Check if got any signals for timer_text
        if not queue_timertext.empty():
            item = queue_timertext.get()
            # Got Signal 'white', update white timer
            if item == "white":
                timer_string = queue_timertext.get()
                # Time game over
                if timer_string == "00:00":
                    dialogue = animator.dialogues("time_done_player")
                    queue_anim.put("text")
                    queue_anim.put(dialogue)
                    ui_handler.set_caption("Game Over")
                    game_over = True
                    queue_bot.put("quit")
                    queue_anim.put("quit")
                    queue_timer.put("quit")
                ui_handler.draw_timer("white", timer_string)
            # Got Signal 'black', update black timer
            elif item == "black":
                timer_string = queue_timertext.get()
                if timer_string == "00:00":
                    dialogue = animator.dialogues("time_done_queen")
                    queue_anim.put("text")
                    queue_anim.put(dialogue)
                    ui_handler.set_caption("Game Over")
                    game_over = True
                    queue_bot.put("quit")
                    queue_anim.put("quit")
                    queue_timer.put("quit")
                ui_handler.draw_timer("black", timer_string)

        # Highlight the selected square if one is selected
        if chess_board.selected_square is not None:
            ui_handler.draw_selected_piece(chess_board)

        # Highlight the last played move
        if chess_board.last_move is not None:
            ui_handler.draw_last_move(chess_board)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    # Quit the game
    pygame.quit()

def bot_process(queue_game, queue_bot, queue_anim, queue_timer):
    running = True
    text_picker = Animation()
    while running:
        if not queue_bot.empty():
            item = queue_bot.get()
            # Got signal 'quit', stop while loop
            if item == "quit":
                running = False
            # Got Signal 'bot', run bot_plays()
            elif item == "bot":
                algorithm = queue_bot.get()
                chess_board = queue_bot.get()
                if chess_board.bot_plays(algorithm) == -1:
                    # Send signal 'quit', if no possible moves
                    choose = random.randint(0, 1)
                    if choose == 1:
                        dialogue = text_picker.dialogues("move_checkmate_queen")
                        chess_board.urgency = True
                        queue_anim.put("text")
                        queue_anim.put(dialogue)
                    else:
                        dialogue = text_picker.dialogues("defeat")
                        chess_board.urgency = True
                        queue_anim.put("text")
                        queue_anim.put(dialogue)
                    queue_game.put("quit")
                    queue_anim.put("quit")
                    queue_timer.put("quit")
                    break
                else:
                    # Send signal 'update', if bot played
                    queue_game.put("update")
                    queue_game.put(chess_board)
            else:
                queue_bot.put(item)
def animation_process(queue_anim, queue_text, queue_textbool):
    running = True
    animator = Animation()
    text_activated = True
    while running:
        if not queue_textbool.empty():
            booly = queue_textbool.get()
            if booly == "active":
                text_activated = True
            elif booly == "inactive":
                text_activated = False
        if not queue_anim.empty():
            item = queue_anim.get()
            if item == "quit":
                running = False
            elif item == "text":
                text = queue_anim.get()
                if text_activated:
                    animator.text_animation(text, queue_text)
            elif item == "anim":
                raise NotImplementedError
            else:
                queue_anim.put(item)

def timer_process(queue_timer, queue_timertext):
    running = True
    turn = "white"
    duration_white = 1200
    duration_black = 1200
    stop = False
    start = False

    while running:
        if not queue_timer.empty():
            item = queue_timer.get()
            if item == "quit":
                running = False
            elif item == "gameover":
                stop = True
            elif item == "start":
                start = True
            elif item == "black":
                turn = "black"
            elif item == "white":
                turn = "white"
            elif item == "20":
                duration_white = 1200
                duration_black = 1200
            elif item == "30":
                duration_white = 1800
                duration_black = 1800
            elif item == "40":
                duration_white = 2400
                duration_black = 2400

        if start and not stop:
            if turn == "white":
                remaining_time = max(0, int(duration_white - 1))
                duration_white = remaining_time
            else:
                remaining_time = max(0, int(duration_black - 1))
                duration_black = remaining_time
            minutes = int(remaining_time / 60)
            seconds = int(remaining_time % 60)
            time_string = f"{minutes:02d}:{seconds:02d}"

            queue_timertext.put(turn)
            queue_timertext.put(time_string)

            time.sleep(1)


if __name__ == "__main__":
    queue_game = mp.Queue()  # Signals to game_process
    queue_bot = mp.Queue()   # Signals to bot_process
    queue_anim = mp.Queue()  # Signal to text_process
    queue_text = mp.Queue()  # Signal to game_process that contain only text prints
    queue_textbool = mp.Queue()  # Signal to bot_process if the bot is muted or not
    queue_timer = mp.Queue()  # Signal to timer_process
    queue_timertext = mp.Queue()  # Signal from timer_process into game_process


    # Handle: UI - Visual Updates ...
    gameM_process = mp.Process(target=game_process, args=(queue_game, queue_bot, queue_anim, queue_text, queue_textbool, queue_timer, queue_timertext))

    # Handle: Animations - Text ...
    anim_process = mp.Process(target=animation_process, args=(queue_anim, queue_text, queue_textbool, ))

    # Handle: Game Algorithms - Machine Learning ...
    bot_ML_process = mp.Process(target=bot_process, args=(queue_game, queue_bot, queue_anim, queue_timer,))

    # Handle: Timer
    time_process = mp.Process(target=timer_process, args=(queue_timer, queue_timertext))

    gameM_process.start()
    bot_ML_process.start()
    anim_process.start()
    time_process.start()

    gameM_process.join()
    bot_ML_process.join()
    anim_process.join()
    time_process.join()

