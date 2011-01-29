#!/usr/bin/python3

# release.py -- Module to hold the release class and his sub classes
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2010-12-04.
# @Revision:    0.1

from math import ceil
from helpers import ePrint
from settings import quint_map
from operator import itemgetter



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
		s = self.artist + " - " + self.title + " - " + self.key + " - " + quint_map[self.key]
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
	# < list of tracks none if zero found
	# search for a track in an release instance
	# ***************************************** #
	def search_track(self, tr):
		sFktname = "search_track"
		
		# build search term. so connect artist and
		# title, delete some characters and split on
		# white spaces
		search_term_list = tr.title.lower() + " " + tr.artist.lower()

		search_term_list = search_term_list.replace("(","").replace(")","")

		search_term_list = search_term_list.split()

		ePrint(2, sFktname, "looking for term: {}".format(search_term_list))

		# to find the track, we constuct a ranking, with the term on the highest rank, wich
		# made the most hits 
		max_hits = 0
	
		match_list = []

		for item in self.tunes:

			item_hits = 0

			# create target term
			search_target_list = item.artist.lower() + " " + item.title.lower()
			search_target_list = search_target_list.split()

			# match
			for s in search_term_list:
				if s in search_target_list:
					item_hits += 1
			
			# create a matchcount, item tupel
			match_list.append((item_hits, item))

		if match_list == 0:
			return None

		# sort matchlist
		match_list = sorted(match_list, key = lambda tup: tup[0], reverse = True)
		
		
		return [match_list[0][1]]

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
	track_1.artist = "Noisia"
	track_1.title = "Inf"
	
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
