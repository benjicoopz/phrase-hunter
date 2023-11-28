# Create your Game class logic in here.
from phrasehunter.phrase import Phrase
import random


class Game():

    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def start(self):
        self.welcome()
        print(f"Number missed: {self.missed}")
        self.active_phrase.display(self.guesses)
        user_guess = self.get_guess()
        self.guesses.append(user_guess)
        print(user_guess)
        self.active_phrase.display(self.guesses)

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
        return input("\nEnter a letter: ")

    def game_over(self):
        pass
