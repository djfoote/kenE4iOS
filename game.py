from scene import *
from sound import load_effect, play_effect

class Boy(object):
	IMG_SIZE = 128
	self.image = 'boy'

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def draw(self):
		image(self.image, self.x, self.y, 128, 128)

class GameScene (Scene):
	def setup(self):
		self.kenny = Boy(10, 10)

	def draw(self):
		kenny.draw()

run(MyScene)


