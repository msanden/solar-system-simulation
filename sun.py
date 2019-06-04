import math
import cTurtle

class Sun:

    def __init__(self, name, radius, mass, temperature):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temperature = temperature
        self.x = 0
        self.y = 0

        self.sunTurtle = cTurtle.Turtle()

        self.sunTurtle.shape('circle')
        self.sunTurtle.color('yellow')

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getTemperature(self):
        return self.temperature

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getVolume(self):
        volume = 4.0/3 * math.pi * self.radius**3
        return volume

    def getSurfaceArea(self):
        surfaceArea = 4.0 * math.pi * self.radius**2
        return surfaceArea

    def getDensity(self):
        density = self.mass / self.getVolume()
        return density
