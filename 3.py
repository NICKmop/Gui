from tkinter import *

root = Tk()
root.title("Jong GUI")  # 타이틀명 지정
root.geometry("640x480")  # 가로 x 세로의 크기 지정

# 스크롤바는 위젯과 스크롤바를 하나의 프레임에 넣고 관리하는 것이 편하다
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended",
                  height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):  # 1~31일
    listbox.insert(END, str(i)+"일")

listbox.pack(side="left")

# 서로서로를 맵핑시켜줘야지 서로가 연동되서 동작을한다.
# listbox에서는 yscrollcommand로 scrollbar을 , scrollbar에서는 config command로 listbox을 맵핑
scrollbar.config(command=listbox.yview)

root.mainloop()  # 창이 닫히지 않게 해주는 것