# Create your Phrase class logic here.
class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")

    def check_guess(self, guess):
        lil_phrase = self.phrase
        big_guess = guess.lower()
        return big_guess in lil_phrase

    def check_complete(self, guesses):
        big_phrase = self.phrase
        for character in big_phrase:
            if character.isalpha() and character not in guesses:
                return False
        return True

