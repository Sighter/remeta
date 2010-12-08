#!/usr/bin/python3

# id3ed.py -- module handle communication with id3ed
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2010-12-04.
# @Revision:    0.1

from release import track

import stagger
from stagger.id3 import *


# function -- id3_to_track
# @ filename
# < a new trak instance
# fetches information using the stagger lib
# ***************************************** #
def id3_to_track (filepath):
	sFktname = "id3_to_track"
	
	tag = stagger.read_tag(filepath)
	
	track_new = track()

	track_new["artist"] = tag.artist
	track_new["title"] = tag.title
	track_new["tn"] = tag.track
	
	return track_new
# end of id3_to_track




# function -- main
# @ none
# < none
# testing function
# **************** #
def main ():
	sFktname = "main"
	
	filename = "Noisia_Crank_Original_Mix.wav"
	
	track_new = id3_to_track(filename)

	print(track_new)
# end of main




if __name__ == "__main__":
	main()
