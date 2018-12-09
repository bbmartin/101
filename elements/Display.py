import constants, pyglet

class Display():
	def __init__(self, text, font, color, size, x, y):
		self.text = text
		self.font = font
		self.color = color
		self.size = size
		self.x, self.y = x, y

	def change_text(self, text):
		self.text = text
		return self

	def get_display(self):
		display = pyglet.text.Label(self.text,
						  font_name=self.font,
                          font_size=self.size,
                          x=self.x, y=self.y,
                          anchor_x='center', anchor_y='center')
		display.color = constants.COLOR_BLACK
		return display

	def draw(self):
		return self.get_display().draw()
