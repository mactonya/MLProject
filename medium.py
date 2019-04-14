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
	global_deck.add(player.Card('Y', 11, "Papaver"))
	global_deck.add(player.Card('Y', 12, "Crateva"))
	global_deck.add(player.Card('R', 13, "Rehmannia"))
	global_deck.add(player.Card('R', 14, "Krameria"))

player_num = 4
player_color = ["Brown", "Blue", "Red", "Green"]
player_name = ["Adam", "Bob", "Carle", "David"]
players = dict()
solution = ''

colors = ['B', 'G', 'Y', 'R']

# Give player names and color
for i in range(0,player_num):
	new_player = player.Player(player_name[i], player_color[i])
	players[player_name[i]] = new_player
# Finishing initialization


def next_player(player):
	if player == player_name[len(player_name) - 1]:
		return player_name[0]
	else:
		return player_name[player_name.index(player) + 1]


def new_round():
	"""To open a new round"""
	global_deck.renew()
	new_deck()
	# Distribute cards
	for pl in players:
		hand = player.Deck(random.sample(global_deck.cards, k = 12//(player_num)))
		global_deck.remove(hand)
		players[pl].hand = hand
	global solution 
	solution = global_deck.cards[0].color + global_deck.cards[1].color


def option_choser(current_player, option, color_pair):
	try:
		option = int(option)
	except ValueError:
		return -1, 'ValueNotInt'
	if option not in range(1,6):
		return -1, 'ValueNotInRange'
	if (color_pair[0] not in colors) or (color_pair[1] not in colors):
		return -1, 'ColorNotFound'

	if option != 5:
		request_player = dialog.enter_player(player_name, current_player.name)
		if request_player not in player_name:
			return -1, 'PlayerNotFound'
		elif request_player == current_player.name:
			return -1, 'RequestYourself'
		print("You choose option " + str(option) + " and a color pair " + color_pair + " to the target player " + request_player)
	else:
		print("You guessed " + color_pair + " as the answer")
	
	if option == 1:

		if current_player.hand.card_count() == 0:
			return -1, "NoCardsInHand"

		if color_pair[0] != color_pair[1]:
			current_pile = current_player.hand.color_card(color_pair[0]) + current_player.hand.color_card(color_pair[1])
		else:
			current_pile = current_player.hand.color_card(color_pair[0])

		if len(current_pile) == 0:
			return -1, 'NoSuitableCardExists'

		x = dialog.choose_card(current_pile)

		try:
			x = int(x)
		except ValueError:
			return -1, 'ValueNotInt'
		if x >= len(current_pile) or x < 0:
			return -1, 'ValueOutOfRange'
		# FORMAT = (Asker, receiver, # of cards) 
		if current_pile[x].color == color_pair[0]:
			return 1, (current_player, request_player, current_player.give_A_ask_B(current_pile[x], color_pair[1],players[request_player]))
		elif current_pile[x].color == color_pair[1]:
			return 1, (current_player, request_player, current_player.give_A_ask_B(current_pile[x], color_pair[0],players[request_player]))
		else:
			return -1, 'UnexceptedError'
	elif option == 2:

		if current_player.hand.card_count() == 0:
			return -1, "NoCardsInHand"

		if color_pair[0] != color_pair[1]:
			current_pile = current_player.hand.color_card(color_pair[0]) + current_player.hand.color_card(color_pair[1])
		else:
			current_pile = current_player.hand.color_card(color_pair[0])

		if len(current_pile) == 0:
			return -1, 'NoSuitableCardExists'

		x = dialog.choose_card(current_pile)
		try:
			x = int(x)
		except ValueError:
			return -1, 'ValueNotInt'
		if x >= len(current_pile) or x < 0:
			return -1, 'ValueOutOfRange'

		if current_pile[x].color == color_pair[0]:
			return 2, (current_player, request_player, current_player.give_A_return_B(current_pile[x], color_pair[1], players[request_player]))
		elif current_pile[x].color == color_pair[1]:
			return 2, (current_player, request_player, current_player.give_A_return_B(current_pile[x], color_pair[0], players[request_player]))
		else:
			return -1, 'UnexceptedError'
	elif option == 3:
		# Requires another player to decide
		request_pile0 = players[request_player].hand.color_card(color_pair[0])
		request_pile1 = players[request_player].hand.color_card(color_pair[1])

		rt_cards = 0


		if len(request_pile0) != 0:
			x0 = dialog.choose_card(request_pile0)
			try:
				x0 = int(x0)
			except ValueError:
				return -1, 'ValueNotInt'
			if x0 >= len(request_pile0) or x0 < 0:
				return -1, 'ValueOutOfRange'
			players[request_player].give_AB(request_pile0[x0], current_player)
			rt_cards += 1
		if color_pair[0] != color_pair[1]:
			if len(request_pile1) != 0:
				x1 = dialog.choose_card(request_pile1)
				try:
					x1 = int(x1)
				except ValueError:
					return -1, 'ValueNotInt'
				if x1 >= len(request_pile1) or x1 < 0:
					return -1, 'ValueOutOfRange'
				players[request_player].give_AB(request_pile1[x1], current_player)
				rt_cards += 1

		return 3, (current_player, request_player, rt_cards)

	elif option == 4:
		request_pile0 = players[request_player].hand.color_card(color_pair[0])
		request_pile1 = players[request_player].hand.color_card(color_pair[1])

		if len(request_pile0) != 0 and len(request_pile1) != 0:
			x = dialog.choose_color(request_pile0, request_pile1)
			try:
				x = int(x) - 1
			except ValueError:
				return -1, 'ValueNotInt'

			if x == 0:
				players[request_player].give_AB(request_pile0, current_player)
				return 4, (current_player, request_player, len(request_pile0))
			elif x == 1:
				players[request_player].give_AB(request_pile1, current_player)
				return 4, (current_player, request_player, len(request_pile1))
			else:
				return -1, 'ValueOutOfRange'
		elif len(request_pile0) != 0:
			players[request_player].give_AB(request_pile0, current_player)
			return 4, (current_player, request_player, len(request_pile0))
		elif len(request_pile1) != 0:
			players[request_player].give_AB(request_pile1, current_player)
			return 4, (current_player, request_player, len(request_pile1))
		else:
			return 4, (current_player, request_player, 0)

	elif option == 5:
		return 5, (current_player, color_pair, current_player.guess(color_pair, solution))
	else:
		return -1, 'UnexceptedError'

def unban_all():
	for plr in player_name:
		players[plr].is_banned = False

def game_end():
	max = 0
	for plr in player_name:
		if max <= players[plr].points:
			max = players[plr].points
	if max >= 9:
		return True
	else:
		return False

def winner():
	win = ''
	max = 0
	for plr in player_name:
		if max <= players[plr].points:
			max = players[plr].points
			win = plr
	return win