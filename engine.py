import constants, pickle, pyglet
from elements.Button import Button
from elements.Card import Card, CardState
from elements.Deck import Deck
from elements.Display import Display
from elements.Timer import Timer
from interface import WINDOW, SCENE_PLAY, SCENE_SCORE

class Game:

	score = 0

	def __init__(self, first_scene):
		self.scene = first_scene 
		self.load_from_file()
		print(self.high_scores)
	
	def load_from_file(self):
		file = open(constants.NAME_SAVE_FILE, 'r')
		self.high_scores = []
		for line in file:
			self.high_scores.append(int(line))
		file.close()

	def save(self):
		file = open(constants.NAME_SAVE_FILE, 'w')
		for high_score in self.high_scores:
			file.write(str(high_score) + "\n")
		file.close()
	
	def get_current_scene(self):
		return self.scene
	
	def next(self):
		self.scene = self.scene._next		
	
	def set_score(self, score):
		self.score = score
		self.add_score_to_high_scores(score)

	def check_if_new_high_score(self):
		if self.score == self.high_scores[0]:
			return True
		return False

	def add_score_to_high_scores(self, score):
		self.high_scores.append(score)	
		self.high_scores = sorted(self.high_scores)
	
	def convert_score_to_text(self, score):
		m, s = divmod(score, 60)
		return '%02d:%02d' % (m, s)

	def get_timer(self):
		return SCENE_PLAY.get_element(Timer)
	
	def start_timer(self):
		if self.get_timer() is not None:
			self.get_timer().running = True
	
	def reset_timer(self):
		self.get_timer().reset()
	
	def check_for_mouse_movement(self, x, y):
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
		if self.get_current_scene().name == constants.NAME_SCENE_LOGO:
			if button is pyglet.window.mouse.LEFT:
				self.next()
		elif self.get_current_scene().name == constants.NAME_SCENE_START:
			play_button = self.get_current_scene().get_element(Button)
			if button is pyglet.window.mouse.LEFT:
				if play_button.under_mouse(x, y):
					self.next()
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
					print(self.high_scores)
					self.save()
