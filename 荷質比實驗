"""
 vpython荷質比
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size, m , v0 = 0.005, 2E-11, 20   # 粒子半徑, 質量 , 水平速度
V, d, L = 1, 0.1, 0.2      # 平行帶電板間的電壓, 距離, 長度
E_field = vec(0, -V/d, 0)  # 電場
t, dt = 0, 1E-5            # 時間, 時間間隔
#四種粒子參數
charges = {"A":-2E-9,"B":-1.2E-9,"C":-0.4E-9,"D":1.2E-9,"E":2E-9}
colors = {"A":color.red,"B":color.white,"C":color.orange,"D":color.purple,"E":color.cyan}
particles = ["A","B","C","D","E"]
"""
 2. 畫面設定
"""
# 產生動畫視窗、平行帶電板、水平線、粒子
scene = canvas(title="Mass-to-Charge Ratio", width=800, height=600, x=0, y=0,
               center=vec(0, 0, 0), background = color.black, range=1.2*L)
p1 = box(pos=vec(-L/2, d/2, 0), size=vec(L, 0.01*L, L), color=color.blue)
p2 = box(pos=vec(-L/2, -d/2, 0), size=vec(L, 0.01*L, L), color=color.blue)
screen = box(pos=vec(L, 0, 0), size=vec(0.01*L, 1.5*L, L), color=color.blue)
line = cylinder(pos=vec(-1.5*L, 0, 0), radius=0.2*size, axis=vec(3*L, 0, 0), color=color.yellow)
charge = sphere(pos=vec(-1.5*L, 0, 0), v=vec(v0, 0, 0), radius=size, m=m,make_trail=True)
# 產生表示電場的箭頭及標籤
arrow_E = arrow(pos=vec(-L, d/2, 0), axis=vec(0, -0.1, 0), shaftwidth=size, color=color.green)
label_E = label(pos=vec(-L, d/2, 0), text="E", xoffset=-25, yoffset=25, color=color.green, font="sans")


"""
 3. 物體運動部分, 當帶電粒子到達屏幕或撞到平行帶電板時停止
 用迴圈跑四種粒子
"""

for name in particles:
    #產生粒子
    particles = sphere(pos=vec(-1.5*L, 0, 0), v=vec(v0, 0, 0),color = colors[name], radius=size, m=m,make_trail=True)
    # 產生表示速度、加速度的箭頭
    arrow_v = arrow(pos=particles.pos, shaftwidth=0.3*size, color=color.cyan)
    arrow_a = arrow(pos=particles.pos, shaftwidth=0.3*size, color=color.magenta)
    while(0 < particles.pos.x < screen.pos.x - screen.length/2 - size or \
          (particles.pos.x < 0 and abs(particles.pos.y) < d/2 - p1.height - size)):
        rate(1000)
# 計算帶電粒子所受合力, 在平行帶電板間才有電場
#操作變因
        if(-L <= particles.pos.x <= 0): F = charges[name]*E_field
        else: F = vec(0, 0, 0)
# 更新帶電粒子加速度、速度、位置
        particles.a = F/m
        particles.v += particles.a*dt
        particles.pos += particles.v*dt
# 更新表示速度、加速度的箭頭

        arrow_v.pos = particles.pos
        arrow_a.pos = particles.pos
        arrow_v.axis = particles.v.norm()*0.05
        arrow_a.axis = particles.a.norm()*0.05
        #更新時間
        t += dt
