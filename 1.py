from cProfile import label
from datetime import datetime, timedelta
from msilib.schema import ListBox
import os , openpyxl, logging,logging.handlers
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from tkinter import messagebox
import tkinter as tk

from pymysql import NULL

log_today = datetime.now();
log_today = str(log_today).split(" ")[0];

log = logging.getLogger("C:/Users/user/OneDrive - 대한광통신/바탕 화면/예약/folderList_"+str(log_today)+".log");
log.setLevel(logging.DEBUG);
fileHandler = logging.FileHandler("C:/Users/user/OneDrive - 대한광통신/바탕 화면/예약/folderList_"+str(log_today)+".log");
streamHadler = logging.StreamHandler();

log.addHandler(fileHandler);
log.addHandler(streamHadler);


# gui 해당 루트 선택 input값으로.
directory = r'\\10.12.11.20\TFO.FAIT.Share'

# 생성 파일
dest_filename = 'folderList.xlsx'
# excel 파일 호출
load_monitoring = openpyxl.load_workbook(dest_filename)

#UI
root = Tk()
root.title("folder Scan")
root.geometry("400x480")



# GUI Text항목 데이터 전달
def getTextInput():
    result=textExample.get("1.0","end");
    # path 체크
    if len(result) == 1:
        print("path를 입력해주세요");
    else:
        # subfolders = run_fast_scandir(r'\\10.12.11.20\TFO.FAIT.Share')
        subfolders = [];
        try:
            # 네트워크 드라이브 폴더 루트 확인
            for f in os.scandir(r'\\10.12.11.20\TFO.FAIT.Share'):
                # 폴더 체크
                if f.is_dir():
                    # 폴더일때 값 추가
                    subfolders.append(f.path);
                    label.configure(text=subfolders);
        except PermissionError as ps:
            pass

        # for i in range(1, len(subfolders)):
        #     print(i); # subfolders[i]
        # label.configure(text=subfolders[i]);

textExample=tk.Text(root, height=5)
textExample.pack()
btnRead=tk.Button(root, height=1, width=4, text="Read", 
                    command=getTextInput)

label = Label(root, wraplength=480);
label.pack();


btnRead.pack()   

#폴더 스캔
def run_fast_scandir(dir):
    subfolders = [];
    try:
        for f in os.scandir(dir):
            if f.is_dir():
                subfolders.append(f.path);
    except PermissionError as ps:
        pass

    # 폴더 배열 List 형 변환
    for dir in list(subfolders):
        # 변수 다시 호출
        sf = run_fast_scandir(dir);
        subfolders.extend(sf);
    return subfolders;

def excelWrite(folderPath, Path):
    load_ws = load_monitoring['Sheet1'];
    for i in range(1, len(folderPath)):
        load_ws['A'+str(i)].value = '=HYPERLINK("{}")'.format(folderPath[i]);

    load_monitoring.save(Path);

root.mainloop()  # 창이 닫히지 않게 해주는 것

# subfolders = run_fast_scandir(directory);

# excelWrite(subfolders, dest_filename);






