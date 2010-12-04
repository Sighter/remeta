#!/usr/bin/python3

# pattern.py -- module to manage the file name pattern
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2010-12-04.
# @Revision:    0.1




# class pattern
# class to replace symbols in the filename pattern
# **************************
class pattern:
	def __init__(self,pat):
		self.pat = pat
	
	def get_result(self):
		return self.pat
	
	def replace_artist(self, artist):
		if self.pat.find("%a") != -1:
			self.pat = self.pat.replace("%a", artist)

	def replace_title(self, title):
		if self.pat.find("%t") != -1:
			self.pat = self.pat.replace("%t", title)

	def replace_tn(self, tn):
		if self.pat.find("%n") != -1:
			self.pat = self.pat.replace("%n", tn)

	def replace_key(self, key):
		if self.pat.find("%k") != -1:
			self.pat = self.pat.replace("%k", key)

#
#
# end of pattern




# function -- main
# @ none
# < none
# main function for testing
# **************************
def main ():
	sFktname = "main"
	
	p = pattern(r"%n %a - %t -- %k")
	p.replace_artist("Sighter")
	p.replace_title("newone")
	p.replace_key("cmoll")
	p.replace_tn("02")

	print(p.get_result())

#
#
# end of main



if __name__ == "__main__":
	main()
