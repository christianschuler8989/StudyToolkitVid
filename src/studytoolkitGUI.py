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
		
		# set up workspace folder
		self.workspaceFolder = "./"
		selectFolderButton = MyButton("Select Workspace Folder", self.selectFolder, toSetEnabled=True)

		# import file button 
		mediaImportButton = MyButton("Import File", self.importfile, toSetEnabled=True)
		mediaImportButton.setIcon(QIcon("open.xpm"))

		# media players 
		self.oldPlayer = MediaPlayer() # it is a layout
		self.newPlayer = MediaPlayer()
		
		# import and display original video, select workspace folder
		oldvideoLayout = QVBoxLayout()
		oldvideoLayout.addWidget(selectFolderButton)
		oldvideoLayout.addWidget(mediaImportButton)
		oldvideoLayout.addLayout(self.oldPlayer)
		
		# a list for buttons to edit videos that appear by themselves
		self.singleEditButtons = []
		# a list for buttons to edit videos that appear within an layout area
		self.areaEditButtons = []
		# a list for layouts to manage edit buttons that have input textx
		editLayouts = []

		# button to mirror horizontally
		mirrorXButton = MyButton("Mirror Horizontally", self.mirrorX, self.singleEditButtons)
		# button to mirror vertically
		mirrorYButton = MyButton("Mirror Vertically", self.mirrorY, self.singleEditButtons)
		
		# area to change video speed
		speedButton = MyButton("Change Speed", self.changeSpeed, self.areaEditButtons)
		self.startInput = QLineEdit(placeholderText="start time")
		self.endInput = QLineEdit(placeholderText="end time")
		self.speedInput = QLineEdit(placeholderText="speed")
		speedLayout = QHBoxLayout()
		speedLayout.addWidget(self.startInput)
		speedLayout.addWidget(self.endInput)
		speedLayout.addWidget(self.speedInput)
		speedLayout.addWidget(speedButton)
		editLayouts.append(speedLayout)

		# area to cut video
		cutButton = MyButton("Cut", self.cutVideo, self.areaEditButtons)
		self.startCut = QLineEdit(placeholderText="start time")
		self.endCut = QLineEdit(placeholderText="end time")
		cutLayout = QHBoxLayout()
		cutLayout.addWidget(self.startCut)
		cutLayout.addWidget(self.endCut)
		cutLayout.addWidget(cutButton)
		editLayouts.append(cutLayout)

		# area to save a frame and give it a name
		saveFrameAtButton = MyButton("Save Frame At: ", self.saveFrameAt, self.areaEditButtons)
		self.frametime = QLineEdit(placeholderText="time of frame")
		self.framename = QLineEdit(placeholderText="name of frame")
		saveFrameLayout = QHBoxLayout()
		saveFrameLayout.addWidget(self.frametime)
		saveFrameLayout.addWidget(self.framename)
		saveFrameLayout.addWidget(saveFrameAtButton)
		editLayouts.append(saveFrameLayout)

		# area to save all frames into a given folder
		self.saveFrameFolder = self.workspaceFolder
		saveFrameFolderButton = MyButton("Choose Directory to Save All Frames", self.selectFramesFolder, self.areaEditButtons)
		saveFramesButton = MyButton("Save All Frames", self.saveFrames, self.areaEditButtons)
		saveFramesLayout = QHBoxLayout()
		saveFramesLayout.addWidget(saveFrameFolderButton)
		saveFramesLayout.addWidget(saveFramesButton)
		editLayouts.append(saveFramesLayout)



		# button to delete a frame
		deleteFrameButton = MyButton("Delete Frame", self.placeholder, self.singleEditButtons)
		# button to extract an occasion
		extractOccasionButton = MyButton("Extract Occasion", self.placeholder, self.singleEditButtons)
		# button to concatenating audios
		concatAudioButton = MyButton("Concatenate Audios", self.placeholder, self.singleEditButtons)
		# button to delete frame at time
		deleteFrameAtButton = MyButton("Delete Frame At: ", self.placeholder, self.singleEditButtons)
		# button to insert frame at time
		insertFrameAtButton = MyButton("Insert Frame At: ", self.placeholder, self.singleEditButtons)
		# button to make video from frames
		makeVideoFromFramesButton = MyButton("Make Video From Frames", self.placeholder, self.singleEditButtons)
	
		# area to edit vidwo
		editinglayout = QVBoxLayout()
		for button in self.singleEditButtons : 
			editinglayout.addWidget(button)
		for layout in editLayouts : 
			editinglayout.addLayout(layout)

		# undo button
		self.undoButton = MyButton("Undo", self.undoGUI)
		# save button
		self.saveButton = MyButton("Save", self.save)

		# area to display new video, undo up to 5 actions and save video
		newvideoLayout = QVBoxLayout()
		newvideoLayout.addLayout(self.newPlayer)
		newvideoLayout.addWidget(self.undoButton)
		newvideoLayout.addWidget(self.saveButton)

		# main window layout
		layout = QHBoxLayout()
		layout.addLayout(oldvideoLayout)
		layout.addLayout(editinglayout)
		layout.addLayout(newvideoLayout)

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
		for button in self.singleEditButtons + self.areaEditButtons: 
			button.setEnabled(True)
		# create editor
		self.editor = editing(self.fname[0], self.workspaceFolder)

	# save clip and give as input to video player
	def updateVideo(self) : 
		self.editor.saveClip("tempClip")
		self.newPlayer.getInput(self.workspaceFolder+"tempClip.mp4")
		self.undoButton.setEnabled(True)
		self.saveButton.setEnabled(True)
		
	# mirror video horizontally 
	def mirrorX(self) : 
		self.editor.mirrorAtX()
		self.updateVideo()

	def mirrorY(self) : 
		self.editor.mirrorAtY()
		self.updateVideo()

	# change speed of video section
	def changeSpeed(self) : 
		self.editor.changeSpeed(self.speedInput, self.startInput, self.endInput)
		self.updateVideo()
	# cut video
	def cutVideo(self): 
		self.editor.cut(self.startCut, self.endCut)
		self.updateVideo()
	# save one frame at time give name
	def saveFrameAt(self): 
		self.editor.saveFrame(self.frametime, self.framename)
		self.newPlayer.getInput(self.workspaceFolder+self.framename+".png")

	# select folder to save all frames
	def selectFramesFolder(self) : 
		self.saveFrameFolder = QFileDialog.getExistingDirectory(self, "Choose Directory to Save All Frames", "${HOME}", ) + "/"
	# save frames to the selected folder
	def saveFrames(self) : 
		self.editor.saveAllFrames(self.saveFrameFolder)

	# undo up to 5 actions
	def undoGUI(self): 
		self.editor.undo()
		self.updateVideo()
	# save video
	def save(self) : 
		outputPath = QFileDialog.getSaveFileName(self,"Save File", self.workspaceFolder)
		self.editor.saveClip(outputPath[0].split("/")[-1])

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