import numpy as np
import random
import math
from moveGenerator import moveGenerator
from evaluation import evaluation


class Node:
    def __init__(self, isMax, move_count, move=None, parent=None):
        self.move = move
        self.parent = parent
        self.children = []
        self.isMax = isMax
        self.move_count = move_count
        self.wins = 0
        self.visits = 0

    def add_child(self, child_move, isMax, move_count):
        child = Node(isMax, move_count, child_move, self)
        self.children.append(child)

    def update(self, result):
        self.visits += 1
        self.wins += result

    def select_child(self):
        exploration_constant = 2
        if self.isMax:
            best_score = float('-inf')
        else:
            best_score = float('inf')
        best_child = None

        for child in self.children:
            if child.visits == 0:
                if self.isMax:
                    score = float('inf')
                else:
                    score = float('-inf')
            else:
                score = (child.wins / child.visits) + exploration_constant * \
                        math.sqrt((np.log(self.visits)) / child.visits)
            if self.isMax:
                if score > best_score:
                    best_score = score
                    best_child = child
            else:
                if score < best_score:
                    best_score = score
                    best_child = child

        return best_child


def simulate_game(node, horizont):
    move_generator = moveGenerator()
    eval = evaluation()
    result = game_over(node.move, node.isMax, move_generator)
    i = 0
    chess_board = np.copy(node.move)
    isMax = node.isMax
    move_count = node.move_count
    while not result and i < horizont:
        # Random choice
        best_move = random.choice(list(generate_child_node(chess_board, isMax)))
        new_child_node = np.copy(chess_board)
        move_piece_monte_carlo(best_move[0], best_move[1], new_child_node)
        chess_board = new_child_node

        isMax = not isMax
        node.move_count += 1
        i += 1
        result = game_over(chess_board, isMax, move_generator)

    if result == 0:
        if isMax:
            return eval.board_evaluation(chess_board, move_count)
        else:
            return (-1) * eval.board_evaluation(chess_board, move_count)
    else:
        return result


def backpropagate(node, result):
    while node is not None:
        node.update(result)
        node = node.parent


def monte_carlo_tree_search(root, horizont):
    for _ in range(horizont):
        node = root

        # Selection
        while node.children:
            node = node.select_child()

        # Expansion
        if node.visits > 0:
            child_states = generate_child_node(node.move, node.isMax)
            # For each possible move create a child node
            if child_states:
                for child_state in child_states:
                    #print("Added a possible move node\n")
                    child_move = np.copy(node.move)
                    move_piece_monte_carlo(child_state[0], child_state[1], child_move)
                    node.add_child(child_move, not node.isMax, node.move_count + 1)
                node = node.children[-1]
            # If no possible moves
            else:
                return 0
        # Simulation
        result = simulate_game(node, 5)
        #print("Current Node:\n ", node.move)
        #print("Returned result: \n", result)

        # Backpropagation
        backpropagate(node, result)

    best_child = root.children[0]
    for child in root.children:
        if child.visits > best_child.visits:
            best_child = child
    #print("Found the best child: \n", best_child.move)
    #print("Result and VisitCount: \n", best_child.wins, best_child.visits)
    return best_child


def generate_child_node(node, isMax):
    child_node_list = []
    positions = np.where(node > 0) if isMax else np.where(node < 0)
    move_generator = moveGenerator()
    move_dict = move_generator.legalMovesProcess(node, positions, isMax)
    for key, value_list in move_dict.items():
        for value in value_list:
            child_node_list.append((key, value))  # Store the selected and destination
    return child_node_list


def game_over(chess_board, is_max, move_generator):
    center = [(3, 3), (3, 4), (4, 3), (4, 4)]
    for pos in center:
        r, c = pos
        if chess_board[r][c] == 2000:
            return 1000
        elif chess_board[r][c] == -2000:
            return -1000
    if is_max:
        positions = np.where(chess_board > 0)
        moves = move_generator.legalMovesProcess(chess_board, positions, is_max)
        if all(element == [] for element in list(moves.values())):
            return -500
    else:
        positions = np.where(chess_board < 0)
        moves = move_generator.legalMovesProcess(chess_board, positions, is_max)
        if all(element == [] for element in list(moves.values())):
            return 500

    return 0


def move_piece_monte_carlo(selected, destination, node):
    from_row, from_col = selected
    to_row, to_col = destination
    piece_value = node[from_row][from_col]
    node[to_row][to_col] = piece_value
    node[from_row][from_col] = 0


def bot_play_monte_carlo(chess_board, isMax, move_count, horizont):
    root = Node(isMax, move_count, chess_board)
    return monte_carlo_tree_search(root, horizont)



