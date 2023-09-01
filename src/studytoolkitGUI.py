import sys
from media_editing import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtMultimediaWidgets import *
from PyQt6.QtMultimedia import *
# Christian joined the chat.

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
		mediaImportBtn.clicked.connect(self.importfile)


		# media player
		self.oldvideoWidget = QVideoWidget()
		self.oldvideoWidget.show()
		self.newvideoWidget = QVideoWidget()
		self.newvideoWidget.show()
		

		self.oldplayButton = QPushButton()
		self.oldplayButton.setEnabled(False)
		self.oldplayButton.setText("Play")
		self.oldplayButton.clicked.connect(self.play)

		self.newplayButton = QPushButton()
		self.newplayButton.setEnabled(False)
		self.newplayButton.setText("Play")
		self.newplayButton.clicked.connect(self.play)

		# import and display original video
		oldvideolayout = QVBoxLayout()
		oldvideolayout.addWidget(mediaImportBtn)
		oldvideolayout.addWidget(self.oldvideoWidget)
		oldvideolayout.addWidget(self.oldplayButton)
		# display new edited video
		newvideolayout = QVBoxLayout()
		newvideolayout.addWidget(self.newvideoWidget)
		newvideolayout.addWidget(self.newplayButton)
		
		# buttons to edit vidwo
		self.editButton1 = QPushButton()
		self.editButton1.setEnabled(False)
		self.editButton1.setText("Mirror Horizontally")
		self.editButton1.clicked.connect(self.mirrorX)
		self.editButton2 = QPushButton()
		self.editButton2.setEnabled(False)
		self.editButton2.setText("Option 2")		
		
		self.editButton3 = QPushButton()
		self.editButton3.setEnabled(False)
		self.editButton3.setText("Option 3")
		
		# area to edit vidwo
		editinglayout = QVBoxLayout()
		editinglayout.addWidget(self.editButton1)
		editinglayout.addWidget(self.editButton2)
		editinglayout.addWidget(self.editButton3)


		layout = QHBoxLayout()
		layout.addLayout(oldvideolayout)
		layout.addLayout(editinglayout)
		layout.addLayout(newvideolayout)

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

	# import file and give to media player
	def importfile(self):
		self.fname = QFileDialog.getOpenFileName(
			self,
			"Open File",
			"${HOME}",
			"All Files (*);; Python Files (*.py);; PNG Files (*.png)",
		)
		self.filename = self.fname[0].split("/")[-1]
		self.filepath = self.fname[0][:-len(self.filename)]
		self.oldplayButton.setEnabled(True)
		self.setplayer(self.oldvideoWidget)
		self.setEditingBtnActive()

	# set buttons for editing active
	def setEditingBtnActive(self): 
		self.editButton1.setEnabled(True)
		self.editButton2.setEnabled(True)
		self.editButton3.setEnabled(True)

	# give player widgets a player instance 
	def setplayer(self, widget):
		self.player = QMediaPlayer()
		self.player.setSource(QUrl.fromLocalFile(self.fname[0]))
		self.player.setVideoOutput(widget)
		self.audioOutput = QAudioOutput()
		self.player.setAudioOutput(self.audioOutput)
		self.audioOutput.setVolume(100)
	
	# play video	
	def play(self) : 
		if self.player.isPlaying():
			self.player.pause()
			self.oldplayButton.setText("Play")
		else :
			self.player.play()
			self.oldplayButton.setText("Pause")
	
	# mirror video horizontally 
	def mirrorX(self) : 
		os.system("python3 media_editing.py -path " + self.filepath + " -name " + self.filename + " -mirrorX ./")
		# to fit media_editing.py 
		# self.showOutput("MIRROR_X")


# window to generate studies
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