from scene import *
from random import random
from sound import load_effect, play_effect
from traceback import print_stack

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
		self.set_frame()

	def set_frame(self):
		self.frame = Rect(self.position.x - self.image_size/2,
		             self.position.y - self.image_size/2,
		             self.image_size, self.image_size)

	def draw(self):
		image(self.image, self.position.x - self.image_size/2, 
			self.position.y - self.image_size/2)

	def hit_test(self, touch):
		return touch.location in self.frame

	def touch_vector(self, touch):
		return Vector2(self.position.x - touch.location.x,
			self.position.y - touch.location.y)

	def move(self, scene):
		g = gravity()
		self.acceleration = Vector2(g.x, g.y)
		self.velocity += self.acceleration
		self.velocity *= .97 #dampening
		self.position += self.velocity
		self.edge_collision(scene)
		self.set_frame()

	def edge_collision(self, scene):
		if self.velocity.x < 0 and self.frame.left() < 0:
			self.position.x = self.image_size/2
			self.velocity.x *= -1
		if self.velocity.x > 0 and self.frame.right() > scene.size.w:
			self.position.x = scene.size.w - self.image_size/2
			self.velocity.x *= -1
		if self.velocity.y < 0 and self.frame.bottom() < 0:
			self.position.y = self.image_size/2
			self.velocity.y *= -1
		if self.velocity.y > 0 and self.frame.top() > scene.size.h:
			self.position.y = scene.size.h - self.image_size/2
			self.velocity.y *= -1

class Vector2 (object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		if type(other) != type(self):
			print_stack()
			print other
		return Vector2(self.x + other.x, self.y + other.y)

	def __mul__(self, c):
		return Vector2(self.x * c, self.y * c)

class Score (object):
	def __init__(self):
		self.points = 0

	def draw(self, scene):
		HEIGHT = 40
		bottom = scene.size.h - HEIGHT
		fill(0, 0, 0)
		rect(0, bottom, scene.size.w, HEIGHT)
		score_string = 'Your Score: ' + str(self.points)
		text(score_string, x=scene.size.w/2, y=bottom + HEIGHT/2)

class GameScene (Scene):
	def setup(self):
		self.kenny = Character(self.size.w/2, self.size.h/2, 1)
		load_effect('Footstep')
		load_image('Boy')
		self.bg_color = Color(0, 0, 0)
		self.score = Score()

	def draw(self):
		self.bg_color.r = \
				max(0, min(1, self.bg_color.r + (random() - 0.5) / 30))
		self.bg_color.g = \
				max(0, min(1, self.bg_color.g + (random() - 0.5) / 30))
		self.bg_color.b = \
				max(0, min(1, self.bg_color.b + (random() - 0.5) / 30))
		background(self.bg_color.r, self.bg_color.g, self.bg_color.b)
		self.score.draw(self)
		self.kenny.move(self)
		self.kenny.draw()

	def touch_began(self, touch):
		if self.kenny.hit_test(touch):
			play_effect('Footstep')
			self.kenny.velocity += self.kenny.touch_vector(touch)
			self.score.points += 1

	def touch_moved(self, touch):
		self.touch_began(touch)
			

run(GameScene())
