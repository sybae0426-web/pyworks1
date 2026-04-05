# 2026.04.04 
# 함수
# 구구단 출력(단을 입력받아서 출력)
'''
# dan = 3       # 소프트 하지 않음/ 물어보는 것이 더 좋은 코딩임
dan = int(input("단 입력:"))  #int함수: 숫자 넣기
for i in range(1, 10):
    print(f"{dan} X {i} ={dan*i}")
'''

# 함수 형태
def get_gugu(dan):
    for i in range(1, 10):
        print(f"{dan} X {i} ={dan*i}")

# 매개변수로 dan을 입력
value = int(input("단 입력:"))  # value = dan
get_gugu(value)

