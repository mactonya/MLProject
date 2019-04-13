"""Stores basic objects"""

class Player(object):
	def __init__ (self, name, color, hand = []):
		self.name = name			# Name
		self.hand = hand			# Hand, a list
		self.color = color			# Pos	 
		self.points = 0				# Points
		self.is_banned = False		# If allowed to do a move
		self.is_followed = False	# If followed

	def give_A_ask_B (self, choose_color, return_color, receiver):
		"""Give <receiver> a Card <choose_color>, return how many <return_color> does <receiver> have
		- choose_color: a Card
		- return_color: a color
		- receiver: a Player
		"""

	def give_A_return_B (self, choose_color, return_color, receiver):
		"""Give <receiver> a Card <choose_color>, then <receiver> gives all <return_color> Card
		- choose_color: a Card
		- return_color: a color
		- receiver: a Player
		"""

	def give_AB(self, choose_color, receiver):

		# choose_color is a str, must be vaild
		A = choose_color[0]
		B = choose_color[1]
		# If there is a multiple of cards A/B:
		#	> Send a signal to frontend 
		#	> wait for sendback
		# Continue

		# Cards is the sum of two results
		self.hand.transer(receiver.hand, cards)

	def give_all_AB(self, choose_color, receiver):

		# choose_color is a str, must be vaild
		A = choose_color[0]
		B = choose_color[1]
		# Ask back whether receiver wants to send A or B, if possible:
		#	> Send a signal to frontend 
		#	> wait for sendback
		# Continue

		# Cards is the results
		self.hand.transer(receiver.hand, cards)

	def guess(self, guess, answer):
		return (guess_color == answer or guess_color == answer[::-1])


class Deck():
	def __init__ (self, cards = []):	
		self.cards = cards
	def remove(self, cards):
		"""Remove a card"""
		if isinstance(cards, list):
			for card in cards:
				self.cards.remove(card)
		else:
			self.cards.remove(cards)
	def add(self, cards):
		"""Add a card"""
		if isinstance(cards, list):
			self.cards += cards
		else:
			self.cards.append(cards)
	def transfer(self, other, cards):
		"""Transfer cards to other"""
		self.remove(cards)
		other.add(cards)
	def card_list(self):	
		"""Return the card list"""
		return [card.give_card() for card in self]
	def __iter__(self):	
		""" Return the iterator of card list """
		return iter(self.cards)
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
		for card in self:
			if card.color == color:
				color_deck.append(card)
		return color_deck
	def renew(self):				
		""" Renew a new global deck """
		for item in self:
			self.remove(item)

class Card():
	def __init__ (self, color, ID, name):
		self.color = color
		self.ID = ID
		self.name = name
	def give_card(self):
		"""Retrun the tuple (Name, ID, Color)"""
		return (self.name, str(self.ID), self.color)





