import maya.cmds as cmds
import boid.Boid as Boid
import random

boids = []
dt=1/60

def createBoids(numBoids):
	'''create numboids boids and randomize position'''
	for i in range(numBoids):
		boid = Boid("boid{0}".format(i))
		x = random.uniform(-10, 10);
		y = random.uniform(-10, 10);
		z = random.uniform(-10, 10);
		boid.setPosition(x, y, z)
		boids.append(Boid("boid{0}".format(i)))

	print 'creating boids done'


def run():
	'''run the simulation'''
	createBoids()
	createKeyFrames(100)

	cmds.playbackOptions(max=nFrames)
	cmds.playbackOptions(aet=nFrames)

	cmds.play()

def clear():
	'''cleanup'''
	while boids:
		boid = boids.pop()
		boid.delete()

def createKeyFrames(numFrames):
	'''create the keyframes for the animation'''
	for frame in range(numFrames)
		for boid in boids
			boid.addVelocity([0.01, 0, 0])
			boid.move(dt)
			boid.setKeyframe(frame*dt)


def alignment():
	'''flocking function'''
	pass
def separation():
	'''flocking function'''
	pass
def cohesion():
	'''flocking function'''
	pass

