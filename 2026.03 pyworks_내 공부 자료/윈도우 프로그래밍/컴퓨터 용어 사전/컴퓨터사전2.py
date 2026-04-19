# 컴퓨터 용어 사전 만들기 (단어 등록 기능 추가)

from tkinter import *
from tkinter import messagebox

dict_terms = {
    "알고리즘": "문제를 해결하기 위한 일련의 절차나 방법",
    "함수": "특정 작업을 수행하는 코드 블록",
    "변수": "데이터를 저장하는 공간",
    "이진수": "0과 1로 이루어진 수 체계"
}

# 검색 함수 정의
def search():
    word = entry_search.get()  # 검색 입력상자에서 검색어 가져오기
    meaning = dict_terms.get(word, "해당 용어가 사전에 없습니다.")  # 사전에서 의미 가져오기
    output.delete(1.0, END)  # 결과 텍스트 상자 초기화
    output.insert(END, meaning)  # 결과 텍스트 상자에 의미 출력

# 등록 함수 정의
def add_word():
    word = entry_word.get().strip()  # 단어 입력상자에서 단어 가져오기
    meaning = entry_meaning.get().strip()  # 의미 입력상자에서 의미 가져오기
    if not word or not meaning:
        messagebox.showwarning("경고", "단어와 의미를 모두 입력하세요.")
        return
    if word in dict_terms:
        messagebox.showinfo("정보", "이미 존재하는 단어입니다.")
        return
    dict_terms[word] = meaning
    messagebox.showinfo("성공", f"'{word}' 단어가 등록되었습니다.")
    entry_word.delete(0, END)  # 입력상자 초기화
    entry_meaning.delete(0, END)

window = Tk()
window.title("컴퓨터 용어 사전")

# 제목 레이블
Label(window, text='컴퓨터 용어 사전').grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=W)

# 검색 섹션
Label(window, text='검색할 단어:').grid(row=1, column=0, padx=10, pady=5, sticky=W)
entry_search = Entry(window, width=30)
entry_search.grid(row=1, column=1, padx=10, pady=5, sticky=W)
Button(window, text='검색', command=search).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# 등록 섹션
Label(window, text='새 단어 등록:').grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=W)
Label(window, text='단어:').grid(row=4, column=0, padx=10, pady=5, sticky=W)
entry_word = Entry(window, width=30)
entry_word.grid(row=4, column=1, padx=10, pady=5, sticky=W)
Label(window, text='의미:').grid(row=5, column=0, padx=10, pady=5, sticky=W)
entry_meaning = Entry(window, width=30)
entry_meaning.grid(row=5, column=1, padx=10, pady=5, sticky=W)
Button(window, text='등록', command=add_word).grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# 결과 텍스트 상자
output = Text(window, width=50, height=10)
output.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky=W)

window.mainloop()