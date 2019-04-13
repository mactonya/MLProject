"""Intermediate level for processing init and other judging stuffs """

import player
import random

# Start initialize
global_deck = player.Deck()
def new_deck():
	global_deck.add(player.Card('B', 1, "Water"))
	global_deck.add(player.Card('B', 2, "Water"))
	global_deck.add(player.Card('B', 3, "Water"))
	global_deck.add(player.Card('B', 4, "Water"))
	global_deck.add(player.Card('B', 5, "Water"))
	global_deck.add(player.Card('G', 6, "Chimaphila"))
	global_deck.add(player.Card('G', 7, "Agathosma"))
	global_deck.add(player.Card('G', 8, "Polygonatum"))
	global_deck.add(player.Card('G', 9, "Crateva"))
	global_deck.add(player.Card('Y', 10, "Agathosma"))
	global_deck.add(player.Card('Y', 11, "Polygonatum"))
	global_deck.add(player.Card('Y', 12, "Crateva"))
	global_deck.add(player.Card('R', 13, "Rehmannia"))
	global_deck.add(player.Card('R', 14, "Krameria"))

player_num = 4
players = []
player_color = ["Brown", "Blue", "Red", "Green"]
player_name = ["A", "B", "C", "D"]
solution = ''	# The solution
colors = ['B', 'G', 'Y', 'R']

# Give player names and color
for i in range(0,player_num):
	new_player = player.Player(player_name[i], player_color[i])
	players.append(new_player)
# Finishing initialization

def new_round():
	"""To open a new round"""
	global_deck.renew()
	new_deck()
	# Distribute cards
	for player in players:
		hand = random.sample(global_deck.cards, k = 12//(player_num))
		global_deck.remove(hand)
		player.hand = hand
	solution = global_deck.cards[0].color + global_deck.cards[1].color

def option_choser(option, color_pair):
	try:
		option = int(option)
	except ValueError:
		return -1

	if option not in range(1,6):
		return -1
	
	if (color_pair[0] not in colors) or (color_pair[1] not in colors):
		return -1

	print("You choose option " + str(option) + " and a color pair " + color_pair)