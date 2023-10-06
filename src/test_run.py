#
# 
# Authors: Christian Schuler & Dominik Hauser
################################################################################

import os
import shutil
import subprocess
from media_editing import * 
from study_setup import *
import sys

"""
Pipeline test class for development and bug-fixing.
"""
def main(testParts):
	current_working_directory = os.getcwd()
	print("Current Working Directory: " + current_working_directory)

	# Test: Part 1 Media Editing ##############################################
	###########################################################################
	if 1 in testParts:
		media_editing=True
		print("Start testing Media Editing:")

		# Necessary directory paths:
		test_media_directory = current_working_directory+"/../projects/exampleProject/mediaEditing"
		test_media_input = current_working_directory+"/../projects/exampleProject/mediaEditing/input"
		test_media_temp = current_working_directory+"/../projects/exampleProject/mediaEditing/temp"
		test_media_output = current_working_directory+"/../projects/exampleProject/mediaEditing/output"
		#print("Testing in Directory: " + test_media_directory) # Debugging

		# Create test protocol
		#try:
		#	with open(test_media_temp+'/test.txt', 'w') as f:
		#		f.write('Test Protocol!')
		#except FileNotFoundError:
		#	print("The media editing directory does not exist")



	# Test: Part 2 Study Setup ################################################
	###########################################################################
	if 2 in testParts:
		study_setup=True
		print("Start testing Study Setup:")
		# Necessary directory paths:
		test_study_directory = current_working_directory+"/../projects/exampleProject/studySetup"
		test_study_input = current_working_directory+"/../projects/exampleProject/studySetup/input"
		test_study_temp = current_working_directory+"/../projects/exampleProject/studySetup/temp"
		test_study_output = current_working_directory+"/../projects/exampleProject/studySetup/output"
		#print("Testing in Directory: " + test_study_directory) # Debugging

		# Create test protocol
		#try:
		#	with open(test_study_temp+'/test.txt', 'w') as f:
		#		f.write('Test Protocol!')
		#except FileNotFoundError:
		#	print("The study setup directory does not exist")



	# Test: Part 3 Statistical Analysis #######################################
	###########################################################################
	if 3 in testParts:
		statistical_analysis=True
		print("Start testing Statistical Analysis:")
		# Necessary directory paths:
		test_statistical_directory = current_working_directory+"/../projects/exampleProject/statisticalAnalysis"
		test_statistical_input = current_working_directory+"/../projects/exampleProject/statisticalAnalysis/input"
		test_statistical_temp = current_working_directory+"/../projects/exampleProject/statisticalAnalysis/temp"
		test_statistical_output = current_working_directory+"/../projects/exampleProject/statisticalAnalysis/output"
		#print("Testing in Directory: " + test_statistical_directory) # Debugging

		# Create test protocol
		#try:
		#	with open(test_statistical_temp+'/test.txt', 'w') as f:
		#		f.write('Test Protocol!')
		#except FileNotFoundError:
		#	print("The statistical analysis directory does not exist")



	# Pipeline-Test: Part 2 Study Setup #######################################
	###########################################################################
	if 7 in testParts:
		study_setup=True
		print("Start testing Study Setup:")
		# Necessary directory paths:
		test_study_directory = current_working_directory+"/../projects/exampleProject/studySetup"
		test_study_input = current_working_directory+"/../projects/exampleProject/studySetup/input"
		test_study_temp = current_working_directory+"/../projects/exampleProject/studySetup/temp"
		test_study_output = current_working_directory+"/../projects/exampleProject/studySetup/output"
		
		# Create a "study_setupper"
		study_setupper = setupping(test_study_input, test_study_temp, test_study_output)
		
		# Set study creation parameters
		study_setupper.setStudyParameters(trial_size=5, language="English")

		study_setupper.createStudy()

		#study_setupper.createTestset(test_study_temp, test_study_output, "my_testset")

		# Get names for all the existing excerpts from input
		#study_setupper.readDirectoryNamesFromInput(test_study_input)

		# Work through the entire input directory
		#study_setupper.processInputFolder(test_study_input, test_study_output)
		

	


	# Pipeline-Test: Preparing Part 2 Study Setup #############################
	###########################################################################
	if 8 in testParts:
		study_setup=True
		print("Prepare testing Study Setup:")
		# Necessary directory paths:
		test_study_directory = current_working_directory+"/../projects/exampleProject/studySetup"
		test_study_input = current_working_directory+"/../projects/exampleProject/studySetup/input"
		test_study_temp = current_working_directory+"/../projects/exampleProject/studySetup/temp"
		test_study_output = current_working_directory+"/../projects/exampleProject/studySetup/output"
		#print("Testing in Directory: " + test_study_directory) # Debugging

		# Create test protocol
		#try:
		#	with open(test_study_temp+'/test.txt', 'w') as f:
		#		f.write('Test Protocol!')
		#except FileNotFoundError:
		#	print("The study setup directory does not exist")
		
		# Using shutil to move all the previously (in 9) created media files
		os.mkdir("../projects/exampleProject/studySetup/input/lohse/")
		source_folder = "../projects/exampleProject/mediaEditing/output/lohse/"
		destination_folder = "../projects/exampleProject/studySetup/input/lohse/"
		for file_name in os.listdir(source_folder):
			# Construct full file path
			source = source_folder + file_name
			destination = destination_folder + file_name
			# Move only files
			if os.path.isfile(source):
				shutil.move(source, destination)
		print('Moved lohse example files.')	
		
		os.mkdir("../projects/exampleProject/studySetup/input/strong/")
		source_folder = "../projects/exampleProject/mediaEditing/output/strong/"
		destination_folder = "../projects/exampleProject/studySetup/input/strong/"
		for file_name in os.listdir(source_folder):
			# Construct full file path
			source = source_folder + file_name
			destination = destination_folder + file_name
			# Move only files
			if os.path.isfile(source):
				shutil.move(source, destination)
		print('Moved strong example files.')	

		os.mkdir("../projects/exampleProject/studySetup/input/go/")
		source_folder = "../projects/exampleProject/mediaEditing/output/go/"
		destination_folder = "../projects/exampleProject/studySetup/input/go/"
		for file_name in os.listdir(source_folder):
			# Construct full file path
			source = source_folder + file_name
			destination = destination_folder + file_name
			# Move only files
			if os.path.isfile(source):
				shutil.move(source, destination)
		print('Moved go example files.')	

		os.mkdir("../projects/exampleProject/studySetup/input/obama/")
		source_folder = "../projects/exampleProject/mediaEditing/output/obama/"
		destination_folder = "../projects/exampleProject/studySetup/input/obama/"
		for file_name in os.listdir(source_folder):
			# Construct full file path
			source = source_folder + file_name
			destination = destination_folder + file_name
			# Move only files
			if os.path.isfile(source):
				shutil.move(source, destination)
		print('Moved obama example files.')	


	# Pipeline-Test: Part 1 Media Editing #####################################
	###########################################################################
	if 9 in testParts:
		media_editing=True
		print("Start testing Media Editing:")

		# Necessary directory paths:
		test_media_directory = current_working_directory+"/../projects/exampleProject/mediaEditing"
		test_media_input = current_working_directory+"/../projects/exampleProject/mediaEditing/input"
		test_media_temp = current_working_directory+"/../projects/exampleProject/mediaEditing/temp"
		test_media_output = current_working_directory+"/../projects/exampleProject/mediaEditing/output"
		#print("Testing in Directory: " + test_media_directory) # Debugging

		# Create test protocol
		#try:
		#	with open(test_media_temp+'/test.txt', 'w') as f:
		#		f.write('Test Protocol!')
		#except FileNotFoundError:
		#	print("The media editing directory does not exist")

		# Working with TextGrids: #############################################

		# Issue with pathing due to "media_editing_command_based.py" adding a "./"... Because FUNNY!
		# → Need to start at "./" and go from there when defining path for these files!
		# just like this: 
		# lohse_media_file = "../projects/exampleProject/mediaEditing/input/lohse.mp4"
		# lohse_textgrid_file = "../projects/exampleProject/mediaEditing/input/lohse.TextGrid"

		# Internal method of "media_editing_command_based.py"
		# get_text_grid_information(clip, text_of_interest, path_textgrid, path_save)
		#get_text_grid_information(lohse_media_file, lohse_text, lohse_textgrid_file, test_media_temp)
		# External method of "media_editing_command_based.py"
		#python media_editing_command_based.py -name ./../projects/exampleProject/mediaEditing/input/lohse.mp4 -textGridInformation aI ./../projects/exampleProject/mediaEditing/input/lohse.TextGrid ./../projects/exampleProject/mediaEditing/temp/


		# For each of the example files: 
		## 0. Setup an editor 
		## 1. Get information from correspoding TextGrid
		## 2. Extract described sequences
		## 3. Modify extracts in various forms
		## 4. Re-combine the extracted sequences to "full" media files again
		## 5. Resulting in test data for study, with recorded modification history
		## 6. Save test-items into the output directory of "mediaEditing"
		##########################################################################


		# Lohse (German)
		## 0. Setup an editor
		################################################
		lohse_media_file = "../projects/exampleProject/mediaEditing/input/lohse.mp4"
		lohse_textgrid_file = "../projects/exampleProject/mediaEditing/input/lohse.TextGrid"
		lohse_temp_dir = "../projects/exampleProject/mediaEditing/temp/lohse/"
		lohse_out_dir = "../projects/exampleProject/mediaEditing/output/lohse/"
		
		media_editor = editing(lohse_media_file, lohse_temp_dir)

		## 1. Get information from correspoding TextGrid
		################################################
		lohse_text_sound = "aI"
		lohse_text_word = "Name"
		
		### Get information about the sound "aI" and the word "Name" in media file "lohse.mp4"
		media_editor.getTextGridInformation(lohse_text_sound, lohse_textgrid_file, lohse_temp_dir)
		media_editor.getTextGridInformation(lohse_text_word, lohse_textgrid_file, lohse_temp_dir)

		## 2. Extract described sequences
		################################# 
		
		### Extract each "aI" and each "Name" in media file "lohse.mp4"
		media_editor.extractTextOccasionsFromGrid(lohse_text_word, lohse_textgrid_file, lohse_temp_dir+'/'+lohse_text_sound+'/', 'mp4')
		media_editor.extractTextOccasionsFromGrid(lohse_text_word, lohse_textgrid_file, lohse_temp_dir+'/'+lohse_text_word+'/')
		
		## TEMP to quickly get some files for Part 2
		### For the word
		# Copy the unmodified original file to output as hidden anchor
		media_editor._getClipFromPath(lohse_media_file)
		media_editor.saveClip("lohse-"+lohse_text_word, lohse_out_dir)

		# Involving mirroring at X
		media_editor.mirrorAtX()
		media_editor.saveClip("lohse-"+lohse_text_word+"-mirror_X", lohse_out_dir)
		
		media_editor.changeSpeed(0.50, 0.44712, 0.62712)
		media_editor.saveClip("lohse-"+lohse_text_word+"-mirror_X-speed_0050_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 0.44712, 0.62712)
		media_editor.saveClip("lohse-"+lohse_text_word+"-mirror_X-speed_0075_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 0.44712, 0.62712)
		media_editor.saveClip("lohse-"+lohse_text_word+"-mirror_X-speed_0150_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 0.44712, 0.62712)
		media_editor.saveClip("lohse-"+lohse_text_word+"-mirror_X-speed_0200_0_44712_0_62712", lohse_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 0.44712, 0.62712)
		#media_editor.saveClip("lohse-"+lohse_text_word+"-mirror_X-speed_0800_0_44712_0_62712", lohse_out_dir)

		# Involving mirroring at Y
		media_editor.undo() # Undo the speed change
		media_editor.undo() # Undo the mirror at X
		media_editor.mirrorAtY()
		media_editor.saveClip("lohse-"+lohse_text_word+"-mirror_Y", lohse_out_dir)

		media_editor.changeSpeed(0.50, 0.44712, 0.62712)
		media_editor.saveClip("lohse-"+lohse_text_word+"-mirror_Y-speed_0050_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 0.44712, 0.62712)
		media_editor.saveClip("lohse-"+lohse_text_word+"-mirror_Y-speed_0075_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 0.44712, 0.62712)
		media_editor.saveClip("lohse-"+lohse_text_word+"-mirror_Y-speed_0150_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 0.44712, 0.62712)
		media_editor.saveClip("lohse-"+lohse_text_word+"-mirror_Y-speed_0200_0_44712_0_62712", lohse_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 0.44712, 0.62712)
		#media_editor.saveClip("lohse-"+lohse_text_word+"-mirror_Y-speed_0800_0_44712_0_62712", lohse_out_dir)

		# Involving only speed change
		media_editor.undo() # Undo the speed change
		media_editor.undo() # Undo the mirror at Y

		media_editor.changeSpeed(0.50, 0.44712, 0.62712)
		media_editor.saveClip("lohse-"+lohse_text_word+"-speed_0050_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 0.44712, 0.62712)
		media_editor.saveClip("lohse-"+lohse_text_word+"-speed_0075_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 0.44712, 0.62712)
		media_editor.saveClip("lohse-"+lohse_text_word+"-speed_0150_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 0.44712, 0.62712)
		media_editor.saveClip("lohse-"+lohse_text_word+"-speed_0200_0_44712_0_62712", lohse_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 0.44712, 0.62712)
		#media_editor.saveClip("lohse-"+lohse_text_word+"-speed_0800_0_44712_0_62712", lohse_out_dir)	

		### For the sound
		# Copy the unmodified original file to output as hidden anchor
		media_editor.undo() # Undo the speed change
		media_editor.saveClip("lohse-"+lohse_text_sound, lohse_out_dir)

		# Involving mirroring at X
		media_editor.mirrorAtX()
		media_editor.saveClip("lohse-"+lohse_text_sound+"-mirror_X", lohse_out_dir)
		
		media_editor.changeSpeed(0.50, 1.82712, 1.89712)
		media_editor.saveClip("lohse-"+lohse_text_sound+"-mirror_X-speed_0050_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 1.82712, 1.89712)
		media_editor.saveClip("lohse-"+lohse_text_sound+"-mirror_X-speed_0075_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 1.82712, 1.89712)
		media_editor.saveClip("lohse-"+lohse_text_sound+"-mirror_X-speed_0150_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 1.82712, 1.89712)
		media_editor.saveClip("lohse-"+lohse_text_sound+"-mirror_X-speed_0200_0_44712_0_62712", lohse_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 1.82712, 1.89712)
		#media_editor.saveClip("lohse-"+lohse_text_sound+"-mirror_X-speed_0800_0_44712_0_62712", lohse_out_dir)

		# Involving mirroring at Y
		media_editor.undo() # Undo the speed change
		media_editor.undo() # Undo the mirror at X
		media_editor.mirrorAtY()
		media_editor.saveClip("lohse-"+lohse_text_sound+"-mirror_Y", lohse_out_dir)

		media_editor.changeSpeed(0.50, 1.82712, 1.89712)
		media_editor.saveClip("lohse-"+lohse_text_sound+"-mirror_Y-speed_0050_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 1.82712, 1.89712)
		media_editor.saveClip("lohse-"+lohse_text_sound+"-mirror_Y-speed_0075_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 1.82712, 1.89712)
		media_editor.saveClip("lohse-"+lohse_text_sound+"-mirror_Y-speed_0150_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 1.82712, 1.89712)
		media_editor.saveClip("lohse-"+lohse_text_sound+"-mirror_Y-speed_0200_0_44712_0_62712", lohse_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 1.82712, 1.89712)
		#media_editor.saveClip("lohse-"+lohse_text_sound+"-mirror_Y-speed_0800_0_44712_0_62712", lohse_out_dir)

		# Involving only speed change
		media_editor.undo() # Undo the speed change
		media_editor.undo() # Undo the mirror at Y

		media_editor.changeSpeed(0.50, 1.82712, 1.89712)
		media_editor.saveClip("lohse-"+lohse_text_sound+"-speed_0050_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 1.82712, 1.89712)
		media_editor.saveClip("lohse-"+lohse_text_sound+"-speed_0075_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 1.82712, 1.89712)
		media_editor.saveClip("lohse-"+lohse_text_sound+"-speed_0150_0_44712_0_62712", lohse_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 1.82712, 1.89712)
		media_editor.saveClip("lohse-"+lohse_text_sound+"-speed_0200_0_44712_0_62712", lohse_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 1.82712, 1.89712)
		#media_editor.saveClip("lohse-"+lohse_text_sound+"-speed_0800_0_44712_0_62712", lohse_out_dir)	


		## 3. Modify extracts in various forms
		######################################

		## 4. Re-combine the extracted sequences to "full" media files again
		####################################################################

		## 5. Resulting in test data for study, with recorded modification history
		##########################################################################

		## 6. Save test-items into the output directory of "mediaEditing"
		#################################################################

		

		# strong (German)
		## 0. Setup an editor
		################################################
		strong_media_file = "../projects/exampleProject/mediaEditing/input/strong.mp4"
		strong_textgrid_file = "../projects/exampleProject/mediaEditing/input/strong.TextGrid"
		strong_temp_dir = "../projects/exampleProject/mediaEditing/temp/strong/"
		strong_out_dir = "../projects/exampleProject/mediaEditing/output/strong/"
		
		media_editor = editing(strong_media_file, strong_temp_dir)

		## 1. Get information from correspoding TextGrid
		################################################
		strong_text_sound = "aI"
		strong_text_word = "Name"
		
		### Get information about the sound "aI" and the word "gemeinsam" in media file "strong.mp4"
		media_editor.getTextGridInformation(strong_text_sound, strong_textgrid_file, strong_temp_dir)
		media_editor.getTextGridInformation(strong_text_word, strong_textgrid_file, strong_temp_dir)

		## 2. Extract described sequences
		################################# 
		
		### Extract each "aI" and each "gemeinsam" in media file "strong.mp4"
		media_editor.extractTextOccasionsFromGrid(strong_text_word, strong_textgrid_file, strong_temp_dir+'/'+strong_text_sound+'/', 'mp4')
		media_editor.extractTextOccasionsFromGrid(strong_text_word, strong_textgrid_file, strong_temp_dir+'/'+strong_text_word+'/')
		
		## TEMP to quickly get some files for Part 2
		### For the word
		# Copy the unmodified original file to output as hidden anchor
		media_editor._getClipFromPath(strong_media_file)
		media_editor.saveClip("strong-"+strong_text_word, strong_out_dir)

		# Involving mirroring at X
		media_editor.mirrorAtX()
		media_editor.saveClip("strong-"+strong_text_word+"-mirror_X", strong_out_dir)
		
		media_editor.changeSpeed(0.50, 0.41712, 1.11712)
		media_editor.saveClip("strong-"+strong_text_word+"-mirror_X-speed_0050_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 0.41712, 1.11712)
		media_editor.saveClip("strong-"+strong_text_word+"-mirror_X-speed_0075_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 0.41712, 1.11712)
		media_editor.saveClip("strong-"+strong_text_word+"-mirror_X-speed_0150_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 0.41712, 1.11712)
		media_editor.saveClip("strong-"+strong_text_word+"-mirror_X-speed_0200_0_44712_0_62712", strong_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 0.41712, 1.11712)
		#media_editor.saveClip("strong-"+strong_text_word+"-mirror_X-speed_0800_0_44712_0_62712", strong_out_dir)

		# Involving mirroring at Y
		media_editor.undo() # Undo the speed change
		media_editor.undo() # Undo the mirror at X
		media_editor.mirrorAtY()
		media_editor.saveClip("strong-"+strong_text_word+"-mirror_Y", strong_out_dir)

		media_editor.changeSpeed(0.50, 0.41712, 1.11712)
		media_editor.saveClip("strong-"+strong_text_word+"-mirror_Y-speed_0050_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 0.41712, 1.11712)
		media_editor.saveClip("strong-"+strong_text_word+"-mirror_Y-speed_0075_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 0.41712, 1.11712)
		media_editor.saveClip("strong-"+strong_text_word+"-mirror_Y-speed_0150_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 0.41712, 1.11712)
		media_editor.saveClip("strong-"+strong_text_word+"-mirror_Y-speed_0200_0_44712_0_62712", strong_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 0.41712, 1.11712)
		#media_editor.saveClip("strong-"+strong_text_word+"-mirror_Y-speed_0800_0_44712_0_62712", strong_out_dir)

		# Involving only speed change
		media_editor.undo() # Undo the speed change
		media_editor.undo() # Undo the mirror at Y

		media_editor.changeSpeed(0.50, 0.41712, 1.11712)
		media_editor.saveClip("strong-"+strong_text_word+"-speed_0050_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 0.41712, 1.11712)
		media_editor.saveClip("strong-"+strong_text_word+"-speed_0075_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 0.41712, 1.11712)
		media_editor.saveClip("strong-"+strong_text_word+"-speed_0150_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 0.41712, 1.11712)
		media_editor.saveClip("strong-"+strong_text_word+"-speed_0200_0_44712_0_62712", strong_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 0.41712, 1.11712)
		#media_editor.saveClip("strong-"+strong_text_word+"-speed_0800_0_44712_0_62712", strong_out_dir)	

		### For the sound
		# Copy the unmodified original file to output as hidden anchor
		media_editor.undo() # Undo the speed change
		media_editor.saveClip("strong-"+strong_text_sound, strong_out_dir)

		# Involving mirroring at X
		media_editor.mirrorAtX()
		media_editor.saveClip("strong-"+strong_text_sound+"-mirror_X", strong_out_dir)
		
		media_editor.changeSpeed(0.50, 0.63712, 0.79712)
		media_editor.saveClip("strong-"+strong_text_sound+"-mirror_X-speed_0050_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 0.63712, 0.79712)
		media_editor.saveClip("strong-"+strong_text_sound+"-mirror_X-speed_0075_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 0.63712, 0.79712)
		media_editor.saveClip("strong-"+strong_text_sound+"-mirror_X-speed_0150_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 0.63712, 0.79712)
		media_editor.saveClip("strong-"+strong_text_sound+"-mirror_X-speed_0200_0_44712_0_62712", strong_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 0.63712, 0.79712)
		#media_editor.saveClip("strong-"+strong_text_sound+"-mirror_X-speed_0800_0_44712_0_62712", strong_out_dir)

		# Involving mirroring at Y
		media_editor.undo() # Undo the speed change
		media_editor.undo() # Undo the mirror at X
		media_editor.mirrorAtY()
		media_editor.saveClip("strong-"+strong_text_sound+"-mirror_Y", strong_out_dir)

		media_editor.changeSpeed(0.50, 0.63712, 0.79712)
		media_editor.saveClip("strong-"+strong_text_sound+"-mirror_Y-speed_0050_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 0.63712, 0.79712)
		media_editor.saveClip("strong-"+strong_text_sound+"-mirror_Y-speed_0075_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 0.63712, 0.79712)
		media_editor.saveClip("strong-"+strong_text_sound+"-mirror_Y-speed_0150_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 0.63712, 0.79712)
		media_editor.saveClip("strong-"+strong_text_sound+"-mirror_Y-speed_0200_0_44712_0_62712", strong_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 0.63712, 0.79712)
		#media_editor.saveClip("strong-"+strong_text_sound+"-mirror_Y-speed_0800_0_44712_0_62712", strong_out_dir)

		# Involving only speed change
		media_editor.undo() # Undo the speed change
		media_editor.undo() # Undo the mirror at Y

		media_editor.changeSpeed(0.50, 0.63712, 0.79712)
		media_editor.saveClip("strong-"+strong_text_sound+"-speed_0050_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 0.63712, 0.79712)
		media_editor.saveClip("strong-"+strong_text_sound+"-speed_0075_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 0.63712, 0.79712)
		media_editor.saveClip("strong-"+strong_text_sound+"-speed_0150_0_44712_0_62712", strong_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 0.63712, 0.79712)
		media_editor.saveClip("strong-"+strong_text_sound+"-speed_0200_0_44712_0_62712", strong_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 0.63712, 0.79712)
		#media_editor.saveClip("strong-"+strong_text_sound+"-speed_0800_0_44712_0_62712", strong_out_dir)	




		## 3. Modify extracts in various forms
		######################################

		## 4. Re-combine the extracted sequences to "full" media files again
		####################################################################

		## 5. Resulting in test data for study, with recorded modification history
		##########################################################################

		## 6. Save test-items into the output directory of "mediaEditing"
		#################################################################
		
		
		# go (English)
		## 0. Setup an editor
		################################################
		go_media_file = "../projects/exampleProject/mediaEditing/input/go.mp4"
		go_textgrid_file = "../projects/exampleProject/mediaEditing/input/go.TextGrid"
		go_temp_dir = "../projects/exampleProject/mediaEditing/temp/go/"
		go_out_dir = "../projects/exampleProject/mediaEditing/output/go/"
		
		media_editor = editing(go_media_file, go_temp_dir)

		## 1. Get information from correspoding TextGrid
		################################################
		go_text_sound = "aI"
		go_text_word = "mortified"
		
		### Get information about the sound "aI" and the word "mortified" in media file "go.mp4"
		media_editor.getTextGridInformation(go_text_sound, go_textgrid_file, go_temp_dir)
		media_editor.getTextGridInformation(go_text_word, go_textgrid_file, go_temp_dir)

		## 2. Extract described sequences
		################################# 
		
		### Extract each "aI" and each "mortified" in media file "go.mp4"
		media_editor.extractTextOccasionsFromGrid(go_text_word, go_textgrid_file, go_temp_dir+'/'+go_text_sound+'/', 'mp4')
		media_editor.extractTextOccasionsFromGrid(go_text_word, go_textgrid_file, go_temp_dir+'/'+go_text_word+'/')
		
		## TEMP to quickly get some files for Part 2
		# Copy the unmodified original file to output as hidden anchor
		media_editor._getClipFromPath(go_media_file)
		media_editor.saveClip("go-"+go_text_word, go_out_dir)

		# Involving mirroring at X
		media_editor.mirrorAtX()
		media_editor.saveClip("go-"+go_text_word+"-mirror_X", go_out_dir)
		
		media_editor.changeSpeed(0.50, 3.04, 3.57)
		media_editor.saveClip("go-"+go_text_word+"-mirror_X-speed_0050_0_44712_0_62712", go_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 3.04, 3.57)
		media_editor.saveClip("go-"+go_text_word+"-mirror_X-speed_0075_0_44712_0_62712", go_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 3.04, 3.57)
		media_editor.saveClip("go-"+go_text_word+"-mirror_X-speed_0150_0_44712_0_62712", go_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 3.04, 3.57)
		media_editor.saveClip("go-"+go_text_word+"-mirror_X-speed_0200_0_44712_0_62712", go_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 3.04, 3.57)
		#media_editor.saveClip("go-"+go_text_word+"-mirror_X-speed_0800_0_44712_0_62712", go_out_dir)

		# Involving mirroring at Y
		media_editor.undo() # Undo the speed change
		media_editor.undo() # Undo the mirror at X
		media_editor.mirrorAtY()
		media_editor.saveClip("go-"+go_text_word+"-mirror_Y", go_out_dir)

		media_editor.changeSpeed(0.50, 3.04, 3.57)
		media_editor.saveClip("go-"+go_text_word+"-mirror_Y-speed_0050_0_44712_0_62712", go_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 3.04, 3.57)
		media_editor.saveClip("go-"+go_text_word+"-mirror_Y-speed_0075_0_44712_0_62712", go_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 3.04, 3.57)
		media_editor.saveClip("go-"+go_text_word+"-mirror_Y-speed_0150_0_44712_0_62712", go_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 3.04, 3.57)
		media_editor.saveClip("go-"+go_text_word+"-mirror_Y-speed_0200_0_44712_0_62712", go_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 3.04, 3.57)
		#media_editor.saveClip("go-"+go_text_word+"-mirror_Y-speed_0800_0_44712_0_62712", go_out_dir)

		# Involving only speed change
		media_editor.undo() # Undo the speed change
		media_editor.undo() # Undo the mirror at Y

		media_editor.changeSpeed(0.50, 3.04, 3.57)
		media_editor.saveClip("go-"+go_text_word+"-speed_0050_0_44712_0_62712", go_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 3.04, 3.57)
		media_editor.saveClip("go-"+go_text_word+"-speed_0075_0_44712_0_62712", go_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 3.04, 3.57)
		media_editor.saveClip("go-"+go_text_word+"-speed_0150_0_44712_0_62712", go_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 3.04, 3.57)
		media_editor.saveClip("go-"+go_text_word+"-speed_0200_0_44712_0_62712", go_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 3.04, 3.57)
		#media_editor.saveClip("go-"+go_text_word+"-speed_0800_0_44712_0_62712", go_out_dir)	

		## 3. Modify extracts in various forms
		######################################

		## 4. Re-combine the extracted sequences to "full" media files again
		####################################################################

		## 5. Resulting in test data for study, with recorded modification history
		##########################################################################

		## 6. Save test-items into the output directory of "mediaEditing"
		#################################################################

		# obama (English)
		## 0. Setup an editor
		################################################
		obama_media_file = "../projects/exampleProject/mediaEditing/input/obama.mp4"
		obama_textgrid_file = "../projects/exampleProject/mediaEditing/input/obama.TextGrid"
		obama_temp_dir = "../projects/exampleProject/mediaEditing/temp/obama/"
		obama_out_dir = "../projects/exampleProject/mediaEditing/output/obama/"
		
		media_editor = editing(obama_media_file, obama_temp_dir)

		## 1. Get information from correspoding TextGrid
		################################################
		obama_text_sound = "aI"
		obama_text_word = "Michelle"
		
		### Get information about the sound "aI" and the word "Michelle" in media file "obama.mp4"
		media_editor.getTextGridInformation(obama_text_sound, obama_textgrid_file, obama_temp_dir)
		media_editor.getTextGridInformation(obama_text_word, obama_textgrid_file, obama_temp_dir)

		## 2. Extract described sequences
		################################# 
		
		### Extract each "aI" and each "Michelle" in media file "obama.mp4"
		media_editor.extractTextOccasionsFromGrid(obama_text_word, obama_textgrid_file, obama_temp_dir+'/'+obama_text_sound+'/', 'mp4')
		media_editor.extractTextOccasionsFromGrid(obama_text_word, obama_textgrid_file, obama_temp_dir+'/'+obama_text_word+'/')
		
		## TEMP to quickly get some files for Part 2
		# Copy the unmodified original file to output as hidden anchor
		media_editor._getClipFromPath(obama_media_file)
		media_editor.saveClip("obama-"+obama_text_word, obama_out_dir)

		# Involving mirroring at X
		media_editor.mirrorAtX()
		media_editor.saveClip("obama-"+obama_text_word+"-mirror_X", obama_out_dir)
		
		media_editor.changeSpeed(0.50, 14.44, 14.9)
		media_editor.saveClip("obama-"+obama_text_word+"-mirror_X-speed_0050_0_44712_0_62712", obama_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 14.44, 14.9)
		media_editor.saveClip("obama-"+obama_text_word+"-mirror_X-speed_0075_0_44712_0_62712", obama_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 14.44, 14.9)
		media_editor.saveClip("obama-"+obama_text_word+"-mirror_X-speed_0150_0_44712_0_62712", obama_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 14.44, 14.9)
		media_editor.saveClip("obama-"+obama_text_word+"-mirror_X-speed_0200_0_44712_0_62712", obama_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 14.44, 14.9)
		#media_editor.saveClip("obama-"+obama_text_word+"-mirror_X-speed_0800_0_44712_0_62712", obama_out_dir)

		# Involving mirroring at Y
		media_editor.undo() # Undo the speed change
		media_editor.undo() # Undo the mirror at X
		media_editor.mirrorAtY()
		media_editor.saveClip("obama-"+obama_text_word+"-mirror_Y", obama_out_dir)

		media_editor.changeSpeed(0.50, 14.44, 14.9)
		media_editor.saveClip("obama-"+obama_text_word+"-mirror_Y-speed_0050_0_44712_0_62712", obama_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 14.44, 14.9)
		media_editor.saveClip("obama-"+obama_text_word+"-mirror_Y-speed_0075_0_44712_0_62712", obama_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 14.44, 14.9)
		media_editor.saveClip("obama-"+obama_text_word+"-mirror_Y-speed_0150_0_44712_0_62712", obama_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 14.44, 14.9)
		media_editor.saveClip("obama-"+obama_text_word+"-mirror_Y-speed_0200_0_44712_0_62712", obama_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 14.44, 14.9)
		#media_editor.saveClip("obama-"+obama_text_word+"-mirror_Y-speed_0800_0_44712_0_62712", obama_out_dir)

		# Involving only speed change
		media_editor.undo() # Undo the speed change
		media_editor.undo() # Undo the mirror at Y

		media_editor.changeSpeed(0.50, 14.44, 14.9)
		media_editor.saveClip("obama-"+obama_text_word+"-speed_0050_0_44712_0_62712", obama_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(0.75, 14.44, 14.9)
		media_editor.saveClip("obama-"+obama_text_word+"-speed_0075_0_44712_0_62712", obama_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(1.5, 14.44, 14.9)
		media_editor.saveClip("obama-"+obama_text_word+"-speed_0150_0_44712_0_62712", obama_out_dir)
		media_editor.undo()
		media_editor.changeSpeed(2.0, 14.44, 14.9)
		media_editor.saveClip("obama-"+obama_text_word+"-speed_0200_0_44712_0_62712", obama_out_dir)
		#media_editor.undo()
		#media_editor.changeSpeed(8.0, 14.44, 14.9)
		#media_editor.saveClip("obama-"+obama_text_word+"-speed_0800_0_44712_0_62712", obama_out_dir)	

		## 3. Modify extracts in various forms
		######################################

		## 4. Re-combine the extracted sequences to "full" media files again
		####################################################################

		## 5. Resulting in test data for study, with recorded modification history
		##########################################################################

		## 6. Save test-items into the output directory of "mediaEditing"
		#################################################################



		


if __name__ == "__main__":
    main(sys.argv[1])

