
import turtle as t

def turn_right():
    t.setheading(0)    # 거북이 머리방향 0도 (오른쪽)
    t.forward(50)

def turn_up():
    t.setheading(90) 
    t.forward(50)
    
def turn_left():
    t.setheading(180) 
    t.forward(50)

def turn_down():
    t.setheading(270) 
    t.forward(50)

t.shape("turtle")

# 오른쪽 방향키 - Right,  turn_right() 함수 호출 
t.onkeypress(turn_right, "Right")     # 오른쪽 방향
t.onkeypress(turn_up, "Up")           # 위쪽 방향
t.onkeypress(turn_left, "Left")           # 왼쪽 방향
t.onkeypress(turn_down, "Down")           # 아래쪽 방향


t.listen()   # 키보드가 입력받을 준비(듣고 있다) : 하드웨어 작동을 위해 꼭 필요함

t.mainloop()