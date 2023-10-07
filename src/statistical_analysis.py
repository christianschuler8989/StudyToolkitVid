# Part 3 - Statistical Analysis
# 
# Authors: Christian Schuler & Dominik Hauser & Anran Wang
################################################################################

import os

"""
Statistical analysis class based on the results from a perception study to explore and analyse the collected data.
"""
class analazizer():
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
            raise Exception('Temp directory or file does not exist: ' + path_to_temp)
        if self._checkDirExists(path_to_output):
            pass
        else:
            raise Exception('Output directory or file does not exist: ' + path_to_output)
     
    # Checks if dir exists
    def _checkDirExists(self, path_to_check):
        return os.path.exists(path_to_check)
    
    ##############################
    # From (Explore Data Button) #
    ##############################
    
    # Exploration of the provided data
    def exploreData():
        print("TODO: Data Exploration") # TODO
        return

    #################################
    # From (Explore Results Button) #
    #################################
    
    # Exploration via minor data transformations
    def exploreResults():
        print("TODO: Result Exploration") # TODO
        return

    #############################################
    # From (Listeningpanel Quantitative Button) #
    #############################################
    
    # Meta data of the study participants (quantitative version)
    def listeningpanelQuantitative():
        print("TODO: Quantitative Listeningpanel") # TODO
        return

    ############################################
    # From (Listeningpanel Qualitative Button) #
    ############################################
    
    # Meta data of the study participants (qualitative version)
    def listeningpanelQualitative():
        print("TODO: Qualitative Listeningpanel") # TODO
        return

    #############################
    # From (ANOVA Check Button) #
    #############################
    
    # Confirm the requirementes of data to be suitable for ANOVA analysis
    def anovaCheck():
        print("TODO: Check for ANOVA prerequisites") # TODO
        return

    ################################
    # From (ANOVA Analysis Button) #
    ################################
    
    # Do an ANOVE analysis of the provided study result data
    def anovaAnalysis():
        print("TODO: Run ANOVA analysis") # TODO
        return

    ###############################
    # From (Kruskalwallis Button) #
    ###############################
    
    # Run a Kruskal Wallis analysis as an alternative to ANOVA
    def kruskalwallisAnalysis():
        print("TODO: Run Kruskal Wallis analysis") # TODO
        return

    ########################
    # From (Wilcox Button) #
    ########################
    
    # Run a Wilcox analysis as an alternative to ANOVA
    def wilcoxAnalysis():
        print("TODO: Run Wilcox analysis") # TODO
        return
