import constants, random, pyglet
from elements.Button import Button
from elements.Card import Card, CardState
from elements.Deck import Deck
from elements.Display import Display
from elements.Timer import Timer

WINDOW = pyglet.window.Window(fullscreen=True)

CENTER_X, CENTER_Y = WINDOW.width // 2, WINDOW.height // 2

class Scene:

	_next = None

	def __init__(self, name, elements):
		self.name = name
		self.elements = elements

	def next(self, scene):
		self._next = scene 
	
	def get_element(self, type):
		for el in self.elements:
			if isinstance(el, type):
				return el

	def draw(self):	
		for el in self.elements:
			el.draw()
		return self

pyglet.font.add_file(constants.GAME_FONT_PATH)

# Scene: LOGO
scene_logo_elements = []

el_logo_img_path = "resources/logo/red.png"
el_logo_img = pyglet.image.load(el_logo_img_path)
el_logo_img.anchor_x, el_logo_img.anchor_y = el_logo_img.width // 2, el_logo_img.height // 2
el_logo = pyglet.sprite.Sprite(el_logo_img, CENTER_X, CENTER_Y)
el_logo.scale = 1.25

scene_logo_elements.append(el_logo)
SCENE_LOGO = Scene("LOGO", scene_logo_elements)

# Scene: START
scene_start_elements = []

el_game_title = Display("1  1", constants.GAME_FONT_NAME, constants.COLOR_BLACK, 190, CENTER_X + 20, CENTER_Y + 10)
el_play_btn = Button("PLAY", 1.30, CENTER_X, CENTER_Y)

scene_start_elements.append(el_game_title)
scene_start_elements.append(el_play_btn)

SCENE_START = Scene("START", scene_start_elements)

# Scene: PLAY
scene_play_elements = []

el_deck = Deck(CENTER_X, CENTER_Y - 50)
el_timer = Timer(CENTER_X, CENTER_Y + constants.TIMER_Y_OFFSET)

scene_play_elements.append(el_timer)
scene_play_elements.append(el_deck)

SCENE_PLAY = Scene("PLAY", scene_play_elements)

# Scene: SCORE
scene_score_elements = []

el_game_over = Display("GAME OVER", constants.GAME_FONT_NAME, constants.COLOR_BLACK, 120, CENTER_X, CENTER_Y + 150)
el_time_taken = Display("", constants.GAME_FONT_NAME, constants.COLOR_BLACK, 50, CENTER_X, CENTER_Y - 100)
el_high_score = Display("", constants.GAME_FONT_NAME, constants.COLOR_BLACK, 50, CENTER_X, CENTER_Y - 200)

scene_score_elements.append(el_game_over)
scene_score_elements.append(el_time_taken)
scene_score_elements.append(el_high_score)

SCENE_SCORE = Scene("SCORE", scene_score_elements)

SCENE_LOGO.next(SCENE_START)
SCENE_START.next(SCENE_PLAY)
SCENE_PLAY.next(SCENE_SCORE)
SCENE_SCORE.next(SCENE_START)