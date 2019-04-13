"""Intermediate level for processing init and other judging stuffs """

import player
import random
import dialog

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
player_color = ["Brown", "Blue", "Red", "Green"]
player_name = ["A", "Bob", "C", "D"]
players = dict()
solution = ''

colors = ['B', 'G', 'Y', 'R']

# Give player names and color
for i in range(0,player_num):
	new_player = player.Player(player_name[i], player_color[i])
	players[player_name[i]] = new_player

# Finishing initialization

def new_round():
	"""To open a new round"""
	global_deck.renew()
	new_deck()
	# Distribute cards
	for pl in players:
		hand = player.Deck(random.sample(global_deck.cards, k = 12//(player_num)))
		global_deck.remove(hand)
		players[pl].hand = player.Deck(hand)
	solution = global_deck.cards[0].color + global_deck.cards[1].color

def option_choser(current_player, option, color_pair):

	if option != '5':
		request_player = dialog.enter_player()
	try:
		option = int(option)
	except ValueError:
		return -1
	if option not in range(1,6):
		return -1
	if (color_pair[0] not in colors) or (color_pair[1] not in colors):
		return -1
	if (option != 5 and request_player not in player_name):
		return -1

	if option != 5:
		print("You choose option " + str(option) + " and a color pair " + color_pair + " to the target player " + request_player)
	else:
		print("You guessed " + color_pair + " as the answer")
	
	if option == 1:
		if color_pair[0] != color_pair[1]:
			current_pile = player.Deck(current_player.hand.color_card(color_pair[0]) + current_player.hand.color_card(color_pair[1]))
		else:
			current_pile = player.Deck(current_player.hand.color_card(color_pair[0]))

		x = dialog.choose_card(current_pile)

		try:
			x = int(x)
		except ValueError:
			return -1
		if x >= current_pile.card_count() or x < 0:
			return -1

		if current_pile[x].color == color_pair[0]:
			return 1, (request_player, color_pair[1], current_player.give_A_ask_B(current_pile[x], color_pair[1], players[request_player]))
		elif current_pile[x].color == color_pair[1]:
			return 1, (request_player, color_pair[0], current_player.give_A_ask_B(current_pile[x], color_pair[0], players[request_player]))
		else:
			return -1
	elif option == 2:
		if color_pair[0] != color_pair[1]:
			current_pile = player.Deck(current_player.hand.color_card(color_pair[0]) + current_player.hand.color_card(color_pair[1]))
		else:
			current_pile = player.Deck(current_player.hand.color_card(color_pair[0]))
		x = dialog.choose_card(current_pile)
		try:
			x = int(x)
		except ValueError:
			return -1
		if x >= current_pile.card_count() or x < 0:
			return -1

		if current_pile[x].color == color_pair[0]:
			return 2, (request_player, color_pair[1], current_player.give_A_return_B(current_pile[x], color_pair[1], players[request_player]))
		elif current_pile[x].color == color_pair[1]:
			return 2, (request_player, color_pair[0], current_player.give_A_return_B(current_pile[x], color_pair[0], players[request_player]))
		else:
			return -1
	elif option == 3:
		# Requires another player to decide
		request_pile0 = request_player.Deck(current_player.hand.color_card(color_pair[0]))
		request_pile1 = request_player.Deck(current_player.hand.color_card(color_pair[1]))
		if color_pair[0] != color_pair[1]:
			if request_pile0.card_count() != 0:
				x1 = dialog.choose_card(request_pile0)
			if request_pile1.card_count() != 0:
				x2 = dialog.choose_card(request_pile1)
	elif option == 5:
		return 5, (current_player, color_pair, current_player.guess(color_pair, solution))
	'''
	elif option == 4:
	
	
	else:
		dialog.error()
	'''