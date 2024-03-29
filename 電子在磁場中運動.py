"""
2021.7.20 
 帶電粒子在磁場中的運動
"""
from vpython import *

"""
 1. 參數設定
    1、theta=0,phi=0：速度只有X分量，沿X軸等速度運動
    2、(theta,phi)=(90,0)、(0,90)：速度沒有X分量，在yz平面上坐等速度運動
    3、速度與X軸夾角=0or180：hea=80/100,phi=80：螺線運動
    """
size, m, q = 0.005, 1E-10, 1E-9 # 粒子半徑, 質量, 電量
theta = radians(80)            # 粒子初速度與 xy 平面夾角
phi = radians(40)              # 粒子初速度在 xy 平面投影與 x 軸夾角
v0 = 10*vec(cos(theta)*cos(phi), cos(theta)*sin(phi), sin(theta))  # 粒子初速度
L = 0.4                      # 坐標軸長度
B_field = vec(10, 0, 0)      # 磁場
t, dt = 0, 1E-5              # 時間, 時間間隔

"""
 2. 畫面設定
"""
# 產生動畫視窗
scene = canvas(title="Charged Particle in Magnetic Field", width=800, height=600, x=0, y=0, 
               center=vec(0, 0, 0), range=0.6*L, background=color.black)
if(theta == pi/2 or phi == pi/2):
    scene.camera.pos = vec(L, L/4, L/4)
    scene.camera.axis = vec(-L, -L/4, -L/4)
else:
    scene.camera.pos = vec(L/4, L/4, L)
    scene.camera.axis = vec(-L/4, -L/4, -L)
# 產生帶電粒子
charge = sphere(pos=vec(0, 0, 0), radius=2*size, v=v0, color=color.red, m=m, make_trail=True, retain = 1000)
# 產生坐標軸及標籤
arrow_x = arrow(pos=vec(-L/2, 0, 0), axis=vec(L, 0, 0), shaftwidth=0.6*size, color=color.yellow)
label_x = label(pos=vec(L/2, 0, 0), text="x", xoffset=25, color=color.yellow, font="sans")
arrow_y = arrow(pos=vec(0, -L/2, 0), axis=vec(0, L, 0), shaftwidth=0.6*size, color=color.yellow)
label_y = label(pos=vec(0, L/2, 0), text="y", yoffset=25, color=color.yellow, font="sans")
arrow_z = arrow(pos=vec(0, 0, -L/2), axis=vec(0, 0, L), shaftwidth=0.6*size, color=color.yellow)
label_z = label(pos=vec(0, 0, L/2), text="z", xoffset=-25, yoffset=-25, color=color.yellow, font="sans")
# 產生表示磁場的箭頭及標籤
arrow_B = arrow(pos=vec(-L/2, 0, 0), axis=B_field.norm()*0.1, shaftwidth=size, color=color.green)
label_B = label(pos=vec(-L/2, 0, 0), text="B", xoffset=25, yoffset=25, color=color.green, font="sans")
# 產生表示速度、加速度的箭頭
arrow_v = arrow(pos=charge.pos, shaftwidth=0.5*size, color=color.blue)
arrow_a = arrow(pos=charge.pos, shaftwidth=0.5*size, color=color.magenta)

"""
 3. 物體運動部分
"""
while(abs(charge.pos.x) < 0.6*L and abs(charge.pos.y) < 0.6*L and abs(charge.pos.z) < 0.6*L):
    rate(2500)
# 計算帶電粒子所受合力, 更新帶電粒子加速度、速度、位置
    F = q*cross(charge.v, B_field)
    charge.a = F/charge.m
    charge.v += charge.a*dt
    charge.pos += charge.v*dt
# 更新表示速度、加速度的箭頭, 只畫出方向以避免動畫自動縮小
    arrow_v.pos = charge.pos
    arrow_a.pos = charge.pos
    arrow_v.axis = charge.v.norm()*0.1
    arrow_a.axis = charge.a.norm()*0.1
# 更新時間
    t += dt
