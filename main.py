import numpy as np
import random
import pickle

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)  # 0: empty, 1: X (agent), 2: O (opponent)
        self.done = False
        self.game_over = False
        self.winner = None
        self.current_player = 1  # X starts
    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        return self.get_state()
    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.done = False
        self.winner = None
        return self.get_state()

    def get_state(self):
        return tuple(self.board.flatten())

    def available_actions(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def step(self, action, player):
        i, j = action
        self.board[i, j] = player
        reward = 0

        # Check for win
        if self.check_win(player):
            self.done = True
            self.winner = player
            reward = 1 if player == 1 else -1
        # Check for draw
        elif len(self.available_actions()) == 0:
            self.done = True
            reward = 0.5

        return self.get_state(), reward, self.done
     
    def available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def make_move(self, move):
        if move in self.available_moves():
            self.board[move] = self.current_player
            self.current_player = -self.current_player
            return True
        return False

    def check_winner(self):
        # Check rows, columns, diagonals
        for i in range(3):
            if abs(sum(self.board[i, :])) == 3:
                return self.board[i, 0]
            if abs(sum(self.board[:, i])) == 3:
                return self.board[0, i]
        if abs(sum(self.board.diagonal())) == 3:
            return self.board[0, 0]
        if abs(sum(np.fliplr(self.board).diagonal())) == 3:
            return self.board[0, 2]
        if not self.available_moves():
            return 0  # Draw
        return None  # Game ongoing

    def print_board(self):
        symbols = {0: '.', 1: 'X', -1: 'O'}
        for row in self.board:
            print(' '.join(symbols[cell] for cell in row))
        print()


    def check_win(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i, :] == player) or all(self.board[:, i] == player):
                return True
        if all(self.board.diagonal() == player) or all(np.fliplr(self.board).diagonal() == player):
            return True
        return False

    def check_game_over(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if abs(sum(self.board[i, :])) == 3:
                self.game_over = True
                self.winner = int(self.board[i, 0])
                return
            if abs(sum(self.board[:, i])) == 3:
                self.game_over = True
                self.winner = int(self.board[0, i])
                return
        if abs(sum(self.board.diagonal())) == 3:
            self.game_over = True
            self.winner = int(self.board[0, 0])
            return
        if abs(sum(np.fliplr(self.board).diagonal())) == 3:
            self.game_over = True
            self.winner = int(self.board[0, 2])
            return
        if not self.available_actions():
            self.game_over = True
            self.winner = 0  # Draw

    def get_reward(self, player):
        if self.game_over:
            if self.winner == player:
                return 1  # Win
            elif self.winner == -player:
                return -1  # Loss
            else:
                return -0.5  # Draw
        return 0  # Ongoing game
