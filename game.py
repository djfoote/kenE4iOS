from scene import *
from sound import load_effect, play_effect

class Boy(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.image = 'Boy'

	def draw(self):
		image(self.image, self.x, self.y)

class GameScene (Scene):
	def setup(self):
		self.kenny = Boy(self.size.w/2, self.size.h/2)

	def draw(self):
		self.kenny.draw()

run(GameScene)


