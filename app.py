# Import your Game class
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase
# Create your Dunder Main statement.
if __name__ == "__main__":
# Inside Dunder Main:
## Create an instance of your Game class
    game = Game()
## Start your game by calling the instance method that starts the game loop

for phrase in game.phrases:
    print(phrase.phrase)