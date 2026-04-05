# 민생회복 지원금 신청 프로그램
birth_year = input("출생연도를 입력하세요.: ")

# 출생연도 끝자리 
last_digit = birth_year[-1]
'''
print(last_digit)
''' 
# If문: 기간 조건 
# 출생연도는 1900년 부터 2006년 사이 

if int(birth_year) < 1900 or int(birth_year) > 2006 :
    print("출생연도는 1900년부터 2006년 사이어야 한다.")
else: 
    if last_digit == "1" or last_digit =="6":
        print("신청일은 월요일입니다.")
    elif last_digit == "2" or last_digit =="7":
        print("신청일은 화요일입니다.")
    elif last_digit == "3" or last_digit =="8":
        print("신청일은 수요일입니다.")
    elif last_digit == "4" or last_digit =="9":
        print("신청일은 목요일입니다.")
    elif last_digit == "5" or last_digit =="0":
        print("신청일은 금요일입니다.")
    else:
        print("신청 요일이 없습니다.")

