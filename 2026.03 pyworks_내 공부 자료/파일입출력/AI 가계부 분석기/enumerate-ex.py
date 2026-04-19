# 리스트: 열거하다 - enumerate()

colors = ['빨강', '초록', '파랑']
print('\n색상 목록')
for index, color in enumerate(colors, 1):   # start = 1
    print(f"{index}: {color}")



# 딕셔너리 열거
person = {
    '이름': '홍길동',
    '나이': '30,',
    '직업': '기자'
}

for index, (key, value) in enumerate(person.items(), 1):
    print(f'{index}. {key}: {value}')

