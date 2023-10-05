#
# 
# Authors: Christian Schuler & Dominik Hauser & Anran Wang
################################################################################

import os
import json
import random
import sys

"""
Study setup class based on directories full of modified media files.
"""
class setupping():
    def __init__(self, path_to_input, path_to_output):
        self.path_to_input = path_to_input
        self.path_to_output = path_to_output
        if self._checkDirExists(path_to_input):
            pass
        else:
            raise Exception('Input directory or file does not exist: ' + path_to_input)
     
    # Checks if dir exists
    def _checkDirExists(self, path_to_check):
        return os.path.exists(path_to_check)

    # For prcoessing all modified media files corresponding to one excerpt
    def readFilenamesFromDirectory(self, path_to_files):
        list_of_filenames = []
        # Iterate directory
        for file_path in os.listdir(path_to_files):
            # Add filename to list
            list_of_filenames.append(file_path)
        return list_of_filenames

    # To getting all existing excerpts
    def readDirectoryNamesFromInput(self, path_to_input):
        self.list_of_directories = [f.path for f in os.scandir(path_to_input) if f.is_dir()]

    # Create a trial based on excerpt and media filenames
    def createTrial(self, original_media, filenames, path_to_output):
        # Check the number of trial_files already placed in the output directory to get number for next one
        number_trial_files = len([trial_file for trial_file in os.listdir(path_to_output) if os.path.isfile(trial_file)])
        print(number_trial_files)
        
        # Padd trial_id with zeros 
        trial_id = f'{number_trial_files:05}'
        print(trial_id)

        trial_name = "trial_"+str(trial_id)

        new_trial = {
            "Name": trial_name,
            "TestID": trial_id,
            "Files":
            {
                "Reference": original_media,
                "1": filenames[0],
                "2": filenames[1],
                "3": filenames[2],
                "4": filenames[3],
                "5": filenames[4],
            }
        }
        return new_trial, trial_name

    # Create a testset made up of trials
    def createTestset(self, original_media, filenames, path_to_output):
        #trial_name="trial_00001"
        #trial_id="00001"

        new_trial, current_trial_name = self.createTrial(original_media, filenames, path_to_output)
        
        # Serializing json (new trial)
        current_trial = json.dumps(new_trial, indent=4)

        # Write the current_trial into a json file
        with open(path_to_output+'/'+original_media+'-'+current_trial_name+'.json', "w") as outfile:
            outfile.write(current_trial) 


    # Set the study parameters
    def setStudyParameters(self, trial_size=5, language="English"):
        self.trial_size = trial_size
        self.language = language
        

    # Create study
    def createStudy(self):
        
        # Get names for all the existing excerpts from the input directory
        self.readDirectoryNamesFromInput(self.path_to_input)

        # Processing all input folders (one per media file that was edited)
        for excerpt in self.list_of_directories:
            print("Processing excerpt: "+excerpt)
            
            # For prcoessing all modified media files corresponding to one excerpt
            excerpt_filenames = self.readFilenamesFromDirectory(excerpt)
            #print("First filename: "+current_filenames[0])

            # The shortest filename is the original media without any modifications
            original_media = min(excerpt_filenames, key=len) #current_filenames[0]
            excerpt_filenames.remove(original_media)
            
            i = 1
            n = 10
            # To prevent a death-loop
            while i <= n:
                # Randomly select a sub-sample of the media files
                current_filenames = random.sample(excerpt_filenames, k=self.trial_size)

                self.createTestset(original_media, current_filenames, self.path_to_output)

                i = i+1
                #print("Done with first read excerpt turned into a test trial.")
                #sys.exit()


        # save to: self.path_to_output







    # Processing all input folders (one per media file that was edited)
    def processInputFolder(self, path_to_input, path_to_output):
        for excerpt in self.list_of_directories:
            print("Processing excerpt: "+excerpt)
            current_filenames = self.readFilenamesFromDirectory(excerpt)
            print("First filename: "+current_filenames[0])