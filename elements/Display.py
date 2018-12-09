import constants, pyglet

class Display():
	"""
    A class used to represent text displays used in-game 

    ...

    Attributes
    ----------
    text : str 
		the text to be displayed
    font : str 
		the name of the font to be used
    color : tuple 
		the color of the font
	size : int 
		the font size
	x : int
        the x-coordinate where the label is to be drawn 
	y : int
		the y-coordinate where the label is to be drawn 

    Methods
    -------
	get_display()
		Gets the label containing the requirements given such as the text and the font to be used	
	draw()
		Draws the label onto the screen
    """

	def __init__(self, text, font, color, size, x, y):
		"""
        Parameters
        ----------
        text : str 
			the text to be displayed
		font : str 
			the name of the font to be used
		color : tuple 
			the color of the font
		size : int 
			the font size
		x : int
			the x-coordinate where the label is to be drawn 
		y : int
			the y-coordinate where the label is to be drawn
        """
		self.text = text
		self.font = font
		self.color = color
		self.size = size
		self.x, self.y = x, y

	def get_display(self):
		"""
			Gets the label containing the requirements given such as the text and the font to be used 

			Returns
			-------
			pyglet.text.Label	
				The label to be drawn onto the screen
		"""
		display = pyglet.text.Label(self.text,
						  font_name=self.font,
                          font_size=self.size,
                          x=self.x, y=self.y,
                          anchor_x='center', anchor_y='center')
		display.color = self.color 
		return display

	def draw(self):
		"""
			Draws the label onto the screen 

			Returns
			-------
			pyglet.text.Label.draw()	
				method for drawing the label onto the screen	
		"""
		return self.get_display().draw()
