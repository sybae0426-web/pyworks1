# 파일 쓰기 - 텍스트(문자열)만 가능 
# with ~ as 구문 : close() 생략 가능 
try:
    with open("output/file02.txt", 'w', encoding='utf-8') as f:

        f.write("좋은 하루 되세요~\n")    # \n 줄 바꾸기
        # f.write(100)                     숫자만 작성하면 오류가 남
        f.write(f'{str(100)}\n') 
        f.write('Good Luck!')  
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")


# 파일 읽기
try:
    with open("output/file02.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다")