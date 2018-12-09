# Source: https://github.com/bitcraft/pyglet/blob/master/examples/timer.py

import pyglet, constants

class Timer:
	def __init__(self, x, y):
		self.label = pyglet.text.Label("00:00", 
									   font_name=constants.GAME_FONT_NAME,
									   font_size=constants.TIMER_FONT_SIZE, 
									   x=x, y=y, 
									   anchor_x='center', anchor_y='center')
		self.reset()

	def reset(self):
		self.time = 0
		self.running = False
		self.label.text = "00:00"
		self.label.color = constants.COLOR_BLACK 

	def update(self, dt):
		if self.running:
			self.time += 1
			m, s = divmod(self.time, 60)
			self.label.text = '%02d:%02d' % (m, s)
	
	def draw(self):
		return self.label.draw()