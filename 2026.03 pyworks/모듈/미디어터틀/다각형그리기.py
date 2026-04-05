
import turtle as t      # 별칭을 t로 사용

def polygon(n):
    t.color("red")
    t.pensize(5)
    for x in range(n):
        t.forward(100)
        t.left(360/n) 

def polygon2(n, d):    # 매개변수 2개
    t.color("blue")
    t.pensize(10)
    for x in range(n):
        t.forward(d)
        t.left(360/n) 



t.shape("turtle")

# 함수 호출
polygon(5)
t.penup()   # 펜 올리기: 선을 그리지 않음

# t.goto(0, 0) 현재 위치
t.goto(200, 200) # x=200, y=200

t.pendown()  # 펜 내리기
polygon2(6, 80)

t.mainloop()
