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
    def __init__(self, path_to_input, path_to_temp, path_to_output):
        self.path_to_input = path_to_input
        self.path_to_temp = path_to_temp
        self.path_to_output = path_to_output
        if self._checkDirExists(path_to_input):
            pass
        else:
            raise Exception('Input directory or file does not exist: ' + path_to_input)
        if self._checkDirExists(path_to_temp):
            pass
        else:
            raise Exception('Input directory or file does not exist: ' + path_to_temp)
        if self._checkDirExists(path_to_output):
            pass
        else:
            raise Exception('Input directory or file does not exist: ' + path_to_output)
     
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

    # To getting all existing excerpt's directory names
    def readDirectoryNamesFromInput(self, path_to_input):
        list_of_directories = [f.path for f in os.scandir(path_to_input) if f.is_dir()]
        return list_of_directories

    # To getting all existing excerpt's directory paths
    def readDirectoryPathsFromInput(self, path_to_input):
        list_of_directory_names = [os.path.basename(f.path) for f in os.scandir(path_to_input) if f.is_dir()]
        return list_of_directory_names


    # Create a trial based on excerpt and media filenames
    def createTrial(self, original_media, filenames, path_to_temp, number_trial_files):
        
        # Note: Old approach based on separate file for each trial- now counting list elements before hand
        # Check the number of trial_files already placed in the output directory to get number for next one
        #number_trial_files = sum(1 for element in os.scandir(path_to_temp) if element.is_file())
        #print("number_trial_files: "+ str(number_trial_files) +"   in path_to_output: "+path_to_temp)
        

        # Padd trial_id with zeros 
        trial_id = f'{number_trial_files:04}'
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

    # Merging json files by extending them
    def mergeJsonFiles(self, filenames, merged_json):
        result = list()
        for f1 in filenames:
            with open(f1, 'r') as infile:
                result.extend(json.load(infile))

        with open(merged_json, 'w') as output_file:
            json.dump(result, output_file)

    # Create a testset made up of trials
    def createTestset(self, path_to_trials, path_to_output, testset_name):
        
        # Read filenames from path_to_trials
        trial_files = self.readFilenamesFromDirectory(path_to_trials)

        testset_file = path_to_output+'/'+testset_name

        # Merge trial_files into a single merged_json
        self.mergeJsonFiles(trial_files, testset_file)

        return
        
        #new_testset = {
        #    "Testsets":[
        #        trials
        #    ]
        #}
        #return new_testset


        #new_trial, current_trial_name = self.createTrial(original_media, filenames, path_to_output)
        
        # Serializing json (new trial)
        #current_trial = json.dumps(new_trial, indent=4)

        # Write the current_trial into a json file
        #with open(path_to_output+'/'+original_media+'-'+current_trial_name+'.json', "w") as outfile:
        #    outfile.write(current_trial) 

    # Quick way to get some testing done
    def turnTestsetIntoConfig(self, path_to_config, name_of_config, current_trial_list, test_url):

        # Put config together
        new_config = {
            "TestName": name_of_config,
            "RateScalePng": "img/scale_abs.png",
            "RateScaleBgPng": "img/scale_abs_background.png",
            "RateMinValue": 0,
            "RateMaxValue": 100,
            "RateDefaultValue":0,
            "ShowFileIDs": "false",
            "ShowResults": "false",
            "LoopByDefault": "false",
            "EnableABLoop": "true",
            "EnableOnlineSubmission": "true",
            "UploadIntermediates": "true",
            "BeaqleServiceURL": test_url,
            "SupervisorContact": "7schuler@informatik.uni-hamburg.de",
            "RandomizeTestOrder": "true",
            "AnchorsNumber": 2,
            "MaxTestsPerRun": 25,
            "RequireMaxRating": "false",
            "AudioRoot": "",
            "Testsets":current_trial_list
        }

        # Write the config file
        with open(path_to_config+'/'+name_of_config+'.js', 'w') as f:
            f.write('var TestConfig = ')

        # Append content to config file
        with open(path_to_config+'/'+name_of_config+'.js', 'a') as f:
            f.write(json.dumps(new_config))

        # Append ending to config file
        #with open(path_to_config+'/'+name_of_config+'.js', 'a') as f:
        #    f.write('')
        
        return

    # Set the study parameters
    def setStudyParameters(self, trial_size=5, language="English", name="MyStudy", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"):
        self.trial_size = trial_size
        self.language = language
        self.test_name = name
        self.test_url = url
        

    # Create study
    def createStudy(self):
        print("Entering createStudy()")
        # Get names and directories for all the existing excerpts from the input directory
        self.list_of_directory_names = self.readDirectoryNamesFromInput(self.path_to_input) 
        self.list_of_directories = self.readDirectoryPathsFromInput(self.path_to_input) 
        # self.list_of_directory_names = ["go", "lohse", "obama", "strong"]
        # self.list_of_directories = ["path/.../go", "path/.../lohse", ...]
        
        # Debugging
        print("path_to_input: "+self.path_to_input)
        print("path_to_output: "+self.path_to_output)
        print("list_of_directory_names: "+str(self.list_of_directory_names))
        print("list_of_directories: "+str(self.list_of_directories))

        # List of created trials to be part of a testset
        current_trial_list = []


        # Processing all input folders (one per media file that was edited)
        # Here for the excerpts: go, lohse, obama, strong
        for excerpt_directory, excerpt_name in zip(self.list_of_directory_names, self.list_of_directories):
            print("Processing excerpt: "+excerpt_name)
            print("    in directory: "+excerpt_directory)
            
            # For prcoessing all modified media files corresponding to one excerpt
            excerpt_filenames = self.readFilenamesFromDirectory(excerpt_directory)
            #print("First filename: "+current_filenames[0])

            # The shortest filename is the original media without any modifications
            original_media = min(excerpt_filenames, key=len) #current_filenames[0]
            excerpt_filenames.remove(original_media)
            
            i = 1
            n = 100
            # To prevent a death-loop
            while i <= n:
                # Randomly select a sub-sample of the media files
                current_filenames = random.sample(excerpt_filenames, k=self.trial_size)

                # TODO: Outsource
                # Note: Old version that creates a file for each trial for manual adjustment in modular approach
                #self.createTestset(original_media, current_filenames, self.path_to_output)
                #new_trial, current_trial_name = self.createTrial(original_media, current_filenames, self.path_to_temp)
        
                # Serializing json (new trial)
                #current_trial = json.dumps(new_trial, indent=4)

                # Write the current_trial into a json file
                #with open(self.path_to_temp+'/'+original_media+'-'+current_trial_name+'.json', "w") as outfile:
                #    outfile.write(current_trial) 

                # Create a trial (in json-suitable dictionary structure) based on filenames
                new_trial, current_trial_name = self.createTrial(original_media, current_filenames, self.path_to_temp, len(current_trial_list))

                # Collect all trials in a list for the testset
                current_trial_list.append(new_trial)

                i = i+1
                #print("Done with first read excerpt turned into a test trial.")
                #sys.exit()

        # All trials as list inside a "Testsets"
        new_testset = {
            "Testsets":
                current_trial_list
        }
         
        # Serializing json (new testset)
        current_testset = json.dumps(new_testset, indent=4)

        # Count number of testsets in output directory of study_setup
        number_testset_files = sum(1 for element in os.scandir(self.path_to_output) if element.is_file())

        # Write the current_trial into a json file
        with open(self.path_to_output+'/testset-'+str(number_testset_files)+'.json', "w") as outfile:
            outfile.write(current_testset) 

        # Quick and basic study-setup
        self.turnTestsetIntoConfig(self.path_to_output, "TestStudy", current_trial_list, "https://www.timobaumann.de/temp/vtts/beaqleJS_Service.php")







    # Processing all input folders (one per media file that was edited)
    def processInputFolder(self, path_to_input, path_to_output):
        for excerpt in self.list_of_directories:
            print("Processing excerpt: "+excerpt)
            current_filenames = self.readFilenamesFromDirectory(excerpt)
            print("First filename: "+current_filenames[0])