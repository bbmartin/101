import constants, random, pyglet
from elements.Card import Card, CardState

# Spacing factor of the cards, taking into account the spaces in between and the card's dimensions
SPACING = constants.CARD_SIDE_LENGTH + constants.CARD_SPACING

# x-offsets of the cards from the center of the screen
x_offsets = [(x * SPACING) for x in [-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]]

# y-offsets of the cards from the center of the screen
y_offsets = [(y * SPACING) for y in [1, 0, -1]]

class Deck:
	"""
    A class used to represent a Deck used in-game 

    ...

    Attributes
    ----------
    cards : list 
		list of cards 
    card_positions : list 
		list of positions where the cards are to be drawn
    center_x : int 
        the x-coordinate from which all card positions are based on 
	center_y : int
		the y-coordinate from which all card positions are based on 

    Methods
    -------
	get_card_positions()
		Generates a list of card positions based on the cards' dimensions and the spacing between them when they're drawn
    shuffle_card_positons()
		Shuffles the cards' positions when drawn unto the screen
	populate()
		Generates a list of cards using the card positions
	get_selected_cards()
		Gets the cards that are selected or that have been clicked
	check_if_empty()
		Checks if the deck is empty
	draws()
		Draws each individual card from the deck
    """

	cards = []
	card_positions = []

	def __init__(self, center_x, center_y):
		"""
        Parameters
        ----------
        cards : list 
			list of cards 
		card_positions : list 
			list of positions where the cards are to be drawn
		center_x : int 
			the x-coordinate from which all card positions are based on 
		center_y : int
			the y-coordinate from which all card positions are based on
        """
		self.center_x = center_x
		self.center_y = center_y
		self.populate()

	def get_card_positions(self):
		"""
			Generates a list of card positions based on the cards' dimensions and the spacing between them when they're drawn 

			Returns
			-------
			Deck	
				Returns itself	
		"""
		card_positions = []
		for x_offset in x_offsets:
			for y_offset in y_offsets:
				x, y = int(self.center_x + x_offset), int(self.center_y + y_offset)
				card_positions.append((x, y))
		self.card_positions = card_positions
		return self

	def shuffle_card_positions(self):
		"""
			Shuffles the cards' positions when drawn unto the screen 
		"""
		random.shuffle(self.card_positions)

	def populate(self):
		"""
			Generates a list of cards using the card positions 

			Returns
			-------
			Deck
				Returns itself	
		"""
		i = 0
		card_faces = []
		self.get_card_positions().shuffle_card_positions()
		while len(self.cards) < constants.DECK_SIZE:
			color, shape = random.choice(constants.CARD_FACE_COLORS), random.choice(constants.CARD_FACE_SHAPES)
			if (color, shape) not in card_faces:
				for j in range(2):
					x, y = self.card_positions[i]
					self.cards.append(Card(color, shape, x, y))
					i += 1
				card_faces.append((color, shape))
		return self

	def get_selected_cards(self):
		"""
			Gets the cards that are selected or that have been clicked 

			Returns
			-------
			list	
				The indices of the cards that cards that are selected	
		"""
		selected_cards = []
		for i in range(len(self.cards)):
			if self.cards[i] is not None:
				if self.cards[i]._state is CardState.SELECTED:
					selected_cards.append(i)
		return selected_cards
	
	def check_if_empty(self):
		"""
			Checks if the deck is empty 

			Returns
			-------
			boolean
				Truth value of whether the deck is empty	
		"""
		for card in self.cards:
			if card is not None:
				return False
		return True

	def draw(self):
		"""
			Draws each individual card from the deck
		"""
		for card in self.cards:
			if card is not None:
				card.get_sprite().draw()	
