# if문
# 조건 - 나이가 20세 미만이면 "미성년자"입니다. 출력
'''
age = 17
if age <20:
    print("미성년자입니다.")
print(f"나이는 {age}세 입니다.")
'''

# 조건 - 나이가 20세 미만이면 "미성년자입니다" 출력하고,
#        아니면 "성인입니다." 출력
# 콜론(:)은 블럭의 시작을 의미한다. 자동으로 4칸 들여쓰기(인덴트)
'''

age = 20
if age <20:
    print("미성년자입니다.")
else:
    print("성인입니다.")
print(f"나이는 {age}세 입니다.")

'''
# 다중 조건문(if ~ elif ~ else문)
# 신호등(빨강색-정지, 노랑-주의, 초록-진행)
'''
color = input("신호등 색상 입력 (빨강/노랑/초록):")

if color == '빨강':
    print("정지")
elif color =='노랑':
    print("주의")
elif color =='초록':
    print("진행")
else:
    print("잘못된 입력입니다")
'''

# 논리연산자 사용 - and
# 조건 - 컴활 필기점수는 60점 이상, 실기점수는 70점 이상 = 합격

'''
필기 = int(input("필기점수 입력:"))  # 일반 점수
실기 = int(input("실기점수 입력:"))

if 필기>=60 and 실기>=70:
    print("합격입니다.")
else:
    print("불합격입니다.")
'''

'''
필기 = float(input("필기점수 입력:")) # 소수점
실기 = float(input("실기점수 입력:"))

if 필기>=60 and 실기>=70:
    print("합격입니다.")
else:
    print("불합격입니다.")
'''
"""
필기 = int(input("필기점수 입력(0~100):"))  # 일반 점수
실기 = int(input("실기점수 입력(0~100):"))

if 필기>=60 and 실기>=70:
    print("합격입니다.")
else:
    print("불합격입니다.")



"""

# 실습문제 1- 조건문 <학점 계산 프로그램>

'''
score= 90 # 점수
grade= '' # 학점

# print=int(input("점수를 입력하세요:", score)) 

if score>=90  and score <=100:
    print("A")

elif score>=80 and score <90:
    print("B")
elif score>=70 and score <80:
    print("C")
elif score>=60 and score <70:
    print("D")
else:
    print("F")
'''
'''
score=int(input("점수를 입력하세요:"))
grade=''

if score>=90  and score <=100:
    grade="A"

elif score>=80 and score <90:
    grade="B"
elif score>=70 and score <80:
    grade="C"
elif score>=60 and score <70:
    grade="D"
else:
    grade="F"

print(f"학점은 {grade} 입니다")  #f 포맷 출력 방식

'''


score=int(input("점수를 입력하세요:"))
grade=''

if score>=90  and score <=100:
    grade="A"

elif score >=89:
    grade="B"
elif score >=79:
    grade="C"
elif score >=69:
    grade="D"
else:
    grade="F"

print(f"학점은 {grade} 입니다")















