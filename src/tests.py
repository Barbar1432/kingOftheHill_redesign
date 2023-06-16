import unittest
import numpy as np
import copy
import timeit
from board import Board
from moveGenerator import moveGenerator

class TestBoard(unittest.TestCase):
    def test_Fricke(self):
        # print(FENtoBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq b3 1 0"))
        boardd, stell, fen, moves = allBoards()[0]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))
    def test_A_1(self):
        boardd, stell, fen, moves = allBoards()[1]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))
    def test_A_2(self):
        boardd, stell, fen, moves = allBoards()[2]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_N_1(self):
        boardd, stell, fen, moves = allBoards()[3]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_N_2(self):
        boardd, stell, fen, moves = allBoards()[4]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_L_1(self):
        boardd, stell, fen, moves = allBoards()[5]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_L_2(self): # TODO: Sıkıntı
        boardd, stell, fen, moves = allBoards()[6]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        #print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_G_1(self):
        boardd, stell, fen, moves = allBoards()[7]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_G_2(self):
        boardd, stell, fen, moves = allBoards()[8]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_O_1(self):
        boardd, stell, fen, moves = allBoards()[9]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_O_2(self):
        boardd, stell, fen, moves = allBoards()[10]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_J_1(self):
        boardd, stell, fen, moves = allBoards()[11]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_J_2(self):
        boardd, stell, fen, moves = allBoards()[12]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_H_1(self):
        boardd, stell, fen, moves = allBoards()[13]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_H_2(self):
        boardd, stell, fen, moves = allBoards()[14]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_AA_1(self):
        boardd, stell, fen, moves = allBoards()[15]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_AA_2(self):
        boardd, stell, fen, moves = allBoards()[16]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_AB_1(self):
        boardd, stell, fen, moves = allBoards()[17]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_AB_2(self):
        boardd, stell, fen, moves = allBoards()[18]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_S_1(self):
        boardd, stell, fen, moves = allBoards()[19]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_S_2(self):
        boardd, stell, fen, moves = allBoards()[20]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_AF_1(self):
        boardd, stell, fen, moves = allBoards()[21]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_AF_2(self):
        boardd, stell, fen, moves = allBoards()[22]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_R_1(self):
        boardd, stell, fen, moves = allBoards()[23]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_R_2(self):
        boardd, stell, fen, moves = allBoards()[24]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_P_1(self):
        boardd, stell, fen, moves = allBoards()[25]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_P_2(self):
        boardd, stell, fen, moves = allBoards()[26]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_AH_1(self):
        boardd, stell, fen, moves = allBoards()[27]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_AH_2(self):
        boardd, stell, fen, moves = allBoards()[28]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_F_1(self):
        boardd, stell, fen, moves = allBoards()[29]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_F_2(self):
        boardd, stell, fen, moves = allBoards()[30]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_T_1(self):
        boardd, stell, fen, moves = allBoards()[31]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_T_2(self):
        boardd, stell, fen, moves = allBoards()[32]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_U_1(self):
        boardd, stell, fen, moves = allBoards()[33]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_U_2(self): # TODO: Left Castling problem
        boardd, stell, fen, moves = allBoards()[34]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_U_3(self):
        boardd, stell, fen, moves = allBoards()[35]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_U_4(self):
        boardd, stell, fen, moves = allBoards()[36]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_V_1(self):
        boardd, stell, fen, moves = allBoards()[37]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_V_2(self):
        boardd, stell, fen, moves = allBoards()[38]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_K_1(self):
        boardd, stell, fen, moves = allBoards()[39]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_K_2(self):
        boardd, stell, fen, moves = allBoards()[40]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_X_1(self):
        boardd, stell, fen, moves = allBoards()[41]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_X_2(self):
        boardd, stell, fen, moves = allBoards()[42]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_C_1(self):
        boardd, stell, fen, moves = allBoards()[43]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_C_2(self):
        boardd, stell, fen, moves = allBoards()[44]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_M_1(self):
        boardd, stell, fen, moves = allBoards()[45]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_M_2(self):
        boardd, stell, fen, moves = allBoards()[46]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_Z_1(self):
        boardd, stell, fen, moves = allBoards()[47]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))

    def test_Z_2(self):
        boardd, stell, fen, moves = allBoards()[48]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = Board()
        createNewBoard(b_board, t_board)
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(t_board.moves, len(legal_moves))
class testingBoard():
    def __init__(self, name, stell, fen, moves):
        self.name = name
        self.stellung = stell
        self.FEN_Notation = fen
        self.moves = moves
        self.board, self.color, self.kingSideCastle_white, self.queenSideCastle_white, \
            self.kingSideCastle_black, self.queenSideCastle_black, \
            self.enPassent, self.halfMoveClock, self.fullMoveClock = FENtoBoard(fen)


def createNewBoard(b_board, t_board):
    b_board.chessBoard = t_board.board
    b_board.can_castle_black_right = t_board.kingSideCastle_black
    b_board.can_castle_black_left = t_board.queenSideCastle_black
    b_board.can_castle_white_right = t_board.kingSideCastle_white
    b_board.can_castle_white_left = t_board.queenSideCastle_white
    if t_board.color == 'black':
        b_board.isMax = False
def returnAllMoves(b_board, t_board):
    #chessBoardVisualize(b_board.chessBoard)
    #print(b_board.boardInteger)
    move_generator = moveGenerator()
    if t_board.color == 'white':
        positions = np.where(b_board.chessBoard > 0)
        can_castle_left = b_board.can_castle_white_left
        can_castle_right = b_board.can_castle_white_right
    else:
        positions = np.where(b_board.chessBoard < 0)
        can_castle_left = b_board.can_castle_black_left
        can_castle_right = b_board.can_castle_black_right
    moves = move_generator.legalMoves(b_board.chessBoard, positions, b_board.isMax, can_castle_right, can_castle_left)
    list_of_possible_moves = []
    row_indices, col_indices = positions
    for row, col in zip(row_indices, col_indices):
        pos = (row, col)
        legal_moves = moves[pos]
        while len(legal_moves) != 0:
            move = legal_moves.pop()
            possible_move = (pos, move)
            list_of_possible_moves.append(possible_move)
    return list_of_possible_moves

def FENtoBoard(FEN):
    board = np.array([[0 for _ in range(8)] for _ in range(8)])
    i = 0
    j = 0
    k = 0 # space counter
    kingsideCastleBlack = False
    queensideCastleBlack = False
    kingsideCastleWhite = False
    queensideCastleWhite = False
    enPassentSquareCol = ()
    enPassentSquareRow = ()
    halfMoveClock = ()
    fullMoveClock = ()
    # [L1]/[L2]/[L3]/[L4]/[L5]/[L6]/[L7]/[L8] [Active Color] [Castling Availability]
    # [En Passant target square - Piyon önceki el 2 kare ilerledi]
    while FEN != "":
        char = FEN[0]
        FEN = ''.join(FEN.split(char, 1))
        if char == '/':
            i += 1
            j = 0
        elif char == 'p':
            board[i][j] = -100
            j += 1
        elif char == 'n':
            board[i][j] = -320
            j += 1
        elif char == 'b':
            board[i][j] = -330
            j += 1
        elif char == 'r':
            board[i][j] = -500
            j += 1
        elif char == 'q':
            board[i][j] = -900
            j += 1
        elif char == 'k':
            board[i][j] = -2000
            j += 1
        elif char == 'N':
            board[i][j] = 320
            j += 1
        elif char == 'B':
            board[i][j] = 330
            j += 1
        elif char == 'R':
            board[i][j] = 500
            j += 1
        elif char == 'Q':
            board[i][j] = 900
            j += 1
        elif char == 'K':
            board[i][j] = 2000
            j += 1
        elif char == 'P':
            board[i][j] = 100
            j += 1
        elif char.isdigit():
            j += int(char)
        elif char == ' ':
            k += 1
            if FEN != '':
                char = FEN[0]
                FEN = ''.join(FEN.split(char, 1))
            if k == 1: # Turn Variable
                if char == 'w':
                    color = 'white'
                elif char == 'b':
                    color = 'black'
            elif k == 2: # Castling availability - Rok nasıl yapılabilir?
                if char == 'K':
                    kingsideCastleWhite = True
                    if len(FEN) != 0:
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                if char == 'Q':
                    queensideCastleWhite = True
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                if char == 'k':
                    kingsideCastleBlack = True
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                if char == 'q':
                    queensideCastleBlack = True
            elif k == 3: # En Passent Variable
                if char == 'a':
                    enPassentSquareCol = 0
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'b':
                    enPassentSquareCol = 1
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'c':
                    enPassentSquareCol = 2
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'd':
                    enPassentSquareCol = 3
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'e':
                    enPassentSquareCol = 4
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'f':
                    enPassentSquareCol = 5
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'g':
                    enPassentSquareCol = 6
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'h':
                    enPassentSquareCol = 7
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                if char.isdigit():
                    if int(char) == 1:
                        enPassentSquareRow = 7
                    elif int(char) == 2:
                        enPassentSquareRow = 6
                    elif int(char) == 3:
                        enPassentSquareRow = 5
                    elif int(char) == 4:
                        enPassentSquareRow = 4
                    elif int(char) == 5:
                        enPassentSquareRow = 3
                    elif int(char) == 6:
                        enPassentSquareRow = 2
                    elif int(char) == 7:
                        enPassentSquareRow = 1
                    elif int(char) == 8:
                        enPassentSquareRow = 0
            elif k == 4: # Half Move Clock
                if char.isdigit():
                    halfMoveClock = int(char)
            elif k == 5: # Full Move Clock
                if char.isdigit():
                    fullMoveClock = int(char)
            #print("Remaining FEN:", FEN)
        elif char == '-':
            continue
            # Board is done

    return board, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, \
        (enPassentSquareRow,enPassentSquareCol), halfMoveClock, fullMoveClock

def chessBoardVisualize(integerList):
    print("+[Board]+")
    print("+--------+")
    for i in range (len(integerList)):
        string = "|"
        for j in range (len(integerList[i])):
            if integerList[i][j] == 0:
                string += "_"
            elif integerList[i][j] == 2000:
                string += "♚"
            elif integerList[i][j] == -2000:
                string += "♔"
            elif integerList[i][j] == 500:
                string += "♜"
            elif integerList[i][j] == -500:
                string += "♖"
            elif integerList[i][j] == 320:
                string += "♞"
            elif integerList[i][j] == -320:
                string += "♘"
            elif integerList[i][j] == 330:
                string += "♝"
            elif integerList[i][j] == -330:
                string += "♗"
            elif integerList[i][j] == 900:
                string += "♛"
            elif integerList[i][j] == -900:
                string += "♕"
            elif integerList[i][j] == 100:
                string += "♟"
            elif integerList[i][j] == -100:
                string += "♙"
        print(string + "|")
    print("+--------+")




def allBoards():
    boards = [("Fricke", 1, "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w", 20),
              ("A", 1, "2b1k3/p5rp/Pppb1p1P/n2qpPpR/1PPpP1P1/R2P1Q1B/1Br4n/1N2K1N1 w", 33),
              ("A", 2, "r1bqk2r/ppp3pp/5p2/2nPp3/P1Pn2P1/3P1N2/1P2BP1P/RN1Q1RK1 b k", 42),
              ("N", 1, "r2qk2r/pp1bp1bp/2np1np1/2pP4/2P1P3/2N2N2/PP3PPP/R1BQKB1R w - - 0 1", 38),
              ("N", 2, "6r1/p5k1/3Q4/2N5/5P2/1p6/P5KP/4qR2 w - - 0 25", 42),
              ("L", 1, "r2qk2r/p1p1p1P1/1pn4b/1N1Pb3/1PB1N1nP/8/1B1PQPp1/R3K2R b Qkq - 0 1", 39), #düzeltildi rocharde yok yanlış yazmışlar
              ("L", 2, "r1bq4/pp1p1k1p/2p2p1p/2b5/3Nr1Q1/2N1P3/PPPK1PPP/3R1B1R w - - 0 1", 51),
              ("G", 1, "r1bqkr2/pp1pbpQp/8/2p1P3/2B5/2N5/PPP2PPP/R1B1K2R b KQq - 2 10", 20),
              ("G", 2, "r2r2k1/ppp1p2p/6p1/4b1p1/PnP4P/2N4P/1P6/R3KB2 w - 0 17", 22),
              ("O", 1, "1k6/p1nrp3/n2p4/2p5/3PP3/2P2P2/P7/RN4K1 w", 14),
              ("O", 2, "8/3np3/3pk3/2p5/1PKPP3/2P2P2/8/8 w", 9),
              ("J", 1, "r3k2r/pp6/2p3Pb/2N1pP2/Q2p4/4P3/PP1K4/7R w q e6 0 34", 42), #Kalıyo R-düzeltildi
              ("J", 2, "r3k2r/pp2qppp/1np2n2/2bPp1B1/B2P2Q1/2N2N2/PPP2PPP/2KR3R b kq - 0 10", 36),
              ("H", 1, "5r2/p2Qb2p/3n1p2/3P2k1/1PB5/8/1B5P/R3K2R b KQ - 1 27", 27),
              ("H", 2, "4k2r/r2n1pbp/3B2p1/p1p3P1/2p4P/7B/PP2K3/1R4NR w k - 0 22", 34),
              ("AA", 1, "K7/8/8/pP6/8/4R3/2Pq1k2/8 w - - 0 1", 20),
              ("AA", 2, "8/5k1K/1q5P/2p5/8/5pp1/8/8 w - - 0 1", 1),
              ("AB", 1, "rnbqk3/p6P/2n1p1P1/1r3p2/8/1PN1K3/P4P2/R1BQ1BNR w q - 0 1", 47),#Kalıyo R düzeltildi
              ("AB", 2, "rnb1kbnr/p6p/Bp4p1/8/Q4p2/N2qBN2/PP3PPP/R3K2R b kq - 0 1 ", 9),
              ("S", 1, "rnbqkbnr/ppp1pppp/8/4p3/3PP3/8/PPP2PPP/RNBQKBNR b KQkq d3 0 2", 29), #Kalıyo R YANLIŞ KAALE ALMA
              ("S", 2, "r3k1nr/pppb1ppp/4q3/2b1B3/3Q1P2/2N5/PPP1P1PP/R3KB1R w KQkq - 1 10", 43),
              ("AF", 1, "8/8/4kpp1/3p4/p6P/2B4b/6P1/6K1 w - - 1 48", 17),
              ("AF", 2, "5rk1/pp4pp/4p3/2R3Q1/3n4/6qr/P1P2PPP/5RK1 w - - 2 24", 41),
              ("R", 1, "r1bqkb1r/p2p2pp/1pn2p1n/2p1p3/3P1B2/1P3N2/P1P1PPPP/RN1QKB1R w KQkq - 0 1", 34),
              ("R", 2, "2r4r/8/8/4k3/8/R7/8/4K2R w K - 0 1 Legale Züge 30", 29), #Kalıyod
              ("P", 1, "r1b1k1nr/1pp2ppp/p1p5/2b1p3/P3P3/2N2PP1/1PPP3q/R1B1KQ2 w Qkq - 0 11", 27),
              ("P", 2, "8/2p2R2/1p2p1Np/1P5k/3nr3/8/P7/2K5 w - - 0 34", 24),
              ("AH", 1, "1n1qkbnr/2pppppp/p7/p2P4/6Q1/8/PPPP1PPP/R1B1K1NR b KQk - 0 6", 16),
              ("AH", 2, "8/8/r3k3/8/8/3K4/8/8 b - - 0 31", 18),
              ("F", 1, "rnbqk2r/ppppppbp/5np1/8/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq - 2 4", 26),
              ("F", 2, "3r2k1/p6p/6p1/4b3/2P5/8/P1K3PP/5R2 w - - 5 27", 24),
              ("T", 1, "r1bqk1nr/ppp2ppp/2n1p3/3p4/1b1P1B2/4PN2/PPP2PPP/RN1QKB1R w KQkq - 3 5", 6),
              ("T", 2, "8/8/4k3/3pP3/3K4/8/8/8 b - - 12 45", 4),
              ("U", 1, "r1bq1rk1/ppp2ppp/2np1n2/3p4/2PP4/2NBPN2/PP3PPP/R1BQK2R w KQ - 4 6", 43),
              ("U", 2, "r4rk1/1pp1q1pp/2np1pn1/p3p3/2PPP3/2N1BP2/PPQ2P1P/R3K2R w KQ - 2 14", 40),
              ("U", 3, "2kr3r/1p3pp1/p1nqbn1p/3p4/3P2P1/1BN2N2/PPP1QPBP/R4RK1 w - - 0 14", 41),
              ("U", 4, "r4rk1/1bqn1ppp/p2bpn2/1p1p4/2pP4/1PNBPN2/PB3PPP/R2Q1RK1 w - - 1 12", 40),
              ("V", 1, "r1bq1rk1/ppp2ppp/2nb1n2/3pp3/2PPP3/2N2N2/PP2BPPP/R1BQ1RK1 w - - 0 10", 36),
              ("V", 2, "2kr1b1r/pp2pppp/2p5/1B6/2PPn3/8/PP3PPP/R1B1R1K1 b - - 0 14", 30),
              ("K", 1, "4k3/pp3pp1/8/8/1P2N1p1/7r/3K4/2r5 b", 41),
              ("K", 2, "r3k2r/p5pp/2p3qn/7K/6P1/2N4N/P5PP/7R w", 1),
              ("X", 1, "8/6P1/5K1k/6N1/5N2/8/8/8 w", 20), #Düzeltildi piyon değişimi
              ("X", 2, "rnbqk1nr/pppp1ppp/4p3/8/1bPP4/8/PP2PPPP/RNBQKBNR w", 4),
              ("C", 1, "r1b1kb1r/pp1p1ppp/1q3n2/2p5/4P3/2N5/PPP2PPP/R1BQKB1R w - - 0 1", 40),
              ("C", 2, "rn1qkbnr/ppp1ppp1/4b3/3pN2p/8/2N4P/PPPPPPP1/R1BQKB1R w - - 0 1", 29),
              ("M", 1, "rnbq1rk1/pp2n1pp/2p2p1b/3pp2N/2PPP3/1PN2P2/P5PP/R1BQKB1R w KQ - 0 1", 38),
              ("M", 2, "2bk2q1/8/8/8/8/8/2Q5/2R3K1 w - - 0 1", 6),
              ("Z", 1, "r1b1kb2/p2qp1pr/n1pp1n1p/1P3p2/5P1P/BPN4R/P2PP1P1/R2QKBN1 w", 33),#Kalıyo düzeltildi
              ("Z", 2, "8/3k4/8/3r4/8/3Q4/8/3K4 w", 8)]
    return boards


