"""This file puts all frontend dialog that might be needed"""
import player
import time
import os
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

	# todo: Return x so that player.py can read the name

def print_deck(player):
	"""Print content of player.hand"""
	i = 0
	for cards in player.hand:
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
	print("Enter a color pair: ")
	return input()

def error():
	"""Something unexcepted happened"""
	print("There is an error.")