# Initialize Pygame
import pygame
from board import Board
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
SQUARE_SIZE = 60
DARK_GREEN = (79, 121, 66)
LIGHT_GREEN = (158, 194, 133)


import numpy as np
def main():
    # Initialize Pygame
    pygame.init()


    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Chess Board")

    # Create an instance of the Board class
    chess_board = Board()
    AI = True

    selected_square = None  # Store the selected square coordinates

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                mouse_pos = pygame.mouse.get_pos()

                # Convert the mouse position to board coordinates
                clicked_col = mouse_pos[0] // SQUARE_SIZE
                clicked_row = mouse_pos[1] // SQUARE_SIZE

                # Check if a square is already selected
                if selected_square is None:
                    # No square selected yet, store the clicked square as the selected square
                    selected_square = (clicked_row, clicked_col)
                else:
                    # A square is already selected, move the piece to the new square
                    new_row, new_col = clicked_row, clicked_col
                    sqDest = (new_row, new_col)

                    # Perform the move operation in your chess engine or game logic
                    # ...
                    # Update the chess board accordingly

                    chess_board.move_piece(selected_square, sqDest,chess_board.chessBoard)

                    # Draw played chess board

                    chess_board.draw_board(screen)
                    pygame.display.flip()

                    # Reset the selected square
                    selected_square = None
        if chess_board.isMax == False :
            if chess_board.bot_plays() == -1:
                pygame.display.set_caption("Game Over")

        # Clear the screen
        screen.fill(DARK_GREEN)

        # Draw the chessboard
        chess_board.draw_board(screen)

        # Highlight the selected square if one is selected
        if selected_square is not None:
            selected_row, selected_col = selected_square
            pygame.draw.rect(screen, (0, 255, 0), (selected_col * SQUARE_SIZE, selected_row * SQUARE_SIZE,
                                                   SQUARE_SIZE, SQUARE_SIZE), 4)
        # Highlight the last played move
        if chess_board.last_move is not None:
            selected, dest = chess_board.last_move
            pygame.draw.rect(screen, (60, 179, 113), (selected[1] * SQUARE_SIZE, selected[0] * SQUARE_SIZE,
                                                   SQUARE_SIZE, SQUARE_SIZE), 4)
            pygame.draw.rect(screen, (60, 179, 113), (dest[1] * SQUARE_SIZE, dest[0] * SQUARE_SIZE,
                                                   SQUARE_SIZE, SQUARE_SIZE), 4)

        # Update the display
        pygame.display.flip()


    # Quit the game
    pygame.quit()

if __name__ == "__main__":
    main()