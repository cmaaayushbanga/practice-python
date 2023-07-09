import math
import turtle

class Planet:
    def __init__(self, name, radius, color, distance, speed):
        self.name = name
        self.radius = radius
        self.color = color
        self.distance = distance
        self.speed = speed
        self.angle = 0
        self.turtle = turtle.Turtle()
        self.turtle.color(color)
        self.turtle.shape("circle")
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(distance, 0)
        self.turtle.pendown()

    def orbit(self):
        x = self.distance * (math.cos(math.radians(self.angle)))
        y = self.distance * (math.sin(math.radians(self.angle)))
        self.turtle.goto(x, y)
        self.angle += self.speed

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")

    sun = Planet("Sun", 69, "yellow", 0, 0)
    mercury = Planet("Mercury", 2.439, "gray", 50, 2)
    venus = Planet("Venus", 6.052, "orange", 100, 1.5)
    earth = Planet("Earth", 6.371, "blue", 150, 1)
    mars = Planet("Mars", 3.389, "red", 200, 0.8)
    jupiter = Planet("Jupiter", 71.492, "orange", 250, 0.5)
    saturn = Planet("Saturn", 60.268, "gold", 300, 0.3)
    uranus = Planet("Uranus", 25.559, "light blue", 350, 0.2)
    neptune = Planet("Neptune", 24.622, "dark blue", 400, 0.1)
    pluto = Planet("Pluto", 1.188, "light gray", 450, 0.05)

    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]

    while True:
        for planet in planets:
            planet.orbit()

    screen.exitonclick()

if __name__ == "__main__":
    main()