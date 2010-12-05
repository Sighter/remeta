#!/usr/bin/python3

# id3ed.py -- module handle communication with id3ed
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2010-12-04.
# @Revision:    0.1

from release import track
import subprocess




# function -- id3_to_track
# @ filename
# < a new trak instance
# fetches information from id3ed and gives a track object
# ******************************************************* #
def id3_to_track (filepath):
	sFktname = "id3_to_track"
	
	p = subprocess.Popen(["id3ed", "-i", filepath], stdout = subprocess.PIPE)
	output = p.communicate()[0].decode().splitlines()
	p.wait()

	track_new = track()

	for item in output:
		if item.startswith("artist: ") == True:
			track_new["artist"] = item.lstrip("artist: ")
		elif item.startswith("songname: ") == True:
			track_new["title"] = item.lstrip("songname: ")
		elif item.startswith("tracknum: ") == True:
			track_new["tn"] = item.lstrip("tracknum: ")
	
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
