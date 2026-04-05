# 2026.04.04 
# 리스트(객체) - 여러 개의 값을 저장

seasons = ["봄", "여름", "가을"]
print(seasons)
print(type(seasons))  # <class 'list'>

# 겨울을 리스트에 추가 - append()
seasons.append("겨울")
print(seasons)

# 변경(수정) - 여름을 summer로 변경
seasons[1]="summer"
print(seasons)

# 삭제 - remove() '가을'
seasons.remove("가을")
print(seasons)

# 반복문 - for문
# "사랑해" 3번 반복 출력
for i in range(1, 4):
    print(f"{i}. 사랑해요~♥")

print("====================")
print("")

# 1~10 출력
for i in range(1, 11):
    print(i, end=' ')    # 옆으로 출력 end='한칸띄고'
print("")
print("====================")
print("")

# 1~10 중 홀수 출력  - If문
for i in range(1, 11):
    if i % 2 != 0:
        print(i, end=' ')    

print("")
print("====================")
print("")

# 1~10 총 합계 계산 total 
total = 0  #합계를 저장할 변수 설정
for i in range(1, 11):
    total += i
    print(f"i={i}, total={total}")
print("합계:", total)    

print("")
print("====================")
print("")


# 국어 과목의 점수를 저장하는 리스트
# 국어 평균 = 총점 / 개수

scores = [80, 70, 95, 86]
count  = len(scores)       # 개수
total  = sum(scores)       # 총점
average = total / count    # 평균
max_val = max(scores)      # 최고 점수 
min_val = min(scores)      # 최저 점수

print("개수:", count)
print("총점:", total)
print("평균:", average)
print("최고점수:", max_val) 
print("최저점수:", min_val)

# 소수 첫째자리까지 출력 - 반올림- round()
print("평균:", round(average, 1))

'''
# 방법 1) 소수점 이하 버림
import math
money = 15000.3
print("금액:", math.floor(money))
'''
# 방법 2) 소수점 이하 버림 - floor()는 math 안에 있음
import math
money = 15000.3
money = math.floor(money)
print("금액:", money)


# 요소 전체 출력
for i in scores: 
    print(i, end=" ")
print()

print("")
print("====================")
print("")

# 요소 합계 출력
sum_val = 0
for i in scores: 
    sum_val += i
    print(i, end=" ")
print("총점:", sum_val)

print("")
print("====================")
print("")
