import pygame
import math as m
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
import os 
import sys
import random
from scipy.optimize import fsolve
from functools import partial
import numpy as np

def check_angle(angle):
    """
    檢查角度是否在範圍內
    """
    if angle < 0:
        angle += 360
    elif angle >= 360:
        angle -= 360
    return angle

def co_equation(vars, m1, m2, v_1_c, v_1_s, v_2_c, v_2_s, v_1, v_2):
    dv1, da1, dv2, da2 = vars
    dv1x, dv1y = dv1 * m.cos(da1), dv1 * m.sin(da1)
    dv2x, dv2y = dv2 * m.cos(da2), dv2 * m.sin(da2)

    return[
        m1 * dv1x + m2 * dv2x - (m1 * dv1x + m2 * dv2x),
        m1 * dv1y + m2 * dv2y - (m1 * dv1y + m2 * dv2y),
        0.5 * m1 * v_1**2 + 0.5 * m2 *v_2**2 - (0.5 * m1 * dv1**2 + 0.5 * m2 * dv2**2),
        (dv1 - dv2) - np.linalg.norm([v_1_c - v_2_c, v_1_s - v_2_s]) / 2
    ]

def ffex(initial_v, t):
    speed_text = font.render(f"Speed: {initial_v}", True, black)
    screen.blit(speed_text, (10, 10))  # 顯示於視窗左上角
    time_text = font.render(f"Time: {t/10:.2f}", True, black)  # 顯示時間
    screen.blit(time_text, (10, 40))  # 顯示於視窗左上角
    exo_text = font.render(f"up&down for speed", True, black)  #說明
    screen.blit(exo_text, (w-200, 10))  # 顯示於視窗左上角
    exfo_text = font.render(f"r for restart", True, black)  #說明
    screen.blit(exfo_text, (w-200, 40))  # 顯示於視窗左上角
    exfi_text = font.render(f"s for start", True, black) #說明
    screen.blit(exfi_text, (w-200, 70))  # 顯示於視窗左上角
    reminder_text = font.render("click space to leave", True, purple, white)  # 提示開始
    screen.blit(reminder_text, (w/2-50, h-50))  # 顯示於視窗左上角
def pmex(initial_v, t, angle):
    speed_text = font.render(f"Speed:{initial_v} (up&down)", True, black)
    screen.blit(speed_text, (10, 10))  # 顯示於視窗左上角
    time_text = font.render(f"Time: {t:.2f}", True, black)  # 顯示時間
    screen.blit(time_text, (10, 40))  # 顯示於視窗左上角
    angle_text = font.render(f"Angle: {angle} (left&right)", True, black)  # 顯示時間
    screen.blit(angle_text, (10, 70))  # 顯示於視窗左上角
    exo_text = font.render(f"up&down for speed", True, black)  #說明
    screen.blit(exo_text, (w-200, 10))  # 顯示於視窗左上角
    extw_text = font.render(f"left&right for angle", True, black)  #說明
    screen.blit(extw_text, (w-200, 40))  # 顯示於視窗左上角
    exth_text = font.render(f"5 for +5 degrees", True, black)  #說明
    screen.blit(exth_text, (w-200, 70))  # 顯示於視窗左上角
    exfo_text = font.render(f"r for restart", True, black)  #說明
    screen.blit(exfo_text, (w-200, 100))  # 顯示於視窗左上角
    exfi_text = font.render(f"s for start", True, black) #說明
    screen.blit(exfi_text, (w-200, 130))  # 顯示於視窗左上角
    reminder_text = font.render("click space to leave", True, purple, white)  # 提示開始
    screen.blit(reminder_text, (w/2-50, h-50))  # 顯示於視窗左上角
def ipex(initial_v, t, angle, tx3):
    """
    使用上下操控速度，
    使用左右操控斜面長度，
    按五代表角度加五，
    r是重新開始，
    s是開始。
    按6代表角度加一，
    按4代表角度減一。
    """
    speed_text = font.render(f"Speed:{initial_v} (up&down)", True, black)
    screen.blit(speed_text, (10, 10))  # 顯示於視窗左上角
    time_text = font.render(f"Time: {t:.2f}", True, black)  # 顯示時間
    screen.blit(time_text, (10, 40))  # 顯示於視窗左上角
    angle_text = font.render(f"Angle: {angle} (4&6)", True, black)  # 顯示時間
    screen.blit(angle_text, (10, 110))  # 顯示於視窗左上角
    tr_text = font.render(f"Trangle length: {tx3} (left&right)", True, black)  # 顯示時間
    screen.blit(tr_text, (10, 70))  # 顯示於視窗左上角
    exo_text = font.render(f"up&down for speed", True, black)  #說明
    screen.blit(exo_text, (w-200, 10))  # 顯示於視窗右上角
    extw_text = font.render(f"left&right for length", True, black)  #說明
    screen.blit(extw_text, (w-200, 40))  # 顯示於視窗右上角
    exth_text = font.render(f"4 for -1 degrees", True, black)  #說明
    screen.blit(exth_text, (w-200, 70))  # 顯示於視窗右上角
    exfo_text = font.render(f"6 for +1 degrees", True, black)  #說明
    screen.blit(exfo_text, (w-200, 100))  # 顯示於視窗右上角
    exfi_text = font.render(f"r for restart", True, black)  #說明
    screen.blit(exfi_text, (w-200, 130))  # 顯示於視窗右上角
    exsi_text = font.render(f"s for start", True, black) #說明
    screen.blit(exsi_text, (w-200, 160))  # 顯示於視窗右上角
    reminder_text = font.render("click space to leave", True, purple, white)  # 提示開始
    screen.blit(reminder_text, (w/2-50, h-50))  # 顯示於視窗下方
def coex(t, ball_amount, ball_di, now_t):
    """

    """
    i=0
    blue = (72, 61, 139)
    time_text = font.render(f"play time: {t} (left&right)", True, blue)  # 顯示時間
    screen.blit(time_text, (10, 10))  # 顯示於視窗左上角
    ball_text = font.render(f"ball amount: {ball_amount} (up&down)", True, blue)  # 顯示時間
    screen.blit(ball_text, (10, 40))  # 顯示於視窗左上角
    ball_text = font.render(f"Time: {now_t:.2f}", True, blue)  # 顯示時間
    screen.blit(ball_text, (10, 70))  # 顯示於視窗左上角
    exo_text = font.render(f"up&down for ball amount", True, blue)  #說明
    screen.blit(exo_text, (w-300, 10))  # 顯示於視窗右上角
    extw_text = font.render(f"left&right for Time", True, blue)  #說明
    screen.blit(extw_text, (w-300, 40))  # 顯示於視窗右上角
    for i in range(ball_amount):
        exth_text = font.render(f"ball{i} (x,y)={ball_di[i][0]:.2f}, {ball_di[i][1]:.2f}, weight={ball_di[i][2]:.1f}, angle={ball_di[i][3]:.2f}, speed={ball_di[i][4]:.2f}", True, blue)  #說明
        screen.blit(exth_text, (w-600, 70+30*i))  # 顯示於視窗右上角
    reminder_text = font.render("click space to leave", True, purple, white)  # 提示開始
    screen.blit(reminder_text, (w/2-50, h-50))  # 顯示於視窗下方

def coplay(t, ball_amount, ball_di, now_t):
    white= (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(white)
    for i in range(ball_amount):
        pygame.draw.circle(screen, black, (ball_di[i][0],ball_di[i][1]), r)
        pygame.draw.line(screen, black, (ball_di[i][0],ball_di[i][1]), (ball_di[i][0]+(r+ball_di[i][4])*m.cos(m.radians(ball_di[i][3])),ball_di[i][1]+(r+ball_di[i][4])*m.sin(m.radians(ball_di[i][3]))), 2)
    coex(t, ball_amount, ball_di, now_t)


def free_fall(w, h,white, black, initial_v, v, g, t, circle_x, circle_y, r): #自由落體
    """
    使用上下操控速度，
    r是重新開始，
    s是開始。
    """

    # 狀態檢查：如果正在運行模擬
    simulation_running = True  # 初始化模擬狀態為運行中

    while simulation_running:
        # 顯示速度和時間
        screen.fill(white)
        pygame.draw.circle(screen, black, (circle_x, circle_y), r)
        ffex(initial_v, t)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                circle_y = h//2
                if event.key == pygame.K_UP:
                    initial_v += 10
                    v = initial_v
                elif event.key == pygame.K_DOWN:
                    initial_v -= 10
                    v = initial_v
                elif event.key == pygame.K_r:
                    t = 0
                    initial_v = 0
                    v = initial_v
                    screen.fill(white)
                    pygame.draw.circle(screen, black, (circle_x, circle_y), r)
                elif event.key == pygame.K_s:

                    # 初始時間
                    t = 0
                    delta_t = 0.01  # 設定每次迴圈時間步長 (秒)

                    while circle_y <= (h-r):


                        circle_y += initial_v*t + (1/2*g*t*t)  # 更新位置

                        screen.fill(white)
                        # 顯示初速
                        ffex(initial_v, t)

                        pygame.draw.circle(screen, black, (circle_x, circle_y), r)

                        pygame.display.flip()  # 更新畫面
                        clock.tick(60)  # 控制幀數，每秒60幀

                        t += delta_t  # 增加時間
                elif event.key == pygame.K_SPACE:
                        simulation_running = False
                        break
            elif event.type == pygame.QUIT:
                return circle_y, initial_v, t, 0
    return circle_y, initial_v, t, 1

def Projectile_Motion(w, h,white, black, initial_v, v, g, t, circle_x, circle_y, r): #斜拋
    """
    使用上下操控速度，
    使用左右操控角度，
    按五代表角度加五，
    r是重新開始，
    s是開始。
    """
    simulation_running = True
    v = initial_v
    circle_x = r
    angle = 0

    while simulation_running:
        show_angle = check_angle(angle)
        run_a  = -angle
        run_a = check_angle(run_a)
        screen.fill(white)
        pygame.draw.circle(screen, black, (circle_x, circle_y), r)
        pygame.draw.line(screen, black, (circle_x, circle_y), (circle_x+(r+v)*m.cos(m.radians(run_a)),circle_y+(r+v)*m.sin(m.radians(run_a))), 2)
        pmex(initial_v, t, show_angle)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                circle_y = h//2
                if event.key == pygame.K_UP:
                    initial_v += 1
                    v = initial_v
                elif event.key == pygame.K_DOWN:
                    initial_v -= 1
                    v = initial_v
                elif event.key == pygame.K_RIGHT:
                    # if angle<90:
                    angle += 1
                elif event.key == pygame.K_LEFT:
                    # if angle>0 :
                    angle -= 1
                elif event.key == pygame.K_5:
                    if angle<90 :
                        angle +=5
                elif event.key == pygame.K_r:
                    t = 0
                    initial_v = 0
                    v = initial_v
                    circle_x = r
                    circle_y = h//2
                    angle = 0
                    screen.fill(white)
                    pygame.draw.circle(screen, black, (circle_x, circle_y), r)
                elif event.key == pygame.K_s:

                    if v<0: 
                        circle_x = w

                    # 初始時間
                    t = 0
                    delta_t = 0.01  # 設定每次迴圈時間步長 (秒)
                    show_angle = angle
                    run_a  = -angle
                    run_a = check_angle(run_a)
                    show_angle = check_angle(show_angle)
                    
                    while circle_y <= (h-r):
                        
                        v_x = v * m.cos(m.radians(run_a))
                        v_y = 1*v * m.sin(m.radians(run_a))
                        circle_y += v_y*t + (1/2*g*t*t)  # 更新位置
                        circle_x += v_x * t 

                        screen.fill(white)
                        # 顯示初速
                        pmex(initial_v, t, show_angle)
                        #計算速度
                        v_y += g*t

                        pygame.draw.circle(screen, black, (circle_x, circle_y), r)
                        
                        

                        pygame.display.flip()  # 更新畫面
                        clock.tick(60)  # 控制幀數，每秒60幀

                        t += delta_t  # 增加時間
                elif event.key == pygame.K_SPACE:
                        simulation_running = False
                        break
            elif event.type == pygame.QUIT:
                return circle_y, initial_v, t, 0
    return circle_y, initial_v, t, 1

def inclined_plane(w, h,white, black, initial_v, v, g, t, circle_x, circle_y, r): #三角形斜面
    """
    使用上下操控速度，
    使用左右操控斜面長度，
    按五代表角度加五，
    r是重新開始，
    s是開始。
    按6代表角度加一，
    按4代表角度減一。
    """
    path = os.path.dirname(os.path.abspath(__file__))
    excel_path = path+"/data.xlsx"
    # print(path)
    simulation_running = True
    yyy=250
    xxx=300
    circle_x = r
    angle = 0
    tx1 = 0
    ty1 = h
    tx2 = 0
    ty2 = h-yyy
    tx3 = xxx
    ty3 = h
    tan = float(yyy/tx3)
    trangle_points = [(tx1, ty1), (tx2, ty2), (tx3, ty3)]
    x_data = []
    y_data = []
    x_new =[]
    tan_data = []
    tan1_data = []
    test_new_data = []
    test_data = []
    xx = circle_x
    yy = circle_y

    while simulation_running:
        screen.fill(white)
        pygame.draw.polygon(screen, black, trangle_points, 0)
        pygame.draw.circle(screen, black, (circle_x, circle_y-50), r)
        ipex(initial_v, t, angle, tx3)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                circle_y = h//2
                if event.key == pygame.K_UP:
                    initial_v += 1
                    v = initial_v
                elif event.key == pygame.K_DOWN:
                    initial_v -= 1
                    v = initial_v
                elif event.key == pygame.K_RIGHT:
                    if tx3<w:
                        tx3 += 50
                        tan = float(yyy/tx3)
                        trangle_points = [(tx1, ty1), (tx2, ty2), (tx3, ty3)]
                        pygame.draw.polygon(screen, black, trangle_points, 0)
                        pygame.draw.circle(screen, black, (circle_x, circle_y), r)
                elif event.key == pygame.K_LEFT:
                    if tx3>0 :
                        tx3 -= 50
                        tan = float(yyy/tx3)
                        trangle_points = [(tx1, ty1), (tx2, ty2), (tx3, ty3)]
                        pygame.draw.polygon(screen, black, trangle_points, 0)
                        pygame.draw.circle(screen, black, (circle_x, circle_y), r)
                elif event.key == pygame.K_6:
                    if angle<90 :
                        angle +=1
                elif event.key == pygame.K_4:
                    if angle<90 and angle>0 :
                        angle -=1
                elif event.key == pygame.K_r:
                    yyy=250
                    xxx=300
                    circle_x = r
                    angle = 0
                    tx1 = 0
                    ty1 = h
                    tx2 = 0
                    ty2 = h-yyy
                    tx3 = xxx
                    ty3 = h
                    tan = float(yyy/tx3)
                    x_data = []
                    y_data = []
                    x_new =[]
                    tan_data = []
                    tan1_data = []
                    test_new_data = []
                    test_data = []
                    trangle_points = [(tx1, ty1), (tx2, ty2), (tx3, ty3)]
                    screen.fill(white)
                    pygame.draw.polygon(screen, black, trangle_points, 0)
                    pygame.draw.circle(screen, black, (circle_x, circle_y), r)
                    pygame.display.flip()  # 更新畫面
                elif event.key == pygame.K_s:
                    check = 0
                    circle_x = r
                    circle_y = h//2
                    screen.fill(white)
                    trangle_points = [(tx1, ty1), (tx2, ty2), (tx3, ty3)]
                    pygame.draw.polygon(screen, black, trangle_points, 0)
                    pygame.draw.circle(screen, black, (circle_x, circle_y), r)
                    pygame.display.flip()  # 更新畫面

                    if v<0: 
                        circle_x = w

                    # 初始時間
                    t = 0
                    delta_t = 0.1  # 設定每次迴圈時間步長 (秒)

                    while circle_y <= (h-r):
                        v_x = v * m.cos(m.radians(angle))
                        v_y = -1*v * m.sin(m.radians(angle))
                        v_y = v_y + g * t 
                        test = circle_x*tan
                        test_new = test +h-yyy-r
                        x_data.append(circle_x)
                        y_data.append(circle_y)
                        tan_data.append(tan)
                        tan1_data.append(circle_y/circle_x)
                        test_data.append(test)
                        test_new_data.append(test_new)
                        x_new.append(circle_y + v_y * delta_t)
                        #錯誤
                        # if circle_y > test_new:  
                        #     circle_y = test_new  # 確保不會超過斜面
                        # else:
                        #     circle_y += v_y * delta_t  # 正常運動
                        if circle_y > test_new:  
                            check+=1
                        if check >0:
                            if initial_v==0:
                                circle_x = v_y * m.cos(m.radians(angle))
                                circle_y = test_new + (1/2*g * delta_t*delta_t)   # 確保不會超過斜面
                            else:
                                circle_y = test_new + (1/2*g * delta_t*delta_t)   # 確保不會超過斜面
                        else:
                            circle_y += v_y * delta_t  # 正常運動


                        circle_x += v_x

                        screen.fill(white)
                        # 顯示初速
                        ipex(initial_v, t, angle, tx3)
                        #計算速度
                        v_y += g*t

                        pygame.draw.polygon(screen, black, trangle_points, 0)
                        pygame.draw.circle(screen, black, (circle_x, circle_y), r)

                        pygame.display.flip()  # 更新畫面
                        clock.tick(60)  # 控制幀數，每秒60幀

                        t += delta_t  # 增加時間
                    df.drop(df.index, inplace=True)  
                    df=pd.DataFrame({"x":x_data,"y":y_data,"x_new":x_new,"tan":tan_data,"tan1":tan1_data,"test":test_data,"test_new":test_new_data})
                    df.to_excel(excel_path, index=False)  # 儲存為Excel檔案

                    plt.plot(x_data, y_data, 'ro')
                    plt.title("Projectile Motion")
                    plt.xlabel("X Position (m)")
                    plt.ylabel("Y Position (m)")
                    plt.grid()
                    plt.savefig("imgs/display.png")
                elif event.key == pygame.K_SPACE:
                        simulation_running = False
                        break
            elif event.type == pygame.QUIT:
                return circle_y, initial_v, t, 0
    return circle_y, initial_v, t, 1

def collision(w, h,white, black, initial_v, v, g, t, r):
    """
    """
    path = os.path.dirname(os.path.abspath(__file__))
    excel_path = path+"/coll_data1.xlsx"

    
    v = initial_v
    t=10
    # 狀態檢查：如果正在運行模擬
    simulation_running = True
    ball_amount = 2
    run_t = t
    ball_di = []
    speed = [] #v_x, v_y
    ball_p = []
    ball_k = []
    now_t = 0.00

    #重量設定
    weight_max = 10
    weight_min = 1

    #速度範圍設定
    speed_max = 20
    speed_min = 5

    qq = 0

    for i in range(ball_amount):
        #ball_di (x,y,weight,angle,speed)
        x = random.randint(2*r,w-r-r)
        y = random.randint(2*r,h-r-r)
        weight = random.randint(weight_min,weight_max)
        angle = random.randint(0,360)
        speed = random.randint(speed_min,speed_max)
        ball_di.append([x,y,weight,angle,speed])
    print(ball_di)
    x_data = []
    y_data = []
    angle_data = []
    speed_data = []
    ball_name = []
    time_data = []
    v_x_data = []
    v_y_data = []
    

#要設提醒，設完後可以開始做運動的設定，可以將物品加上重量，依樣用random在旁邊顯示每一個數值
    while simulation_running:
        
        screen.fill(white)
        for i in range(ball_amount):
            pygame.draw.circle(screen, black, (ball_di[i][0],ball_di[i][1]), r)
            pygame.draw.line(screen, black, (ball_di[i][0],ball_di[i][1]), (ball_di[i][0]+(r+ball_di[i][4])*m.cos(m.radians(ball_di[i][3])),ball_di[i][1]+(r+ball_di[i][4])*m.sin(m.radians(ball_di[i][3]))), 2)
        coex(run_t, ball_amount, ball_di, now_t)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball_amount+=1
                    x = random.randint(2*r,w-r-r)
                    y = random.randint(2*r,h-r-r)
                    weight = random.randint(weight_min,weight_max)
                    angle = random.randint(0,360)
                    speed = random.randint(speed_min,speed_max)
                    ball_di.append([x,y,weight,angle,speed])
                    screen.fill(white)
                    for i in range(ball_amount):
                        pygame.draw.circle(screen, black, (ball_di[i][0],ball_di[i][1]), r)
                        pygame.draw.line(screen, black, (ball_di[i][0],ball_di[i][1]), (ball_di[i][0]+(r+ball_di[i][4])*m.cos(m.radians(ball_di[i][3])),ball_di[i][1]+(r+ball_di[i][4])*m.sin(m.radians(ball_di[i][3]))), 2)
                    coex(run_t, ball_amount, ball_di, now_t)
                    pygame.display.flip()
                elif event.key == pygame.K_DOWN:
                    if ball_amount<=2:
                        ball_amount = 2
                    else:
                        ball_amount-=1
                        ball_di.pop()
                        screen.fill(white)
                        for i in range(ball_amount):
                            pygame.draw.circle(screen, black, (ball_di[i][0],ball_di[i][1]), r)
                            pygame.draw.line(screen, black, (ball_di[i][0],ball_di[i][1]), (ball_di[i][0]+(r+ball_di[i][4])*m.cos(m.radians(ball_di[i][3])),ball_di[i][1]+(r+ball_di[i][4])*m.sin(m.radians(ball_di[i][3]))), 2)
                        coex(run_t, ball_amount, ball_di, now_t)
                        pygame.display.flip()
                elif event.key == pygame.K_LEFT:
                    t-=1
                    run_t = t
                    coplay(run_t, ball_amount, ball_di, now_t)
                elif event.key == pygame.K_RIGHT:
                    t+=1
                    run_t = t
                    coplay(run_t, ball_amount, ball_di, now_t)
                elif event.key == pygame.K_r:
                    screen.fill(white)
                    ball_di = []
                    for i in range(ball_amount):
                        x = random.randint(2*r,w-r-r)
                        y = random.randint(2*r,h-r-r)
                        weight = random.randint(weight_min,weight_max)
                        angle = random.randint(0,360)
                        speed = random.randint(speed_min,speed_max)
                        ball_di.append([x,y,weight,angle,speed])
                     
                    print(ball_di)
                    for i in range(ball_amount):
                        pygame.draw.circle(screen, black, (ball_di[i][0],ball_di[i][1]), r)
                        pygame.draw.line(screen, black, (ball_di[i][0],ball_di[i][1]), (ball_di[i][0]+(r+ball_di[i][4])*m.cos(m.radians(ball_di[i][3])),ball_di[i][1]+(r+ball_di[i][4])*m.sin(m.radians(ball_di[i][3]))), 2)
                    coex(run_t, ball_amount, ball_di, now_t)
                    pygame.display.flip()
                    v_x = 0
                    v_y = 0

                elif event.key == pygame.K_s:
                    
                        
                    run_t = t
                    times = run_t*60

                    while times > 0:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    qq += 1
                                    run_t = t
                                    coplay(run_t, ball_amount, ball_di, now_t)
                                    break
                                else:continue
                        if qq >0:
                            qq = 0
                            break
                        else:
                            for i in range(ball_amount):
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_p:
                                            qq += 1
                                            run_t = t
                                            coplay(run_t, ball_amount, ball_di, now_t)
                                            break
                                        else:continue
                                if qq >0:
                                    break

                                else:
                                
                                    for j in range(i+1, ball_amount):
                                        if i != j:
                                            #檢查是否碰撞
                                            if (ball_di[i][0] - ball_di[j][0])**2 + (ball_di[i][1] - ball_di[j][1])**2 <= (2 * r)**2:
                                                # p[cos,sin] 
                                                # k[cos,sin]
                                                v_1_c = ball_di[i][4]*m.cos(m.radians(ball_di[i][3]))
                                                v_1_s = ball_di[i][4]*m.sin(m.radians(ball_di[i][3]))
                                                v_2_c = ball_di[j][4]*m.cos(m.radians(ball_di[j][3]))
                                                v_2_s = ball_di[j][4]*m.sin(m.radians(ball_di[j][3]))
                                                v_1 = ball_di[i][4]
                                                v_2 = ball_di[j][4]
                                                m1 = ball_di[i][2]
                                                m2 = ball_di[j][2]

                                                eqs = partial(co_equation, m1=m1, m2=m2, v_1_c=v_1_c, v_1_s=v_1_s, v_2_c=v_2_c, v_2_s=v_2_s, v_1=v_1, v_2=v_2)
                                                ball_di[i][4], ball_di[i][3], ball_di[j][4], ball_di[j][3] = fsolve(eqs, [0, m.radians(60),0, m.radians(60)])
                                                ball_di[i][4] = abs(ball_di[i][4])
                                                ball_di[j][4] = abs(ball_di[j][4])
                                            
                                    v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                    v_y = ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                    ball_di[i][0] += v_x
                                    ball_di[i][1] += v_y
                                    ball_di[i][3] = check_angle(ball_di[i][3])
                                    # v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                    # v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                    if ball_di[i][1] <= (h-r) and ball_di[i][1] >= r and ball_di[i][0] <= (w-r) and ball_di[i][0] >= r:
                                        # ball_di (x,y,weight,angle,speed)
                                        # print(ball_di[i][0])
                                        # print(ball_di[i][4])
                                        # print(f"v_x={v_x}, v_y={v_y}")
                                        pass
                                        # ball_di[i][0] += v_x
                                        # ball_di[i][1] += v_y   # 更新位置

                                        # ball_di[i][0] += ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                        # ball_di[i][1] += ball_di[i][4] * m.sin(m.radians(ball_di[i][3])) + g*t
                                        # pygame.draw.circle(screen, black, (ball_di[i][0],ball_di[i][1]), r)
                                        # pygame.display.flip()
                                        # clock.tick(60)  # 控制幀數，每秒60幀

                                    #底端確認 bottom check
                                    elif ball_di[i][1] >= (h-r): #check 0~90 90~180 180~270 270~360
                                        ball_di[i][0] -= v_x
                                        ball_di[i][1] -= v_y
                                        if ball_di[i][3]<90 and ball_di[i][3]>0:
                                            ball_di[i][3] = 360 - ball_di[i][3]
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]>90 and ball_di[i][3]<180:
                                            ball_di[i][3] = 360 - ball_di[i][3] 
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]>180 and ball_di[i][3]<270:
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]>270 and ball_di[i][3]<360:
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]==270 or ball_di[i][3]==90:
                                            ball_di[i][3] = 90
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x

                                    #上端確認 top check
                                    elif ball_di[i][1] <= r:
                                        ball_di[i][0] -= v_x
                                        ball_di[i][1] -= v_y
                                        if ball_di[i][3]<270 and ball_di[i][3]>180:
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                            ball_di[i][3] = 360 - ball_di[i][3]
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                        elif ball_di[i][3]>270 and ball_di[i][3]<360:
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                            ball_di[i][3] =  360 - ball_di[i][3] 
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                        elif ball_di[i][3]>0 and ball_di[i][3]<90:
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]>90 and ball_di[i][3]<180:
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]==270 or ball_di[i][3]==90:
                                            ball_di[i][3] = 270
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x

                                    #右端確認 right check
                                    elif ball_di[i][0] >= (w-r):
                                        ball_di[i][0] -= v_x
                                        ball_di[i][1] -= v_y
                                        if ball_di[i][3]<90 and ball_di[i][3]>0:
                                            ball_di[i][3] = 540 - ball_di[i][3]
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]>270 and ball_di[i][3]<360:
                                            # ball_di[i][3] =  ball_di[i][3] -270
                                            ball_di[i][3] =  540 - ball_di[i][3] 
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]>180 and ball_di[i][3]<270:
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]>90 and ball_di[i][3]<180:
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]==0 or ball_di[i][3]==180:
                                            ball_di[i][3] = 180
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x

                                    #左端確認 left check
                                    elif ball_di[i][0] <= r:
                                        ball_di[i][0] -= v_x
                                        ball_di[i][1] -= v_y
                                        if ball_di[i][3]<270 and ball_di[i][3]>180:
                                            ball_di[i][3] = 540 - ball_di[i][3]
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]>90 and ball_di[i][3]<180:
                                            # ball_di[i][3] =  ball_di[i][3] -270
                                            ball_di[i][3] =  540 - ball_di[i][3] 
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]>270 and ball_di[i][3]<360:
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                        elif ball_di[i][3]>0 and ball_di[i][3]<90:
                                            ball_di[i][3] = check_angle(ball_di[i][3])
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] -= v_x
                                        elif ball_di[i][3]==0 or ball_di[i][3]==180:
                                            ball_di[i][3] = 0
                                            v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                            v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                            ball_di[i][1] += v_y
                                            ball_di[i][0] += v_x
                                    
                                    #四角確認 corner check  
                                    #左上角
                                    elif ball_di[i][0] <= r and ball_di[i][1] <= r :
                                        ball_di[i][0] -= v_x
                                        ball_di[i][1] -= v_y
                                        ball_di[i][3] +=180
                                        ball_di[i][3] = check_angle(ball_di[i][3])
                                        v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                        v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                        ball_di[i][1] += v_y
                                        ball_di[i][0] += v_x
                                    #右上角
                                    elif ball_di[i][0] >= (w-r) and ball_di[i][1] <= r :
                                        ball_di[i][0] -= v_x
                                        ball_di[i][1] -= v_y
                                        ball_di[i][3] +=180
                                        ball_di[i][3] = check_angle(ball_di[i][3])
                                        v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                        v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                        ball_di[i][1] += v_y
                                        ball_di[i][0] += v_x
                                    #右下角
                                    elif ball_di[i][0] >= (w-r) and ball_di[i][1] >= (h-r) :
                                        ball_di[i][0] -= v_x
                                        ball_di[i][1] -= v_y
                                        ball_di[i][3] +=180
                                        ball_di[i][3] = check_angle(ball_di[i][3])
                                        v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                        v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                        ball_di[i][1] += v_y
                                        ball_di[i][0] += v_x
                                    #左下角
                                    elif ball_di[i][0] <= r and ball_di[i][1] >= (h-r) :
                                        ball_di[i][0] -= v_x
                                        ball_di[i][1] -= v_y
                                        ball_di[i][3] +=180
                                        ball_di[i][3] = check_angle(ball_di[i][3])
                                        v_x = ball_di[i][4] * m.cos(m.radians(ball_di[i][3]))
                                        v_y = 1*ball_di[i][4] * m.sin(m.radians(ball_di[i][3]))
                                        ball_di[i][1] += v_y
                                        ball_di[i][0] += v_x


                                            
                                        
                                    # elif ball_di[i][1] >= (h-r):
                                    #     print(2)
                                    #     v_y = -1*v_y

                                    #     ball_di[i][1] = h-r
                                    #     ball_di[i][4] = -1*ball_di[i][4]
                                    #     ball_di[i][0] += v_x
                                    #     ball_di[i][1] += v_y
                                    #     print(f"v_x={v_x}, v_y={v_y}")
                                    # elif ball_di[i][1] <= r:
                                    #     print(3)
                                    #     ball_di[i][1] = r
                                    #     ball_di[i][4] = -1*ball_di[i][4]
                                    #     ball_di[i][0] += v_x
                                    #     ball_di[i][1] += v_y
                                    #     print(f"v_x={v_x}, v_y={v_y}")
                                    # elif ball_di[i][0] >= (w-r):
                                    #     print(4)
                                    #     ball_di[i][0] = w-r
                                    #     ball_di[i][4] = -1*ball_di[i][4]
                                    #     ball_di[i][0] += v_x
                                    #     ball_di[i][1] += v_y
                                    #     print(f"v_x={v_x}, v_y={v_y}")
                                    # elif ball_di[i][0] <= r:
                                    #     print(5)
                                    #     ball_di[i][0] = r
                                    #     ball_di[i][4] = -1*ball_di[i][4]
                                    #     ball_di[i][0] += v_x
                                    #     ball_di[i][1] += v_y
                                    #     print(f"v_x={v_x}, v_y={v_y}")
                                    times-=1
                                    run_t-=1

                                    now_t = times/60
                                    coplay(t, ball_amount, ball_di, now_t)
                                    pygame.display.flip()
                                    clock.tick(60)  # 控制幀數，每秒60幀
                                    
                                    x_data.append(ball_di[i][0])
                                    y_data.append(ball_di[i][1])
                                    angle_data.append(ball_di[i][3])
                                    speed_data.append(ball_di[i][4])
                                    ball_name.append(i)
                                    time_data.append(run_t)
                                    v_x_data.append(v_x)
                                    v_y_data.append(v_y)
                                

                    
                    df=pd.DataFrame({"name":ball_name,"time":time_data,"x":x_data,"y":y_data,"angle":angle_data,"v_x":v_x_data, "v_y":v_y_data,"speed":speed_data})
                    
                    df.to_excel(excel_path, index=False)  # 儲存為Excel檔案
                    run_t = t
                
                elif event.key == pygame.K_SPACE:
                        simulation_running = False
                        break


            elif event.type == pygame.QUIT:
                return initial_v, t, 0
    return initial_v, t, 1


if __name__ == "__main__":
    pygame.init()

    # 創建字型
    font = pygame.font.SysFont("Arial", 24)

    #畫面設定
    w, h = 1200,600
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("simulation")

    #色彩設定
    white = (255, 255, 255)
    black = (0, 0, 0)
    purple = (160, 32, 240, 255)

    #物體運動數據
    initial_v = 0
    v = initial_v
    g = 9.8
    t=0

    #物體設定
    circle_x = w//2
    circle_y = h//2
    r = 10

    #功能選項
    fun = ["free fall","Projectile_Motion", "inclined_plane","collision"]
    num = 0

    # 用於控制幀數
    clock = pygame.time.Clock()

    running = True

    while running:

        #更新項目
        screen.fill(white)

        if num+1 < len(fun) :
            opt1_text = font.render(fun[num-1], True, black, white)  # 反白
            screen.blit(opt1_text, (w//7*1, h//2))  # 顯示於視窗左上角
            font_w, font_h = opt1_text.get_size()
            n_w = w//7*1+font_w+w//7*1
            opt2_text = font.render(fun[num], True, (255, 255, 255), (0,0,0))  # 黑色文字
            screen.blit(opt2_text, (n_w, h//2))  # 顯示於視窗左上角
            font_w, font_h = opt2_text.get_size()
            n_w += font_w+w//7*1
            opt3_text = font.render(fun[num+1], True, black, white)  # 反白ˋ
            screen.blit(opt3_text, (n_w, h//2))  # 顯示於視窗左上角
            reminder_text = font.render("click space to start", True, purple, white)  # 提示開始
            screen.blit(reminder_text, (w/2-50, h-50))  # 顯示於視窗左上角
            pygame.display.flip()
        elif  num-1>-1 :
            opt1_text = font.render(fun[num-1], True, black, white)  # 反白
            screen.blit(opt1_text, (w//7*1, h//2))  # 顯示於視窗左上角
            opt2_text = font.render(fun[num], True, (255, 255, 255), (0,0,0))  # 黑色文字
            screen.blit(opt2_text, (w//7*3, h//2))  # 顯示於視窗左上角
            reminder_text = font.render("click space to start", True, purple, white)  # 提示開始
            screen.blit(reminder_text, (w/2-50, h-50))  # 顯示於視窗左上角
            pygame.display.flip()
        else: 
            opt2_text = font.render(fun[num], True, (255, 255, 255), (0,0,0))  # 黑色文字
            screen.blit(opt2_text, (w//7*3, h//2))  # 顯示於視窗左上角
            opt3_text = font.render(fun[num+1], True, black, white)  # 反白
            screen.blit(opt3_text, (w//7*5, h//2))  # 顯示於視窗左上角
            reminder_text = font.render("click space to start", True, purple, white)  # 提示開始
            screen.blit(reminder_text, (w/2-50, h-50))  # 顯示於視窗左上角
            pygame.display.flip()
                # pygame.display.flip()



        # pygame.draw.circle(screen, black, (circle_x, circle_y), r)
        # # 顯示初速
        # speed_text = font.render(f"Speed: {initial_v}", True, (0, 0, 0))  # 黑色文字
        # screen.blit(speed_text, (10, 10))  # 顯示於視窗左上角
        # time_text = font.render(f"Time: {t:.2f}", True, (0, 0, 0))  # 黑色文字
        # screen.blit(time_text, (10, 40))  # 顯示於視窗左上角
        #畫面更新
        pygame.display.flip()

        for event in pygame.event.get():
            #如果畫面關掉就結束
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if num+1<len(fun):
                        num+=1
                elif event.key == pygame.K_LEFT:
                    if num-1>-len(fun):
                        num-=1
                elif event.key == pygame.K_SPACE:
                    if num == 0:
                        circle_y, initial_v, t, running = free_fall(w, h,white, black, 0, v, g, 0, circle_x, circle_y, r)
                    elif  num == 1:
                        circle_y, initial_v, t, running = Projectile_Motion(w, h,white, black, 0, v, g, 0, circle_x, circle_y, r)
                    elif  num == 2:
                        circle_y, initial_v, t, running = inclined_plane(w, h,white, black, 0, v, g, 0, circle_x, circle_y, r)
                    elif  num == 3:
                        initial_v, t, running = collision(w, h,white, black, 0, v, g, 0, r)


                
                
                    


                # circle_y, initial_v, t = free_fall(w, h,white, black, initial_v, v, g, t, circle_x, circle_y, r)
                

    pygame.quit()