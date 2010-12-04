#!/usr/bin/python3

# remeta.py -- head script for the remeta project
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2010-12-04.
# @Revision:    0.1

import getopt
import sys
import settings



# function -- main
# @ none
# < none
# The main function
# **************************
def main ():
	sFktname = "main"
	
	# handle arguments
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hc", ["help", "copy"])
	except:
		print(err) # will print something like "option -a not recognized"
		usage()
		sys.exit(2)
	
	
	

# end of main






if __name__ == "__main__":
	main ()
