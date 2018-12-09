import constants, random, pyglet
from elements.Button import Button
from elements.Card import Card, CardState
from elements.Deck import Deck
from elements.Display import Display
from elements.Timer import Timer

# Game window, which is in fullscreen mode 
WINDOW = pyglet.window.Window(fullscreen=True)

# Center of the screen
CENTER_X, CENTER_Y = WINDOW.width // 2, WINDOW.height // 2

class Scene:
	"""
    A class used to represent a scene in the game 

    ...

    Attributes
    ----------
    name : str 
		the name of the game scene
    elements : list 
		list of elements to be drawn on the screen

    Methods
    -------
	next()
		Sets up the scene that is next	
	get_element(type)
		Gets a specific element from the scene based on its type
	draw()	
		Draws all elements of the scene onto the screen
    """
	_next = None

	def __init__(self, name, elements):
		self.name = name
		self.elements = elements

	def next(self, scene):
		"""
			Sets up the scene that is next
		"""
		self._next = scene 
	
	def get_element(self, type):
		"""
		Gets a specific element from the scene based on its type

		Parameters
		----------
		type : varies
			Gets the element of the scene based on the type given

		Returns
		-------
		Scene element
			An element of the scene that is drawn onto the screen
		"""
		for el in self.elements:
			if isinstance(el, type):
				return el

	def draw(self):	
		"""
			Draws all elements of the scene onto the screen
		"""
		for el in self.elements:
			el.draw()
		return self

pyglet.font.add_file(constants.GAME_FONT_PATH)

# Scene: LOGO
scene_logo_elements = []

# Group logo
el_logo_img_path = "resources/logo/red.png"
el_logo_img = pyglet.image.load(el_logo_img_path)
el_logo_img.anchor_x, el_logo_img.anchor_y = el_logo_img.width // 2, el_logo_img.height // 2
el_logo = pyglet.sprite.Sprite(el_logo_img, CENTER_X, CENTER_Y)
el_logo.scale = 1.25

scene_logo_elements.append(el_logo)
SCENE_LOGO = Scene("LOGO", scene_logo_elements)

# Scene: START
scene_start_elements = []

# Game title
el_game_title = Display("1  1", constants.GAME_FONT_NAME, constants.COLOR_BLACK, 190, CENTER_X + 20, CENTER_Y + 10)

# Play button
el_play_btn = Button("PLAY", 1.30, CENTER_X, CENTER_Y)

scene_start_elements.append(el_game_title)
scene_start_elements.append(el_play_btn)

SCENE_START = Scene("START", scene_start_elements)

# Scene: PLAY
scene_play_elements = []

# Deck of cards 
el_deck = Deck(CENTER_X, CENTER_Y - 50)

# Timer
el_timer = Timer(CENTER_X, CENTER_Y + constants.TIMER_Y_OFFSET)

scene_play_elements.append(el_timer)
scene_play_elements.append(el_deck)

SCENE_PLAY = Scene("PLAY", scene_play_elements)

# Scene: SCORE
scene_score_elements = []

# Game over text
el_game_over = Display("GAME OVER", constants.GAME_FONT_NAME, constants.COLOR_BLACK, 120, CENTER_X, CENTER_Y + 150)

# Text that shows your current score 
el_time_taken = Display("", constants.GAME_FONT_NAME, constants.COLOR_BLACK, 50, CENTER_X, CENTER_Y - 100)

# Text that shows your highest score achieved 
el_high_score = Display("", constants.GAME_FONT_NAME, constants.COLOR_BLACK, 50, CENTER_X, CENTER_Y - 200)

scene_score_elements.append(el_game_over)
scene_score_elements.append(el_time_taken)
scene_score_elements.append(el_high_score)

SCENE_SCORE = Scene("SCORE", scene_score_elements)

# Scene progression
SCENE_LOGO.next(SCENE_START)
SCENE_START.next(SCENE_PLAY)
SCENE_PLAY.next(SCENE_SCORE)
SCENE_SCORE.next(SCENE_START)