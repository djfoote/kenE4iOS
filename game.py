from scene import *
from sound import load_effect, play_effect

class Character(object):
	IMG_SIZE = 128
	def __init__(self, x, y, scale):
		assert(scale >= 0)
		self.image_size = IMG_SIZE * scale
		self.x = x
		self.y = y
		self.image = 'Boy'
		self.sound = 'Footstep'

	def draw(self):
		image(self.image, self.x - self.image_size/2, 
			self.y - self.image_size/2)

	def hit_test(self, touch):
		frame = Rect(self.x - self.image_size/2,
		             self.y - self.image_size/2,
		             image_size, image_size)
		return touch.location in frame

class GameScene (Scene):
	def setup(self):
		self.kenny = Character(self.size.w/2, self.size.h/2)
		load_effect('Footstep')

	def draw(self):
		self.kenny.draw()
		if self.kenny.hit_test()

	def touch_began(self, touch):
		if self.kenny.hit_test(touch):
			play_effect('Footstep')

run(GameScene())
