from vpython.vector import vector
from vpython.vpython import box, color, curve, label, sphere,arrow
from vpython.rate_control import rate
 
 

size = 0.2  # 공의 반지름 m
g = -9.81   # 중력가속도
 
# 공을 생성하고 초기 위치를 3m로 설정합니다
ball = sphere(radius=size, color=color.white)
ball.pos = vector(0,3,0)
ball.v = vector(0,0,0)
 
# 바닥면을 생성합니다
bottom = box(pos=vector(0,-1+size,0), length=3, heigth=0.1, width=3, texture=textures.wood)
 
t = 0
dt = 0.0004   
 
label1 = label()
label2 = label()
 
while True:
    rate(1/dt)  # rate * dt = 1이 되게 설정하면 실제 시간과 같은 루프주기를 얻을 수 있습니다
    t += dt
 
    # 공이 땅에 닿으면 (y == 0) 공의 속도를 반대로 바꿉니다. 완전탄성충돌
    if ball.pos.y <= 0:
        ball.v.y = abs(ball.v.y)

    # 공의 위치와 속도를 업데이트합니다
    ball.pos += ball.v*dt
    ball.v += vector(0,g*dt,0)
    # 텍스트 데이터
    # label1.pos = bottom.pos + vector(0, -0.5,0)
    # label1.text = 'time : %.2f s' % t
    # label2.pos = bottom.pos + vector(0, -1.2,0)
    # label2.text = 'vel : %.2f m/s' % ball.v.y

