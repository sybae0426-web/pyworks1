#  예시
x = 4
y = 5
total = x + y
print(total)   # 9


#  함수 정의 
def add(x, y):
    sum = x + y    # sum -> 지역 변수
    return sum     # 호출한 곳으로 보내줌(반환)


# 함수 호출
#  방법 1)
# print(add(4, 5))   # 9

# 방법 2)
result = add(4, 5)
print(result)


arr = [3, 6, 9]
# 리스트의 합계 : sum(arr) -> 내장 함수
print(sum(arr))     # 18

# 직접 리스트 합계
# sum_n = arr[0] + arr[1] + arr[2]  : 이거는 너무 길다. 그래서 for문으로 작성

sum_n = 0     # 합계를 저장할 변수
for i in arr:
    sum_n += i  # sum_n = sum_n + i
    print("i=", i, "sum_n=", sum_n)  # i=3 sum_n=3, i=6 sum_n=9, i=9 sum_n=18
print(sum_n)        # 18



# 함수 만들기 => 사고력 높이기
def sum_n(arr):
    total = 0
    for n in arr:
        total += i
    return total


v = [1, 2, 3, 4]
print(sum_n(v))