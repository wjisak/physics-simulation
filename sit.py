import pygame
import math as m
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
import os 
import sys
import random

def ffex(initial_v, t):
    speed_text = font.render(f"Speed: {initial_v}", True, black)
    screen.blit(speed_text, (10, 10))  # 顯示於視窗左上角
    time_text = font.render(f"Time: {t:.2f}", True, black)  # 顯示時間
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
def coex(initial_v, t, angle, tx3):
    """

    """
    speed_text = font.render(f"Speed:{initial_v} (up&down)", True, black)
    screen.blit(speed_text, (10, 10))  # 顯示於視窗左上角
    time_text = font.render(f"Time: {t:.2f}", True, black)  # 顯示時間
    screen.blit(time_text, (10, 40))  # 顯示於視窗左上角
    angle_text = font.render(f"ball amount: {angle} (4&6)", True, black)  # 顯示時間
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
                    delta_t = 0.1  # 設定每次迴圈時間步長 (秒)

                    while circle_y <= (h-r):
                        v = initial_v + g * t 
                        circle_y += v * delta_t  # 更新位置

                        screen.fill(white)
                        # 顯示初速
                        ffex(initial_v, t)
                        #計算速度
                        v += g*t

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
    circle_x = r
    angle = 0

    while simulation_running:
        screen.fill(white)
        pygame.draw.circle(screen, black, (circle_x, circle_y), r)
        pmex(initial_v, t, angle)
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
                    if angle<90:
                        angle += 1
                elif event.key == pygame.K_LEFT:
                    if angle>0 :
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
                    delta_t = 0.1  # 設定每次迴圈時間步長 (秒)

                    while circle_y <= (h-r):
                        v_x = v * m.cos(m.radians(angle))
                        v_y = -1*v * m.sin(m.radians(angle))
                        v_y = v_y + g * t 
                        circle_y += v_y * delta_t  # 更新位置
                        circle_x += v_x

                        screen.fill(white)
                        # 顯示初速
                        pmex(initial_v, t, angle)
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
                    t = 0
                    initial_v = 0
                    v = initial_v
                    circle_x = r
                    circle_y = h//2
                    angle = 0
                    screen.fill(white)
                    pygame.draw.polygon(screen, black, trangle_points, 0)
                    pygame.draw.circle(screen, black, (circle_x, circle_y), r)
                elif event.key == pygame.K_s:
                    check = 0
                    circle_x = r
                    circle_y = h//2
                    pygame.draw.circle(screen, black, (circle_x, circle_y), r)

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
                            circle_y = test_new  # 確保不會超過斜面
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

    simulation_running = True
    ball_amount = 2
    t = 10
    ball_di = []
    for i in range(ball_amount):
        x = random.randint(0,w)
        y = random.randint(0,h)
        ball_di.append((x,y))
    print(ball_di)

#要設提醒，設完後可以開始做運動的設定，可以將物品加上重量，依樣用random在旁邊顯示每一個數值
    while simulation_running:
        
        screen.fill(white)
        for i in range(ball_amount):
            pygame.draw.circle(screen, black, ball_di[i], r)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.key == pygame.K_UP:
                ball_amount+=1
            elif event.key == pygame.K_DOWN:
                ball_amount-=1
            elif event.key == pygame.K_LEFT:
                if v>0:
                    v-=1
            elif event.key == pygame.K_RIGHT:
                v+=1
            elif event.key == pygame.K_1:
                t-=1
            elif event.key == pygame.K_2:
                t+=1

            elif event.type == pygame.QUIT:
                    return initial_v, t, 0
        


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