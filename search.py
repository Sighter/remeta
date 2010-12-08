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
import cache




# function -- search_clever
# @ a track object
# < a track object or none on failure
# search for a track, while checking the cache
# **************************
def search_clever (tr):
	sFktname = "search_clever"
	
	# build search-term
	if tr.artist != "" and tr.title != "":
		term = tr.artist + "+" + tr.title
		term = term.replace("&","")
		term = term.replace(" ","+")
	
	# first try to find the track in the release
	# cache
	if len(cache.rels_found) > 0:
		for rel in cache.rels_found:

			ePrint(1, sFktname, "search in cache")

			# search track in release
			res = rel.search_track(tr)

			# nothing found
			if res == None:
				continue

			# more than one item found
			if len(res) > 1:
				ePrint(1, sFktname, "Multiple tracks found in release, make a choice")
				k = 0
				for t in res:
					print("{0:3d}:\t{1}".format(k , t))
					k = k + 1
				print("\n")
				choice = int(input(" <-- "))
				res = res[choice]
				return res

			return res[0]

	ePrint(1, sFktname, "search the web")

	# search on chemical
	query_chemical = chemical.chemical()
	results = query_chemical.search(term)

	# case if nothing was found
	if len(results) == 0:
		return None

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

	# append the release to the cache
	cache.rels_found.append(rel)

	# search track in release
	res = rel.search_track(tr)

	# nothing found
	if res == None:
		return None

	# more than one item found
	if len(res) > 1:
		ePrint(1, sFktname, "Multible tracks found in release, make a choice")
		k = 0
		for t in res:
			print("{0:3d}:\t{1}".format(k , t))
			k = k + 1
		print("\n")
		choice = int(input(" <-- "))
		res = res[choice]
	
	return res[0]
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

	res = search_clever(track_new)
	print(res)

	track_new.artist = "Futurebound camo krooked"
	track_new.title = "chic"

	res = search_clever(track_new)
	print(res)

# end of main




if __name__ == "__main__":
	main ()
