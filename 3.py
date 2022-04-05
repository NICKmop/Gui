## Ex 5-19. QTextBrowser.

from msilib.schema import ListView
from functools import partial
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

    def clear_widget(self):
        self.listwidget.clear();
        self.listwidget2.clear();
        self.listwidget3.clear();
        self.listwidget4.clear();

    def initUI(self):
        #라벨
        self.label1 = QLabel('검색', self)

        # 검색창
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text);

        # QListWidget 추가
        self.listwidget = QListWidget(self)
        self.listwidget.resize(200, 100)
        self.listwidget2 = QListWidget(self)
        self.listwidget2.resize(150, 100)
        self.listwidget3 = QListWidget(self)
        self.listwidget3.resize(150, 100)
        self.listwidget4 = QListWidget(self)
        self.listwidget4.resize(150, 100)

        #스크롤링
        self.vs1 = self.listwidget.verticalScrollBar();
        self.vs2 = self.listwidget2.verticalScrollBar();
        self.vs3 = self.listwidget3.verticalScrollBar();
        self.vs4 = self.listwidget4.verticalScrollBar();
        self.vs1.valueChanged.connect(self.move_scrollbar);
        self.vs2.valueChanged.connect(self.move_scrollbar);
        self.vs3.valueChanged.connect(self.move_scrollbar);
        self.vs4.valueChanged.connect(self.move_scrollbar);

        # 시그널 연결
        self.listwidget.itemSelectionChanged.connect(self.selectchanged_listwidget);

        # --- 비우기 버튼 생성 --
        self.delete_button = QPushButton(self);
        self.delete_button.move(180, 5)
        self.delete_button.setText('청소')
        self.delete_button.clicked.connect(self.clicked_delete_button)

        self.layout = QGridLayout()
        self.layout.addWidget(self.label1,0,0);
        self.layout.addWidget(self.le,0,1);
        self.layout.addWidget(self.delete_button,2,0);
        self.layout.addWidget(self.listwidget, 1, 0);
        self.layout.addWidget(self.listwidget2, 1, 1)
        self.layout.addWidget(self.listwidget3, 1, 2);
        self.layout.addWidget(self.listwidget4, 1, 3);
        
        self.listwidget.resizeMode();

        self.setLayout(self.layout)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 1000, 500)
        self.show()

    def move_scrollbar(self,value):
        self.vs1.setValue(value);
        self.vs2.setValue(value);

    def append_text(self):
        self.listwidget4.clear();
        self.listwidget3.clear();
        self.listwidget2.clear();
        self.listwidget.clear();

        text = self.le.text();
        # with open(r'\\10.12.11.20\TFO.FAIT.Share\folderScan.json', 'r', encoding='utf-8') as f:
        with open('folderScan.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f);

            cnt = 0;
            for i in range(0,len(json_data)):
                path = json_data[i]['path'];
                # dir = json_data[i]['dir'];
                file = json_data[i]['file'];
                cTime = json_data[i]['fileExe'];
                fileExe = json_data[i]['fileCreateTime'];
                for j in file:
                    try:
                        if text in j:
                            cnt += 1;
                            self.listwidget.insertItem(cnt,path);
                            self.listwidget2.insertItem(cnt, j);
                            self.listwidget3.insertItem(cnt, cTime);
                            self.listwidget4.insertItem(cnt, fileExe);

                    except IndexError as In:
                        print(In);
                        pass
    # file
    def selectchanged_listwidget(self):

        lst_item = self.listwidget.selectedItems(); # 선택된 데이터 체크
        text = self.le.text();
        with open('folderScan.json', 'r', encoding='utf-8') as f:
        # with open(r'\\10.12.11.20\TFO.FAIT.Share\folderScan.json', 'r', encoding='utf-8') as f:
                json_data = json.load(f);

                for item in lst_item:
                    itemText = item.text();
                    
                    for i in range(0,len(json_data)):
                        path = json_data[i]['path'];
                        dir = json_data[i]['dir'];
                        file = json_data[i]['file'];
            
                        if path == text+"\\"+itemText:
                            for i in range(len(dir)):
                                self.listwidget2.insertItem(i, dir[i]);               
                            for i in range(len(file)):
                                self.listwidget3.insertItem(i,file[i]);
                
    def search_folderName(self):
        print("search");
    
    def search_fileExe(self):
        print("search");

    def clicked_delete_button(self):
        self.listwidget.clear();
        self.listwidget2.clear();
        self.listwidget3.clear();
        self.listwidget4.clear();
        self.le.clear();

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_());