# json 데이터 읽기
import json
import os

# 현재 파일의 디렉터리 경로(path) 가져옴
# 절대 경로
base_dir = os.path.dirname(os.path.abspath(__file__))
print("디렉터리 이름:", base_dir)
file_path = os.path.join(base_dir, "products.json")
print("파일 경로:", base_dir)

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        # json.load(데이터)로 데이터 가져옴
        data = json.load(f)
        print(data)
except FileExistsError:
    print("파일을 찾을 수 없습니다.")


# 제품 정보 출력
print("첫번째 제품 정보")
print(f"ID: {data[0]['id']}")
print(f"Name: {data[0]['name']}")
print(f"Price: {data[0]['price']}")
print(f"Description: {data[0]['description']}")

print("\n 제목 목록")
print('='*50)
for product in data:
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: {product['price']}")
    print(f"Description: {product['description']}")
    print('-'*50)

 
