"""This file puts all frontend dialog that might be needed"""
import player
import medium
import time
import os
from colorama import init, Back
init()	# mediumialize colorama

# Dict for converting abbr. colors to colorama code
colorize = {'B':Back.BLUE, 'G':Back.GREEN, 'Y':Back.YELLOW, 'R':Back.RED}
unzip_color = {'B':'BLUE', 'G':'GREEN', 'Y':'YELLOW', 'R':'RED'}

def start_game():
	"""Starting a new game, entering mediumials"""
	x = input("Enter your name: ")
	print("Hello, " + x + "!" )
	time.sleep(1)
	return x

	# todo: Return x so that player.py can read the name

def print_deck(hand, vert = '\n'):
	"""Print content of hand"""
	i = 0
	for cards in hand:
		print("#" + str(i) + ": " + colorize[cards.color] + cards.name, end = '')
		print(Back.BLACK, end = vert)
		i += 1
	print()

def status(playerX):
	"""Print player X's hand, other player's # of cards, their direction (counterclockwise order)"""
	print("|****************************************************|")
	print(playerX.name + "'s turn:")
	print("Current hand: ", end = '')
	print_deck(playerX.hand)
	print("|****************************************************|")

def enter_options():
	"""List out all actions, return the action number"""
	print("Choose an action below:")
	print("1: Give A, ask how many B")
	print("2: Give A, take all B")
	print("3: Take one of A and/or B")
	print("4: Take all of A or B")
	print("5: Guess the answer")
	return input("Your choice: ")

def enter_color():
	"""To choose a color pair"""
	return input('Enter a color pair: ')

def enter_player(lst, exclude = []):
	"""To choose a player"""
	print("Enter the player name who you would like to request(", end = '')
	for players in lst:
		if players == lst[-1]:
			print(players, end = '): ')
		else:
			print(players, end = '/')
	return input()

def error(err_code = ''):
	"""Something happened"""
	print("There is an error: " + err_code + ". Please retry. ")

def choose_card(Deck):
	"""Choose a card to discard; used in case 1 & 2"""
	print("Choose a card to discard: ")
	print_deck(Deck)
	return input("Your choice: ")

def choose_color(color_deck1, color_deck2):
	print("You must choose between 2 different colors hands")
	print("DECK 1:")
	print_deck(color_deck1, ' ')
	print("OR DECK2:")
	print_deck(color_deck2, ' ')
	return input("Your choice (1 or 2): ")


def return_result(code, FORMAT = []):
	"""Print the query result
	FORMAT = (Asker(PLAYER), receiver(STR), # of cards), except case 5
	"""
	print(Back.RED)
	if code == 1:
		print(FORMAT[0].name + ' gives ' + FORMAT[1] + ' 1 card.')
		print(FORMAT[1] + ' has ' + str(FORMAT[2])+ ' card(s) of that color.')
	elif code == 2:
		print(FORMAT[0].name + ' gives ' + FORMAT[1] + ' 1 card.')
		print(FORMAT[1] + ' gives ' + FORMAT[0].name + ' ' + str(FORMAT[2]) + ' cards.')
	elif code == 3:
		print(FORMAT[1] + ' gives ' + FORMAT[0].name + ' ' + str(FORMAT[2]) + ' cards.')
	elif code == 4:
		print(FORMAT[1] + ' gives ' + FORMAT[0].name + ' ' + str(FORMAT[2]) + ' cards.')
	elif code == 5:
		if FORMAT[2] == True:
			print(FORMAT[0].name + ' has guess the correct answer: ' + FORMAT[1] + '!')
			print(Back.BLACK)
			return 100
		else:
			print(FORMAT[0].name + ' has guess the wrong answer: ' + FORMAT[1] + '.')
			print(FORMAT[0].name + ' will no longer to do any actions.')
	elif code == -1:
		error(FORMAT)
	print(Back.BLACK)
	input("Press Enter to continue... ")
	os.system('cls' if os.name == 'nt' else 'clear')
	return code

def current_score(lst):
	print("Current scoresheet: ")
	for pls in lst:
		print(medium.players[pls].name + ": " + str(medium.players[pls].points) + " point(s)")
	input("Press Enter to continue... ")
	os.system('cls' if os.name == 'nt' else 'clear')
