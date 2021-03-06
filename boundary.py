import maya.cmds as cmds
import vectors ; from vectors import *
import math

class Boundary:
	def __init__(self, w = 17.0, h = 17.0, d = 17.0, x = 0.0, y = 0.0, z = 0.0):
		self.dimensions = V(w, h, d)
		self.boidSpawnBoundary = 0.2 # works as a padding in percentage
		self.position = V(x, y, z)
		self.force = 4.0

	def setFromName(self, name):
		if cmds.objExists(name):
			self.position = V(cmds.getAttr("{0}.translate".format(name))[0])
			boundaryScale = cmds.getAttr("{0}.scale".format(name))[0]
			self.dimensions[0] = cmds.polyCube(name, query=True, width=True) * boundaryScale[0]
			self.dimensions[1] = cmds.polyCube(name, query=True, height=True) * boundaryScale[1]
			self.dimensions[2] = cmds.polyCube(name, query=True, depth=True) * boundaryScale[2]
		else:
			print "box with name \"{0}\" does not exist".format(name)

	def getSpawnDimensions(self):
		area = [
			self.dimensions[0] * self.boidSpawnBoundary,
			self.dimensions[1] * self.boidSpawnBoundary,
			self.dimensions[2] * self.boidSpawnBoundary
		]
		return area

	def getPosition(self):
		return self.position

	def avoidWalls(self, boid):
		position = boid.getPosition()
		if position[0] > self.position[0] + self.dimensions[0]/2:
			boid.addForce(V(-self.force, 0.0, 0.0))
		elif position[0] < self.position[0] - self.dimensions[0]/2:
			boid.addForce(V(self.force, 0.0, 0.0))

		if position[1] > self.position[1] + self.dimensions[1]/2:
			boid.addForce(V(0.0, -self.force, 0.0))
		elif position[1] < self.position[1] - self.dimensions[1]/2:
			boid.addForce(V(0.0, self.force, 0.0))

		if position[2] > self.position[2] + self.dimensions[2]/2:
			boid.addForce(V(0.0, 0.0, -self.force))
		elif position[2] < self.position[2] - self.dimensions[2]/2:
			boid.addForce(V(0.0, 0.0, self.force))