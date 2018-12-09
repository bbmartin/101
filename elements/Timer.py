# Source: https://github.com/bitcraft/pyglet/blob/master/examples/timer.py

import pyglet, constants

class Timer:
	"""
    A class used to represent a timer used in-game 

    ...

    Attributes
    ----------
	x : int
        the x-coordinate where the timer is to be drawn 
	y : int
		the y-coordinate where the timer is to be drawn
    time : int 
		time that has passed in seconds	
    running : boolean 
		truth value for whether the timer is running	
	label : pyglet.text.Label
		label to be drawn onto the screen

    Methods
    -------
	reset()
		Resets the timer back to 0
	update(dt)
		Updates the text that the timer shows per second
	draw()
		Draws the timer onto the screen
    """

	def __init__(self, x, y):
		"""
        Parameters
        ----------
        x : int
			the x-coordinate where the timer is to be drawn 
		y : int
			the y-coordinate where the timer is to be drawn
		time : int 
			time that has passed in seconds	
		running : boolean 
			truth value for whether the timer is running	
		label : pyglet.text.Label
			label to be drawn onto the screen
        """
		self.x, self.y = x, y
		self.label = pyglet.text.Label("00:00", 
									   font_name=constants.GAME_FONT_NAME,
									   font_size=constants.TIMER_FONT_SIZE, 
									   x=self.x, y=self.y, 
									   anchor_x='center', anchor_y='center')
		self.reset()

	def reset(self):
		"""
			Resets the timer back to 0
		"""
		self.time = 0
		self.running = False
		self.label.text = "00:00"
		self.label.color = constants.COLOR_BLACK 

	def update(self, dt):
		"""
			Updates the text that the timer shows per second
		"""
		if self.running:
			self.time += 1
			m, s = divmod(self.time, 60)
			self.label.text = '%02d:%02d' % (m, s)
	
	def draw(self):
		"""
			Draws the timer onto the screen 

			Returns
			-------
			pyglet.text.Label.draw()	
				method for drawing the timer onto the screen	
		"""
		return self.label.draw()