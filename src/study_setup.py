# Part 2 - Study Setup
# 
# Authors: Christian Schuler & Dominik Hauser & Anran Wang
################################################################################

import os
import json
import random
import sys
import shutil

"""
Study setup class based on directories full of modified media files.
"""
class setupping():
    def __init__(self, path_to_input, path_to_temp, path_to_output, path_to_study):
        self.path_to_input = path_to_input
        self.path_to_temp = path_to_temp
        self.path_to_output = path_to_output
        self.path_to_study = path_to_study
        if self._checkDirExists(path_to_input):
            pass
        else:
            raise Exception('Input directory or file does not exist: ' + path_to_input)
        if self._checkDirExists(path_to_temp):
            pass
        else:
            raise Exception('Temp directory or file does not exist: ' + path_to_temp)
        if self._checkDirExists(path_to_output):
            pass
        else:
            raise Exception('Output directory or file does not exist: ' + path_to_output)
        if self._checkDirExists(path_to_study):
            pass
        else:
            raise Exception('Study directory or file does not exist: ' + path_to_study)
     
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
    def readDirectoryPathsFromInput(self, path_to_input):
        list_of_directories = [f.path for f in os.scandir(path_to_input) if f.is_dir()]
        return list_of_directories

    # To getting all existing excerpt's directory paths
    def readDirectoryNamesFromInput(self, path_to_input):
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
                "Reference": "video/"+original_media,
                "1": "video/"+filenames[0],
                "2": "video/"+filenames[1],
                "3": "video/"+filenames[2],
                "4": "video/"+filenames[3],
                "5": "video/"+filenames[4],
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
    def turnTestsetIntoConfig(self, path_to_config, name_of_config, config_file_name, current_trial_list, test_url):

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
        with open(path_to_config+'/'+config_file_name+'.js', 'w') as f:
            f.write('var TestConfig = ')

        # Append content to config file
        with open(path_to_config+'/'+config_file_name+'.js', 'a') as f:
            f.write(json.dumps(new_config))

        # Append ending to config file
        #with open(path_to_config+'/'+config_file_name+'.js', 'a') as f:
        #    f.write('')
        
        return
    
    ##############################
    # From (Create Study Button) #
    ##############################
    # Confirm format of provided study paramters
    def checkStudyParameters():
        # TODO
        pass

    # Set the study parameters
    def setStudyParameters(self, 
                           study_name="MyStudy", 
                           config_name="TestStudyConfig", 
                           language="English", 
                           rate_scale_png="img/scale_abs.png",
                           rate_scale_bg_png="img/scale_abs_background.png",
                           supervisor_contact="7schuler@informatik.uni-hamburg.de",
                           study_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                           testset_size=4, 
                           trial_size=5, 
                           rate_min_value=0,
                           rate_max_value=100,
                           rate_default_value=0,
                           anchors_number=2,
                           max_tests_per_run=25,
                           show_file_ids="false",
                           show_results="false",
                           loop_by_default="false",
                           enable_ab_loop="false",
                           randomize_test_order="true",
                           online_submission="true",
                           upload_intermediates="true",
                           require_max_rating="false",
                           ):
        
        # Text
        self.study_name = study_name                        # TestName: "My Awesome Study"
        self.config_name = config_name                      # ConfigFileName: "my_config.js"
        self.language = language                            # Language: "English"
        # Filepaths
        self.rate_scale_png = rate_scale_png                # RateScalePng: "img/scale_abs.png",
        self.rate_scale_bg_png = rate_scale_bg_png          # RateScaleBgPng: "img/scale_abs_background.png",
        # Special 
        self.supervisor_contact = supervisor_contact        # SupervisorContact: "7schuler@informatik.uni-hamburg.de"
        self.beaqle_service_url = study_url                 # BeaqleServiceURL: "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        #self.study_url = study_url
        # Integer
        self.testset_size = testset_size                    # Testsize: 4
        self.trial_size = trial_size                        # TrialSize: 5
        self.rate_min_value = rate_min_value                # RateMinValue: 0
        self.rate_max_value = rate_max_value                # RateMaxValue: 100
        self.rate_default_value = rate_default_value        # RateDefaultValue: 0
        self.anchors_number = anchors_number                # AnchorsNumber: 2
        self.max_tests_per_run = max_tests_per_run          # MaxTestsPerRun: 25
        # Boolean
        self.show_file_ids = show_file_ids                  # ShowFileIDs: "false"
        self.show_results = show_results                    # ShowResults: "false"
        self.loop_by_default = loop_by_default              # LoopByDefault: "false"
        self.enable_ab_loop = enable_ab_loop                # EnableABLoop: "false"
        self.randomize_test_order = randomize_test_order    # RandomizeTestOrder: "true"
        self.online_submission = online_submission          # EnableOnlineSubmission: "true"
        self.upload_intermediates = upload_intermediates    # UploadIntermediates: "true"
        self.require_max_rating = require_max_rating        # RequireMaxRating: "false"

        return
        
    # Create the study
    def createStudy(self):
        print("Entering createStudy()")
        # Get names and directories for all the existing excerpts from the input directory
        self.list_of_directory_names = self.readDirectoryNamesFromInput(self.path_to_input) 
        self.list_of_directories = self.readDirectoryPathsFromInput(self.path_to_input) 
        # self.list_of_directory_names = ["go", "lohse", "obama", "strong"]
        # self.list_of_directories = ["path/.../go", "path/.../lohse", ...]
        
        # Debugging
        #print("path_to_input: "+self.path_to_input)
        #print("path_to_output: "+self.path_to_output)
        #print("list_of_directory_names: "+str(self.list_of_directory_names))
        #print("list_of_directories: "+str(self.list_of_directories))

        # List of created trials to be part of a testset
        current_trial_list = []


        # Processing all input folders (one per media file that was edited)
        # Here for the excerpts: go, lohse, obama, strong
        for excerpt_name, excerpt_directory in zip(self.list_of_directory_names, self.list_of_directories):
            print("Processing excerpt: "+excerpt_name)
            print("    in directory: "+excerpt_directory)
            
            # For prcoessing all modified media files corresponding to one excerpt
            excerpt_filenames = self.readFilenamesFromDirectory(excerpt_directory)
            #print("First filename: "+current_filenames[0])

            # The shortest filename is the original media without any modifications
            original_media = min(excerpt_filenames, key=len) #current_filenames[0]
            excerpt_filenames.remove(original_media)
            
            i = 1
            n = self.testset_size
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
        #self.turnTestsetIntoConfig(self.path_to_output, "FunWithAnranAndDomi", "TestStudy", current_trial_list, "https://www.timobaumann.de/temp/vtts/beaqleJS_Service.php")
        self.turnTestsetIntoConfig(self.path_to_output, self.study_name, self.config_name, current_trial_list, self.study_url)



    # Moving all video files into a single folder for the online study
    def moveMediaFilesToStudy(self, path_to_study):
        for excerpt_directory in self.list_of_directories:
            #print("excerpt_directory: "+excerpt_directory) #Debugging
            for file_name in os.listdir(excerpt_directory):
                #print("file_name: "+file_name) #Debugging
                # Construct full file path
                source = excerpt_directory+'/'+file_name
                destination = path_to_study+'/video/'+file_name
                # Move only files
                if os.path.isfile(source):
                    shutil.copy(source, destination)






    # Processing all input folders (one per media file that was edited)
    def processInputFolder(self, path_to_input, path_to_output):
        for excerpt in self.list_of_directories:
            print("Processing excerpt: "+excerpt)
            current_filenames = self.readFilenamesFromDirectory(excerpt)
            print("First filename: "+current_filenames[0])