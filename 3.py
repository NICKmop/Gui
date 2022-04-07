## Ex 5-19. QTextBrowser.

from ast import Num
from msilib.schema import ListView
from functools import partial
import sys, json, os
from tkinter import messagebox
from PyQt5.QtWidgets import (QApplication, QWidget
, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import collections

class MyApp(QWidget):
    def __init__(self):
        super().__init__();
        self.drawn();
        self.initUI();

    def clear_widget(self):
        self.listwidget.clear();
        self.listwidget2.clear();
        self.listwidget3.clear();
        self.listwidget4.clear();

    def drawn(self):
        self.palette = QPalette();
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("1.png")));
        self.setPalette(self.palette);

    def initUI(self):
        #라벨
        self.label = QLabel('검색', self);
        self.label.setStyleSheet("border : 1px solid black");
        self.label.setAlignment(Qt.AlignCenter);

        self.label1 = QLabel('경로', self);
        self.label1.setFont(QFont("궁서",20));
        self.label2 = QLabel('파일', self);
        self.label2.setFont(QFont("궁서",20));
        self.label3 = QLabel('날짜', self);
        self.label3.setFont(QFont("궁서",20));
        self.label4 = QLabel('확장명', self);
        self.label4.setFont(QFont("궁서",20));

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

        # --- 비우기 버튼 생성 --
        self.delete_button = QPushButton(self);
        self.delete_button.setText('청소')
        self.delete_button.clicked.connect(self.clicked_delete_button)

        # 파일 열기 버튼
        self.open_button = QPushButton(self);
        self.open_button.setText('열기');
        self.open_button.clicked.connect(self.double_selectchanged_listwidget);

        self.layout = QGridLayout()
        self.layout.addWidget(self.label,0,0);
        self.layout.addWidget(self.le,0,1);

        self.layout.addWidget(self.label1,1,0);
        self.layout.addWidget(self.label2,1,1);
        self.layout.addWidget(self.label3,1,2);
        self.layout.addWidget(self.label4,1,3);

        self.layout.addWidget(self.listwidget, 2, 0);
        self.layout.addWidget(self.listwidget2, 2, 1)
        self.layout.addWidget(self.listwidget3, 2, 2);
        self.layout.addWidget(self.listwidget4, 2, 3);

        self.layout.addWidget(self.delete_button,3,0);
        self.layout.addWidget(self.open_button,3,1);
        
        
        self.listwidget.resizeMode();

        self.setLayout(self.layout)

        self.setWindowTitle('폴더검색')
        self.setGeometry(300, 300, 1000, 500)
        self.show()

    def move_scrollbar(self,value):
        self.vs1.setValue(value);
        self.vs2.setValue(value);
        self.vs3.setValue(value);
        self.vs4.setValue(value);

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
                try:
                    path = json_data[i]['path'];
                    # dir = json_data[i]['dir'];
                    file = json_data[i]['file'];
                    cTime = json_data[i]['fileCreateTime'];
                    fileExe = json_data[i]['fileExe'];

                    for j,k,l in zip(file, cTime, fileExe):
                        if text in j:
                            cnt += 1;
                            self.listwidget.insertItem(cnt,path);
                            self.listwidget2.insertItem(cnt, j);
                            #수정 필요
                            self.listwidget3.insertItem(cnt, k);
                            self.listwidget4.insertItem(cnt, l);
                    
                        # else:
                        #     print("None 파일")
                        #     QMessageBox.about(self, 'None file','파일이 없습니다.');
                        #     return self.append_text;

                except IndexError as In:
                    print(In);
                    pass
                except KeyError as ke:
                    print(ke);
                    pass;
    
    def double_selectchanged_listwidget(self):
        lst_item = self.listwidget2.selectedItems();

        with open('folderScan.json', 'r', encoding='utf-8') as f:
        # with open(r'\\10.12.11.20\TFO.FAIT.Share\folderScan.json', 'r', encoding='utf-8') as f:
                json_data = json.load(f);

                for item in lst_item:
                    for i in range(0,len(json_data)):
                        path = json_data[i]['path'];
                        file = json_data[i]['file'];

                        for j in file:
                            
                            if j == item.text():
                                print("j 데이타 : ", len(j));
                                print("path : ", path);

                                # print("duplPath : ", duplPath);
                                # full_path = path+"\\"+item.text();
                                # os.startfile(full_path);

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