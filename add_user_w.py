import sys

from PyQt5.QtCore import QRect, QSize, QPoint

import add_face_window
import Main_Window
from PyQt5.QtWidgets import  QMessageBox
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtTest
from PyQt5.QtGui import QIcon, QMovie, QPainter, QPalette
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QLabel, QGraphicsView, QVBoxLayout, QPushButton, QWidget, QLineEdit)
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
import face_recognition
import cv2
import numpy as np
import os

# add new user
folder_name = "/home/ivan/PycharmProjects/Face_recognizeXXX/known_faces/"

class MyWindow_1(QMainWindow):
    def __init__(self):
        super(MyWindow_1, self).__init__()
        self.setGeometry(200, 200, 600, 500)
        self.setWindowTitle("Smart door")
        self.arr = []

        # css style
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
               border-radius: 70%;
               font-size: 24px;
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

        self.initUI()

    def initUI(self):
        self.picture = QLabel(self)

        # menu
        back = QAction(QIcon('exit.png'), '&goBack', self)
        back.setShortcut('Ctrl+Q')
        back.setStatusTip('go back')
        back.triggered.connect(self.go_to_main_window)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Back')
        fileMenu.addAction(back)

        # ask for password
        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText("Password")
        self.label_1.setGeometry(QtCore.QRect(20, 20, 300, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_1.setFont(font)
        self.label_1.setFrameShadow(QtWidgets.QFrame.Raised)

        # line edit 1
        self.lineEdit_1 = QtWidgets.QLineEdit(self)
        self.lineEdit_1.setGeometry(QtCore.QRect(150, 42, 291, 25)) #291 25
        self.name = ""

        # 'ok' button 1
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("OK")
        self.b1.setGeometry(450, 40, 35, 33) # something
        self.b1.clicked.connect(self.clicked_b1)

        # ask for user's name
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText("Please user's name ")
        self.label_2.setGeometry(QtCore.QRect(20, 20, 0, 0)) # 300 61
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)

        # line edit 2
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 42, 0, 0)) #291 25
        self.name = ""

        # 'ok' button 2
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("OK")
        self.b2.setGeometry(450, 150, 0, 0)
        self.b2.clicked.connect(self.clicked_b2)

        # 'make photo' button 3
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Make photo")
        self.b3.setGeometry(0, 0, 0, 0)
        self.b3.clicked.connect(self.clicked_b3)

        # 'Save photo' button 4
        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Save photo")
        self.b4.setGeometry(0, 0, 0, 0)
        self.b4.clicked.connect(self.clicked_b4)

    def clicked_b1(self):
        self.password  = self.lineEdit_1.text()
        self.lineEdit_1.clear()
        if (self.password == Main_Window.password):
            self.label_2.setText("Please write user's name ")
            self.label_2.setGeometry(QtCore.QRect(20, 100, 300, 61))  # 300 61
            self.lineEdit_2.setGeometry(QtCore.QRect(150, 150, 291, 25))  # 291 25
            self.b2.setGeometry(450, 150, 35, 33) # something
        else:
            self.wrong_password_pop_up()

    def clicked_b2(self):
        self.name  = self.lineEdit_2.text()
        self.b3.setGeometry(90, 250, 200, 150)

    def clicked_b3(self):
        self.countdown()
        self.make_photo()
        self.b4.setGeometry(350, 250, 200, 150)
        self.b3.setText("Remake photo")

    def clicked_b4(self):
        self.save_photo()
        msg = QMessageBox()
        msg.setWindowTitle("Message box")
        msg.setText("Photo is successfully saved")

        x = msg.exec_()

        self.go_to_main_window()

    def countdown(self):
        self.b4.setGeometry(0, 0, 0, 0)
        self.picture.setPixmap(QPixmap(Main_Window.folder_funny_photos + 'first.png'))
        self.picture.setGeometry(350, 250, 200, 180)
        QtTest.QTest.qWait(1000)

        self.picture.setPixmap(QPixmap(Main_Window.folder_funny_photos + 'key.png'))
        self.picture.setGeometry(350, 250, 200, 180)
        QtTest.QTest.qWait(1000)

        self.picture.setPixmap(QPixmap(Main_Window.folder_funny_photos + 'first.png'))
        self.picture.setGeometry(350, 250, 200, 180)
        QtTest.QTest.qWait(1000)
        self.picture.setGeometry(0, 0, 0, 0)

    def wrong_password_pop_up(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message box")
        msg.setText("Password is wrong")
        msg.setIcon(QMessageBox.Critical)

        x = msg.exec_()

    def go_to_main_window(self):
        self.w = Main_Window.MyWindow_main()
        self.w.show()
        self.hide()

    def save_photo(self):
        filename = folder_name + self.name + ".jpg"
        cv2.imwrite(filename, self.arr[-1])

    def make_photo(self):
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
        cv2.imshow('pic', frame)
        self.arr.append(frame)






