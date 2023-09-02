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

		statAnaBtn = QPushButton(self)
		statAnaBtn.setText("Statistical Analysis")
		statAnaBtn.clicked.connect(self.openStatAnaWindow)

		layout = QHBoxLayout()

		layout.addWidget(mediaEditBtn)
		layout.addWidget(studyGenBtn)
		layout.addWidget(statAnaBtn)
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

	def openMediaEditWindow(self):
		self.w = MediaEditWindow()
		self.w.show()

	def openStudyGenWindow(self):
		self.w = StudyGenWindow()
		self.w.show()

	def	openStatAnaWindow(self) : 
		self.w = StatAnaWindow()
		self.w.show()

class MediaEditWindow(QMainWindow):

	def __init__(self):
		super(MediaEditWindow, self).__init__()

		self.setWindowTitle("Media Editing")
		self.setMinimumSize(QSize(900,600))
		
		# import file button 
		mediaImportBtn = QPushButton(self)
		mediaImportBtn.setText("Import file")
		mediaImportBtn.clicked.connect(self.importfile)


		# media player
		self.oldvideoWidget = QVideoWidget()
		self.oldvideoWidget.setMinimumWidth(300)
		self.oldvideoWidget.show()
		self.newvideoWidget = QVideoWidget()
		self.newvideoWidget.setMinimumWidth(300)
		self.newvideoWidget.show()
		

		self.oldplayButton = QPushButton()
		self.oldplayButton.setEnabled(False)
		self.oldplayButton.setText("Play")
		self.oldplayButton.clicked.connect(self.playold)

		self.newplayButton = QPushButton()
		self.newplayButton.setEnabled(False)
		self.newplayButton.setText("Play")
		self.newplayButton.clicked.connect(self.playnew)

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
		# button to mirror horizontally
		self.mirrorXButton = QPushButton()
		self.mirrorXButton.setEnabled(False)
		self.mirrorXButton.setText("Mirror Horizontally")
		self.mirrorXButton.clicked.connect(self.mirrorX)
		# container to change video speed
		self.speedButton = QPushButton()
		self.speedButton.setEnabled(False)
		self.speedButton.setText("Change Speed")		
		self.speedButton.clicked.connect(self.changeSpeed)
		self.startInput = QLineEdit(placeholderText="start time")
		self.endInput = QLineEdit(placeholderText="end time")
		self.speedInput = QLineEdit(placeholderText="speed")

		speedlayout = QHBoxLayout()
		speedlayout.addWidget(self.startInput)
		speedlayout.addWidget(self.endInput)
		speedlayout.addWidget(self.speedInput)
		speedlayout.addWidget(self.speedButton)


		
		self.editButton3 = QPushButton()
		self.editButton3.setEnabled(False)
		self.editButton3.setText("Option 3")
		
	

		# area to edit vidwo
		editinglayout = QVBoxLayout()
		editinglayout.addWidget(self.mirrorXButton)
		editinglayout.addLayout(speedlayout)
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
		self.setplayer(self.oldvideoWidget, self.fname[0])
		self.setEditingBtnActive()

	# set buttons for editing active
	def setEditingBtnActive(self): 
		self.mirrorXButton.setEnabled(True)
		self.speedButton.setEnabled(True)
		self.editButton3.setEnabled(True)

	# give player widgets a player instance 
	def setplayer(self, widget, resource):
		self.player = QMediaPlayer()
		self.player.setSource(QUrl.fromLocalFile(resource))
		self.player.setVideoOutput(widget)
		self.audioOutput = QAudioOutput()
		self.player.setAudioOutput(self.audioOutput)
		self.audioOutput.setVolume(100)
	
	# play original video 
	def playold(self) : 
		if self.player.isPlaying():
			self.player.pause()
			self.oldplayButton.setText("Play")
		else :
			self.player.play()
			self.oldplayButton.setText("Pause")
	# play edited vidwo
	def playnew(self) : 
		if self.player.isPlaying():
			self.player.pause()
			self.newplayButton.setText("Play")
		else :
			self.player.play()
			self.newplayButton.setText("Pause")
	# show edited video
	def showNewVideo(self, extension) : 
		filetype = self.filename.split(".")[-1]
		self.setplayer(self.newvideoWidget, self.filename[:-(len(filetype)+1)] + extension + "." + filetype) 
		self.newplayButton.setEnabled(True)
		
	# mirror video horizontally 
	def mirrorX(self) : 
		# to fit media_editing.py 
		os.system("python3 media_editing.py -path " + self.filepath + " -name " + self.filename + " -mirrorX ./")
		# pass new video to player widget 
		self.showNewVideo("_MIRROR_X")

	# change speed of video section
	def changeSpeed(self) : 
		os.system("python3 media_editing.py -path " + self.filepath + " -name " + self.filename + " -speedChange " + self.startInput.text() + " " + self.endInput.text() + " " + self.speedInput.text() +  " ./")
		# pass new video to player widget 
		self.showNewVideo("_SPEEDx" + self.speedInput.text())

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


# window for statistical analysis
class StatAnaWindow(QMainWindow):

	def __init__(self):
		super(StatAnaWindow, self).__init__()

		self.setWindowTitle("Statistical Analysis")
		self.setMinimumSize(QSize(400,600))

		statAnaBtn = QPushButton(self)
		statAnaBtn.setText("Analyse your data")

		layout = QHBoxLayout()

		layout.addWidget(statAnaBtn)
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)








################## main stream of the program #################
app = QApplication(sys.argv)

window = MainWindow()
window.show()



app.exec()