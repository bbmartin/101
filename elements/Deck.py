import constants, random, pyglet
from elements.Card import Card, CardState

ctc_spacing = constants.CARD_SIDE_LENGTH + constants.CARD_SPACING
x_offsets = [(x * ctc_spacing) for x in [-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]]
y_offsets = [(y * ctc_spacing) for y in [1, 0, -1]]

class Deck:

	cards = []
	card_positions = []

	def __init__(self, center_x, center_y):
		self.center_x = center_x
		self.center_y = center_y
		self.populate()

	def get_card_positions(self):
		card_positions = []
		for x_offset in x_offsets:
			for y_offset in y_offsets:
				x, y = int(self.center_x + x_offset), int(self.center_y + y_offset)
				card_positions.append((x, y))
		self.card_positions = card_positions
		return self

	def shuffle_card_positions(self):
		random.shuffle(self.card_positions)

	def populate(self):
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
		selected_cards = []
		for i in range(len(self.cards)):
			if self.cards[i] is not None:
				if self.cards[i]._state is CardState.SELECTED:
					selected_cards.append(i)
		return selected_cards
	
	def check_if_empty(self):
		for card in self.cards:
			if card is not None:
				return False
		return True

	def draw(self):
		for card in self.cards:
			if card is not None:
				card.get_sprite().draw()	
