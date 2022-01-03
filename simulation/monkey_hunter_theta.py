from math import cos, sin, sqrt, tan
from vpython.vector import vector
from vpython.vpython import box, color, curve, label, sphere, arrow
from vpython.rate_control import rate


# GlowScript 3.2 VPython

for i in range(1,90,0.1) :
    size = 0.2
    g = -9.81
    t = 0
    dt = 0.0004
    v_0 = 20
    L = 20
    theta = i
    H = L * tan(theta)
    
    bullet = sphere(radius=size, color=color.white)
    bullet.pos = vector(-L/2, 0, 0)
    bullet.v = vector(v_0*cos(theta), v_0*sin(theta), 0)

    monkey = sphere(radius=size, color=color.white)
    monkey.pos = vector(L/2, H, 0)
    monkey.v = vector(0, 0, 0)

    while 1:
        rate(1/dt)
        t += dt

        bullet.pos += bullet.v*dt
        bullet.v += vector(0, g*dt, 0)

        monkey.pos += monkey.v*dt
        monkey.v += vector(0, g*dt, 0)
        
        if bullet.pos.x-monkey.pos.x >=-0.1 and bullet.pos.x-monkey.pos.x <= 0.1 :
            break
