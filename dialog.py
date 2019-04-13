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
	#x = input()
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
	return input("Your choice: ")

def enter_color():
	"""To choose a color pair"""
	return input('Enter a color pair: ')

def enter_player():
	"""To choose a player"""
	return input("Enter the player name who you would like to request: ")

def error(err_code = ''):
	"""Something unexcepted happened"""
	print("There is an error. Please retry.")

def choose_card(Deck):
	"""Choose a card to discard; used in case 1 & 2"""
	print("Choose a card to discard: ")
	print_deck(Deck)
	return input("Your choice: ")

def player_list(exclude = []):
	"""Print a player list excluding <exclude>"""


def return_result(code, FORMAT):
	"""Print the query result
	FORMAT = (The target player, The target color, # of given cards/ list of given cards)
	"""
	if code == 1:
		print(FORMAT[0] + ' has ' + str(FORMAT[2])+ ' ' + colorize[FORMAT[1]] + unzip_color[FORMAT[1]] + Back.BLACK + ' cards.')
	elif code == 2:
		print(FORMAT[0] + ' gives you ' + str(FORMAT[2][0])+ ' ' + colorize[FORMAT[1]] + unzip_color[FORMAT[1]] + Back.BLACK + ' cards:')
		print_deck(FORMAT[2][1])
	elif code == 5:
		if FORMAT[2] == True:
			print(FORMAT[0].name + ' has guess the correct answer: ' + FORMAT[1] + '!')
		else:
			print(FORMAT[0].name + ' has guess the wrong answer: ' + FORMAT[1] + '.')
