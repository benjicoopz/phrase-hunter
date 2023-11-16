# Create your Game class logic in here.

class Game():
    phrases = ["Embrace the glorious mess that you are", "Elevate your mindset and your altitude will follow", "Dance with the waves move with the sea", "In a world where you can be anything be kind", "life is about balance"]

    def __init__(self):
        self.missed = 0
        self.active_phrase = None
        self.guesses = [" "]
    
        
