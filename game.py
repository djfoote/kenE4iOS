from scene import *
from random import random
from sound import load_effect, play_effect

class Character (object):
	IMG_SIZE = 128
	def __init__(self, x, y, scale):
		assert(scale >= 0)
		self.image_size = Character.IMG_SIZE * scale
		self.x = x
		self.y = y
		self.velocity = Vector2(0, 0)
		self.acceleration = Vector2(0, 0)
		self.image = 'Boy'
		self.sound = 'Footstep'

	def draw(self):
		image(self.image, self.x - self.image_size/2, 
			self.y - self.image_size/2)

	def hit_test(self, touch):
		frame = Rect(self.x - self.image_size/2,
		             self.y - self.image_size/2,
		             self.image_size, self.image_size)
		return touch.location in frame

class GameScene (Scene):
	def setup(self):
		self.kenny = Character(self.size.w/2, self.size.h/2, 1)
		load_effect('Footstep')
		load_image('Boy')
		self.bg_color = Color(0, 0, 0)

	def draw(self):
		self.bg_color.r = \
				max(0, min(1, self.bg_color.r + (random() - 0.5) / 30))
		self.bg_color.g = \
				max(0, min(1, self.bg_color.g + (random() - 0.5) / 30))
		self.bg_color.b = \
				max(0, min(1, self.bg_color.b + (random() - 0.5) / 30))
		background(self.bg_color.r, self.bg_color.g, self.bg_color.b)
		self.kenny.draw()

	def touch_began(self, touch):
		if self.kenny.hit_test(touch):
			play_effect('Footstep')

run(GameScene())

class Vector2 ():
	def __init__(self, x, y):
		self.x = x
		self.y = y
