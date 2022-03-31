## Ex 5-19. QTextBrowser.

import sys, json
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
        self.listwidget.itemSelectionChanged.connect(self.selectchanged_listwidget)
        # --- 삭제 버튼 생성 --
        self.delete_button = QPushButton(self);
        self.delete_button.move(180, 5)
        self.delete_button.setText('삭제')

        # 삭제 시그널
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
        text = self.le.text();
        if text == r'\\10.12.11.20\TFO.FAIT.Share':
            with open('folderScan.json', 'r', encoding='utf-8') as f:
                json_data = json.load(f);
            
            # fileBox = [];
            cnt = 0;
            for i in range(0,len(json_data)):
                path = json_data[i]['path'];
                dir = json_data[i]['dir'];
                file = json_data[i]['file'];
                for j in dir:
                    cnt += 1;
                    self.listwidget.insertItem(cnt, j);
        else:
            print("none path");

    def selectchanged_listwidget(self):
        lst_item = self.listwidget.selectedItems()# 선택된 데이터 체크
        # 선택된 데이터 출력 file 리스트 출력
        for item in lst_item:
            print(item.text())
    def clicked_delete_button(self):
        # 선택된 데이터가 있는지 체크
        lst_modelindex = self.listwidget.selectedIndexes()
        # 선택된 데이터 삭제
        for modelindex in lst_modelindex:
            print(modelindex.row())
            self.listwidget.model().removeRow(modelindex.row())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_());