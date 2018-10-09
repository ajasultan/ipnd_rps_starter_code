#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        choice = random.choice(moves)
        return choice


class CyclePlayer(Player):
    def move(self):
        self.index = 0
        if self.index > 2:
            self.index = 0
        choice = moves[self.index]
        self.index += 1
        return choice


class HumanPlayer(Player):
    def move(self):
        choice = ""
        while not (choice == 'scissors' or choice == 'paper' or choice =='rock'):
            choice = input("Select 'scissors', 'paper' or 'rock' ")
        return choice


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game_type = ""
    player_type = ""
    while not (game_type == "1" or game_type == "2" or
                game_type == "3" or game_type == "4"):
        game_type = input('''Choose what type of game you would like to play:\n
        1) RandomPlayer\n
        2) CyclePlayer\n
        3) ReflectPlayer\n
        4) HumanPlayer\n
        Note: Please Type the number and then click Enter\n''')
    if game_type == "1":
        game = Game(RandomPlayer(), RandomPlayer())
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
