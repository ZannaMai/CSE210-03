import random

# Class declaration
class Card:

    ## A set of cards each with a different value 1-13, default is 0
    ## Start with 300 points

    ## Attributes:
        ## value (int): the number value of the 2 cards, where ace = 1 and king = 13
        ## points (int): start with 300 points 

    def __init__(self):

        self.value1 = 0
        self.value2 = 0
        self.points = 300

    def draw(self):
        # draw random card number and displays it
        # hilo = ''
        self.value1 = random.randint(1,13)
        # print(f"The card is {self.value1}")

        # self.value2 = random.randint(1, 13)
        # if self.value1 > self.value2:
        #     hilo = 'l'
        # else:
        #     hilo = 'h'
        # guess = input("Higher or Lower (h/l)? ")
        # self.points = self.points + 100 if guess == hilo else self.points - 75 if guess == hilo

        


