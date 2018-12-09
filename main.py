import constants, pyglet
from elements.Timer import Timer
from interface import WINDOW, SCENE_LOGO
from engine import Game

window = WINDOW 

pyglet.gl.glClearColor(360.0, 360.0, 360.0, 0.0)

pyglet.font.add_file(constants.GAME_FONT_PATH)

game = Game(SCENE_LOGO)
start_timer = False

@window.event
def on_mouse_motion(x, y, dx, dy):
	game.check_for_mouse_movement(x, y)
	
@window.event
def on_mouse_press(x, y, button, modifiers):
	game.check_for_mouse_press(x, y, button)	

@window.event
def on_key_release(symbol, modifiers):	
	game.check_for_key_release(symbol)

@window.event
def on_draw():
	window.clear()
	game.get_current_scene().draw()

pyglet.clock.schedule_interval(game.get_timer().update, 1)
pyglet.app.run()