class Player(object):
	def __init__ (self, name, hand, color):
		self.name = name		# Name
		self.hand = hand		# Hand, a list
		self.color = color		# Pos	
		self.points = 0			# Points
		self.is_banned = False	# If allowed to do a move
		self.is_followed = False # If followed

class Deck():
	def __init__ (self, cards = []):
		self.cards = cards
	def rmv(self, cards):
		self.cards -= cards
	def add(self, cards):
		if isinstance(cards, Deck):
			self.cards += cards
		else:
			self.cards.append(cards)

class Card():
	def __init__ (self, color, ID, name):
		self.color = color
		self.ID = ID
		self.name = name

global_deck = Deck()
global_deck.add(Card('B', 1, "Water"))