import turtle
turtle.shape("turtle")  # 거북이 모양 등장

'''
4번 같은 문장을 쓸때: 반복문 for i in range
turtle.forward(100)   # 100필셀만큼 직진
turtle.right(90)      # 오른쪽 90도 방향
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

# 색상 변경
turtle.color('blue')

# 반복문 사용 - 사각형
for i in range(4):
    turtle.forward(100)
    turtle.right(90)


turtle.color('red')
# 삼각형
for i in range(4):
    turtle.forward(100)
    turtle.left(120)
'''

n = 4     # 변의 개수
d = 150   # 거리(distance)

turtle.color('blue')
turtle.pensize(2)
# 사각형
for i in range(n):
    turtle.forward(d)
    turtle.right(360/n)


turtle.color('red')
turtle.pensize(3)
n = 3     # 변의 개수
d = 75    # 거리(distance)
# 삼각형
for i in range(n):
    turtle.forward(d)
    turtle.right(360/n)

# 원
turtle.color('black')
turtle.circle(50)  # 반지름 - 50 픽셀



turtle.mainloop() # 윈도우창 계속 유지
