from game.card import Card

class Director:

    """A person who directs the game.
    
    Responsibility of a director is to control the sequence of play. 
    
    Attributes: 
        cards (list[card]): a list of the 2 cards
        is_playing (boolean): whether or not the game is being played. 
        score (int): The score for one round of play. 
        total_score: The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director
        
        Args:
            self (Director): an instance of Director.
        """

        self.cards = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range (1):
            card = Card()
            self.cards.append(card)


    def start_game(self):
        """Starts the game by running the main loop.
        
        Args:
            self (Director): and instance of Director
        """
        while self.is_playing:
            print(f"The first card is: {self.cards[0]}")
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user """
        guess = input("Is the next card higher or lower (h/l)?")
        return guess


    def do_updates(self):
        """Updates the player's score. 
        
        Args: 
            self (Director): ...
        """
        if self.cards[0] < self.cards[1]:
            hilo = 'h'
        else:
            hilo = 'l'

        # if not self.is_playing:
        #     return
        
        # for i in range(2):
        #     pass
