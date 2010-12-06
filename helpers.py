#!/usr/bin/python3

# helpers.py -- file for minor helper functions
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2010-12-04.
# @Revision:    0.1


import re
import urllib

# function -- split_ld
# @ string
# < first part
# < second part
# split a string on last dot
# **************************
def split_ld (str_orig):
	sFktname = "split_ld"

	p = re.compile(r"(.*)\.(.*$)")
	
	res = p.search(str_orig).groups()

	if len(res) != 2:
		return None
	else:
		return res[1]
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




# function -- subinstr () {{{
# @ list of regex,sub -pairs
# @ the string 
# < new string
# ****************************** #
def subinstr(list,newstr):
	for i in list:
		p = re.compile(i[0])
		newstr = p.sub(i[1], newstr)

	return newstr
# end of subinstr }}} #




# function -- getWebAsSrc () {{{
# @ url
# < decoded string
# ****************************** #
# fkt -- getWebAsSrc(url) {{{
def getWebAsStr(url):
	try:
		response = urllib.request.urlopen(url)
	except:
		print(" --> helpers.getWebAsStr: URL Error")
		return ""

	# print page info
	#for i,j in response.info().items():
	#		print(i,j)

	# get page-source to str
	string = response.read()
	
	# convert the string to a raw-string
	return string.decode('Latin1')
# end of }}} #

