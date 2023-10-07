# The main script of the StudyToolkitVid-pipeline in early phase of development
# 
# Authors: Christian Schuler & Dominik Hauser & Anran Wang
################################################################################

import os.path as path
import argparse
import textwrap
import subprocess
import test_run
import studytoolkitGUI
import setup as pythonBasedSetup
"""
Different modes via arguments:
'-s', '--setup'
'-t', '--test'
'-r', '--run' (default)
"""
def main():
	parser = argparse.ArgumentParser(
	prog='PROG',
	formatter_class=argparse.RawDescriptionHelpFormatter,description=textwrap.dedent('''\
	A toolkit for video perception studies.
	---------------------------------------
	    For more information check out the github repository:
	    https://github.com/christianschuler8989/StudyToolkitVid
	'''))
	parser.add_argument('-s', '--setup', action="store_true",
		                  help='setting up the directory structure for the pipeline.')
	parser.add_argument('-t', '--test', action="store_true",
		                  help='testing the functionalities of the toolkit.')
	parser.add_argument('-n', '--number', nargs="+", type=int,
		                  help='which part to test out of (1,2,3).')
	parser.add_argument('-r', '--run', action="store_true",
		                  help='run the toolkit.')
	args = parser.parse_args()
	
	#parser.print_help()
	
	# Take the input arguments to then decide which mode to run
	setup = args.setup
	test = args.test
	testParts = args.number
	run = args.run

	# Debugging:
	print("setup: "+str(setup) + "    test: "+str(test) + "     run: "+str(run))

	def mode_toolkit():
		if setup:
			setup_toolkit(setup)
		if test:
			test_toolkit(testParts, test)
		if run:
			run_toolkit(run)
	
	"""
	Setup: Call "setup.bh" to build directory structure and copy examples into place.
	"""
	def setup_toolkit(setup=False):
		if setup:
			print("Setting up the workspace.")
			#subprocess.call("./setup.bh")
			pythonBasedSetup.setupWorkplace()
			return
			
	"""
	Test: Call "test_run.py" to test various toolkit functionalities.
	"""
	def test_toolkit(testParts=1, test=False):
		if test:
			print("Testing the toolkits functionalities.")
			test_run.main(testParts)
			return
	
	"""
	Run: Call "studytoolkitGUI.py" to run the graphical userinterface of the toolkit.
	"""
	def run_toolkit(run=False):
		if run:
			print("Running the toolkit.")
			studytoolkitGUI.main()
			return

	mode_toolkit()
	print("Debugging: End of script.")

if __name__ == "__main__":
    main()

