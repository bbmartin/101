import pyglet

class Button:
	def __init__(self, name, scale, x, y, hover=False):
		self.name = name
		self.scale = scale
		self.x, self.y = x, y
		self._hover = hover

	@property
	def hover(self):
		return self._hover

	@hover.setter
	def hover(self, hover):
		self._hover = hover

	def get_image(self):
		btn_img_path = "resources/buttons/" + self.name
		if not self._hover:
			btn_img_path += "/silver.png"
		else:
			btn_img_path += "/gold.png"
		btn_img = pyglet.image.load(btn_img_path)
		btn_img.anchor_x, btn_img.anchor_y = btn_img.width // 2, btn_img.height // 2
		return btn_img

	def get_sprite(self):
		btn_img = self.get_image()	
		btn_sprite = pyglet.sprite.Sprite(btn_img, self.x, self.y)
		btn_sprite.scale = self.scale
		return btn_sprite

	def under_mouse(self, x, y):
		edge_left = self.x - self.get_sprite().width // 2
		edge_right = self.x + self.get_sprite().width // 2
		edge_top = self.y + self.get_sprite().height // 2
		edge_bottom = self.y - self.get_sprite().height // 2 
		return (x in range(edge_left, edge_right + 1)) and (y in range(edge_bottom, edge_top + 1))

	def draw(self):
		return self.get_sprite().draw()
		