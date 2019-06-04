import cTurtle
from planet import *
from sun import *

class SolarSystem:
    '''
    Constructor uses Turtle to define bounds to planetary coordinate system.
    We hide turtle so it doesn't appear on screen; coordinate system is
    distributed equally around (0,0).
    '''
    def __init__(self, width, height):
        self.theSun = None
        self.planets = []

        self.turtle = cTurtle.Turtle()
        self.turtle.hideturtle()

        self.turtle.setWorldCoordinates(-width/2.0, -height/2.0,
                                        width/2.0, height/2.0)

    def addSun(self, sun):
        self.theSun = sun

    def addPlanet(self, aplanet):
        self.planets.append(aplanet)

    def showPlanets(self):
        for aplanet in self.planets:
            print(aplanet)

    # method prevents animation from closing automatically upon completion
    def freeze(self):
        self.turtle.exitOnClick()

    # Animation method
    def movePlanets(self):
        G = 6.673e-11
        dt = 1800

        for p in self.planets:
            p.moveTo(p.getXPos() + dt * p.getXVelocity(),
                     p.getYPos() + dt * p.getYVelocity())

            rx = self.theSun.getXPos() - p.getXPos()
            ry = self.theSun.getYPos() - p.getYPos()
            r = math.sqrt(rx**2 + ry**2)

            accx = G * self.theSun.getMass()*rx/r**3
            accy = G * self.theSun.getMass()*ry/r**3

            p.setXVelocity(p.getXVelocity() + dt * accx)
            p.setYVelocity(p.getYVelocity() + dt * accy)

#simple solar system function with sun and four planets
def createSolarSysandAnimate():
    solarsys = SolarSystem(6,6)

    sun = Sun("Sun", 5000, 10, 5800)
    solarsys.addSun(sun)

    '''
    def __init__(self, name, radius, mass, distance, color,
                xVelocity, yVelocity, numOfMoons):
    '''

    p1 = Planet("Mercury", 2439.5, 0.330, 57.9, 'blue', 0, 2, 0)
    solarsys.addPlanet(p1)

    p1 = Planet("Venus", 6052, 4.87, 108.2, 'blue', 0, 2, 0)
    solarsys.addPlanet(p1)

    p2 = Planet("Earth", 6378, 5.97, 149.6, 'green', 0, 2.0, 1)
    solarsys.addPlanet(p2)

    p3 = Planet("Mars", 3396, 0.642, 227.9, 'red', 0, 1.63, 2)
    solarsys.addPlanet(p3)

    p4 = Planet("Jupiter", 71492, 1898, 778.6, 'orange', 0, 1, 79)
    solarsys.addPlanet(p4)

    p1 = Planet("Saturn", 60268, 568, 1433.5, 'blue', 0, 2, 62)
    solarsys.addPlanet(p1)

    p1 = Planet("Uranus", 25559, 86.8, 2872.5, 'blue', 0, 2, 27)
    solarsys.addPlanet(p1)

    p1 = Planet("Neptune", 24764, 102, 4495.1, 'blue', 0, 2, 14)
    solarsys.addPlanet(p1)

    p1 = Planet("Pluto", 1185, 0.0146, 5906.4, 'blue', 0, 2, 5)
    solarsys.addPlanet(p1)

    numTimePeriods = 2000
    for amove in range(numTimePeriods):
        solarsys.movePlanets()

    solarsys.freeze()

createSolarSysandAnimate()
