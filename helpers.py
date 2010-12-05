#!/usr/bin/python3

# helpers.py -- file for minor helper functions
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2010-12-04.
# @Revision:    0.1


import re

# function -- split_ld
# @ string
# < first part
# < second part
# split a string on last dot
# **************************
def split_ld (str_orig):
	sFktname = "split_ld"

	p = re.compile(r"(^.*)\.(.*)+?^")
# end of split_ld




# function -- ePrint
# @ verLevel
# @ function name
# @ message
# < none
# print messages while controling the verbosity level
# **************************
def ePrint (verLevel, fName, message):
	sFktname = "ePrint"
	print(" --> {}: {}".format(fName, message))
# end of ePrint
