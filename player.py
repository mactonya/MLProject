import random
	
class Player(object):
	def __init__ (self, name, color):
		self.name = name			# Name
		#self.hand = hand			# Hand, a list
		self.color = color			# Pos	 
		self.points = 0				# Points
		self.is_banned = False		# If allowed to do a move
		self.is_followed = False	# If followed
	def give_A_ask_B (self, choose_color, given_card, receiver):
		
		if choose_color == "same":
			choose_color = given_card.color + given_card.color

		# choose_color is a 2-char str, must be vaild
		A = given_card.color
		B = choose_color.replace(A, "")

		return receiver.hand.color_count(B)

	def give_A_return_B (self, choose_color, given_card, receiver):
		
		if choose_color == "same":
			choose_color = given_card.color + given_card.color

		# choose_color is a str, must be vaild
		A = given_card.color
		B = choose_color.replace(A, "")

		cards = receiver.hand.color_card(B)
		self.hand.transer(receiver.hand, cards)

	def give_AB(self, choose_color, receiver):

		# choose_color is a str, must be vaild
		A = choose_color[0]
		B = choose_color[1]
		# What card to give

	def guess(self, guess_color):
		return (guess_color == answer or guess_color == answer[::-1])


class Deck():
	def __init__ (self, cards = []):
		#self.name = name
		self.cards = cards
	def remove(self, cards):
		if isinstance(cards, list):
			for card in cards:
				self.cards.remove(card)
		else:
			self.cards.remove(cards)
	def add(self, cards):
		if isinstance(cards, list):
			self.cards += cards
		else:
			self.cards.append(cards)
	def transfer(self, other, cards):
		self.remove(cards)
		other.add(cards)
	def __str__(self):
		return str([str(card) for card in self])
	def __iter__(self):
		return iter(self.cards)
	def color_count(self, color):
		color_num = 0
		for card in self:
			if card.color == color:
				color_num += 1
		return color_num
	def color_card(self, color):
		color_deck = []
		for card in self:
			if card.color == color:
				color_deck.append(card)
		return color_deck

class Card():
	def __init__ (self, color, ID, name):
		self.color = color
		self.ID = ID
		self.name = name
	#def __hash__(self):
	#	return self.ID
	def __str__(self):
		return self.name + str(self.ID)

global_deck = Deck()
global_deck.add(Card('B', 1, "Water"))
global_deck.add(Card('B', 2, "Water"))
global_deck.add(Card('B', 3, "Water"))
global_deck.add(Card('B', 4, "Water"))
global_deck.add(Card('B', 5, "Water"))
global_deck.add(Card('G', 6, "Chimaphila"))
global_deck.add(Card('G', 7, "Agathosma"))
global_deck.add(Card('G', 8, "Polygonatum"))
global_deck.add(Card('G', 9, "Crateva"))
global_deck.add(Card('Y', 10, "Agathosma"))
global_deck.add(Card('Y', 11, "Polygonatum"))
global_deck.add(Card('Y', 12, "Crateva"))
global_deck.add(Card('R', 13, "Rehmannia"))
global_deck.add(Card('R', 14, "Krameria"))

player_num = 4
players = []
player_color = ["Brown", "Blue", "Red", "Green"]
for i in range(player_num):
	player = Player(str(i), player_color[i])
	players.append(player)

for player in players:
	hand = random.sample(global_deck.cards, k = 12//(player_num))
	global_deck.remove(hand)
	player.hand = Deck(hand)

answer = global_deck.cards[0].color + global_deck.cards[1].color

#print(global_deck)
#for player in players:
	#print(player.hand)

