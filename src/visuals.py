import pygame.font

from board import *
import time

# Constants for colors, screen size, and square size
SCREEN_WIDTH = 480 * 2
SCREEN_HEIGHT = 480 + 240
BOARD_DISLOCATION_WIDTH = 120
BOARD_DISLOCATION_HEIGHT = 120
SQUARE_SIZE = 60
DARK_GREEN = (79, 121, 66)
LIGHT_GREEN = (158, 194, 133)
BORDER_BROWN_LIGHT = (164, 144, 124)
BORDER_BROWN_LIGHT_2 = (183, 159, 135)
BORDER_BROWN_DARK = (141, 123, 104)

chess_V_dark = (115, 108, 100)
chess_V_light = (209, 201, 193)
DARK_GREY = (90, 90, 90)

class BoardVisuals:

    def __init__(self):
        self.screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 9)
        self.text_font = pygame.font.Font("fonts/PublicPixel.ttf", 14)
        self.about_font = pygame.font.Font("fonts/PublicPixel.ttf", 12)
        self.button_font = pygame.font.Font("fonts/PublicPixel.ttf", 24)
        self.hint_font = pygame.font.Font("fonts/PublicPixel.ttf", 10)
        self.line = 0
        self.menu_status = "menu"
        self.menu_buttons = [pygame.Rect(340, 150, 280, 60), pygame.Rect(340, 250, 280, 60),
                             pygame.Rect(340, 350, 280, 60), pygame.Rect(340, 450, 280, 60)]

        self.setting_buttons = [pygame.Rect(80, 620, 140, 60),
                                pygame.Rect(540, 175, 60, 60), pygame.Rect(630, 175, 60, 60),
                                pygame.Rect(540, 275, 60, 60), pygame.Rect(630, 275, 60, 60), pygame.Rect(720, 275, 60, 60),
                                pygame.Rect(540, 375, 80, 60), pygame.Rect(650, 375, 80, 60),
                                pygame.Rect(540, 475, 100, 60), pygame.Rect(660, 475, 100, 60)]
        # pygame.Rect(290, 175, 380, 60), pygame.Rect(290, 275, 380, 60), pygame.Rect(290, 375, 380, 60),
        # pygame.Rect(290, 475, 380, 60)
        self.about_buttons = [pygame.Rect(80, 620, 140, 60)]

        self.start_button = pygame.Rect(340, 150, 280, 60)
        self.setting_button = pygame.Rect(340, 250, 280, 60)
        self.white_button = pygame.Rect(540, 175, 60, 60)  # 0
        self.black_button = pygame.Rect(630, 175, 60, 60)  # 1
        self.color_selected = 0
        self.button_20 = pygame.Rect(540, 275, 60, 60)  # 0
        self.button_30 = pygame.Rect(630, 275, 60, 60)  # 1
        self.button_40 = pygame.Rect(720, 275, 60, 60)  # 2
        self.time_selected = 0
        self.button_bot_speak_on = pygame.Rect(540, 375, 80, 60)  # 0
        self.button_bot_speak_off = pygame.Rect(650, 375, 80, 60)  # 1
        self.bot_speak = 0
        self.button_alphabeta = pygame.Rect(540, 475, 100, 60)  # 0
        self.button_montecarlo = pygame.Rect(660, 475, 100, 60)  # 1
        self.algo_selected = 0
        self.button_link = pygame.Rect(615, 542, 265, 18)
        self.back_button = pygame.Rect(80, 620, 140, 60)
        self.about_button = pygame.Rect(340, 350, 280, 60)
        self.quit_button = pygame.Rect(340, 450, 280, 60)


    def draw_start_menu(self):
        self.screen.fill((202, 206, 187))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (340, 150, 280, 60))  # Start
        pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (345, 155, 270, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (340, 250, 280, 60))  # Settings
        pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (345, 255, 270, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (340, 350, 280, 60))  # About
        pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (345, 355, 270, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (340, 450, 280, 60))  # Quit
        pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (345, 455, 270, 50))

    def draw_settings_menu(self):
        self.screen.fill((202, 206, 187))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (340, 75, 280, 60))  # Settings
        # pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (345, 80, 270, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (250, 175, 260, 60))  # Play as
        # pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (295, 180, 370, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (540, 175, 60, 60))  # Play as white
        if self.color_selected:
            pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (545, 180, 50, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (630, 175, 60, 60))  # Play as black
        if not self.color_selected:
            pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (635, 180, 50, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (250, 275, 260, 60))  # Time
        # pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (295, 280, 370, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (540, 275, 60, 60))  # Time 20 min
        if not self.time_selected == 0:
            pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (545, 280, 50, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (630, 275, 60, 60))  # Time 30 min
        if not self.time_selected == 1:
            pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (635, 280, 50, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (720, 275, 60, 60))  # Time 40 min
        if not self.time_selected == 2:
            pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (725, 280, 50, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (250, 375, 260, 60))  # Bot chat
        # pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (295, 380, 370, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (540, 375, 80, 60))  # Bot chat On
        if self.bot_speak:
            pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (545, 380, 70, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (650, 375, 80, 60))  # Bot chat Off
        if not self.bot_speak:
            pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (655, 380, 70, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (250, 475, 260, 60))  # Algorithm
        # pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (295, 480, 370, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (540, 475, 100, 60))  # Alpha Beta
        if self.algo_selected:
            pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (545, 480, 90, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (660, 475, 100, 60))  # MonteCarlo
        if not self.algo_selected:
            pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (665, 480, 90, 50))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (80, 620, 140, 60))  # Back
        pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (85, 625, 130, 50))

    def draw_about_menu(self):
        self.screen.fill((202, 206, 187))

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (80, 80, 480, 480))  # About 1

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (600, 80, 280, 480))  # About 2

        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (80, 620, 140, 60))  # Back
        pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (85, 625, 130, 50))

    def draw_button_png(self, page):
        if page == "settings":
            img = pygame.image.load('chesspieces/100.png')
            img = pygame.transform.scale(img, (40, 40))
            self.screen.blit(img, (549, 185))

            img2 = pygame.image.load('chesspieces/-100.png')
            img2 = pygame.transform.scale(img2, (40, 40))
            self.screen.blit(img2, (639, 185))

    def draw_button_text(self,page):
        if page == "menu":
            text_start = self.button_font.render("Start", False, (57, 50, 40))  # Start
            self.screen.blit(text_start, (420, 168))

            text_settings = self.button_font.render("Settings", False, (57, 50, 40))  # Settings
            self.screen.blit(text_settings, (385, 268))

            text_about = self.button_font.render("About", False, (57, 50, 40))  # About
            self.screen.blit(text_about, (420, 368))

            text_quit = self.button_font.render("Quit", False, (57, 50, 40))  # Quit
            self.screen.blit(text_quit, (430, 468))

        elif page == "settings":
            text_settings = self.button_font.render("Settings", False, (57, 50, 40))  # Settings
            self.screen.blit(text_settings, (385, 93))

            text_playas = self.button_font.render("Play as", False, (57, 50, 40))  # Play as
            self.screen.blit(text_playas, (267, 185))
            text_playas_hint = self.hint_font.render("(currently unavailable)", False, (57, 50, 40))  # Hint
            self.screen.blit(text_playas_hint, (260, 218))

            text_time = self.button_font.render("Time(min)", False, (57, 50, 40))  # Time
            self.screen.blit(text_time, (270, 293))
            text_20 = self.button_font.render("20", False, (57, 50, 40))  # Time 20
            self.screen.blit(text_20, (548, 293))
            text_30 = self.button_font.render("30", False, (57, 50, 40))  # Time 30
            self.screen.blit(text_30, (638, 293))
            text_40 = self.button_font.render("40", False, (57, 50, 40))  # Time 40
            self.screen.blit(text_40, (728, 293))

            text_botchat = self.button_font.render("Bot chat", False, (57, 50, 40))  # Bot chat
            self.screen.blit(text_botchat, (267, 385))
            text_botchat_hint = self.hint_font.render("(disables bot dialogues)", False, (57, 50, 40))  # Hint
            self.screen.blit(text_botchat_hint, (260, 418))
            text_botchaton = self.button_font.render("On", False, (57, 50, 40))  # Bot chat On
            self.screen.blit(text_botchaton, (558, 393))
            text_botchatoff = self.button_font.render("Off", False, (57, 50, 40))  # Bot chat Off
            self.screen.blit(text_botchatoff, (657, 393))

            text_algorithm = self.button_font.render("Algorithm", False, (57, 50, 40))  # Algorithm
            self.screen.blit(text_algorithm, (267, 485))
            text_algorithm_hint = self.hint_font.render("(Alpha Beta-Monte Carlo)", False, (57, 50, 40))  # Hint
            self.screen.blit(text_algorithm_hint, (260, 518))
            text_alphabeta = self.button_font.render("α-β", False, (57, 50, 40))  # Alpha Beta
            self.screen.blit(text_alphabeta, (553, 493))
            text_montecarlo = self.button_font.render("mcts", False, (57, 50, 40))  # Monte Carlo
            self.screen.blit(text_montecarlo, (665, 493))

            text_start = self.button_font.render("Back", False, (57, 50, 40))  # Back
            self.screen.blit(text_start, (105, 637))

        elif page == "about":

            text_line1 = self.button_font.render("About", False, (57, 50, 40))
            self.screen.blit(text_line1, (95, 95))
            text_line2 = self.about_font.render("This game was created for the modul", False, (57, 50, 40))
            text_line3 = self.about_font.render("BINF-SWT-KI/PJ of TUBerlin in Summer", False, (57, 50, 40))
            text_line4 = self.about_font.render("Semester 2023 by Yetkin Zambelli,", False, (57, 50, 40))
            text_line5 = self.about_font.render("Yagiz Semercioglu and Baris", False, (57, 50, 40))
            text_line6 = self.about_font.render("Terzioglu.", False, (57, 50, 40))
            text_line7 = self.about_font.render("In this project, we implemented;", False, (57, 50, 40))
            text_line8 = self.about_font.render("first a dummy AI with a random move", False, (57, 50, 40))
            text_line9 = self.about_font.render("choosing, then with the use of", False, (57, 50, 40))
            text_line10 = self.about_font.render("alpha-beta algorithm, hash table ", False, (57, 50, 40))
            text_line11 = self.about_font.render("and heuristics a smarter AI,", False, (57, 50, 40))
            text_line12 = self.about_font.render("lastly, with the use of machine", False, (57, 50, 40))
            text_line13 = self.about_font.render("learning our final AI.", False, (57, 50, 40))

            self.screen.blit(text_line2, (105, 135))
            self.screen.blit(text_line3, (95, 150))
            self.screen.blit(text_line4, (95, 165))
            self.screen.blit(text_line5, (95, 180))
            self.screen.blit(text_line6, (95, 195))
            self.screen.blit(text_line7, (105, 230))
            self.screen.blit(text_line8, (95, 245))
            self.screen.blit(text_line9, (95, 260))
            self.screen.blit(text_line10, (95, 275))
            self.screen.blit(text_line11, (95, 290))
            self.screen.blit(text_line12, (95, 305))
            self.screen.blit(text_line13, (95, 320))

            text_rules1 = self.button_font.render("Rules", False, (57, 50, 40))
            self.screen.blit(text_rules1, (615, 95))

            text_rules2 = self.about_font.render("King of the Hill", False, (57, 50, 40))
            text_rules3 = self.about_font.render("is a chess variant", False, (57, 50, 40))
            text_rules4 = self.about_font.render("that is very similar", False, (57, 50, 40))
            text_rules5 = self.about_font.render("to standard chess.", False, (57, 50, 40))
            text_rules6 = self.about_font.render("The only difference", False, (57, 50, 40))
            text_rules7 = self.about_font.render("is the way the game", False, (57, 50, 40))
            text_rules8 = self.about_font.render("can end. When one of", False, (57, 50, 40))
            text_rules9 = self.about_font.render("the kings gets to", False, (57, 50, 40))
            text_rules10 = self.about_font.render("the middle four", False, (57, 50, 40))
            text_rules11 = self.about_font.render("squares, the one", False, (57, 50, 40))
            text_rules12 = self.about_font.render("who steps on the", False, (57, 50, 40))
            text_rules13 = self.about_font.render("'hill' wins the game.", False, (57, 50, 40))

            self.screen.blit(text_rules2, (625, 135))
            self.screen.blit(text_rules3, (615, 150))
            self.screen.blit(text_rules4, (615, 165))
            self.screen.blit(text_rules5, (615, 180))
            self.screen.blit(text_rules6, (615, 195))
            self.screen.blit(text_rules7, (615, 210))
            self.screen.blit(text_rules8, (615, 225))
            self.screen.blit(text_rules9, (615, 240))
            self.screen.blit(text_rules10, (615, 255))
            self.screen.blit(text_rules11, (615, 270))
            self.screen.blit(text_rules12, (615, 285))
            self.screen.blit(text_rules13, (615, 300))

            koth = pygame.image.load('about.png')
            koth = pygame.transform.scale(koth, (220, 220))
            self.screen.blit(koth, (630, 320))

            text_rules14 = self.about_font.render("For more info click", False, (57, 50, 40))
            self.screen.blit(text_rules14, (615, 542))

            text_start = self.button_font.render("Back", False, (57, 50, 40))  # Back
            self.screen.blit(text_start, (105, 637))

    def draw_bottext_disabled(self):
        drawn_text = self.font.render("- Bot chat is disabled. -", False, (0, 255, 0))
        self.screen.blit(drawn_text, (621, 425))

    def draw_screen(self, bottext):
        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (100, 100, 520, 520))  # Second Border around the board
        pygame.draw.rect(self.screen, BORDER_BROWN_DARK, (110, 110, 500, 500))  # First Border around the board
        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (145, 50, 420, 60))  # Player Black
        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT_2, (155, 60, 400, 45))  # Player Black
        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (145, 610, 420, 60))  # PLayer White
        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT_2, (155, 615, 400, 45))  # Player White
        text_black = self.text_font.render("Player Black", False, (57, 50, 40))  # Text Player Black
        self.screen.blit(text_black, (175, 75))
        if self.time_selected == 0:
            time_string = "20:00"
        elif self.time_selected == 1:
            time_string = "30:00"
        else:
            time_string = "40:00"
        drawn_timer = self.text_font.render(time_string, False, (57, 50, 40))  # Timer
        self.screen.blit(drawn_timer, (375, 75))
        text_white = self.text_font.render("Player White", False, (57, 50, 40))  # Text Player White
        self.screen.blit(text_white, (175, 630))
        drawn_timer = self.text_font.render(time_string, False, (57, 50, 40))  # Timer
        self.screen.blit(drawn_timer, (375, 630))
        # a-b-c indicator
        abc_surface = self.font.render("a     b     c     d     e"
                                       "     f     g     h", False, BORDER_BROWN_LIGHT)
        self.screen.blit(abc_surface, (123, 599))
        # 1-2-3 indicator
        for i in range(8, 0, -1):
            number = i
            number_surface = self.font.render(str(number), False, BORDER_BROWN_LIGHT)
            self.screen.blit(number_surface, (602, 123 + (8 - i) * SQUARE_SIZE))
        # Player Frame
        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (620, 180, 240, 240))
        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT_2, (615, 190, 235, 220))
        # Text Frame
        pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT, (620, 420, 240, 90))
        pygame.draw.rect(self.screen, DARK_GREY, (615, 420, 235, 80))
        if bottext:
            self.draw_bottext_disabled()

    def draw_board(self, board):
        for row in range(8):
            for col in range(8):
                x = col * SQUARE_SIZE + BOARD_DISLOCATION_WIDTH
                y = row * SQUARE_SIZE + BOARD_DISLOCATION_HEIGHT
                color = chess_V_light if (row + col) % 2 == 0 else chess_V_dark
                pygame.draw.rect(self.screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
                # Get the piece value from the chess board
                piece_value = board.chessBoard[row][col]
                # If there is a piece on the current square, load the corresponding image
                if piece_value != 0:
                    piece_image = pygame.image.load(f"chesspieces/{piece_value}.png")
                    self.screen.blit(piece_image, (x, y))

    def draw_selected_piece(self, board):
        if board.selected_square is not None:
            selected_row, selected_col = board.selected_square
            pygame.draw.rect(self.screen, (0, 255, 0), (selected_col * SQUARE_SIZE + BOARD_DISLOCATION_WIDTH,
                                                        selected_row * SQUARE_SIZE + BOARD_DISLOCATION_HEIGHT,
                                                        SQUARE_SIZE, SQUARE_SIZE), 4)

    def draw_last_move(self, board):
        if board.last_move is not None:
            selected, dest = board.last_move
            pygame.draw.rect(self.screen, (60, 179, 113), (selected[1] * SQUARE_SIZE + BOARD_DISLOCATION_WIDTH,
                                                           selected[0] * SQUARE_SIZE + BOARD_DISLOCATION_HEIGHT,
                                                      SQUARE_SIZE, SQUARE_SIZE), 4)
            pygame.draw.rect(self.screen, (60, 179, 113), (dest[1] * SQUARE_SIZE + BOARD_DISLOCATION_WIDTH,
                                                           dest[0] * SQUARE_SIZE + BOARD_DISLOCATION_HEIGHT,
                                                      SQUARE_SIZE, SQUARE_SIZE), 4)

    def set_caption(self, caption):
        pygame.display.set_caption(caption)

    def draw_text(self, text):
        drawn_text = self.font.render(text, True, (0, 255, 0))
        self.screen.blit(drawn_text, (620, 425 + (self.line * 15)))

    def draw_timer(self, turn, timer):
        if turn == "black":
            pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT_2, (155, 60, 400, 45))
            text_black = self.text_font.render("Player Black", False, (57, 50, 40))  # Text Player Black
            self.screen.blit(text_black, (175, 75))
            drawn_timer = self.text_font.render(timer, False, (57, 50, 40))  # Timer
            self.screen.blit(drawn_timer, (375, 75))
        elif turn == "white":
            pygame.draw.rect(self.screen, BORDER_BROWN_LIGHT_2, (155, 615, 400, 45))
            text_white = self.text_font.render("Player White", False, (57, 50, 40))  # Text Player White
            self.screen.blit(text_white, (175, 630))
            drawn_timer = self.text_font.render(timer, False, (57, 50, 40))  # Timer
            self.screen.blit(drawn_timer, (375, 630))



    def animations(self, act):
        image = pygame.image.load(act)
        image = pygame.transform.scale(image, (220, 220))
        self.screen.blit(image, (620, 190))








