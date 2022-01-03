from vpython.vector import vector
from vpython.vpython import box, color, curve, label, sphere,arrow
from vpython.rate_control import rate

ball = sphere(
    pos=vector(-5,18,0),
    radius=1,
    color=color.green
)
bottom = box(
    pos=vector(0,-9,0),
    size=vector(25,0.5,25)
)

v = vector(0.7, 0,0)
y = ball.pos
g = vector(0, -9.81, 0)

ball.trail = curve(color=ball.color)
arroww = arrow(pos=ball.pos,axis=v,color=color.yellow)

label1 = label()


dt = 0.005
t = 0.0


while True:
    rate(300) # 300 Hz의 속도로 루프를 실행합니다
 
    # 바닥에 닿는 순간 속도의 크기는 그대로하고 방향을 바꿉니다
    # 완전탄성충돌 
    if ball.pos.y < (bottom.pos.y + 1):
        v.y = -v.y

    # 공식을 사용해 속도와 위치를 계산합니다
    v += g*dt   
    y += v*dt + 0.5*g*dt**2
 

    # 공의 위치와 궤적을 업데이트합니다
    ball.pos = y
    ball.trail.append(pos = ball.pos)
 
    # 속도 화살표를 설정합니다
    arroww.pos = ball.pos
    arroww.axis = v*0.3
 
    label1.pos = bottom.pos + vector(0,-0.5,0)
    label1.text = 'v is : %.2f m/s'  % v.y