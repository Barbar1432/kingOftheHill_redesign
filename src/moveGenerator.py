import numpy as np
class moveGenerator:
    def __init__(self):
        return



    def get_possible_moves(self, board,sqSelected):
        row,col=sqSelected
        piece = board[row][col]

        if piece== 100 or piece ==-100:
            return self.possible_moves_pawn( board,sqSelected)
        if piece == 320 or piece ==-320:
            return self.possible_moves_knight( board,sqSelected)
        if piece == 330 or piece ==-330:
            return self.possible_moves_bishop( board,sqSelected)
        if piece == 500 or piece == -500:
            return self.possible_moves_rook(board, sqSelected)
        if piece == 900 or piece ==-900:
            return self.possible_moves_queen(board, sqSelected)
        if piece == 2000 or piece ==-2000:
            return self.possible_moves_king(board, sqSelected)
        else:
            return []

    def possible_moves_pawn(self, board,sqSelected):

        possible_moves_list =[]
        (row, column) = sqSelected
        if row == 1 and board[row][column] == -100:
            (row, column) = sqSelected
            if board[row + 1][column] == 0 and board[row + 2][column] == 0:
                possible_moves_list.append((row + 1, column))
                possible_moves_list.append((row + 2, column))
            elif board[row + 1][column] == 0 and board[row + 2][column] != 0:
                possible_moves_list.append((row + 1, column))

            if column + 1 <= 7:
                if board[row + 1][column + 1] != 0:
                    possible_moves_list.append((row + 1, column + 1))
            if column - 1 >= 0:
                if board[row + 1][column - 1] != 0:
                    possible_moves_list.append((row + 1, column - 1))

        elif (board[row][column] == -100):
            (row, column) = sqSelected
            if row + 1 <= 7:
                if board[row + 1][column] == 0:
                    possible_moves_list.append((row + 1, column))
                if column + 1 <= 7:
                    if board[row + 1][column + 1] != 0:
                        possible_moves_list.append((row + 1, column + 1))
                if column - 1 >= 0:
                    if board[row + 1][column - 1] != 0:
                        possible_moves_list.append((row + 1, column - 1))

        elif (row == 6 and board[row][column] == 100):
            (row, column) = sqSelected

            if board[row - 1][column] == 0 and board[row - 2][column] == 0:
                possible_moves_list.append((row - 1, column))
                possible_moves_list.append((row - 2, column))
            elif board[row - 1][column] == 0 and board[row - 2][column] != 0:
                possible_moves_list.append((row - 1, column))

            if column + 1 <= 7:
                if board[row - 1][column + 1] != 0:
                    possible_moves_list.append((row - 1, column + 1))
            if column - 1 >= 0:
                if board[row - 1][column - 1] != 0:
                    possible_moves_list.append((row - 1, column - 1))

        elif ( board[row][column] == 100):
            (row, column) = sqSelected
            if row - 1 >= 0:
                if board[row - 1][column] == 0:
                    possible_moves_list.append((row - 1, column))
                if column + 1 <= 7:
                    if board[row - 1][column + 1] != 0:
                        possible_moves_list.append((row - 1, column + 1))
                if column - 1 >= 0:
                    if board[row - 1][column - 1] != 0:
                        possible_moves_list.append((row - 1, column - 1))
        return possible_moves_list

    def possible_moves_bishop(self, board,sqSelected):
        possible_moves_list = []
        (row, column) = sqSelected

        while row > 0 and column < 7:  # right top
            row -= 1
            column += 1
            if board[row][column] == 0:
                possible_moves_list.append((row, column))
            elif board[row][column] != 0 :
                possible_moves_list.append((row, column))
                break
            else:
                break

        (row, column) = sqSelected

        while row < 7 and column > 0:  # sol asagi
            row += 1
            column -= 1
            if board[row][column] == 0:
                possible_moves_list.append((row, column))
            elif board[row][column] != 0 :
                possible_moves_list.append((row, column))
                break
            else:
                break

        (row, column) = sqSelected

        while row > 0 and column > 0:  # sol yukari
            row -= 1
            column -= 1
            if board[row][column] == 0:
                possible_moves_list.append((row, column))
            elif board[row][column] != 0 :
                possible_moves_list.append((row, column))
                break
            else:
                break

        (row, column) = sqSelected

        while row < 7 and column < 7:  # sag asagi
            row += 1
            column += 1
            if board[row][column] == 0:
                possible_moves_list.append((row, column))
            elif board[row][column] != 0 :
                possible_moves_list.append((row, column))
                break
            else:
                break

        (row, column) = sqSelected
        return possible_moves_list

    def possible_moves_knight(self, board,sqSelected):
        possible_moves_list =[]
        (row, column) = sqSelected

        if row - 2 >= 0 and row - 2 <= 7 and column + 1 >= 0 and column + 1 <= 7:
            possible_moves_list.append((row - 2, column + 1))

        if row - 1 >= 0 and row - 1 <= 7 and column + 2 >= 0 and column + 2 <= 7:
            possible_moves_list.append((row - 1, column + 2))

        if row + 1 >= 0 and row + 1 <= 7 and column + 2 >= 0 and column + 2 <= 7:
            possible_moves_list.append((row + 1, column + 2))

        if row + 2 >= 0 and row + 2 <= 7 and column + 1 >= 0 and column + 1 <= 7:
            possible_moves_list.append((row + 2, column + 1))

        if row - 2 >= 0 and row - 2 <= 7 and column - 1 >= 0 and column - 1 <= 7:
            possible_moves_list.append((row - 2, column - 1))

        if row - 1 >= 0 and row - 1 <= 7 and column - 2 >= 0 and column - 2 <= 7:
            possible_moves_list.append((row - 1, column - 2))

        if row + 2 >= 0 and row + 2 <= 7 and column - 1 >= 0 and column - 1 <= 7:
            possible_moves_list.append((row + 2, column - 1))

        if row + 1 >= 0 and row + 1 <= 7 and column - 2 >= 0 and column - 2 <= 7:
            possible_moves_list.append((row + 1, column - 2))
        return possible_moves_list

    def possible_moves_queen(self, board,sqSelected):
        (row, column) = sqSelected

        possible_moves_list =[]


        for i in range(column + 1, len(board[0])):
            if board[row][i] == 0:  # empty square
                possible_moves_list.append((row, i))
            elif ((board[row][i] > 0 and board[row][column]>0) or (board[row][i] < 0 and board[row][column]<0) ):
                break
            elif ( (board[row][i] > 0 and board[row][column]<0) or (board[row][i] < 0 and board[row][column]>0)) :
                possible_moves_list.append((row, i))
                break

            # Check moves to the left
        for i in range(column - 1, -1, -1):
            # if board[row][i] ==0:  # empty square
            if board[row][i] ==0:  # empty square
                possible_moves_list.append((row, i))
            elif (board[row][i] > 0 and board[row][column] > 0) or (board[row][i] < 0 and board[row][column] < 0):
                break
            elif (board[row][i] > 0 and board[row][column] < 0) or (board[row][i] < 0 and board[row][column] > 0):
                possible_moves_list.append((row, i))
                break

            # Check moves down
        for i in range(row + 1, len(board)):
            # if board[i][column] ==0:  # empty square
            if board[i][column] ==0:  # empty square
                possible_moves_list.append((i, column))
            elif (board[i][column] > 0 and board[row][column] > 0) or (board[i][column] < 0 and board[row][column] < 0):
                break
            elif(board[i][column] > 0 and board[row][column] < 0) or (board[i][column] < 0 and board[row][column] > 0):
                possible_moves_list.append((i, column))
                break

            # Check moves up
        for i in range(row - 1, -1, -1):
            # if board[i][column] ==0:  # empty square
            if board[i][column] ==0:  # empty square
                possible_moves_list.append((i, column))
            elif (board[i][column] > 0 and board[row][column] > 0) or (board[i][column] < 0 and board[row][column] < 0):
                break
            elif (board[i][column] > 0 and board[row][column] < 0) or (board[i][column] < 0 and board[row][column] > 0):
                possible_moves_list.append((i, column))
                break


        (r, c) = sqSelected

        while r > 0 and c < 7:  # right top
            r -= 1
            c += 1
            if board[r][c] == 0:
                possible_moves_list.append((r, c))
            elif (board[r][c] > 0 and board[row][column] > 0) or (board[r][c] < 0 and board[row][column] < 0):
                break
            elif (board[r][c] > 0 and board[row][column] < 0) or (board[r][c] < 0 and board[row][column] > 0):
                possible_moves_list.append((r, c))
                break

        (r, c) = sqSelected

        while r < 7 and c > 0:  # sol asagi
            r += 1
            c -= 1
            if board[r][c] == 0:
                possible_moves_list.append((r, c))
            elif board[r][c] != 0 and ((board[row][column] >0 and board[r][c]<0 )or (board[row][column] <0 and board[r][c]>0)):
                possible_moves_list.append((r, c))
                break
            else:
                break

        (r, c) = sqSelected

        while r > 0 and c > 0:  # sol yukari
            r -= 1
            c -= 1
            if board[r][c] == 0:
                possible_moves_list.append((r, c))
            elif board[r][c] != 0 and ((board[row][column] >0 and board[r][c]<0 )or (board[row][column] <0 and board[r][c]>0)):
                possible_moves_list.append((r, c))
                break
            else:
                break

        (r, c) = sqSelected

        while r < 7 and c < 7:  # sag asagi
            r += 1
            c += 1
            if board[r][c] == 0:
                possible_moves_list.append((r, c))
            elif board[r][c] != 0 and ((board[row][column] > 0 and board[r][c] < 0) or (board[row][column] < 0 and board[r][c] > 0)):
                possible_moves_list.append((r, c))
                break
            else:
                break

        (r, c) = sqSelected
        return possible_moves_list
    def possible_moves_rook(self, board,sqSelected):
        (row, column) = sqSelected
        possible_moves_list = []

        for i in range(column + 1, len(board[0])):
            if board[row][i] ==0 : # empty square
                possible_moves_list.append((row, i))
            elif (board[row][i] > 0 and board[row][column] > 0) or (board[row][i] < 0 and board[row][column] < 0):
                break
            elif (board[row][i] > 0 and board[row][column] < 0) or (board[row][i] < 0 and board[row][column] > 0):
                possible_moves_list.append((row, i))
                break

            # Check moves to the left
        for i in range(column - 1, -1, -1):
            # if board[row][i] is None:  # empty square
            if board[row][i] ==0:  # empty square
                possible_moves_list.append((row, i))
            elif (board[row][i] > 0 and board[row][column] > 0) or (board[row][i] < 0 and board[row][column] < 0):
                break
            elif (board[row][i] > 0 and board[row][column] < 0) or (board[row][i] < 0 and board[row][column] > 0):
                possible_moves_list.append((row, i))
                break

            # Check moves down
        for i in range(row + 1, len(board)):
            # if board[i][column] is None:  # empty square
            if board[i][column] ==0:  # empty square
                possible_moves_list.append((i, column))
            elif (board[i][column] > 0 and board[row][column] > 0) or (board[i][column] < 0 and board[row][column] < 0):
                break
            else:
                possible_moves_list.append((i, column))
                break

            # Check moves up
        for i in range(row - 1, -1, -1):
            # if board[i][column] is None:  # empty square
            if board[i][column] == 0:  # empty square
                possible_moves_list.append((i, column))
            elif (board[i][column] > 0 and board[row][column] > 0) or (board[i][column] < 0 and board[row][column] < 0):
                break
            else:
                possible_moves_list.append((i, column))
                break


        return possible_moves_list


    def possible_moves_king(self, board,sqSelected):
        (row, column) = sqSelected
        possible_moves_list =[]
        try:
            possible_moves_list.append((row + 1, column))
        except IndexError:
            pass
        try:
            possible_moves_list.append((row - 1, column))
        except IndexError:
            pass
        try:
            possible_moves_list.append((row, column - 1))
        except IndexError:
            pass
        try:
            possible_moves_list.append((row, column + 1))
        except IndexError:
            pass
        try:
           possible_moves_list.append((row - 1, column + 1))
        except IndexError:
            pass
        try:
            possible_moves_list.append((row + 1, column - 1))
        except IndexError:
            pass
        try:
            possible_moves_list.append((row + 1, column + 1))
        except IndexError:
            pass
        try:
            possible_moves_list.append((row - 1, column - 1))
        except IndexError:
            pass
        return possible_moves_list

    def legalMoves(self,board,positions,isMax,can_castle_right,can_castle_left):
            legalMoves = {}

            row_indices, col_indices = positions
            x = self.castling_eligible(board, isMax, can_castle_right,can_castle_left)

            for row, col in zip(row_indices, col_indices):
                pos = (row, col)
                possible_moves_list= self.get_possible_moves(board,pos)
                legalMoves[pos] = []
                for pM in possible_moves_list:

                    if (self.isLegal(pos, pM,board,isMax,possible_moves_list) and self.is_king_threatened( pos, pM,isMax,board)==False):
                        legalMoves[pos].append(pM)

            if x is not None :
                kR, kC = x
                legalMoves[(kR,4)].append(x)
            return legalMoves


    def isLegal(self, start_pos, dest_pos,board,isMax,possible_moves_list):
        start_row, start_col = start_pos
        dest_row, dest_col = dest_pos
        if not (0 <= start_row < len(board) and 0 <= start_col < len(board[0])):
            return False
        if not (0 <= dest_row < len(board) and 0 <= dest_col < len(board[0])):
            return False
        if (isMax and board[start_row][start_col]<0):
            return False
        if (isMax == False and board[start_row][start_col]>0):
            return False
        start = board[start_row][start_col] # start is a piece
        dest = board[dest_row][dest_col] # dest can either be a square (None) or a piec
        if start ==0 : # look if there actually is a piece on the start square
            return False
        if not possible_moves_list.__contains__(dest_pos) : # look if the destination is a possible move for the piece
            return False

        if dest != 0:
               if board[start_row][start_col]<0 and board[dest_row][dest_col]>0:
                  return True
               if  board[start_row][start_col]> 0 and  board[dest_row][dest_col]<0 :
                    return True
        else :
            return True

    def is_king_threatened(self, start_pos, des_pos,isMax,board):
        if isMax:
           kingPos = np.where (board==2000)
           positions =np.where (board<0)
        if isMax==False:
            kingPos = np.where(board == -2000)
            positions = np.where(board >0)
        king_row = kingPos[0].item()
        king_col = kingPos[1].item()
        king = (king_row,king_col)
        row, column = start_pos
        a, b = des_pos
        dest = board[a][b]
        pinned = board[row][column]
        if (start_pos == king):
            king = (a,b)
            king_row=a
            king_col=b
        board[row][column] = 0
        board[a][b] = pinned
        row_indices, col_indices = positions
        for x, y in zip(row_indices, col_indices):

                sq = (x, y)
                if  self.get_possible_moves(board,sq).__contains__(king):
                    board[row][column] = pinned
                    board[a][b] = dest
                    return True

        board[row][column] = pinned
        board[a][b] = dest
        return False

    def castling_eligible (self,board,isMax,can_castle_right,can_castle_left):
        row= 0
        if isMax:
            row = 7
        if isMax == False:
            row = 0
        if ((board[row][5]!= 0 or board[row][6]!=0) and (board[row][3]!= 0 or board[row][2]!=0 )):
                return None
        if can_castle_right== False and can_castle_left==False:
            return None

        if(board[row][5] == 0 and board[row][6] == 0):
               if( self.is_king_threatened((row,4),(row,5),isMax,board) == False) and (self.is_king_threatened((row,4),(row,6),isMax,board)== False):
                  return (row,6)
        if (board[row][3] == 0 and board[row][2] == 0):
                if (self.is_king_threatened((row, 4), (row, 3), isMax, board) == False) and (self.is_king_threatened((row, 4), (row, 2), isMax, board) == False):
                    return (row, 2)






