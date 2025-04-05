import random


ball_amount = 2
t = 10
ball_di = []
for i in range(ball_amount):
    x = random.randint(0,50)
    y = random.randint(0,200)
    ball_di.append((x,y))
print(ball_di)

