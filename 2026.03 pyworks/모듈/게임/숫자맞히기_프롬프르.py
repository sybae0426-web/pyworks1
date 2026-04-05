'''
파이썬으로 숫자 맞히기 게임을 만들거야
1 ~ 100 사이의 무작위 숫자를 생성하고, 
내가 숫자를 입력하면 무작위 숫자랑 비교해서
숫자가 큰지, 작은지 알려줘. 
숫자를 맞히면 몇 회 만에 맞췄는지 알려주고 게임을 종류해줘.
'''

import random

# 1 ~ 100 사이 랜덤 숫자 생성
answer = random.randint(1, 100)
count = 0

print("숫자 맞히기 게임 시작! (1 ~ 100)")

while True:
    try:
        guess = int(input("숫자를 입력하세요: "))
        count += 1

        if guess < answer:
            print("▲ 더 큰 숫자입니다!")
        elif guess > answer:
            print("▼ 더 작은 숫자입니다!")
        else:
            print(f"정답입니다! {count}번 만에 맞추셨습니다.")
            break

    except ValueError:
        print("숫자만 입력해주세요!")

print("게임 종료!")