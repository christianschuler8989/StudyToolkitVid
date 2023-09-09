import sys, os 
from media_editing import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtMultimediaWidgets import *
from PyQt6.QtMultimedia import *
# Christian joined the chat.

class MainWindow(QMainWindow):

	def __init__(self):
		super(MainWindow, self).__init__()

		self.setWindowTitle("Study Tool Kit")
		self.setMinimumSize(QSize(600,400))

		mediaEditButton = QPushButton(self)
		mediaEditButton.setText("Media Editing")
		mediaEditButton.clicked.connect(self.openMediaEditWindow)

		studyGenButton = QPushButton(self)
		studyGenButton.setText("Study Generation")
		studyGenButton.clicked.connect(self.openStudyGenWindow)

		statAnaButton = QPushButton(self)
		statAnaButton.setText("Statistical Analysis")
		statAnaButton.clicked.connect(self.openStatAnaWindow)

		layout = QHBoxLayout()

		layout.addWidget(mediaEditButton)
		layout.addWidget(studyGenButton)
		layout.addWidget(statAnaButton)
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

# helper class for buttons in the video editing window
class MyButton(QPushButton) : 
	def __init__(self, text, toAppend=[], toSetEnabled=False) : 
		super(QPushButton, self).__init__()
		self.setEnabled(toSetEnabled)
		self.deleteFrameButton.setText(text)
		toAppend.append(self)
	def __init__(self, text, function, toAppend=[], toSetEnabled=False) : 
		super(QPushButton, self).__init__()
		self.setEnabled(toSetEnabled)
		self.setText(text)
		self.clicked.connect(function)
		toAppend.append(self)



class MediaEditWindow(QMainWindow):
	def __init__(self):
		super(MediaEditWindow, self).__init__()

		self.setWindowTitle("Media Editing")
		self.setMinimumSize(QSize(1200,600))
		
		# import file button 
		mediaImportButton = MyButton("Import File", self.importfile, toSetEnabled=True)

		# set up workspace folder
		selectFolderButton = MyButton("Select Workspace Folder", self.selectFolder, toSetEnabled=True)

		# media player 
		self.oldvideoWidget = QVideoWidget()
		self.oldvideoWidget.setMinimumWidth(400)
		self.oldvideoWidget.show()
		self.newvideoWidget = QVideoWidget()
		self.newvideoWidget.setMinimumWidth(400)
		self.newvideoWidget.show()
		
		self.oldplayButton = MyButton("Play", self.playold)
		self.newplayButton = MyButton("Play", self.playnew)

		# import and display original video, select workspace folder
		oldvideolayout = QVBoxLayout()
		oldvideolayout.addWidget(selectFolderButton)
		oldvideolayout.addWidget(mediaImportButton)
		oldvideolayout.addWidget(self.oldvideoWidget)
		oldvideolayout.addWidget(self.oldplayButton)
		# display new edited video
		newvideolayout = QVBoxLayout()
		newvideolayout.addWidget(self.newvideoWidget)
		newvideolayout.addWidget(self.newplayButton)
		
		# a list for buttons to edit videos
		self.editButtons = []
		# button to mirror horizontally
		mirrorXButton = MyButton("Mirror Horizontally", self.mirrorX, self.editButtons)
		# button to mirror vertically
		mirrorYButton = MyButton("Mirror Vertically", self.placeholder, self.editButtons)
		
		# area to change video speed
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

		# button to save all frames
		saveFrameButton = MyButton("Save All Frames", self.placeholder, self.editButtons)
		# button to delete a frame
		deleteFrameButton = MyButton("Delete Frame", self.placeholder, self.editButtons)
		# button to extract an occasion
		extractOccasionButton = MyButton("Extract Occasion", self.placeholder, self.editButtons)
		# button to concatenating audios
		concatAudioButton = MyButton("Concatenate Audios", self.placeholder, self.editButtons)
		# button to save frame at time
		saveFrameAtButton = MyButton("Save Frame At: ", self.placeholder, self.editButtons)
		# button to delete frame at time
		deleteFrameAtButton = MyButton("Delete Frame At: ", self.placeholder, self.editButtons)
		# button to insert frame at time
		insertFrameAtButton = MyButton("Insert Frame At: ", self.placeholder, self.editButtons)
		# button to make video from frames
		makeVideoFromFramesButton = MyButton("Make Video From Frames", self.placeholder, self.editButtons)
	

		# area to edit vidwo
		editinglayout = QVBoxLayout()
		for button in self.editButtons : 
			if button != self.speedButton : 
				editinglayout.addWidget(button)
		editinglayout.addLayout(speedlayout)
		


		# main window layout
		layout = QHBoxLayout()
		layout.addLayout(oldvideolayout)
		layout.addLayout(editinglayout)
		layout.addLayout(newvideolayout)

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)
	# placeholder function, for no use
	def placeholder() : 
		pass 

	# import file and give to media player, requires existing workspace folder
	def importfile(self):
		self.fname = QFileDialog.getOpenFileName(
			self,
			"Open File",
			self.workspaceFolder[0],
			"All Files (*);; Python Files (*.py);; PNG Files (*.png)",
		)
		self.filename = self.fname[0].split("/")[-1]
		self.filepath = self.fname[0][:-len(self.filename)]
		self.oldplayButton.setEnabled(True)
		self.setplayer(self.oldvideoWidget, self.fname[0])
		# set all edit buttons active
		for button in self.editButtons : 
			button.setEnabled(True)
		self.editor = editing(self.fname[0], workspaceFolder)

	def selectFolder(self) : 
		self.workspaceFolder = QFileDialog.getExistingDirectory(
			self,
			"Choose Workspace Directory", 
			"${HOME}",
			)

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
		self.showNewVideo("-MIRROR_X")

	# change speed of video section
	def changeSpeed(self) : 
		os.system("python3 media_editing.py -path " + self.filepath + " -name " + self.filename + " -speedChange " + self.startInput.text() + " " + self.endInput.text() + " " + self.speedInput.text() +  " ./")
		# pass new video to player widget 
		self.showNewVideo("-SPEEDx" + str(float(self.speedInput.text())))

# window to generate studies
class StudyGenWindow(QMainWindow):

	def __init__(self):
		super(StudyGenWindow, self).__init__()

		self.setWindowTitle("Study Generation")
		self.setMinimumSize(QSize(400,600))

		studyGenButton = QPushButton(self)
		studyGenButton.setText("Generate your study")

		layout = QHBoxLayout()

		layout.addWidget(studyGenButton)
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)


# window for statistical analysis
class StatAnaWindow(QMainWindow):

	def __init__(self):
		super(StatAnaWindow, self).__init__()

		self.setWindowTitle("Statistical Analysis")
		self.setMinimumSize(QSize(400,600))

		statAnaButton = QPushButton(self)
		statAnaButton.setText("Analyse your data")

		layout = QHBoxLayout()

		layout.addWidget(statAnaButton)
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)








################## main stream of the program #################
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()