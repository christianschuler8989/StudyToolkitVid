import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtMultimediaWidgets import *
from PyQt6.QtMultimedia import *


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
		self.setMinimumSize(QSize(600,400))
		
		# import file button 
		mediaImportBtn = QPushButton(self)
		mediaImportBtn.setText("Import file")
		mediaImportBtn.clicked.connect(self.open_dialog)


		# media player
		self.videoWidget = QVideoWidget()
		self.videoWidget.show()

		
		self.playButton = QPushButton()
		self.playButton.setEnabled(False)
		self.playButton.setText("Play")
		self.playButton.clicked.connect(self.play)

		controllayout = QVBoxLayout()
		controllayout.addWidget(self.videoWidget)
		controllayout.addWidget(self.playButton)
		layout = QHBoxLayout()

		layout.addWidget(mediaImportBtn)
		layout.addLayout(controllayout)
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

	# import file and give to media player
	def open_dialog(self):
		self.fname = QFileDialog.getOpenFileName(
			self,
			"Open File",
			"${HOME}",
			"All Files (*);; Python Files (*.py);; PNG Files (*.png)",
		)
		self.playButton.setEnabled(True)
	# play video	
	def play(self):
		self.player = QMediaPlayer()
		self.player.setSource(QUrl.fromLocalFile(self.fname[0]))
		self.player.setVideoOutput(self.videoWidget)
		self.audioOutput = QAudioOutput()
		self.player.setAudioOutput(self.audioOutput)
		self.audioOutput.setVolume(100)

		if self.player.playbackState() == QMediaPlayer.PlaybackState:
			self.player.pause()
		else:
			self.player.play()



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