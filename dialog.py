"""This file puts all frontend dialog that might be needed"""
import player
import time
from colorama import init, Back
init()	# Initialize colorama

# Dict for converting abbr. colors to colorama code
colorize = {'B':Back.BLUE, 'G':Back.GREEN, 'Y':Back.YELLOW, 'R':Back.RED}


def start_game():
	"""Starting a new game, entering initials"""
	print("Enter your name: ", end = '')
	#x = str(input())
	#print("Hello, " + x + "!" )
	time.sleep(1)

	# Return x so that player.py can read the name

def print_deck(Deck):
	"""Print content of player.Deck"""
	for cards in Deck.card_list():
		print(colorize[cards[2]] + cards[0], end = '')
		print(Back.BLACK + ' ', end = '')
	print()

def options(playerX):
	"""Print player X's hand, other player's # of cards, their direction (counterclockwise order)"""
	print("|****************************************************|")
	print("|                                                    |")	
	print("|                                                    |")	
	print("|                                                    |") 
	print("|                                                    |")  
	print("|                                                    |") 
	print("|                                                    |") 
	print("|                                                    |")
	print("|                                                    |")
	print("|                                                    |")
	print("|                                                    |")
	print("|                                                    |")
	print("|****************************************************|")
