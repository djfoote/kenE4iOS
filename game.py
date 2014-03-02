from scene import *
from random import random
from sound import load_effect, play_effect

class Character (object):
	IMG_SIZE = 128
	def __init__(self, x, y, scale):
		assert(scale >= 0)
		self.image_size = Character.IMG_SIZE * scale
		self.position = Vector2(x, y)
		self.velocity = Vector2(0, 0)
		self.acceleration = Vector2(0, 0)
		self.image = 'Boy'
		self.sound = 'Footstep'

	def draw(self):
		image(self.image, self.position.x - self.image_size/2, 
			self.position.y - self.image_size/2)

	def hit_test(self, touch):
		frame = Rect(self.x - self.image_size/2,
		             self.y - self.image_size/2,
		             self.image_size, self.image_size)
		return touch.location in frame

	def touch_vector(self, touch):
		return Vector2(self.position.x - touch.location.x,
			self.position.y - touch.location.y)

	def move(self, g):
		self.acceleration = Vector2(0, g.y)
		self.velocity += self.acceleration
		self.position += self.velocity

class Vector2 ():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vector2(self.x + other.x, self.y + other.y)

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
		self.kenny.move(gravity())
		self.kenny.draw()

	def touch_began(self, touch):
		if self.kenny.hit_test(touch):
			play_effect('Footstep')
			self.kenny.velocity += self.kenny.touch_vector
			

run(GameScene())
