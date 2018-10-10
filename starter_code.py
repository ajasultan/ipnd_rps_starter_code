#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.index = 0
        self.my_move = random.choice(moves)
        self.their_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


def check_winner(move1,move2):
    if beats(move1, move2):
        print('Player 1 Won!')
        return 'Player 1'
    else:
        if move1 == move2:
            print('Draw Match!')
            return 'None'
        else:
            print('Player 2 Won!')
            return 'Player 2'


class RandomPlayer(Player):
    def move(self):
        choice = random.choice(moves)
        return choice


class CyclePlayer(Player):
    def move(self):
        choice = moves[self.index]
        self.index += 1
        if self.index > 2:
            self.index = 0
        return choice


class HumanPlayer(Player):
    def move(self):
        choice = ""
        while not (choice == 'scissors' or choice == 'paper' or choice =='rock'):
            choice = input("Select 'scissors', 'paper' or 'rock'\n ")
        return choice


class ReflectPlayer(Player):
    def move(self):
        choice = self.their_move
        return choice


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        winner = check_winner(move1, move2)
        if winner == "Player 1":
            self.score_p1 += 1
        elif winner == "Player 2":
            self.score_p2 += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print(f'''Game over!
    The Score is: Player 1 ({self.score_p1}): Player 2 ({self.score_p2})''')


if __name__ == '__main__':
    game_type = ""
    player_type = ""
    print('''Here are the rules of the game: scissor cuts paper,paper covers
    rock, and rock crushes scissors. Play either "rock", "paper", or "scissors".
    The game cosists of 3 rounds!''')
    while not (game_type == "1" or game_type == "2" or
                game_type == "3" or game_type == "4"):
        game_type = input('''Choose what type of game you would like to play:\n
    1) RandomPlayer\n : Two Random Computer Players
    2) CyclePlayer\n : Two Cycle Computer Players
    3) ReflectPlayer\n : Two Reflect Computer Players
    4) HumanPlayer\n : A Human Player with another Computer Player
    Note: Please Type the number and then click Enter\n''')
    if game_type == "1":
        game = Game(RandomPlayer(), RandomPlayer())
        game.play_game()
    elif game_type == "2":
        game = Game(CyclePlayer(), CyclePlayer())
        game.play_game()
    elif game_type == "3":
        game = Game(ReflectPlayer(), ReflectPlayer())
        game.play_game()
    elif game_type == "4":
        while not (player_type == "1" or player_type == "2" or
                    player_type== "3" or player_type == "4"):
            player_type = input('''Choose who you would like to play with:\n
            1) RandomPlayer\n
            2) CyclePlayer\n
            3) ReflectPlayer\n
            Note: Please Type the number\n''')
        if  player_type == "1":
            game = Game(HumanPlayer(), RandomPlayer())
            game.play_game()
        elif  player_type == "2":
            game = Game(HumanPlayer(), CyclePlayer())
            game.play_game()
        elif  player_type == "3":
            game = Game(HumanPlayer(), ReflectPlayer())
            game.play_game()
