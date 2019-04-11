class Player(object):
	def __init__ (self, name, hand, color):
		self.name = name		# Name
		self.hand = hand		# Hand, a list
		self.color = color		# Pos	
		self.points = 0			# Points
		self.is_banned = False	# If allowed to do a move