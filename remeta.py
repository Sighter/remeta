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
from helpers import split_ld
from os import path
from os import rename
import shutil
from stagger_to_track import id3_to_track
import pattern
from search import search_clever
from search import search_release
import cache



# function -- print_help
# @ none
# < none
# function to print help
# **************************
def print_help ():
	sFktname = "print_help"
	print("Synopsis: remeta [ -c ] [ -p pattern ] [ -s term ] file1 file2 ...")
	print("  -c	| --copy     make a copy of original files before copying")
	print("  -h	| --help     print this help")
	print("  -p	| --pattern  specify pattern for renaming")
	print("  -w	|            use Cemelot format for keys")
	print("  -s	| --search   search for release, to append this to the cache\n")
	print("Keys for patterns:")
	print("%a - Artist")
	print("%t - Title")
	print("%n - Track number")
	print("%k - Harmonic key")
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
		opts, args = getopt.getopt(sys.argv[1:], "hcws:p:", ["help", "copy", "use-chemical-format", "search=", "pattern="])
	except:
		print_help ()
		sys.exit(2)

	# handle options
	for o, a in opts:
		if o in ("-h", "--help"):
			print_help()
			sys.exit(2)
		elif o in ("-c", "--copy"):
			settings.copymode = True
		elif o in ("-p", "--pattern"):
			settings.pattern_user = a
		elif o in ("-w", "--use-chemical-format"):
			settings.use_chemical_format = True
		elif o in ("-s", "--search"):
			settings.search_term = a
				
	# handle arguments
	if len(args) == 0:
		ePrint(1, sFktname, "No Files specified")
	
	# check, whether files have valid paths
	for fn in args:
		if path.exists(fn) == False:
			ePrint(1, sFktname, "Path not found: {}".format(fn))
			sys.exit(2)

	# if search_term is given search for it first
	# and if found append it to the cache
	if settings.search_term:
		rel = search_release(settings.search_term)
		if rel:
			cache.rels_found.append(rel)

	# enter main loop
	for fn in args:

		# fill pattern
		if settings.pattern_user:
			pat = pattern.pattern(settings.pattern_user)
		else:
			pat = pattern.pattern(settings.pattern_default)

		# try to get information from tags
		new_track = id3_to_track(fn)

		suffix = split_ld(fn)

		# we have flags in the pattern class to
		# determine wich keys are used

		res_t = None

		# currently we only can operate if we have some information
		if new_track.is_empty() == False: 
			# if artist field is set
			if pat.artist:
				if new_track.artist == "":
					res_t = search_clever(new_track)
					if res_t:
						new_track.artist = res_t.artist
					else:
						ePrint(1, sFktname, "Cant determine Artist Field for: {}".format(fn))
						continue
				pat.replace_artist(new_track.artist)

			# if title field is set
			if pat.title:
				if new_track.title == "":
					res_t = search_clever(new_track)
					if res_t:
						new_track.title = res_t.title
					else:
						ePrint(1, sFktname, "Cant determine title Field for: {}".format(fn))
						continue
				pat.replace_title(new_track.title)

			# if key field is set
			if pat.key:
				if new_track.key == "":
					res_t = search_clever(new_track)
					if res_t:
						# map key
						if (res_t.key in settings.quint_map) and settings.use_chemical_format == None:
							new_track.key = settings.quint_map[res_t.key]
						else:
							new_track.key = res_t.key
					else:
						ePrint(1, sFktname, "Cant determine key Field for: {}".format(fn))
						continue
				pat.replace_key(new_track.key)

			pat.replace_tn(new_track.tn)

			final_name = "{}.{}".format(pat.get_result(), suffix)
		else:
			final_name = fn

		ePrint(1, sFktname, "{} will be renamed to: {}".format(fn, final_name))

		# rename or copy
		if fn == final_name:
			continue
		else:
			if settings.copymode:
				shutil.copy(fn, final_name)
			else:
				rename(fn, final_name)
			

# end of main




if __name__ == "__main__":
	main ()
