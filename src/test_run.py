#
# 
# Authors: Christian Schuler & Dominik Hauser
################################################################################

import os.path as path

"""
Pipeline test class for development and bug-fixing.
"""
def main(media_editing=True, study_setup=True, statistical_analysis=True):
	print("media_editing: "+str(media_editing)+"   study_setup: "+str(study_setup)+"    statistical_analysis: "+str(statistical_analysis))
						
	# Test: Part 1 Media Editing
	if media_editing:
		print("Start testing Media Editing:")

	# Test: Part 2 Study Setup
	if study_setup:
		print("Start testing Study Setup:")
	
	# Test: Part 3 Statistical Analysis
	if statistical_analysis:
		print("Start testing Statistical Analysis:")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])

