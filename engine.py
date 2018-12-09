import constants, pickle, pyglet
from elements.Button import Button
from elements.Card import Card, CardState
from elements.Deck import Deck
from elements.Display import Display
from elements.Timer import Timer
from interface import WINDOW, SCENE_PLAY, SCENE_SCORE

class Game:
	"""
    A class used to represent the game 

    ...

    Attributes
    ----------
	score : int
		score of the player
    scene : Scene
		current scene being displayed on-screen
	high_scores : list
		list of scores that the player has achieved arranged in ascending order

    Methods
    -------
	load_from_file()
		Loads scores from an external file
	save()
		Saves scores to an external file
	get_current_scene()
		Gets the current scene being displayed
	next()
		Sets the scene to the next one in the queue
	set_score(score)
		Sets the score to the most recent one
	check_if_new_high_score()
		Checks if a new high score has been achieved
	add_score_to_high_scores(score)
		Add the most recent score to the list of high scores
	convert_score_to_text(score)
		Converts the score, which is in seconds, into mm:ss format
	get_timer()
		Gets the game timer
	start_timer()
		Starts the game timer
	reset_timer()
		Resets the game timer
	check_for_mouse_movement(x, y)
		Checks for mouse movement and handles related events based on the current scene
	check_for_mouse_press(x, y, button):
		Checks for mouse press and handles related events based on the current scene
	check_for_key_release(symbol):
		Checks for key press and handles related events based on the current scene
    """

	score = 0

	def __init__(self, first_scene):
		"""
        Parameters
        ----------
        score : int
			score of the player
		scene : Scene
			current scene being displayed on-screen
		high_scores : list
			list of scores that the player has achieved arranged in ascending order
        """
		self.scene = first_scene 
		self.load_from_file()
	
	def load_from_file(self):
		"""
			Loads scores from an external file
		"""
		file = open(constants.NAME_SAVE_FILE, 'r')
		self.high_scores = []
		for line in file:
			self.high_scores.append(int(line))
		file.close()

	def save(self):
		"""
			Saves scores to an external file
		"""
		file = open(constants.NAME_SAVE_FILE, 'w')
		for high_score in self.high_scores:
			file.write(str(high_score) + "\n")
		file.close()
	
	def get_current_scene(self):
		"""
			Gets the current scene being displayed
		"""
		return self.scene
	
	def next(self):
		"""
			Sets the scene to the next one in the queue
		"""
		self.scene = self.scene._next		
	
	def set_score(self, score):
		"""
			Sets the score to the most recent one
		"""
		self.score = score
		self.add_score_to_high_scores(score)

	def check_if_new_high_score(self):
		"""
			Checks if a new high score has been achieved
		"""
		if self.score == self.high_scores[0]:
			return True
		return False

	def add_score_to_high_scores(self, score):
		"""
			Adds the most recent score to the list of high scores
		"""
		self.high_scores.append(score)	
		self.high_scores = sorted(self.high_scores)
	
	def convert_score_to_text(self, score):
		"""
			Converts the score, which is in seconds, into mm:ss format
		"""
		m, s = divmod(score, 60)
		return '%02d:%02d' % (m, s)

	def get_timer(self):
		"""
			Gets the game timer
		"""
		return SCENE_PLAY.get_element(Timer)
	
	def start_timer(self):
		"""
			Starts the game timer
		"""
		if self.get_timer() is not None:
			self.get_timer().running = True
	
	def reset_timer(self):
		"""
			Resets the game timer
		"""
		self.get_timer().reset()
	
	def check_for_mouse_movement(self, x, y):
		"""
			Checks for mouse movement and handles related events based on the current scene

			Parameters
			----------
			x : int 
				The x-coordinate of the mouse cursor after movement	
			y : int 
				The y-coordinate of the mouse cursor after movement
		"""
		if self.get_current_scene().name == constants.NAME_SCENE_START:
			play_button = self.get_current_scene().get_element(Button)
			if play_button.under_mouse(x, y):
				cursor = WINDOW.get_system_mouse_cursor(WINDOW.CURSOR_HAND)
				play_button._hover = True
			else:
				cursor = WINDOW.get_system_mouse_cursor(WINDOW.CURSOR_DEFAULT)
				play_button._hover = False
			WINDOW.set_mouse_cursor(cursor)
		elif self.get_current_scene().name == constants.NAME_SCENE_PLAY:
			card_index = None
			deck = self.get_current_scene().get_element(Deck)
			if len(deck.get_selected_cards()) < 2:
				for i in range(len(deck.cards)):
					if deck.cards[i] is not None:
						if not deck.cards[i].under_mouse(x, y):
							if deck.cards[i]._state is not CardState.SELECTED:
								deck.cards[i]._state = CardState.FACE_DOWN
						else:
							card_index = i
			if card_index is not None:
				if deck.cards[card_index]._state is CardState.FACE_DOWN:
					deck.cards[card_index]._state = CardState.HOVER
				cursor = WINDOW.get_system_mouse_cursor(WINDOW.CURSOR_HAND)
			else:
				cursor = WINDOW.get_system_mouse_cursor(WINDOW.CURSOR_DEFAULT)
			WINDOW.set_mouse_cursor(cursor)
	
	def check_for_mouse_press(self, x, y, button):
		"""
			Checks for mouse press and handles related events based on the current scene

			Parameters
			----------
			x : int 
				The x-coordinate of the mouse cursor after clicking	
			y : int 
				The y-coordinate of the mouse cursor after clicking
		"""
		if self.get_current_scene().name == constants.NAME_SCENE_LOGO:
			if button is pyglet.window.mouse.LEFT:
				self.next()
		elif self.get_current_scene().name == constants.NAME_SCENE_START:
			play_button = self.get_current_scene().get_element(Button)
			if button is pyglet.window.mouse.LEFT:
				if play_button.under_mouse(x, y):
					self.next()
					if self.get_current_scene().get_element(Deck).check_if_empty():
						self.get_current_scene().get_element(Deck).populate()
					self.get_current_scene().get_element(Timer).running = True
		elif self.get_current_scene().name == constants.NAME_SCENE_PLAY:
			deck = self.get_current_scene().get_element(Deck)
			if button is pyglet.window.mouse.LEFT:
				for card in deck.cards:
					if card is not None:
						if card.under_mouse(x, y):
							if len(deck.get_selected_cards()) != 2:
								card._state = CardState.SELECTED
		elif self.get_current_scene().name == constants.NAME_SCENE_SCORE:
			if button is pyglet.window.mouse.LEFT:
				self.next()
	
	def check_for_key_release(self, symbol):
		"""
			Checks for key press and handles related events based on the current scene

			Parameters
			----------
			symbol: pyglet.window.key
				the key pressed
		"""
		if self.get_current_scene().name == constants.NAME_SCENE_PLAY:
			if symbol is pyglet.window.key.SPACE:
				deck = self.get_current_scene().get_element(Deck)
				if len(deck.get_selected_cards()) == 2:
					fci, sci = deck.get_selected_cards()
					if deck.cards[fci].compare_with(deck.cards[sci]):
						deck.cards[fci], deck.cards[sci] = None, None
					else:
						deck.cards[fci]._state = CardState.FACE_DOWN
						deck.cards[sci]._state = CardState.FACE_DOWN
				if deck.check_if_empty():
					self.set_score(self.get_timer().time)
					self.reset_timer()
					self.next()
					self.get_current_scene().elements[1].text = "Time taken: " + self.convert_score_to_text(self.score)
					self.get_current_scene().elements[2].text = "High Score: " + self.convert_score_to_text(self.high_scores[0])
					if self.check_if_new_high_score():
						self.get_current_scene().elements[2].color = constants.COLOR_RED
					else:
						self.get_current_scene().elements[2].color = constants.COLOR_BLACK
					self.save()
					SCENE_PLAY.get_element(Deck).populate()
