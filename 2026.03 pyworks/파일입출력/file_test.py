# 파일 쓰기 - 텍스트(문자열)만 가능 
try:
    f = open("output/file01.txt", 'w', encoding='utf-8')    # 쓰기는 'w'

    f.write("좋은 하루 되세요~\n")    # \n 줄 바꾸기
    # f.write(100)                     숫자만 작성하면 오류가 남
    f.write(str(100))   

    # 파일 닫기
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")


# 파일 읽기
try:
    f = open("output/file01.txt", 'r', encoding='utf-8')    # 읽기는 'r'
    content = f.read()
    print(content)

    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다")