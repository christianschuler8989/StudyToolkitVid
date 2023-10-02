#
# 
# Authors: Christian Schuler & Dominik Hauser
################################################################################

import os
import subprocess
import media_editing_command_based

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
		try:
			with open(test_media_temp+'/test.txt', 'w') as f:
				f.write('Test Protocol!')
		except FileNotFoundError:
			print("The media editing directory does not exist")

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
		## 1. Get information from correspoding TextGrid
		## 2. Extract described sequences
		## 3. Modify extracts in various forms
		## 4. Re-combine the extracted sequences to "full" media files again
		## 5. Resulting in test data for study, with recorded modification history
		## 6. Save test-items into the output directory of "mediaEditing"
		##########################################################################

		# Lohse (German)
		## 1. Get information from correspoding TextGrid
		################################################
		lohse_media_file = "../projects/exampleProject/mediaEditing/input/lohse.mp4"
		lohse_textgrid_file = "../projects/exampleProject/mediaEditing/input/lohse.TextGrid"
		lohse_text_sound = "aI"
		lohse_text_word = "Name"
		lohse_temp_dir = "../projects/exampleProject/mediaEditing/temp/lohse/"

		### Get information about the sound "aI" in media file "lohse.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			lohse_media_file, 
			"-textGridInformation", 
			lohse_text_sound,
			lohse_textgrid_file,
			lohse_temp_dir+'/'])

		### Get information about the word "Name" in media file "lohse.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			lohse_media_file, 
			"-textGridInformation", 
			lohse_text_word, 
			lohse_textgrid_file,
			lohse_temp_dir+'/'])

		## 2. Extract described sequences
		################################# 
		
		### Extract each "aI" in media file "lohse.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			lohse_media_file, 
			"-extractTextGridOccasions", 
			lohse_text_sound,
			lohse_textgrid_file,
			lohse_temp_dir+'/'+lohse_text_sound+'/'])

		### Extract each "Name" in media file "lohse.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			lohse_media_file, 
			"-extractTextGridOccasions", 
			lohse_text_word,
			lohse_textgrid_file,
			lohse_temp_dir+'/'+lohse_text_word+'/'])


		## 3. Modify extracts in various forms
		######################################

		## 4. Re-combine the extracted sequences to "full" media files again
		####################################################################

		## 5. Resulting in test data for study, with recorded modification history
		##########################################################################

		## 6. Save test-items into the output directory of "mediaEditing"
		#################################################################


		# Strong (German)
		## 1. Get information from correspoding TextGrid
		################################################
		strong_media_file = "../projects/exampleProject/mediaEditing/input/strong.mp4"
		strong_textgrid_file = "../projects/exampleProject/mediaEditing/input/strong.TextGrid"
		strong_text_sound = "aI"
		strong_text_word = "gemeinsam"
		strong_temp_dir = "../projects/exampleProject/mediaEditing/temp/strong/"

		### Get information about the sound "aI" in media file "strong.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			strong_media_file, 
			"-textGridInformation", 
			strong_text_sound,
			strong_textgrid_file,
			strong_temp_dir+'/'])

		### Get information about the word "gemeinsam" in media file "stong.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			strong_media_file, 
			"-textGridInformation", 
			strong_text_word, 
			strong_textgrid_file,
			strong_temp_dir+'/'])

		## 2. Extract described sequences
		################################# 

		### Extract each "aI" in media file "strong.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			strong_media_file, 
			"-extractTextGridOccasions", 
			strong_text_sound,
			strong_textgrid_file,
			strong_temp_dir+'/'+strong_text_sound+'/'])

		### Extract each "gemeinsam" in media file "strong.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			strong_media_file, 
			"-extractTextGridOccasions", 
			strong_text_word,
			strong_textgrid_file,
			strong_temp_dir+'/'+strong_text_word+'/'])

		## 3. Modify extracts in various forms
		######################################

		## 4. Re-combine the extracted sequences to "full" media files again
		####################################################################

		## 5. Resulting in test data for study, with recorded modification history
		##########################################################################

		## 6. Save test-items into the output directory of "mediaEditing"
		#################################################################
		

		# Go (English)
		## 1. Get information from correspoding TextGrid
		################################################
		go_media_file = "../projects/exampleProject/mediaEditing/input/go.mp4"
		go_textgrid_file = "../projects/exampleProject/mediaEditing/input/go.TextGrid"
		go_text_sound = "aI"
		go_text_word = "Terrified"
		go_temp_dir = "../projects/exampleProject/mediaEditing/temp/go/"

		### Get information about the sound "aI" in media file "go.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			go_media_file, 
			"-textGridInformation", 
			go_text_sound,
			go_textgrid_file,
			go_temp_dir+'/'])

		### Get information about the word "Terrified" in media file "go.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			go_media_file, 
			"-textGridInformation", 
			go_text_word, 
			go_textgrid_file,
			go_temp_dir+'/'])

		## 2. Extract described sequences
		################################# 

		### Extract each "aI" in media file "go.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			go_media_file, 
			"-extractTextGridOccasions", 
			go_text_sound,
			go_textgrid_file,
			go_temp_dir+'/'+go_text_sound+'/'])

		### Extract each "Terrified" in media file "go.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			go_media_file, 
			"-extractTextGridOccasions", 
			go_text_word,
			go_textgrid_file,
			go_temp_dir+'/'+go_text_word+'/'])

		## 3. Modify extracts in various forms
		######################################

		## 4. Re-combine the extracted sequences to "full" media files again
		####################################################################

		## 5. Resulting in test data for study, with recorded modification history
		##########################################################################

		## 6. Save test-items into the output directory of "mediaEditing"
		#################################################################
		

		# Obama (English)
		## 1. Get information from correspoding TextGrid
		################################################
		obama_media_file = "../projects/exampleProject/mediaEditing/input/obama.mp4"
		obama_textgrid_file = "../projects/exampleProject/mediaEditing/input/obama.TextGrid"
		obama_text_sound = "aI"
		obama_text_word = "the"
		obama_temp_dir = "../projects/exampleProject/mediaEditing/temp/obama/"

		### Get information about the sound "aI" in media file "obama.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			obama_media_file, 
			"-textGridInformation", 
			obama_text_sound,
			obama_textgrid_file,
			obama_temp_dir+'/'])

		### Get information about the word "the" in media file "obama.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			obama_media_file, 
			"-textGridInformation", 
			obama_text_word, 
			obama_textgrid_file,
			obama_temp_dir+'/'])
		
		## 2. Extract described sequences
		################################# 

		### Extract each "aI" in media file "obama.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			obama_media_file, 
			"-extractTextGridOccasions", 
			obama_text_sound,
			obama_textgrid_file,
			obama_temp_dir+'/'+obama_text_sound+'/'])

		### Extract each "the" in media file "obama.mp4"
		subprocess.call([
			"python", 
			"media_editing_command_based.py", 
			"-name", 
			obama_media_file, 
			"-extractTextGridOccasions", 
			obama_text_word,
			obama_textgrid_file,
			obama_temp_dir+'/'+obama_text_word+'/'])

		## 3. Modify extracts in various forms
		######################################

		## 4. Re-combine the extracted sequences to "full" media files again
		####################################################################

		## 5. Resulting in test data for study, with recorded modification history
		##########################################################################

		## 6. Save test-items into the output directory of "mediaEditing"
		#################################################################
		


		




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
		try:
			with open(test_study_temp+'/test.txt', 'w') as f:
				f.write('Test Protocol!')
		except FileNotFoundError:
			print("The study setup directory does not exist")



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
		try:
			with open(test_statistical_temp+'/test.txt', 'w') as f:
				f.write('Test Protocol!')
		except FileNotFoundError:
			print("The statistical analysis directory does not exist")
	
	



if __name__ == "__main__":
    main(sys.argv[1])

