'''
# 내장 함수
# 반올림 - round(숫자, 자리수)

print(round(2.74))  # 3 (정수)
print(round(2.44))  # 2 (정수)


x = 706.351
print(round(x, 1))  # 706.4  소수 첫째자리 표시
print(round(x, 0))  # 706.0  
print(round(x))     # 706
print(round(x, -1)) # 710.0


# 절대값
print(abs(-8))      # 8
print(abs(8))       # 8


# if 조건문으로 입력된 수가 음수이면 양수 반환, 양수이면 양수 반환
def my_abs(x):
    if x < 0:
        return -x   # -(-8)
    else :          # x >=0    
        return x

print(my_abs(-8))    # 8
print(my_abs(8))     # 8
'''

# 합계
a = [1, 2, 3, 4]
print(sum(a))     # 10

'''
# 배열의 합계
total = 0
for i in a:
    total += i
print(total)        # 10


# 배열의 합계를 함수로 작성
def sum_n(a):
    total = 0
    for i in a:
        total += i
    return total

print("sum_n의 합계:", sum_n(a))        # 10


# 최대값
nums = [7, 53, 68, 44, 25]
print("최대값1:", max(nums))   # 68

# 사용자 정의
max_v = nums[0]    #첫째 요소를 최대값을 설정  
print(max_v)


# for 요소 in 리스트
for num in nums:
    if max_v < num:  # max_v가 요소값보다 작으면
        max_v = num  # num이 최대값이 된다. 

print("최대값2:", max_v) # 68
'''

# # 최소값
# nums = [44, 53, 68, 7, 25]
# print("최소값1:", min(nums))

# # 최소값 함수 정의
# min_v = nums[0]  # 최소값을 첫째요소로 설정

# for num in nums:
#     if min_v > num:  
#         min_v = num  

# print("최소값2:", min_v) 



# 사용자 정의 (최대값)

nums = [44, 53, 68, 7, 25]

def max_n(nums):
    max_v = nums[0]    
    
    for num in nums:
        if max_v < num:  
           max_v = num  
    return max_v

print("최대값2:", max_v) 