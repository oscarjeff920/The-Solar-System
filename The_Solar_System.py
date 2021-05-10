from vpython import *
import numpy as np
from matplotlib import pyplot as plt

from time_converter import time_converter
from Planets_Class import Planets

from random import randrange as rr

scene = canvas(title = "The Solar System")
solar_vel = vector(0,0,0)

the_sun = Planets(name = "The Sun",  pos = vector(0,0,0),              vel = vector(0,0,0),   mass = 1.989e30,  radius = 6.963e8, colour = color.yellow)
mercury = Planets(name = "Mercury",  pos = vector(Planets.StoMur,0,0), vel = vector(0,0,0),   mass = 3.285e23,  radius = 2.440e6, colour = vector(0.3, 0.3, 0.3))
venus =   Planets(name = "Venus",    pos = vector(1.078e11,0,0),       vel = vector(0,0,0),   mass = 4.867e24,  radius = 6.052e6, colour = vector(0.7,0.6,0.6))
earth =   Planets(name = "Earth",    pos = vector(149.6e9,0,0),        vel = vector(0,0,0),   mass = 5.972e24,  radius = 6.371e6, colour = vector(0,0.4,1))


mars =    Planets(name = "Mars",     pos = vector(2.475e11,0,0),       vel = vector(0,0,0),   mass = 6.390e23,  radius = 3.390e6, colour = color.red)
jupiter = Planets(name = "Jupiter",  pos = vector(7.566e11,0,0),       vel = vector(0,0,0),   mass = 1.898e27,  radius = 6.991e7, colour = vector(0.8,0.5,0.5))
saturn =  Planets(name = "Saturn",   pos = vector(1.488e12,0,0),       vel = vector(0,0,0),   mass = 5.683e26,  radius = 5.823e7, colour = vector(1,1,0.5))
uranus =  Planets(name = "Uranus",   pos = vector(2.955e12,0,0),       vel = vector(0,0,0),   mass = 8.681e25,  radius = 2.536e7, colour = vector(0.7,0.7,1))
neptune = Planets(name = "Neptune",  pos = vector(4.476e12,0,0),       vel = vector(0,0,0),   mass = 1.024e26,  radius = 2.462e7, colour = color.blue)

#blackhole = Planets(name = "Blackhole", pos = vector(0,-6e12,-5e13),        vel = vector(0,0,3e4),   mass = 7e30,    radius = the_sun.radius["m"]*2, colour = vector(1,1,1), in_solar_system = False)
comet = Planets(name = "Comet", pos = vector(-5e8,-2e10,0),             vel = vector(2e2,0,0), mass = 3e3, radius = 2e6, colour = vector(1,1,1))

for name in Planets.planetary_bodies:
    planet = Planets.planetary_bodies[name]
    if planet.in_solar_system:
        if name != "The Sun":
            planet.vel += planet.tang_vel(the_sun)
            #planet.vel = mag(planet.vel) * norm(vector(0,0.1*rr(-10,11),0.1*rr(-10,11)))
            
        planet.vel += solar_vel
    

rate(10)

t, dt = 0, time_converter(0, hours = 1)
increased_mass = False
while t < time_converter(0, centuries = 10):
    scene.camera.follow(earth.sphere)
    for name in Planets.planetary_bodies:
        planet = Planets.planetary_bodies[name]
        planet.motion(scene.camera.pos, dt)
        if name != "The Sun":
            if round(planet.pos["m"].x) == 0:
                planet.quarter_orbit = True
            if planet.quarter_orbit and round(planet.pos["m"].x) == planet.initPos.x:
                print("%s has made a full orbit in %s\nOr %s\m"%(name,t,time_converter(t)))
                planet.quarter_orbit = False

    if t < time_converter(0,years = 4):
        comet.pos["m"] = vector(-5e8,-2e10,0)
        
    """
    if t % 0.5 == 0:    
        print("sun mass = %s, mass lost = %s\ngrav on earth from sun = %s\n\n"%(the_sun.mass, 1.989e30 - the_sun.mass, mag(earth.a_grav(the_sun))))
    """   
    if t == time_converter(0, years = 1):
        print("earth coords = %s, distance from sun = %s\n"%(mag(earth.pos["m"]), earth.pos["m"]))
    
    t += dt
