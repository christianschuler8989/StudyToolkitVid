import sys, os 
from media_editing import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtMultimediaWidgets import *
from PyQt6.QtMultimedia import *
# Christian joined the chat.
# Anran says hi. 

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



class MediaEditWindow(QMainWindow):
	def __init__(self):
		super(MediaEditWindow, self).__init__()

		self.setWindowTitle("Media Editing")
		self.setMinimumSize(QSize(1200,600))
		
		# import file button 
		mediaImportButton = MyButton("Import File", self.importfile, toSetEnabled=True)

		# set up workspace folder
		selectFolderButton = MyButton("Select Workspace Folder", self.selectFolder, toSetEnabled=True)

		# media players 
		self.oldPlayer = MediaPlayer() # it is a layout
		self.newPlayer = MediaPlayer()
		
		# import and display original video, select workspace folder
		oldvideolayout = QVBoxLayout()
		oldvideolayout.addWidget(selectFolderButton)
		oldvideolayout.addWidget(mediaImportButton)
		oldvideolayout.addLayout(self.oldPlayer)
		
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
		layout.addLayout(self.newPlayer)

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)
	# placeholder function, for no use
	def placeholder() : 
		pass 
	# select workspace folder
	def selectFolder(self) : 
		self.workspaceFolder = QFileDialog.getExistingDirectory(
			self,
			"Choose Workspace Directory", 
			"${HOME}",
			) + "/"

	# import file and give to media player, requires existing workspace folder
	def importfile(self):
		self.fname = QFileDialog.getOpenFileName(
			self,
			"Open File",
			self.workspaceFolder,
			"All Files (*);; Python Files (*.py);; PNG Files (*.png)",
		)
		self.oldPlayer.getInput(self.fname[0])
		# set all edit buttons active
		for button in self.editButtons : 
			button.setEnabled(True)
		# create editor
		self.editor = editing(self.fname[0], self.workspaceFolder)

		
	# mirror video horizontally 
	def mirrorX(self) : 
		self.editor.mirrorAtX()
		self.editor.saveClip("tempClip", self.workspaceFolder)
		self.newPlayer.getInput(self.workspaceFolder+"tempClip.mp4")


	# change speed of video section
	def changeSpeed(self) : 
		os.system("python3 media_editing.py -path " + self.inputPath + " -name " + self.filename + " -speedChange " + self.startInput.text() + " " + self.endInput.text() + " " + self.speedInput.text() +  " ./")
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

# the area with media player 
class MediaPlayer(QVBoxLayout) : 
	def __init__(self) : 
		super(MediaPlayer, self).__init__()
		# buttons and widgets to help layout 
		self.playButton = MyButton("Play", self.play)
		self.playerWidget = QVideoWidget()
		self.playerWidget.setMinimumWidth(400)
		self.playerWidget.show()
			
		self.addWidget(self.playerWidget)		
		self.addWidget(self.playButton)
	# click behavoir of the play button		
	def play(self) : 
		if self.player.isPlaying() :
			self.player.pause()
			self.playButton.setText("Play")
		else : 
			self.player.play()
			self.playButton.setText("Pause")
	# give widget a player instance
	def getInput(self,resource) : 
		# the actual player
		self.player = QMediaPlayer()
		# resource is the absolute path of the video
		self.player.setSource(QUrl.fromLocalFile(resource))
		self.player.setVideoOutput(self.playerWidget)
		self.audioOutput = QAudioOutput()
		self.player.setAudioOutput(self.audioOutput)
		self.audioOutput.setVolume(100)
		self.playButton.setEnabled(True)





	
	
	
	





################## main stream of the program #################
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()