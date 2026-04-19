from tkinter import *

window = Tk()
window.title("Grid 레이아웃")
window.geometry("300x200")

# 레이블 만들기
Label(window, text='안녕하세요').grid(row=0, column=0, padx=20, pady=20)   
# 위/아래여백 pady,     좌우여백 padx


# 버튼 만들기
Button(window, text='동').grid(row=0, column=1)
Button(window, text='서').grid(row=0, column=2)
Button(window, text='남').grid(row=1, column=1)
Button(window, text='북').grid(row=1, column=2)





window.mainloop()