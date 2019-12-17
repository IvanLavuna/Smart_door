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

class MyWindow_2(QMainWindow):
    def __init__(self):
        super(MyWindow_2,self).__init__()
        self.setGeometry(200,200,600,500)
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
        self.label_2.setText("Write user's name you want to delete")
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

    # to delete user
    def clicked_b2(self):
        self.name = self.lineEdit_2.text()

        if(cv2.os.path.isfile(Main_Window.folder_name + self.name + ".jpg") == True):
            cv2.os.remove(Main_Window.folder_name + self.name + ".jpg")
            self.success()
        else:
            self.failing()

    def success(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message box")
        msg.setText("User is successfully deleted")

        x = msg.exec_()

    def failing(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message box")
        msg.setText("User is not exit on database!")
        msg.setIcon(QMessageBox.Critical)

        x = msg.exec_()


    def clicked_b1(self):
        self.password  = self.lineEdit_1.text()
        self.lineEdit_1.clear()
        if (self.password == Main_Window.password):
            self.label_2.setText("Write name of user you want to delete ")
            self.label_2.setGeometry(QtCore.QRect(20, 100, 500, 61))  # 300 61
            self.lineEdit_2.setGeometry(QtCore.QRect(150, 150, 291, 25))  # 291 25
            self.b2.setGeometry(450, 150, 35, 33) # something
        else:
            self.wrong_password_pop_up()

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