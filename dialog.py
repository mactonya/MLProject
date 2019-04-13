"""This file puts all frontend dialog that might be needed"""
import player
import time
import os
from colorama import init, Back
init()	# Initialize colorama

# Dict for converting abbr. colors to colorama code
colorize = {'B':Back.BLUE, 'G':Back.GREEN, 'Y':Back.YELLOW, 'R':Back.RED}
unzip_color = {'B':'BLUE', 'G':'GREEN', 'Y':'YELLOW', 'R':'RED'}

def start_game():
	"""Starting a new game, entering initials"""
	print("Enter your name: ", end = '')
	#x = str(input())
	#print("Hello, " + x + "!" )
	time.sleep(1)

	# todo: Return x so that player.py can read the name

def print_deck(hand):
	"""Print content of hand"""
	i = 0
	for cards in hand:
		print("#" + str(i) + ": " + colorize[cards.color] + cards.name, end = '')
		print(Back.BLACK)
		i += 1
	print()

def status(playerX):
	"""Print player X's hand, other player's # of cards, their direction (counterclockwise order)"""
	print("|****************************************************|")
	print(playerX.name + "'s turn:")
	print("Current hand: ", end = '')
	print_deck(playerX.hand)
	print("|****************************************************|")
	os.system('cls' if os.name == 'nt' else 'clear')

def enter_options():
	"""List out all actions, return the action number"""
	print("Choose an action below:")
	print("1: Give A, ask how many B")
	print("2: Give A, take all B")
	print("3: Take one of A and/or B")
	print("4: Take all of A or B")
	print("5: Guess the answer")
	print("Your choice: ", end = '')
	return input()

def enter_color():
	"""To choose a color pair"""
	print("Enter a color pair: ", end = '')
	return input()

def enter_player():
	"""To choose a player"""
	print("Enter the player name who you would like to request: ", end = '')
	return input()

def error(err_code = ''):
	"""Something unexcepted happened"""
	print("There is an error. Please retry.")

def choose_card(Deck):
	"""Choose a card to discard; used in case 1 & 2"""
	print("Choose a card to discard: ")
	print_deck(Deck)
	print("Your choice: ", end = '')
	return input()

def return_result(FORMAT):
	if FORMAT[0] == 1:
		print(FORMAT[1] + ' has ' + FORMAT[3] + ' ' + colorize[FORMAT[2]] + unzip_color[FORMAT[2]] + Back.BLACK + ' cards.')
