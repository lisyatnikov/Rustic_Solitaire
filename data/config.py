# main variables <- this is terrible description
clock = None

# Basic colors
BLACK = (0, 0, 0, 255)
RED = (255, 0, 0, 255)
GRAY = (100, 100, 0, 255)
GREEN = (100, 255, 100, 255)

# Window settings
size = width, height = 800, 600


'''List of playing cards'''
#setting score value of card suit
hearts = 1
diamonds = 2
clubs = 3
spades = 4
card_suit = (hearts, diamonds, clubs, spades)

# setting score value of honour cards
ace = 14
king = 13
queen = 12
jack = 11

# setting score value of pip cards
tens = 10
nines = 9
eights = 8
sevens = 7
sixes = 6
fives = 5
fours = 4
triplets = 3
deuces = 2

card_value = (ace, king, queen, jack,                                         # Honour cards
         tens, nines, eights, sevens, sixes, fives, fours, triplets, deuces)  # Pip cards

def creating_deck():
    pass
