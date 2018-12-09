import pyglet

class Button:
	"""
    A class used to represent a Button used for player input 

    ...

    Attributes
    ----------
    name : str
		the name of the button
    scale : float 
		the scale of the button sprite
    x : int 
        the x-coordinate of where the button sprite is to be drawn 
	y : int
		the y-coordinate of where the button sprite is to be drawn
    _hover : boolean 
		truth value for whether the button is being hovered over

    Methods
    -------
    get_image()
		Gets the appropriate image for the button based on its hover state
	get_sprite()
		Gets the sprite of the button, which changes based on the button's hover state
	under_mouse(x, y)
		Checks if the button is underneath the mouse cursor by using the mouse cursor's coordinates
	draw()
		Draws the button sprite
    """
	
	def __init__(self, name, scale, x, y, hover=False):
		"""
        Parameters
        ----------
        name : str
            The name of the animal
        scale : float 
			The scale of the button sprite
		x : int 
			The x-coordinate of where the button sprite is to be drawn 
		y : int
			The y-coordinate of where the button sprite is to be drawn
		_hover : boolean 
			Truth value for whether the button is being hovered over
        """
		self.name = name
		self.scale = scale
		self.x, self.y = x, y
		self._hover = hover

	def get_image(self):
		"""
			Gets the appropriate image for the button based on its hover state 

			Returns
			-------
			pyglet.image
				Image of the button to be rendered in-game
		"""
		btn_img_path = "resources/buttons/" + self.name
		if not self._hover:
			btn_img_path += "/silver.png"
		else:
			btn_img_path += "/gold.png"
		btn_img = pyglet.image.load(btn_img_path)
		btn_img.anchor_x, btn_img.anchor_y = btn_img.width // 2, btn_img.height // 2
		return btn_img

	def get_sprite(self):
		"""
			Gets the sprite of the button, which changes based on the button's hover state

			Returns
			-------
			pyglet.sprite.Sprite
				Sprite of the button to be drawn
		"""
		btn_img = self.get_image()	
		btn_sprite = pyglet.sprite.Sprite(btn_img, self.x, self.y)
		btn_sprite.scale = self.scale
		return btn_sprite

	def under_mouse(self, x, y):
		"""
		Checks if the button is underneath the mouse cursor by using the mouse cursor's coordinates

		Parameters
		----------
		x : int 
			The x-coordinate of the mouse cursor	
		y : int 
			The y-coordinate of the mouse cursor

		Returns
		-------
		boolean
			truth value for whether the cursor is hovering over the button	
		"""
		edge_left = self.x - self.get_sprite().width // 2
		edge_right = self.x + self.get_sprite().width // 2
		edge_top = self.y + self.get_sprite().height // 2
		edge_bottom = self.y - self.get_sprite().height // 2 
		return (x in range(edge_left, edge_right + 1)) and (y in range(edge_bottom, edge_top + 1))

	def draw(self):
		"""
			Draws the button sprite

			Returns
			-------
			pyglet.sprite.Sprite.draw()
				method for drawing the button sprite to the screen 
		"""
		return self.get_sprite().draw()
		