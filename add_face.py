import sys
import add_face_window

from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtTest
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QLabel)
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
import face_recognition
import cv2
import numpy as np
import os

folder_name = "/home/ivan/PycharmProjects/Face_recognizeXXX/known_faces/"
folder_funny_photos = "/home/ivan/PycharmProjects/Face_recognizeXXX/funny_photos/"



# starting from MyWindow_main


class MyWindow_main(QMainWindow):
    def __init__(self):
        super(MyWindow_main, self).__init__()
        self.setGeometry(200, 200, 600, 500)
        self.setWindowTitle("Scarlet is my love")
        self.initUI()

    def initUI(self):
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("add new user")
        self.b1.setGeometry(QtCore.QRect(0, 40, 600, 111))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(22)
        self.b1.setFont(font)
        self.b1.setObjectName("pushButton")
        self.b1.clicked.connect(self.clicked_b1) # func

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("delete user")
        self.b2.setGeometry(QtCore.QRect(0, 150, 600, 111))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(22)
        self.b2.setFont(font)
        self.b2.setObjectName("pushButton_2")
        self.b2.clicked.connect(self.clicked_b2) # func

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("run smart door")
        self.b3.setGeometry(QtCore.QRect(0, 260, 600, 111))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(22)
        self.b3.setFont(font)
        self.b3.setObjectName("pushButton_3")
        self.b3.clicked.connect(self.clicked_b3) # func

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

    def clicked_b3(self): # connect to window 3
        self.w = MyWindow_3()
        self.w.show()
        self.hide()

    def clicked_b2(self): # connect to window 2
        self.w = MyWindow_2()
        self.w.show()
        self.hide()

    def clicked_b1(self):    # connect to window 1
        self.w = MyWindow_1()
        self.w.show()
        self.hide()

# add new user
class MyWindow_1(QMainWindow):
    def __init__(self):
        super(MyWindow_1, self).__init__()
        self.setGeometry(200, 200, 600, 500)
        self.setWindowTitle("Scarlet is my love")
        self.arr = []
        self.initUI()

    def initUI(self):

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText("Do you want to bring your photo to the database?")
        self.label_1.setGeometry(QtCore.QRect(0, 20, 661, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_1.setFont(font)
        self.label_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_1.setObjectName("label_1")


        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Yes")
        self.b1.setGeometry(0, 80, 89, 25)
        self.b1.clicked.connect(self.clicked_b1)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("No")
        self.b2.setGeometry(170, 80, 89, 25)
        self.b2.clicked.connect(self.clicked_b2)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText("Print user\'s name,please")
        self.label_2.setGeometry(QtCore.QRect(10, 129, 0, 0)) # 661 61
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.b5 = QtWidgets.QPushButton(self)
        self.b5.setText("OK")
        self.b5.setGeometry(200, 200, 0, 0) # something
        self.pushed = 0
        if(self.pushed == 0):
            self.b5.clicked.connect(self.clicked_b5)
            self.pushed = 1

        self.lineEdit_1 = QtWidgets.QLineEdit(self)
        self.lineEdit_1.setGeometry(QtCore.QRect(20, 200, 0, 0)) #291 25
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.name = ""

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setText("PPPPPrepere")
        self.label_3.setGeometry(QtCore.QRect(20, 260, 0, 0)) # 421 61
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.picture = QLabel(self)

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setText("Remake a photo?")
        self.label_4.setGeometry(QtCore.QRect(30, 336, 0, 0)) # 231 81
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("yes,photo is horrible")
        self.b3.setGeometry(30, 430, 0, 0)# 251 61
        self.b3.clicked.connect(self.clicked_b3)

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("no,it\'s fine")
        self.b4.setGeometry(380, 430, 0, 0)# 251 61
        self.b4.clicked.connect(self.clicked_b4)

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


    def save_photo(self):
        filename = folder_name + self.name + ".jpg"
        cv2.imwrite(filename, self.arr[-1])

    def make_photo(self):
        self.picture.setPixmap(QPixmap('jonnie.png'))
        self.picture.setGeometry(0, 0, 600, 500)
        self.sleep(1000)

        video_capture = cv2.VideoCapture(0)
        ret,frame = video_capture.read()

        cv2.imshow('pic', frame)

        self.arr.append(frame)

        self.picture.setGeometry(0, 0, 0, 0)

        self.label_4.setGeometry(QtCore.QRect(30, 336, 231, 81)) # 231 81
        self.b3.setGeometry(30, 430, 251, 61)# 251 61
        self.b4.setGeometry(380, 430, 251, 61)# 251 61

    def clicked_b3(self):
        self.make_photo()

    def clicked_b4(self):
        self.save_photo()
        self.go_to_main_window()

    def clicked_b5(self):
        self.name  = self.lineEdit_1.text()
        self.sleep()
        self.label_3.setGeometry(QtCore.QRect(20, 260, 421, 61)) # 421 61

        self.sleep(5000)
        self.make_photo()

    def clicked_b1(self):
        self.label_2.setGeometry(QtCore.QRect(10, 129, 661, 61)) # 661 61
        self.lineEdit_1.setGeometry(QtCore.QRect(20, 200, 291, 25)) #291 25
        self.b5.setGeometry(350, 195, 50, 30) # something

    def clicked_b2(self):
        self.go_to_main_window()

    def sleep(self, time = 2500):
        QtTest.QTest.qWait(time)

# delete user /here i must write/
class MyWindow_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 500)
        self.setWindowTitle("Scarlet is my love")
        self.initUI()

    def initUI(self):

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText("write a name of whom you want to delete")
        self.label_1.setGeometry(QtCore.QRect(0, 20, 661, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_1.setFont(font)
        self.label_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_1.setObjectName("label_1")

        self.lineEdit_1 = QtWidgets.QLineEdit(self)
        self.lineEdit_1.setGeometry(QtCore.QRect(20, 90, 291, 25)) #291 25
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.name = ""

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Delete")
        self.b1.setGeometry(330, 82, 100, 40) # something
        self.b1.clicked.connect(self.clicked_b1_delete)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText(" ")
        self.label_2.setGeometry(QtCore.QRect(0, 190, 0, 0)) # 661 61
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setObjectName("label_2")


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

    def clicked_b1_delete(self):

        self.name  = self.lineEdit_1.text()

        if cv2.os.path.isfile(folder_name + self.name + ".jpg") == True:

            cv2.os.remove(folder_name + self.name + ".jpg")

            self.label_2.setText("Person is successfully deleted")
            self.label_2.setGeometry(QtCore.QRect(0, 110, 661, 61))  # 661 61
        else:
            self.label_2.setText("Person does not exist in database")
            self.label_2.setGeometry(QtCore.QRect(0, 110, 661, 61))

class MyWindow_3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 500)
        self.setWindowTitle("Scarlet is my love")
        self.folder_name = "/home/ivan/PycharmProjects/Face_recognizeXXX/known_faces/"
        self.initUI()

    def initUI(self):

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText(" ")
        self.label_1.setGeometry(QtCore.QRect(20, 260, 0, 0)) # 421 61
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")



        # menu
        back = QAction(QIcon('exit.png'), '&goBack', self)
        back.setShortcut('Ctrl+Q')
        back.setStatusTip('go back')
        back.triggered.connect(self.go_to_main_window)
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Back')
        fileMenu.addAction(back)

        self.face_rec()


    def go_to_main_window(self):
        self.w = MyWindow_main()
        self.w.show()
        self.hide()

    def face_rec(self):
        self.known_names = []
        self.known_encodings = []

        self.known_images = self.load_images_from_folder()
        self.create_known_encodings()
        self.create_known_names()
        self.webcam_recognition()

    def create_known_encodings(self):
        for img in self.known_images:
            current_face_encoding = face_recognition.face_encodings(img)[0]
            self.known_encodings.append(current_face_encoding)

    def create_known_names(self):
        for filename in os.listdir(folder_name):
            self.known_names.append(filename[:-4])

    def load_images_from_folder(self):
        images = []
        for filename in os.listdir(self.folder_name):
            img = cv2.imread(os.path.join(self.folder_name, filename))
            if img is not None:
                images.append(img)
        return images

    def webcam_recognition(self):
        video_capture = cv2.VideoCapture(0)

        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        while True:
            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx = 0.25, fy = 0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            if process_this_frame:
                face_encodings = face_recognition.face_encodings(rgb_small_frame)

                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
                    name = "Unknown"

                    face_distances = face_recognition.face_distance(self.known_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)

                    if matches[best_match_index]:
                        name = self.known_names[best_match_index]
                        self.label_1.setText("Hello," + self.known_names[best_match_index] )
                        self.label_1.setGeometry(QtCore.QRect(20, 260, 421, 61)) # 421 61
                        video_capture.release()
                        return 0

                    else:
                        self.label_1.setText("You are not recognised")
                        self.label_1.setGeometry(QtCore.QRect(20, 260, 421, 61))  # 421 61
                        return 0

            process_this_frame = not process_this_frame

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

def window():
    app = QApplication(sys.argv)
    win = MyWindow_main()
    win.show()
    sys.exit(app.exec_())


window()
'''
app = QApplication([])
foo = add_face_window.MyMainWindow()
foo.show()
sys.exit(app.exec_())
'''





