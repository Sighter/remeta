#!/usr/bin/python3

# search.py -- module to clever search for the information
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2010-12-06.
# @Revision:    0.1


from release import track
from release import release

from helpers import ePrint

import chemical




# function -- search_clever
# @ a track object
# < a track object
# search for a track, while checking the cache
# **************************
def search_clever (tr):
	sFktname = "search_clever"
	
	# build search-term
	if tr.artist != "" and tr.title != "":
		term = tr.artist + "+" + tr.title
		term = term.replace(" ","+")

	# search on chemical
	query_chemical = chemical.chemical()
	results = query_chemical.search(term)
	print(results)

	# case, if more then one was found
	if len(results) > 1:
		ePrint(1, sFktname, "Multiple Links found. Make a Choice\n")
		k = 0
		for i in results:
			print("{0:3d}:\t{1}".format(k , results[k][1]))
			k = k + 1
		print("\n")
		choice = int(input(" <-- "))
		results = [ [ results[choice][0], results[choice][1] ] ]

	# create an release instance and feed it
	rel = release()
	rel.shortinfo = results[0][1]
	rel.infopage = results[0][0]
	rel = query_chemical.getReleaseInfo(rel)



# end of search_clever




# function -- main
# @ none
# < none
# test
# **************************
def main ():
	sFktname = "main"
	track_new = track()
	
	track_new.artist = "Inside Info"
	track_new.title = "Awkward"

	search_clever(track_new)

# end of main




if __name__ == "__main__":
	main ()
