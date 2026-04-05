
# 기본 매개 변수

# 방벙 1)
def greet(name):
    print(f"{name}님, 안녕하세요!")

greet("영우")   # 영우님, 안녕하세요!

#  방법 2) 기본 매개 변수
def greet(name, message="안녕하세요"):
    print(f"{name}님, {message}!")

# 인자(매개변수)를 모두 전달한 경우
greet("민주", "반갑습니다")  # 민주님, 반갑습니다!


# 기본 매개 변수를 생략한 경우
greet("영우")   # 영우님, 안녕하세요!


#  버스 요금 함수 (1)
def take_bus(fare):
    print(f"버스 요금은 {fare}원입니다.")

take_bus(1200)    # 버스 요금은 1200원입니다.

#  버스 요금 함수 (2)
def take_bus(fare=1500):
    print(f"버스 요금은 {fare}원입니다.")

take_bus(1200)    # 버스 요금은 1200원입니다.
take_bus()         # 버스 요금은 1500원입니다.



 
 