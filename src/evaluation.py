import numpy as np

from PST import PST
class evaluation:
    def __init__(self):
        return
    def board_evaluation(self,board,move_count):
        whitePoints = 0
        blackPoints = 0
        print(move_count)
        pst = PST()
        black_positions = np.where(board < 0)
        white_positions = np.where(board > 0)
        row_indices, col_indices = white_positions
        for row, col in zip(row_indices, col_indices):
            piece = board[row][col]
            whitePoints += piece
            table = pst.piece_tables[piece]
            if  move_count >30 and piece==2000:
                table = pst.piece_tables_midGame[2000]
            whitePoints += table[row][col]
            whitePoints += self.center_control_heuristics(row, col)
            if (piece == 100):
              whitePoints+= self.white_pawn_heuristics(row,col,board)
            if (piece==2000):
                whitePoints+= self.king_safety_heuristics(row,col,board)
            if piece==500:
                whitePoints+= self.rook_heuristics(board,row,col)



        rindices, cindices = black_positions
        for r, c in zip(rindices, cindices):
            piece = board[r][c]
            blackPoints += abs(piece)
            table = pst.piece_tables[piece]
            if move_count > 30 and piece == -2000:
                table = pst.piece_tables_midGame[-2000]
            blackPoints += table[r][c]
            blackPoints+=self.center_control_heuristics(r, c)
            if (piece == -100):
                blackPoints += self.black_pawn_heuristics(r, c, board)
            if (piece == -2000):
                blackPoints += self.king_safety_heuristics(r, c, board)
            if piece == -500:
                blackPoints += self.rook_heuristics(board, r, c)
        evaluation = (whitePoints - blackPoints)
        evaluation= evaluation+self.bishop_heuristics(board)  +self.mobility_heuristics(evaluation,white_positions,black_positions)

        return evaluation
    def rook_heuristics(self,board,row,col):
        points = 0
        white_pawns_col = np.where(board== 100)[1]  # Accessing column indices using [1]
        black_pawns_col = np.where( board== -100)[1]  # Accessing column indices using [1]
        # Check for open files
        if np.sum(white_pawns_col == col) + np.sum(black_pawns_col == col) == 0:
            points = 5
        # Check for semi-open files
        if np.sum(white_pawns_col == col) + np.sum(black_pawns_col == col) == 1:
            points = 2.5
        return points
    def center_control_heuristics(self, row, col):
        points = 0
        central_squares = [(3, 3), (3, 4), (4, 3), (4, 4)]
        neighbor_squares = [(2, 2), (2, 3), (2, 4), (3, 2), (3, 5), (4, 2), (4, 5), (5, 2), (5, 3), (5, 4)]
        if (row, col) in central_squares:
            points += 10
        if (row, col) in neighbor_squares:
            points += 5
        return points
    def king_safety_heuristics (self,row,col,board):
        # Evaluate king's pawn cover
     points = 0
     pawn_cover = 0
     try:
        if board[row][col] > 0:  # White king
            pawn_cover = np.sum(board[row - 1, col - 1:col + 2] < 0)
            points = pawn_cover * 5
            return points
        else:  # Black king
            pawn_cover = np.sum(board[row + 1, col - 1:col + 2] > 0)
            points = pawn_cover * 5
        # check for opponent pieces in kings vicinity
        subarea = board[max(row - 1, 0):min(row + 2, board.shape[0]), max(col - 1, 0):min(col + 2, board.shape[1])]
        if board[row][col] > 0:  # White king
            opponent_pieces = np.sum(subarea < 0) / 100
        else:  # Black king
            opponent_pieces = np.sum(subarea > 0) / 100
        points -= opponent_pieces
     except IndexError:
            pass  # out of bounds errror
     return points
    def bishop_heuristics (self,board):
        whitepoints = 0
        blackpoints =0
        if (len(np.where(board==330))==2):
            whitepoints = 5
        if (len(np.where(board==-330))==2):
            blackpoints = 5
        points = whitepoints-blackpoints
        return points
    def white_pawn_heuristics(self,row,col, board):
        points = 0
        piece = board[row][col]
        try:
            temp = board[row + 1][col]
            if temp == 100:
                points -= 10  # double pawn check
            if board[row + 1][col + 1] == 100:
                if board[row + 2][col + 2] == 100:  # Pawn chain check
                    points += 10

            if board[row + 1][col - 1] == 100:
                if board[row + 2][col - 2] == 100:  # Pawn chain check
                    points += 10

            if board[row ][col - 1] != 100 and board[row ][col +1] != 100 and board[row +1][col - 1] != 100 and board[row+1 ][col +1] != 100:
                    points -= 7.5
                    # isolated pawn check

        except IndexError:
            pass  # out of bounds errror
        return points

    def mobility_heuristics(self,eval,white_pos,black_pos):
        white_piece_count = len(white_pos)
        black_piece_count = len(black_pos)
        if white_piece_count> black_piece_count and eval>0:
             return 5

        if white_piece_count < black_piece_count and eval < 0:
            return -5
        else :
            return 0

    def black_pawn_heuristics(self,row,col, board):
        points = 0
        piece = board[row][col]
        try:
            temp = board[row + 1][col]
            if temp == -100:
                points -= 10  # double pawn check

            if board[row + 1][col + 1] == -100:
                if board[row + 2][col + 2] == -100:  # Pawn chain check
                    points += 10

            if board[row + 1][col - 1] == 100:
                if board[row + 2][col - 2] == -100:  # Pawn chain check
                    points += 10

            if board[row ][col - 1] != -100 and board[row ][col +1] != -100 and board[row -1][col - 1] != -100 and board[row-1 ][col +1] != -100:

                    points -= 7.5

                    # isolated pawn check

        except IndexError:
            pass  # out of bounds errror
        return points



































