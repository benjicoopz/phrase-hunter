# Create your Game class logic in here.
from phrasehunter.phrase import Phrase
import random


class Game():

    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = None
        self.guesses = [" "]

    def start(self):
        pass

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
        pass

    def get_guess(self):
        pass

    def game_over(self):
        pass
