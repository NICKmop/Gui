## Ex 5-19. QTextBrowser.

import sys, json, os
from tkinter import messagebox
from PyQt5.QtWidgets import (QApplication, QWidget
, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text);

        # QListWidget 추가
        self.listwidget = QListWidget(self)
        self.listwidget.resize(150, 100)

        # QListWidget 추가
        self.listwidget2 = QListWidget(self)
        self.listwidget2.resize(150, 100)
        # 시그널 연결
        self.listwidget.itemSelectionChanged.connect(self.selectchanged_listwidget);

        # --- 비우기 버튼 생성 --
        self.delete_button = QPushButton(self);
        self.delete_button.move(180, 5)
        self.delete_button.setText('청소')

        # 비우기 시그널
        self.delete_button.clicked.connect(self.clicked_delete_button)

        self.layout = QGridLayout()
        self.layout.addWidget(self.le,1,0)
        self.layout.addWidget(self.delete_button,2,0);
        self.layout.addWidget(self.listwidget, 0, 0)

        self.layout.addWidget(self.listwidget2, 0, 1)

        self.setLayout(self.layout)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 1000, 500)
        self.show()

    def append_text(self):
        self.listwidget2.clear();
        self.listwidget.clear();

        text = self.le.text();
        with open(r'\\10.12.11.20\TFO.FAIT.Share\folderScan.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f);

            # if text == r'\\10.12.11.20\TFO.FAIT.Share':
                
                # fileBox = [];
            cnt = 0;
            for i in range(0,len(json_data)):
                path = json_data[i]['path'];
                dir = json_data[i]['dir'];
                file = json_data[i]['file'];
                if text == path:
                    if not dir:
                        dir = ["폴더가 없습니다."]
                    elif not file:
                        file = ["파일이 없습니다."]

                    for j in dir:
                        cnt += 1;
                        self.listwidget.insertItem(cnt, j);
                    for k in file:
                        cnt += 1;
                        self.listwidget2.insertItem(cnt, k);

    def selectchanged_listwidget(self):
        self.listwidget2.clear();

        lst_item = self.listwidget.selectedItems(); # 선택된 데이터 체크
        text = self.le.text();
        with open(r'\\10.12.11.20\TFO.FAIT.Share\folderScan.json', 'r', encoding='utf-8') as f:
                json_data = json.load(f);

                for item in lst_item:
                    itemText = item.text();
                    
                    for i in range(0,len(json_data)):
                        path = json_data[i]['path'];
                        dir = json_data[i]['dir'];
                        file = json_data[i]['file'];

                        # print("path : ",path);
                        # print("R Path : ", r"'"+path+"'")

                        if path == text+"\\"+itemText:
                            # print(len(file));
                            for i in range(len(file)):
                                self.listwidget2.insertItem(i,file[i]);
    
    def clicked_delete_button(self):
        self.listwidget.clear();
        self.listwidget2.clear();
        self.le.clear();

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_());