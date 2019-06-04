import math
import cTurtle

class Planet:

    def __init__(self, name, radius, mass, distance, color,
                xVelocity, yVelocity, numOfMoons):
        '''Constructor to create instances of our Planet class'''
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.numOfMoons = numOfMoons
        self.listOfMoons = []

        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

        self.x = distance
        self.y = 0
        self.color = color

        self.planetTurtle = cTurtle.Turtle()

        self.planetTurtle.color(self.color)
        self.planetTurtle.shape('circle')

        self.planetTurtle.up()
        self.planetTurtle.goto(self.x, self.y)
        self.planetTurtle.down()

    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.planetTurtle.goto(newx, newy)

    # Accessor methods to access instance variables of the object
    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getDistance(self):
        return self.distance

    def getMoons(self):
        return self.numOfMoons

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getXVelocity(self):
        return self.xVelocity

    def getYVelocity(self):
        return self.yVelocity

    # Accessor methods that return computed results based upon values of instance
    # variables
    def getCircumference(self):
        circumference = 2 * math.pi * self.radius

    def getVolume(self):
        volume = 4.0/3 * math.pi * self.radius**3
        return volume

    def getSurfaceArea(self):
        surfaceArea = 4.0 * math.pi * self.radius**2
        return surfaceArea

    def getDensity(self):
        density = self.mass / self.getVolume()
        return density

    # Mutator methods to manipulate instance variables (mutator methods typically
    # return nothing)
    def setName(self, newName):
        self.name = newName

    def setMoons(self, newNumOfMoons):
        self.numOfMoons = newNumOfMoons

    def addMoon(self, newMoon):
        self.listOfMoons.append(newMoon)

    def setXVelocity(self, newXVelocity):
        self.xVelocity = newXVelocity

    def setYVelocity(self, newYVelocity):
        self.yVelocity = newYVelocity

    def __str__(self):
        return self.name
