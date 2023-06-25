import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


####### Defining different windows #######
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Study Tool Kit")
        self.setMinimumSize(QSize(600,400))

        mediaEditBtn = QPushButton(self)
        mediaEditBtn.setText("Media Editing")
        mediaEditBtn.clicked.connect(self.openMediaEditWindow)

        studyGenBtn = QPushButton(self)
        studyGenBtn.setText("Study Generation")
        studyGenBtn.clicked.connect(self.openStudyGenWindow)


        layout = QHBoxLayout()

        layout.addWidget(mediaEditBtn)
        layout.addWidget(studyGenBtn)
        layout.addWidget(Color('blue'))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def openMediaEditWindow(self):
        self.w = MediaEditWindow()
        self.w.show()

    def openStudyGenWindow(self):
        self.w = StudyGenWindow()
        self.w.show()


class MediaEditWindow(QMainWindow):

    def __init__(self):
        super(MediaEditWindow, self).__init__()

        self.setWindowTitle("Media Editing")
        self.setMinimumSize(QSize(400,600))

        mediaEditBtn = QPushButton(self)
        mediaEditBtn.setText("Import file")
        mediaEditBtn.clicked.connect(self.open_dialog)

        layout = QHBoxLayout()

        layout.addWidget(mediaEditBtn)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_dialog(self):
        fname = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "${HOME}",
            "All Files (*);; Python Files (*.py);; PNG Files (*.png)",
        )
        print(fname)




class StudyGenWindow(QMainWindow):

    def __init__(self):
        super(StudyGenWindow, self).__init__()

        self.setWindowTitle("Study Generation")
        self.setMinimumSize(QSize(400,600))

        studyGenBtn = QPushButton(self)
        studyGenBtn.setText("Generate your study")

        layout = QHBoxLayout()

        layout.addWidget(studyGenBtn)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)









################## main stream of the program #################
app = QApplication(sys.argv)

window = MainWindow()
window.show()



app.exec()