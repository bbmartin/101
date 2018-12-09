import enum, pyglet

class CardState(enum.Enum):
	"""
	An enumeration of card states

	Attributes
    ----------
    FACE_DOWN : int 
		Represents the state of a card when it is facing down
	HOVER : int 
		Represents the state of a card when it is being hovered over 
	SELECTED : int
		Represents the state of a card when it is selected
	"""
	FACE_DOWN = 0
	HOVER = 1
	SELECTED = 2

class Card:
	"""
    A class used to represent a Card used in-game 

    ...

    Attributes
    ----------
    color : str
		the color of the card's face 
    shape : str 
		the shape of the card's face 
    x : int 
        the x-coordinate of where the card sprite is to be drawn 
	y : int
		the y-coordinate of where the card sprite is to be drawn
    _state : CardState 
		the state of the card

    Methods
    -------
	set_position(x, y)
		Changes the position of the card to the coordinates given
    get_image()
		Gets the appropriate image for the card based on its state
	get_sprite()
		Gets the sprite of the card, which changes based on the card's state
	under_mouse(x, y)
		Checks if the card is underneath the mouse cursor by using the mouse cursor's coordinates
	compares_with(card)
		Compares its color and shape to that of another card
    """
	def __init__(self, color, shape, x, y, state=CardState.FACE_DOWN):
		"""
        Parameters
        ----------
        color : str
			the color of the card's face 
		shape : str 
			the shape of the card's face 
		x : int 
			the x-coordinate of where the card sprite is to be drawn 
		y : int
			the y-coordinate of where the card sprite is to be drawn
		_state : CardState 
			the state of the card
        """
		self.color = color
		self.shape = shape
		self.x, self.y = x, y
		self._state = state

	def set_position(self, x, y):
		"""
		Changes the position of the card to the coordinates given

		Parameters
		----------
		x : int 
			The x-coordinate of where the card is to be drawn	
		y : int 
			The y-coordinate of where the card is to be drawn
		"""
		self.x, self.y = x, y

	def get_image(self):
		"""
			Gets the appropriate image for the card based on its state 

			Returns
			-------
			pyglet.image
				Image of the card to be rendered in-game
		"""
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
		"""
			Gets the sprite of the card, which changes based on the card's state

			Returns
			-------
			pyglet.sprite.Sprite
				Sprite of the card to be drawn
		"""
		card_img = self.get_image()
		return pyglet.sprite.Sprite(card_img, self.x, self.y)

	def under_mouse(self, x, y):
		"""
		Checks if the card is underneath the mouse cursor by using the mouse cursor's coordinates

		Parameters
		----------
		x : int 
			The x-coordinate of the mouse cursor	
		y : int 
			The y-coordinate of the mouse cursor

		Returns
		-------
		boolean
			truth value for whether the mouse cursor is over the card	
		"""
		edge_left = self.x - self.get_sprite().width // 2
		edge_right = self.x + self.get_sprite().width // 2
		edge_top = self.y + self.get_sprite().height // 2
		edge_bottom = self.y - self.get_sprite().height // 2 
		return (x in range(edge_left, edge_right + 1)) and (y in range(edge_bottom, edge_top + 1))

	def compare_with(self, card):
		"""
		Compares its own color and shape to that of another card

		Parameters
		----------
		card : Card 
			The card being compared

		Returns
		-------
		boolean
			truth value for whether both cards are the same in terms of its face shapes and colors	
		"""
		return self.color == card.color and self.shape == card.shape
