"""Stores basic objects"""

class Player(object):
	def __init__ (self, name, color, hand = []):
		self.name = name			# Name
		self.hand = hand			# Hand, a list
		self.color = color			# Pos	 
		self.points = 0				# Points
		self.is_banned = False		# If allowed to do a move
		self.is_followed = False	# If followed
	def give_A_ask_B (self, sent_card, return_color, receiver):
		"""Give <receiver> a <sent_card>, return how many <return_color> does <receiver> have
		- sent_card: a Card (guranteed to exist by init)
		- return_color: a color
		- receiver: a Player
		"""
		self.hand.transfer(receiver.hand, Deck(sent_card))
		return receiver.hand.color_count(return_color)
	def give_A_return_B (self, sent_card, return_color, receiver):
		"""Give <receiver> a Card <choose_color>, then <receiver> gives all <return_color> Card
		- sent_card: a Card (guranteed to exist by init)
		- return_color: a color
		- receiver: a Player
		"""
		self.hand.transfer(receiver.hand, Deck(sent_card))
		X = Deck(receiver.hand.color_card(return_color))
		if X.card_count != 0:
			receiver.hand.transfer(self.hand, X)
		return (X.card_count(), X)

	def give_AB(self, choose_color, receiver):
		"""Choose a color pair <choose_color>; <receiver> must give one <choose_color[0]> and/or <choose_color[1]> colored Card
		- choose_color: a color pair
		- receiver: a Player
		"""


	def give_all_AB(self, choose_color, receiver):
		"""Choose a color pair <choose_color>; <receiver> must give all of <choose_color[0]> or <choose_color[1]> colored Card
		- choose_color: a color pair
		- receiver: a Player
		"""

		self.hand.transer(receiver.hand, cards)

	def guess(self, guess, answer):
		"""Guess the answer"""
		if (guess == answer or guess == answer[::-1]):
			self.points += 3
			return True
		else:
			self.is_banned = True
			return False


class Deck():
	def __init__ (self, cards = []):
		self.cards = []
		if isinstance(cards, Card):
			self.cards.append(cards)
		else:
			self.cards.extend(cards)
	def __iter__(self):	
		return iter(self.cards)
	def __getitem__(self, key):
		return self.cards[key]
	def __add__(self, other):
		return self.cards.extend(other)

	def remove(self, cards):
		"""Remove a card FROM SELF"""
		if isinstance(cards, Deck):
			for card in cards:
				self.cards.remove(card)
		else:
			self.cards.remove(cards)
	def add(self, cards):
		"""Add a card"""
		if isinstance(cards, Deck):
			self.cards += cards
		else:
			self.cards.append(cards)
	def transfer(self, other, cards):
		"""Transfer SELF's cards to other"""
		self.remove(cards)
		other.add(cards)

	def card_list(self):	
		"""Return the card list"""
		return [card.give_card() for card in self]
	
	def card_count(self):
		return len(self.cards)

	def color_count(self, color): 
		""" Count how many <color> cards are in list """
		color_num = 0
		for card in self:
			if card.color == color:
				color_num += 1
		return color_num
	def color_card(self, color):  
		""" Return what are <color> cards """
		color_deck = []
		if self == Deck():
			return color_deck
		for card in self:
			if card.color == color:
				color_deck.append(card)
		return color_deck
	
	def renew(self):				
		"""Remove all items in deck"""
		self.cards = []

class Card():
	def __init__ (self, color, ID, name):
		self.color = color
		self.ID = ID
		self.name = name
	def give_card(self):
		"""Retrun the tuple (Name, ID, Color)"""
		return (self.name, str(self.ID), self.color)





