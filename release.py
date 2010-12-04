#!/usr/bin/python3

# release.py -- Module to hold the release class and his sub classes
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2010-12-04.
# @Revision:    0.1




# class -- track () {{{
# class to manage a single track
# ****************************** #
class track:
	def __init__(self):
		# init all variables
		self.artist = "Unknown"
		self.title = "Unknown"
		self.key = "Unknown"
		self.link = "" 
		self.tn = "" 
	def __str__(self):
		s = self.artist + " - " + self.title
		return s

	# let the class act like a dict
	def __getitem__(self, key):
		if key == "artist":
			return self.artist
		elif key == "title":
			return self.title
		elif key == "key":
			return self.key
		elif key == "link":
			return self.link
		elif key == "tn":
			return self.tn

	def __setitem__(self, key, value):
		if key == "artist":
			self.artist = value
		elif key == "title":
			self.title = value
		elif key == "key":
			self.key = value
		elif key == "link":
			self.link = value
		elif key == "tn":
			self.tn = value
# end of release }}} #




# class -- release () {{{
# class to manage a single release
# ****************************** #
class release:

	# constructor
	def __init__(self):
		# init all variables
		self.catid = "Unknown"
		self.shortinfo = "Unknown"
		self.infopage = ""
		self.tunes = []

	# string method
	def __str__(self):
		s = "     Release: {}\n".format(self.catid)
		k = 1
		for tune in self.tunes:
			if k == len(self.tunes):
				s = s + "      " + str(tune)
			else:
				s = s + "      " + str(tune) + "\n"
			k = k + 1
		return s
	
	# iteration method method
	def __iter__(self):
		self.track_c = len(self.tunes)
		self.track_idx = 0

		return self

	# next method
	def __next__(self):
		if self.track_idx == self.track_c:
			raise StopIteration

		cur_track = self.tunes[self.track_idx]
		
		self.track_idx += 1

		return cur_track

	# append new track
	def append (self, new_track):
		self.tunes.append(new_track)
	
# end of release }}} #




# function -- main
# @ none
# < none
# main function for testing the module
# **************************
def main ():
	sFktname = "main"

	print("Hello this is the release Module\n")

	# create some tracks

	track_1 = track()
	track_1.artist = "Sighter"
	track_1.title = "newthingno"
	
	track_2 = track()
	track_2.artist = "Kaim"
	track_2.title = "Sunder"

	rel = release()
	rel.append (track_1)
	rel.append (track_2)


	for tr in rel:
		print(tr)
# end of main



if __name__ == "__main__":
	main()
