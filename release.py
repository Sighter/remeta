#!/usr/bin/python3

# release.py -- Module to hold the release class and his sub classes
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2010-12-04.
# @Revision:    0.1

from math import ceil
from helpers import ePrint



# class -- track () {{{
# class to manage a single track
# ****************************** #
class track:
	def __init__(self):
		# init all variables
		self.artist = ""
		self.title = ""
		self.key = ""
		self.link = "" 
		self.tn = "" 
	def __str__(self):
		s = self.artist + " - " + self.title + " - " + self.key
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

	def is_empty(self):
		if self.key == "" and self.artist == "" and self.title == "" and self.tn == "":
			return True
		else:
			return False
# end of release }}} #




# class -- release () {{{
# class to manage a single release
# ****************************** #
class release:

	# constructor
	def __init__(self):
		# init all variables
		self.catid = ""
		self.shortinfo = ""
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
	
	# function -- search_track
	# @ a track
	# < list of tracks
	# search for a track in an release instance
	# ***************************************** #
	def search_track(self, tr):
		sFktname = "search_track"
		
		# create match lists - these lists contains all
		# items from artist and title wich are separated
		# by spaces
		set_artist_wanted = tr.artist.lower().split()
		set_title_wanted = tr.title.lower().split()

		ePrint(2, sFktname, "looking for track: {} {}".format(set_artist_wanted, set_title_wanted))

		min_hits = 0.0
	
		match_list = []
		match_list2	= []

		for item in self.tunes:

			# try to match the artist, at least the half of
			# elements from the target set has to be matched
			set_target = item.artist.lower().split()
			min_hits = ceil(len(set_target) * 0.5)

			match = False
			matchc = 0
			
			for i in set_artist_wanted:
				if i in set_target:
					matchc += 1
				if matchc >= min_hits:
					match = True
					match_list.append(item)
					break

		# if we already have found the track
		if len(match_list) == 1:
			return match_list

		# try to match title
		if len(match_list) > 1:
			for item in match_list:
				
				set_target = item.title.lower().split()
				min_hits = ceil(len(set_target) * 0.5)

				match = False
				matchc = 0

				for i in set_title_wanted:
					if i in set_target:
						matchc += 1
					if matchc >= min_hits:
						match = True
						match_list2.append(item)
						break

		ePrint(2, sFktname, match_list2)

		return match_list2
		# end of search_track		
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
	track_1.artist = "Black Sun Empire"
	track_1.title = "Infusion"
	
	track_2 = track()
	track_2.artist = "Black Sun Empire"
	track_2.title = "Infusion lala vip"

	track_3 = track()
	track_3.artist = "Sighter & Aphector"
	track_3.title = "Infusion"

	rel = release()
	rel.append (track_1)
	rel.append (track_2)
	rel.append (track_3)


	search_track = track()
	search_track.artist = "black sun"
	search_track.title = "infusion"

	rel.search_track(search_track)

# end of main




if __name__ == "__main__":
	main()
