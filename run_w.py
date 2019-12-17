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

import Main_Window
import add_user_w
import delete_user_w


class MyWindow_3(QMainWindow):
    def __init__(self):
        super(MyWindow_3, self).__init__()
        self.setGeometry(200, 200, 600, 500)
        self.setWindowTitle("Smart door")
        self.folder_name = Main_Window.folder_name
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

        # menu
        back = QAction(QIcon('exit.png'), '&goBack', self)
        back.setShortcut('Ctrl+Q')
        back.setStatusTip('go back')
        back.triggered.connect(self.go_to_main_window)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Back')
        fileMenu.addAction(back)

        self.picture = QLabel(self)
        self.picture.setPixmap(QPixmap(Main_Window.folder_funny_photos + 'closed_door.jpeg'))
        self.picture.setGeometry(0, 40, 600, 500)

        # 'run' button
        self.run = QtWidgets.QPushButton(self)
        self.run.setText("run")
        self.run.setGeometry(450, 40, 35, 33) # something
        self.run.clicked.connect(self.face_rec)

    def go_to_main_window(self):
        self.w = Main_Window.MyWindow_main()
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
        for filename in os.listdir(self.folder_name):
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
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
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
                        print("Hello " + name)
                        self.picture.setPixmap(QPixmap(Main_Window.folder_funny_photos + 'opened_door.jpg'))
                        self.picture.setGeometry(0, 40, 600, 500)
                        video_capture.release()
                        return 0
                    else:
                        print("Bad attempt")
                        self.picture.setPixmap(QPixmap(Main_Window.folder_funny_photos + 'sad_man.jpg'))
                        self.picture.setGeometry(0, 40, 600, 500)
                        return 0

            process_this_frame = not process_this_frame

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()











