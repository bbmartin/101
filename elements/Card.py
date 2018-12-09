import enum, pyglet

class CardState(enum.Enum):
	FACE_DOWN = 0
	HOVER = 1
	SELECTED = 2

class Card:
	def __init__(self, color, shape, x, y, state=CardState.FACE_DOWN):
		self.color = color
		self.shape = shape
		self.x, self.y = x, y
		self._state = state

	@property
	def state(self):
		return self._state

	@state.setter
	def state(self, state):
		self._state = state

	def set_position(self, x, y):
		self.x, self.y = x, y

	def get_image(self):
		card_img_path = "resources/cards/"
		if self._state is CardState.SELECTED:
			card_img_path += "front/" + self.color + "_" + self.shape + ".png"
		elif self._state is CardState.HOVER:
			card_img_path += "back/gold.png"
		else:
			card_img_path += "back/silver.png"
		card_img = pyglet.image.load(card_img_path)
		card_img.anchor_x, card_img.anchor_y = card_img.width // 2, card_img.height // 2
		return card_img

	def get_sprite(self):
		card_img = self.get_image()
		return pyglet.sprite.Sprite(card_img, self.x, self.y)

	def under_mouse(self, x, y):
		edge_left = self.x - self.get_sprite().width // 2
		edge_right = self.x + self.get_sprite().width // 2
		edge_top = self.y + self.get_sprite().height // 2
		edge_bottom = self.y - self.get_sprite().height // 2 
		return (x in range(edge_left, edge_right + 1)) and (y in range(edge_bottom, edge_top + 1))

	def compare_with(self, card):
		return self.color == card.color and self.shape == card.shape
