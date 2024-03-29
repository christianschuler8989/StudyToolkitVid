# StudyToolkitVid - Graphical User Interface
# 
# Authors: Christian Schuler & Dominik Hauser & Anran Wang
################################################################################

import sys, os 
from media_editing import * 
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtMultimediaWidgets import *
from PyQt6.QtMultimedia import *
from setup import *
# Christian joined the chat.
# Anran says hi. 

class MainWindow(QMainWindow):

	def __init__(self):
		super(MainWindow, self).__init__()

		self.setWindowTitle("Study Toolkit Video")
		self.setMinimumSize(QSize(600,400))
		# Display project logo
		self.image_logo = QPixmap("./../images/logo.png") 
		self.image_logo = self.image_logo.scaled(330, 100, Qt.AspectRatioMode.KeepAspectRatio)
		self.label_logo = QLabel()
		self.label_logo.setPixmap(self.image_logo)

		# grid layout so much better! 
		layout = QGridLayout()

		# menu bars
		MyMenu(self, "StudyToolkit")

		# Layout - Row 1
		layout.addWidget(self.label_logo,1,3,2,2)

		# Layout - Row 2
		# buttons to do some general functions
		exampleButton = MyButton("Re-setup Examples", self.setupWorkplace, toSetEnabled=True)
		exampleButton.setStyleSheet('QPushButton {background-color: #737ca1;}')
		layout.addWidget(exampleButton,2,2,1,2)
		testButton = MyButton("Test Toolkit", toSetEnabled=True) # todo: link to implementation of testing
		testButton.setStyleSheet('QPushButton {background-color: #737ca1;}')
		layout.addWidget(testButton,2,4,1,2)
		
		# Layout - Row 3
		try : 
			self.projectFolder = os.path.abspath('..')+"/projects/" # current directory then projects
		except FileNotFoundError : 
			self.projectFolder = os.getcwd()+"/" # current directory
		self.projectButton = MyButton("Create Project", self.createProject) 
		self.projectButton.setStyleSheet('QPushButton {background-color: #a4e7f5;}')
		self.projectName = QLineEdit(placeholderText="project name")
		self.projectName.textChanged.connect(self.enableButton)
		layout.addWidget(self.projectName, 3,1,1,2)
		layout.addWidget(self.projectButton, 3,3,1,2)
		selProjectButton = MyButton("Select Project", self.selectProject, toSetEnabled=True)
		selProjectButton.setStyleSheet('QPushButton {background-color: #a4e7f5;}')
		layout.addWidget(selProjectButton, 3,5,1,2)

		# Layout - Row 4
		# buttons to open separate windows
		mediaEditButton = MyButton("Start Media Editing", self.openMediaEditWindow, toSetEnabled=True)
		mediaEditButton.setStyleSheet('QPushButton {background-color: #f87217;}')
		studyGenButton = MyButton("Start Study Generation", self.openStudyGenWindow, toSetEnabled=True)
		studyGenButton.setStyleSheet('QPushButton {background-color: #82d18b;}')
		statAnaButton = MyButton("Start Statistical Analysis", self.openStatAnaWindow, toSetEnabled=True)
		statAnaButton.setStyleSheet('QPushButton {background-color: #897bff;}')
		# layout for area to open corresponding windows 
		# usage: addWidget(QWidget *widget, int fromRow, int fromColumn, int rowSpan, int columnSpan, Qt::Alignment alignment = Qt::Alignment())
		layout.addWidget(mediaEditButton, 4, 1, 1, 2)
		layout.addWidget(studyGenButton, 4, 3, 1, 2)
		layout.addWidget(statAnaButton, 4, 5, 1, 2)

		
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

	# create project button is only enabled if project name is not empty
	def enableButton(self) : 
		if not self.projectName.text() == "" : 
			self.projectButton.setEnabled(True)
		else : 
			self.projectButton.setEnabled(False)
	# create project folder
	def createProject(self) : 
		# select location for projects 
		try : 
			self.projectFolder = QFileDialog.getExistingDirectory(
				self,
				"Choose Project Location", 
				"${PWD}",
				) + "/" + self.projectName.text()
			os.mkdir(self.projectFolder)
		except: 
			msg=QMessageBox()
			msg.setText("Please select project location! ")
			msg.exec()

	# select existing project
	def selectProject(self) : 
		self.projectFolder = QFileDialog.getExistingDirectory(
				self,
				"Choose Project", 
				"${PWD}",
				) + "/" 
	
	def setupWorkplace(self) : 
		setupWorkplace()
		msg = QMessageBox()
		msg.setText("Done! ")
		msg.exec()
	

	def openMediaEditWindow(self):
		self.w = MediaEditWindow(self.projectFolder)
		self.w.show()

	def openStudyGenWindow(self):
		self.w = StudyGenWindow(self.projectFolder)
		self.w.show()

	def	openStatAnaWindow(self) : 
		self.w = StatAnaWindow(self.projectFolder)
		self.w.show()



class MediaEditWindow(QMainWindow):
	def __init__(self, projectFolder):
		super(MediaEditWindow, self).__init__()

		MyMenu(self, "MediaEdit")

		self.setWindowTitle("Media Editing")
		self.setMinimumSize(QSize(1200,600))
		

		# set up workspace folder - this can be considered to be the "root" of the project
		self.workspaceFolder = projectFolder
		selectFolderButton = MyButton("Change Project Location", self.selectFolder, toSetEnabled=True)

		# current mode of toolkit (important for location temporary files: eg. studySetup = "studySetup/temp/"
		self.mode = "mediaEditing" 
		#self.mode = "studySetup" 
		#self.mode = "statisticalAnalysis" 
		self.tempDir = self.workspaceFolder+self.mode+"/temp/"

		# import file button - default locations depending on the current mode: e.g. media_editing = "mediaEditing/input/"
		# self.fname = "${HOME}"
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
		saveFrameAtButton = MyButton("Save Frame", self.saveFrameAt, self.areaEditButtons)
		self.frametime = QLineEdit(placeholderText="time of frame")
		self.framename = QLineEdit(placeholderText="name of frame")
		saveFrameLayout = QHBoxLayout()
		saveFrameLayout.addWidget(self.frametime)
		saveFrameLayout.addWidget(self.framename)
		saveFrameLayout.addWidget(saveFrameAtButton)
		editLayouts.append(saveFrameLayout)

		# area to save all frames into a given folder
		saveFrameFolderButton = MyButton("Choose Directory to Save All Frames", self.selectFramesFolder, self.areaEditButtons)
		saveFramesButton = MyButton("Save All Frames", self.saveFrames, self.areaEditButtons)
		saveFramesLayout = QHBoxLayout()
		saveFramesLayout.addWidget(saveFrameFolderButton)
		saveFramesLayout.addWidget(saveFramesButton)
		editLayouts.append(saveFramesLayout)

		# area to delete a frame at given time
		deleteFrameAtButton = MyButton("Delete Frame with Audio", self.deleteFrameSync, self.areaEditButtons)
		self.delFrametime = QLineEdit(placeholderText="time of frame")
		delFrameLayout = QHBoxLayout()
		delFrameLayout.addWidget(self.delFrametime)
		delFrameLayout.addWidget(deleteFrameAtButton)
		editLayouts.append(delFrameLayout)

		# area to insert a selected frame at given time
		selectFrameButton = MyButton("Select Frame File", self.selectFrame, self.areaEditButtons)
		self.insertFrameTime = QLineEdit(placeholderText="time of frame")
		# button to insert frame at time
		insertFrameAtButton = MyButton("Insert Frame", self.insertFrameAt, self.areaEditButtons)
		insertFrameLayout = QHBoxLayout()
		insertFrameLayout.addWidget(selectFrameButton)
		insertFrameLayout.addWidget(self.insertFrameTime)
		insertFrameLayout.addWidget(insertFrameAtButton)
		editLayouts.append(insertFrameLayout)
		
		# area to make video from frames with given fps then save to workspace
		self.fps = QLineEdit(placeholderText="fps")
		# button to make video from frames
		makeVideoFromFramesButton = MyButton("Make Video From Frames", self.makeVideoFromFrames, self.areaEditButtons)		
		makeVideoLayout = QHBoxLayout()
		makeVideoLayout.addWidget(self.fps)
		makeVideoLayout.addWidget(makeVideoFromFramesButton)
		editLayouts.append(makeVideoLayout)

	
		# area to edit video
		upEditLayout = QHBoxLayout()
		for button in self.singleEditButtons : 
			upEditLayout.addWidget(button)
		midEditLayout = QHBoxLayout()
		sep = 3
		for layout in editLayouts[:sep] : 
			midEditLayout.addLayout(layout)
		downEditLayout = QHBoxLayout()
		for layout in editLayouts[sep:] : 
			downEditLayout.addLayout(layout)
		editinglayout = QVBoxLayout()
		editinglayout.addLayout(upEditLayout)
		editinglayout.addLayout(midEditLayout)
		editinglayout.addLayout(downEditLayout)

		# undo button
		self.undoButton = MyButton("Undo", self.undoGUI)
		# save button
		self.saveButton = MyButton("Save", self.save)

		# area to display new video, undo up to 5 actions and save video
		newvideoLayout = QVBoxLayout()
		newvideoLayout.addWidget(self.undoButton)
		newvideoLayout.addWidget(self.saveButton)
		newvideoLayout.addLayout(self.newPlayer)

		# upper half of main window
		upLayout = QHBoxLayout()
		upLayout.addLayout(oldvideoLayout)
		upLayout.addLayout(newvideoLayout)
		# main window layout
		layout = QVBoxLayout()
		layout.addLayout(upLayout)
		layout.addLayout(editinglayout)

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

	# select workspace folder
	def selectFolder(self) : 
		self.workspaceFolder = QFileDialog.getExistingDirectory(
			self,
			"Choose Workspace Directory", 
			"${PWD}",
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
		try : 
			self.editor = editing(self.fname[0], self.workspaceFolder)
		except : 
			self.popMsg("Please select a file! ")


	# save clip and give as input to video player
	def updateVideo(self) : 
		self.editor.saveClip("tempClip")
		# for the followinhg line to work you need to also write the file with the above line to the corresponding location
		# self.newPlayer.getInput(self.workspaceFolder+self.mode+"/temp/tempClip.mp4")
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
		try : 
			self.editor.changeSpeed(float(self.speedInput.text()), float(self.startInput.text()), float(self.endInput.text()))
			self.updateVideo()
		except ValueError : 
			self.popMsg("Invalid Input! ")
	# cut video
	def cutVideo(self): 
		try : 
			self.editor.cut(float(self.startCut.text()), float(self.endCut.text()))
			self.updateVideo()
		except ValueError : 
			self.popMsg("Invalid Input! ")
	# save one frame at time give name
	def saveFrameAt(self): 
		try: 
			self.editor.saveFrame(self.frametime.text(), self.framename.text())
			self.newPlayer.getInput(self.workspaceFolder+self.framename.text()+".png")
		except ValueError : 
			self.popMsg("Invalid Input! ")

	# select folder to save all frames
	def selectFramesFolder(self) : 
		self.saveFrameFolder = QFileDialog.getExistingDirectory(self, "Choose Directory to Save All Frames", "${HOME}", ) + "/"
	# save frames to the selected folder
	def saveFrames(self) : 
		try : 
			self.editor.saveAllFrames(self.saveFrameFolder)
		except : 
			self.popMsg("Please select a folder to save the frames! ")

	# select a frame file
	def selectFrame(self) : 
		self.framepath = QFileDialog.getOpenFileName(
			self,
			"Select Frame",
			self.workspaceFolder,
			"All Files (*);; Python Files (*.py);; PNG Files (*.png)",
		)
	# select frame and insert to given time
	def insertFrameAt(self) : 
		try : 
			self.editor.insertFrame(self.framepath, self.insertFrameTime.text())
			self.updateVideo()
		except : 
			self.popMsg("Please select a frame file and input a time to insert the frame!")

	# make video from frames and save it in workspace
	def makeVideoFromFrames(self) : 
		framefolder = QFileDialog.getExistingDirectory(
			self,
			"Choose Directory Containing All Frames", 
			self.workspaceFolder,
			) + "/"
		try : 
			self.editor.makeVideoFromFrames(framefolder, self.fps.text())
			self.editor.saveClip("videoFrom"+self.framepath[:-1].split("/")[-1])
			self.updateVideo()
		except: 
			self.popMsg("Please select a folder containing all frame files and input a valid fps!")

	# undo up to 5 actions
	def undoGUI(self): 
		self.editor.undo()
		self.updateVideo()
	# save video
	def save(self) : 
		outputPath = QFileDialog.getSaveFileName(self,"Save File", self.workspaceFolder)
		self.editor.saveClip(outputPath[0].split("/")[-1], self.workspaceFolder)

	# delete a frame with its audio 
	def deleteFrameSync(self) : 
		try: 
			self.editor.deleteFrameSynchronous(float(self.delFrametime.text()))
			self.updateVideo()
		except ValueError : 
			self.popMsg("Invalid Input! ")

	# pop an error message 
	def popMsg(self, msg) : 
		self.msgBox = QMessageBox()
		self.msgBox.setText(msg)
		self.msgBox.exec()

# window to generate studies
class StudyGenWindow(QMainWindow):

	def __init__(self, projectFolder):
		super(StudyGenWindow, self).__init__()
		self.projectFolder = projectFolder

		MyMenu(self, "StudyGeneration")

		self.setWindowTitle("Study Generation")
		self.setMinimumSize(QSize(600,400))

		# current mode of toolkit (important for location temporary files: eg. studySetup = "studySetup/temp/"
		#self.mode = "mediaEditing" 
		self.mode = "studySetup" 
		#self.mode = "statisticalAnalysis" 
		# self.tempDir = self.workspaceFolder+self.mode+"/temp/" # anran: this line leads to error!!!

		# reference: https://stackoverflow.com/questions/72155657/mouseclick-event-on-pyqt-folder-tree
		# tree view of project folder
		model = QFileSystemModel()
		tree = QTreeView()
		tree.setModel(model)
		tree.setRootIndex(model.setRootPath(self.projectFolder))
		
		fileTreeLayout = QHBoxLayout() # Left side
		fileTreeLayout.addWidget(tree)

		userInputLayout = QVBoxLayout() # Middle side

		self.studyName = QLineEdit(placeholderText="Study Name") # String
		userInputLayout.addWidget(self.studyName)
		self.configName = QLineEdit(placeholderText="Config Name") # String
		userInputLayout.addWidget(self.configName)
		self.studyUrl = QLineEdit(placeholderText="Study URL") # String (url)
		userInputLayout.addWidget(self.studyUrl)
		self.studyLanguage = QLineEdit(placeholderText="Study Language") # String
		userInputLayout.addWidget(self.studyLanguage)
		self.beaqleServiceUrl = QLineEdit(placeholderText="Beaqle Service URL") # String (url)
		userInputLayout.addWidget(self.beaqleServiceUrl)
		self.supervisorContact = QLineEdit(placeholderText="Supervisor Contact") # String (mail)
		userInputLayout.addWidget(self.supervisorContact)

		self.testsetSize = QLineEdit(placeholderText="Testset Size") # Integer
		userInputLayout.addWidget(self.testsetSize)
		self.trialSize = QLineEdit(placeholderText="Trial Size") # Integer
		userInputLayout.addWidget(self.trialSize)
		self.rateMinValue = QLineEdit(placeholderText="Rate Min Value") # Integer
		userInputLayout.addWidget(self.rateMinValue)
		self.rateMaxValue = QLineEdit(placeholderText="Rate Max Value") # Integer
		userInputLayout.addWidget(self.rateMaxValue)
		self.rateDefaultValue = QLineEdit(placeholderText="Rate Default Value") # Integer
		userInputLayout.addWidget(self.rateDefaultValue)
		self.anchorsNumber = QLineEdit(placeholderText="Anchors Number") # Integer
		userInputLayout.addWidget(self.anchorsNumber)
		self.maxTestsPerRun = QLineEdit(placeholderText="Max Tests Per Run") # Integer
		userInputLayout.addWidget(self.maxTestsPerRun)

		userChecksLayout = QVBoxLayout() # Right side
		self.showFileIds = QLineEdit(placeholderText="Show File ID") # Boolean
		userChecksLayout.addWidget(self.showFileIds)
		self.showResults = QLineEdit(placeholderText="Show Results") # Boolean
		userChecksLayout.addWidget(self.showResults)
		self.loopByDefault = QLineEdit(placeholderText="Loop By Default") # Boolean
		userChecksLayout.addWidget(self.loopByDefault)
		self.enableABLoop = QLineEdit(placeholderText="Enable AB Loop") # Boolean
		userChecksLayout.addWidget(self.enableABLoop)
		self.enableOnlineSubmission = QLineEdit(placeholderText="Enable Online Submission") # Boolean
		userChecksLayout.addWidget(self.enableOnlineSubmission)
		self.randomizeTestOrder = QLineEdit(placeholderText="Randomize Test Order") # Boolean
		userChecksLayout.addWidget(self.randomizeTestOrder)
		self.requireMaxRating = QLineEdit(placeholderText="Require Max Rating") # Boolean
		userChecksLayout.addWidget(self.requireMaxRating)

		layout = QVBoxLayout() # Outer Window "Layout holder"
		layoutBox = QHBoxLayout()
		layout.addLayout(layoutBox)
		layoutBox.addLayout(fileTreeLayout)
		layoutBox.addLayout(userInputLayout)
		layoutBox.addLayout(userChecksLayout)

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

		studyGenButton = QPushButton(self)
		studyGenButton.setText("Generate your study")
		layout.addWidget(studyGenButton)


# window for statistical analysis
class StatAnaWindow(QMainWindow):

	def __init__(self, projectFolder):
		super(StatAnaWindow, self).__init__()
		self.projectFolder = projectFolder

		MyMenu(self, "StatAnalysis")

		self.setWindowTitle("Statistical Analysis")
		self.setMinimumSize(QSize(400,600))

		# current mode of toolkit (important for location temporary files: eg. studySetup = "studySetup/temp/"
		#self.mode = "mediaEditing" 
		#self.mode = "studySetup" 
		self.mode = "statisticalAnalysis" 
		# self.tempDir = self.workspaceFolder+self.mode+"/temp/" # anran: this line leads to error!!!

		model = QFileSystemModel()
		tree = QTreeView()
		tree.setModel(model)
		tree.setRootIndex(model.setRootPath(self.projectFolder))
		
		fileTreeLayout = QHBoxLayout() # Left side
		fileTreeLayout.addWidget(tree)
		
		userInputLayout = QVBoxLayout() # Middle side

		exploreDataButton = QPushButton(self)
		exploreDataButton.setText("Explore your data")
		userInputLayout.addWidget(exploreDataButton)

		exploreResultsButton = QPushButton(self)
		exploreResultsButton.setText("Explore your results")
		userInputLayout.addWidget(exploreResultsButton)

		listeningpanelQuantitativeButton = QPushButton(self)
		listeningpanelQuantitativeButton.setText("Quantitative Listeningpanel Analysis")
		userInputLayout.addWidget(listeningpanelQuantitativeButton)

		listeningpanelQualitativeButton = QPushButton(self)
		listeningpanelQualitativeButton.setText("Qualitative Listeningpanel Analysis")
		userInputLayout.addWidget(listeningpanelQualitativeButton)

		checkAnovaButton = QPushButton(self)
		checkAnovaButton.setText("Check ANOVA requirements")
		userInputLayout.addWidget(checkAnovaButton)

		runAnovaButton = QPushButton(self)
		runAnovaButton.setText("Run ANOVA Analysis")
		userInputLayout.addWidget(runAnovaButton)

		runKruskalwallisButton = QPushButton(self)
		runKruskalwallisButton.setText("Run Kruskal-Wallis Analysis")
		userInputLayout.addWidget(runKruskalwallisButton)

		runWilcoxButton = QPushButton(self)
		runWilcoxButton.setText("Run Wilcox Analysis")
		userInputLayout.addWidget(runWilcoxButton)

		layout = QVBoxLayout() # Outer Window "Layout holder"
		layoutBox = QHBoxLayout()
		layout.addLayout(layoutBox)
		layoutBox.addLayout(fileTreeLayout)
		layoutBox.addLayout(userInputLayout)

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)

		analysisSaveButton = QPushButton(self)
		analysisSaveButton.setText("Save Statistical Analysis Visualisations")
		layout.addWidget(analysisSaveButton)


# helper class for buttons in the video editing window
class MyButton(QPushButton) : 
	def __init__(self, text, function=None, toAppend=[], toSetEnabled=False) : 
		super(QPushButton, self).__init__()
		self.setEnabled(toSetEnabled)
		self.setText(text)
		if not function == None: 
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


# menu bars
def MyMenu(self, name) : 
	bar = self.menuBar() 
	tk = bar.addMenu(name)
	save = QAction("Close",self)
	save.setShortcut("Ctrl+W")
	tk.addAction(save)
	quit = QAction("Quit",self) 
	tk.triggered[QAction].connect(self.close)


################## main stream of the program #################
def main():
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()
	# app.setActiveWindow(window)
	# window.activateWindow()

	# check if project folder is empty
	path = "../projects"
	try : 
		dir = os.listdir(path) 
	except FileNotFoundError : 
		dir = []
	# if empty them pop up a window asking whether to set up examples
	if len(dir) == 0 or len(dir) == 1 and dir[0] == ".DS_Store": # .ds_store is always there for macos
		msgBox=QMessageBox()
		msgBox.setText("Set up example project? ")
		msgBox.setInformativeText("Welcome to the StudyToolkitVid! Seems like you are using it for the first time, you can set up an example project to test it out! ")
		yes = MyButton("Yes", setupWorkplace, toSetEnabled=True)
		no = MyButton("No", toSetEnabled=True)
		msgBox.addButton(yes, QMessageBox.ButtonRole.NoRole)
		msgBox.addButton(no, QMessageBox.ButtonRole.YesRole)
		msgBox.show()

	app.exec()



if __name__ == "__main__":
	main()
	

