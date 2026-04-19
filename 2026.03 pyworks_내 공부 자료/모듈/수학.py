'''
# 수학 관련 모듈
import math

# 올림
print(math.ceil(2.14))    #3

# 내림(버림)
print(math.floor(2.14))   #2

# 반올림 - round()는 내장 함수
print(round(2.54))        #3

# 제곱근
print(math.sqrt(16))      #4.0
print(math.sqrt(2))       #1.4142135623730951


# 원주율
print(math.pi)            #3.141592653589793

# 원의 면적 = 반지름 * 반지름 * 3.14
radius = 5
area =  radius * radius * math.pi
print(f"원의 면적: {area}")   # 원의 면적: 78.53981633974483


# 소수 2째 자리 
radius = 5
area =  radius * radius * math.pi
print(f"원의 면적: {area:.2f}")   # 원의 면적: 78.53 

print("======================================")
'''
# 달력
import calendar as cal   #이름 함축: 편집->> 찾기

# 2026년 전체 달력
# cal.prcal(2026)

print("======================================")

# 2026년 4월 달력
cal.prmonth(2026,4)

print("======================================")

# 요일, 이름
print(cal.day_name[0])     # Monday
print(cal.day_name[6])     # Sunday


print(cal.day_name[:])     # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print("======================================")
print(list(cal.day_name))


print("======================================")

# 특정 날짜의 요일 확인
day_of_week = cal.weekday(2026, 3, 28)
print(day_of_week)                       # 5
print(cal.day_name[day_of_week])         # Saturday


