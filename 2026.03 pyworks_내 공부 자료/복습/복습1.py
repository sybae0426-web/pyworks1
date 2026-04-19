# 2026.04.04
# 변수 이름 - season
# 시즌에서 봄을 기억시킨 후, 출력
season = "봄"
print(season)
print("계절은 ", season, "입니다.") # 쉼표로 하면 글자 사이에 띄어쓰기가 발생
print(f"계절은 {season}입니다.")    # 원하는 문장으로 변경 가능
print(type(season))                # 시즌의 자료형은? <class 'str'> 문자형이다.


n = 10
print(f"숫자는 {n}입니다.")

# n 변수에 20을 더하세요
n +=20     # n = n + 20
print(n)
print(f"n = {n}")
print(type(n))

# 원의 둘레를 계산(2 x 원주율 x 반지름)
pi = 3.14
radius = 6         #반지름
print(type(pi))    #<class 'float'>
print(type(radius)) #<class 'int'>
# 계산 공식
result = 2 * pi * radius
print(f"원의 둘레는 {result}입니다.")

# 정밀한 계산 - 수학 모듈(math)
import math
PI = math.pi
radius = 10
print(f"원주율은 {PI}입니다.")

# 정밀한 원의 둘레
result2 = 2 * PI * radius
print(f"새로운 원의 둘레는 {result2}입니다.")
