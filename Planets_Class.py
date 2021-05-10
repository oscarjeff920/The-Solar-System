from vpython import *
import numpy as np
class Planets():
    G = 6.67e-11
    AU = 1.496e11
    StoMur = 5.07e10
    planetary_bodies = {}
    def __init__(self, name, pos, mass, radius, colour, in_solar_system = True, stable_orbit = False, vel = 0):
        self.name = name
        self.in_solar_system = in_solar_system
        self.initPos = pos
        self.pos = dict(m = pos, model = 1000*(pos/Planets.StoMur))
        self.radius = dict(m = radius, model = Planets.radius_fudge(radius))
        self.vel = vel
        self.mass = mass
        self.sphere = sphere(canvas = scene, pos = self.pos["model"], radius = self.radius["model"], color = colour, make_trail = True)
        self.quarter_orbit = False
        self.orbit_data = []
        Planets.planetary_bodies[name] = self
    
    def tang_vel(self, bodyB):
        a = mag(self.a_grav(bodyB))
        v2 = a*mag(self.pos["m"])
        return vector(0,np.sqrt(v2),0)
    
    def radius_fudge(r):
        mag = Planets.order_mag(r)
        mag += round(r*10**-(Planets.order_mag(r)+1)) if int(r*10**-(Planets.order_mag(r))) != 1 else -1
        answer = 9 - mag
        return 10000*round(0.05 - 0.01*answer,2)
    
    def __str__(self):
        print("%s sits at pos = %s, with velocity = %s, mass = %s and radius = %s"%(self.name,self.pos,self.vel,self.mass,self.radius))
                           
    def order_mag(n):
        return len(str(n)) - 3
    
    def a_grav(self, bodyB):
        answer = (Planets.G * bodyB.mass)
        distance = mag(bodyB.pos["m"]) - mag(self.pos["m"])
        distanceSqurd = distance**2
        answer /= distanceSqurd
        answer *= -norm(self.pos["m"])
        return answer
    
    def update_attr(self, cam_pos):
        self.pos["model"] = 1000*(self.pos["m"]/Planets.StoMur)
        self.sphere.pos = self.pos["model"]
        """cam_distance = abs(mag(cam_pos - self.pos["model"]))
        if cam_distance < 5000:
            factor = (cam_distance/(5000))
        else:
            factor = 1
        self.radius["model"] = Planets.radius_fudge(self.radius["m"]) * factor
        
        self.sphere.radius = self.radius["model"]"""
    
    def motion(self, cam_pos, dt):
        self.pos["m"] += self.vel * dt
        for name in Planets.planetary_bodies:
            planet = Planets.planetary_bodies[name]
            if name != self.name:
                self.vel += self.a_grav(planet) * dt
        self.update_attr(cam_pos)
