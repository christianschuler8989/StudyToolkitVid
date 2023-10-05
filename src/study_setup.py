#
# 
# Authors: Christian Schuler & Dominik Hauser & Anran Wang
################################################################################

import os

"""
Study setup class based on directories full of modified media files.
"""
class setuping():
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

    # Lets go!
    def sanityCheck(self, input):
        print(input+"'s sanity has been lost.")