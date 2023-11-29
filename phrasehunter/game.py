# Create your Game class logic in here.
from phrasehunter.phrase import Phrase
import random
import sys


class Game():

    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f"Number missed: {self.missed}")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()

    @staticmethod
    def create_phrases():
        return [
            Phrase("hello world"),
            Phrase("there is no trying"),
            Phrase("may the force be with you"),
            Phrase("you have to see the matrix for yourself"),
            Phrase("life is like a box of chocolates")
        ]

    def get_random_phrase(self):
        phrase_object = random.choice(self.phrases)
        return phrase_object

    def welcome(self):
        print("------------------------")
        print("Welcome to Phrase-Hunter")
        print("------------------------")

    def get_guess(self):
        while True:
            user_input = input("\nEnter a Letter: ").lower()
            if user_input.isalpha() and len(user_input) == 1 and user_input not in self.guesses:
                return user_input
            else:
                print("ooh So Close! Try a Single Letter that Hasn't Been Guessed!")

    def reset_game(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def game_over(self):
        if self.missed == 5:
            print("\nGAME OVER")
        else:
            print("\nEPIC!! YOU WIN!!!")

        game2 = input("\nPLAY AGAIN?(y/n)   ")
        if game2 == "Y".lower():
            self.reset_game()
            self.start()
        else:
            print("\nThanks for Playing!")
            sys.exit()
