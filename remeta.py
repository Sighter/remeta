#!/usr/bin/python3

# remeta.py -- head script for the remeta project
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2010-12-04.
# @Revision:    0.1

import getopt
import sys
import settings
from helpers import ePrint
from os import path
from id3ed import id3_to_track
import pattern



# function -- print_help
# @ none
# < none
# function to print help
# **************************
def print_help ():
	sFktname = "print_help"
	print("Synopsis: remeta file1 file2 ... [ -c ]")
	print("  -c	| --copy     make a copy of original files before copying")
	print("  -h	| --help     print this help")
# end of print_help




# function -- main
# @ none
# < none
# The main function
# **************************
def main ():
	sFktname = "main"
	
	# handle arguments
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hcp:", ["help", "copy", "pattern="])
	except:
		print(err) # will print something like "option -a not recognized"
		usage()
		sys.exit(2)

	
	# handle options
	for o, a in opts:
		if o in ("-h", "--help"):
			print_help()
		elif o in ("-c", "--copy"):
			settings.copymode = True
		elif o in ("-p", "--pattern"):
				
	# handle arguments
	if len(args) == 0:
		ePrint(1, sFktname, "No Files specified")
	
	# check, whether files have valid paths
	for fn in args:
		if path.exists(fn) == False:
			ePrint(1, sFktname, "Path not found: {}".format(fn))
			sys.exit(2)
	
	# 
	
	# enter main loop
	for fn in args:

		# try to get information from tags
		new_track = id3_to_track(fn)

		# artist found ?
		if new_track.artist != "":
			
			
			
			
		
		

# end of main




if __name__ == "__main__":
	main ()
