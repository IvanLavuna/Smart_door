import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtTest
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QLabel, QWidget, QVBoxLayout, QPushButton)
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
import face_recognition
import cv2
import numpy as np
import os
import add_user_w
import delete_user_w
import run_w
folder_funny_photos = "/home/ivan/PycharmProjects/Face_recognizeXXX/funny_photos/"
folder_name = "/home/ivan/PycharmProjects/Face_recognizeXXX/known_faces/"
password = '1111'


class MyWindow_main(QMainWindow):
    def __init__(self):
        super(MyWindow_main, self).__init__()
        self.setGeometry(200, 200, 600, 500)
        self.setWindowTitle("Smart door")

        #css style
        self.stylesheet = '''
            QWidget {
               background-color: #222222;
            }

            QLineEdit {
               background-color: aliceblue;
               color: #618b38;
               font-style: italic;
               font-weight: bold;
            }

            QLabel {
               background-color: #222222;
               color: #618b38;
            }

            QPushButton {
               font-size: 24px;
               font-family: "Times New Roman", Times, serif;
               background-color: white;
               width: 300px;
               height: 100px;
               font-weight: bold;
               border:none;
               text-align:center; 

            }
            QPushButton:hover{
                background-color:silver;
            }
            QPushButton:pressed{
                background-color: blue;
            }
        '''
        self.setStyleSheet(self.stylesheet)

        # crete 3 buttons

        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)

        self.initUI()

    def initUI(self):

        # menu
        back = QAction(QIcon('exit.png'), '&goBack', self)
        back.setShortcut('Ctrl+Q')
        back.setStatusTip('go back')
        back.triggered.connect(self.go_to_main_window)
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Back')
        fileMenu.addAction(back)

    def go_to_main_window(self):
        self.w = MyWindow_main()
        self.w.show()
        self.hide()

class FormWidget(QWidget):
    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)

        self.button1 = QPushButton("add new user")
        self.layout.addWidget(self.button1)
        self.button1.clicked.connect(self.clicked_b1) # func

        self.button2 = QPushButton("delete user")
        self.layout.addWidget(self.button2)
        self.button2.clicked.connect(self.clicked_b2) # func

        self.button3 = QPushButton("run")
        self.layout.addWidget(self.button3)
        self.button3.clicked.connect(self.clicked_b3) # func

        self.setLayout(self.layout)

    def clicked_b3(self): # connect to window 3
        self.w = run_w.MyWindow_3()
        self.w.show()
        self.hide()
        self.parent().hide()

    def clicked_b2(self): # connect to window 2
        self.w = delete_user_w.MyWindow_2()
        self.w.show()
        self.hide()
        self.parent().hide()

    def clicked_b1(self):    # connect to window 1
        self.w = add_user_w.MyWindow_1()
        self.w.show()
        self.hide()
        self.parent().hide()


def window():
    app = QApplication(sys.argv)
    win = MyWindow_main()
    win.show()
    sys.exit(app.exec_())


