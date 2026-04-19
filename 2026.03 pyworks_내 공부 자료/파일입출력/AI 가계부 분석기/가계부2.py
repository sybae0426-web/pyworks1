import pandas as pd

df = pd.read_csv('expenses.csv')

# 천 단위 구분 쉼표 추가
def format_currency(x):
    return f"{x:,}원"   

print("\n[지출 내역]")
print(df['amount'].apply(format_currency))

print("\n[카테고리별 합계]")
category_sum = df.groupby('category')['amount'].sum().sort_values(ascending=False)
print(category_sum.apply(format_currency))  

# print(df.groupby('category')['amount'].sum().sort_values(ascending=False).apply(format_currency))

monthly_total = df['amount'].sum()
print(f"총 지출: {monthly_total:,}원")   # 쉼표(,) 천단위로 구분       

print("\n[절약 목표 제안]")
print(f'다음 달 목표 지출: {int(monthly_total*0.9):,}원(10% 절감)') 
         