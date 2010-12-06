# ***************************************************#
# Classes and functions to search on chemical records#
# ***************************************************#

# chemical search link
# http://www.chemical-records.co.uk/sc/search?must=GRIDUK040&Type=&inandout=true&SRI=true&ND=-1
# http://www.chemical-records.co.uk/sc/search?Sort=NI&Search=High+Rankin&inandout=both&All=True&ND=-1&Type=Music
from release import release
from helpers import getWebAsStr
from release import track
from helpers import subinstr
from html.parser import HTMLParser
import urllib.request

import html5lib
from html5lib import treebuilders, treewalkers, serializer



# class -- chemical () {{{
# manage access on chemical-records.co.uk 
# ************************************* #
class chemical:

	# function init -- {{{
	# @ catid
	# < none
	# ****************************** #
	def __init__(self):
		# site baselink
		self.baseUrl = r"http://www.chemical-records.co.uk"
	# end of __init__ }}} #



	# function fetch_HitLinks -- {{{
	# @ stream
	# < list of links to info pages
	# ****************************** #
	def fetch_HitLinks(self, stream):
		l_itemFound = False;
		l_linkList = []

		for item in stream:
			# check for item found
			if ("name" in item) and (item["name"] == "div"):
				for attTupel in item["data"]:
					if ("class" in attTupel) and ("item" in attTupel):
						l_itemFound = True

			# grab link
			if l_itemFound == True:
				if ("name" in item) and (item["name"] == "a"):
					for attTupel in item["data"]:
						if ("href" in attTupel):
							l_linkList.append(attTupel[1])
							l_itemFound = False
				

		return l_linkList;
	# end of __init__ }}} #



	# function fetch_ShortInfo -- {{{
	# @ stream
	# < list of short info
	# ****************************** #
	def fetch_ShortInfo(self, stream):
		l_itemFound = False;
		l_artistFound = False;
		l_titleFound = False;
		l_artistList = []
		l_titleList = []
		l_curArtist = ""
		l_curTitle = ""

		for item in stream:
			# check for item found
			if ("name" in item) and (item["name"] == "div"):
				for attTupel in item["data"]:
					if ("class" in attTupel) and ("item" in attTupel):
						l_itemFound = True

				# check if artist field ends
			if l_artistFound == True:
				if ("name" in item) and (item["name"] == "h4") and (item["type"] == "EndTag"):
					l_artistFound = False
					# add to list and init
					l_artistList.append(l_curArtist.strip())
					l_curArtist =  ""
						 
			# check if title field ends
			if l_titleFound == True:
				if ("name" in item) and (item["name"] == "p") and (item["type"] == "EndTag"):
					l_titleFound = False
					# add to list and init
					l_titleList.append(l_curTitle.strip())
					l_curTitle =  ""
						 
			# check if artist found
			if l_itemFound == True:
				if ("name" in item) and (item["name"] == "h4"):
					for attTupel in item["data"]:
						if ("class" in attTupel) and ("artist" in attTupel):
							l_artistFound = True

			# check if title found
			if l_itemFound == True:
				if ("name" in item) and (item["name"] == "p"):
					for attTupel in item["data"]:
						if ("class" in attTupel) and ("title" in attTupel):
							l_titleFound = True

			# fetch artists
			if l_artistFound == True:
				if item["type"] == "SpaceCharacters":
					l_curArtist += " "
				if item["type"] == "Characters":
					l_curArtist += item["data"]
				
			# fetch title
			if l_titleFound == True:
				if item["type"] == "SpaceCharacters":
					l_curTitle += " "
				if item["type"] == "Characters":
					l_curTitle += item["data"]
				

		# zip lists and return item
		l_shortInfoList = []
		for artist, title in zip(l_artistList, l_titleList):
			l_shortInfoList.append(artist + " -- " + title)

		return l_shortInfoList;
	# end of fetch_ShortInfo }}} #



	# function fetch_TuneInfo -- {{{
	# @ stream
	# < list of artist - title pairs
	# ****************************** #
	def fetch_TuneInfo(self, stream):
		l_itemFound = False
		l_tdCount = 0
		l_tuneList = []
		l_linkList = []
		l_artistList = []
		l_titleList = []
		l_keyList = []
		l_curArtist = ""
		l_curTitle = ""
		l_curKey = ""
		l_artistFound = False
		l_titleFound = False
		l_linkFound = False
		l_keyFound = False

		for item in stream:
			# check for item end
			if l_itemFound == True and ("name" in item) and (item["name"] == "tr") and (item["type"] == "EndTag"):
				l_itemFound = False

			# check for item found
			if ("name" in item) and (item["name"] == "tr"):
				for attTupel in item["data"]:
					if ("class" in attTupel) and (("odd" in attTupel) or ("even" in attTupel)):
						l_itemFound = True
						l_tdCount = 0

			# artist section end
			if (l_artistFound == True) and ("name" in item) and (item["name"] == "td") and (item["type"] == "EndTag"):
				l_artistFound = False
				l_artistList.append(l_curArtist.strip())
				l_curArtist = ""

			# title section end
			if (l_titleFound == True) and ("name" in item) and (item["name"] == "td") and (item["type"] == "EndTag"):
				l_titleFound = False
				l_titleList.append(l_curTitle.strip())
				l_curTitle = ""

			# key section end
			if (l_keyFound == True) and ("name" in item) and (item["name"] == "td") and (item["type"] == "EndTag"):
				l_keyFound = False
				l_keyList.append(l_curKey.strip())
				l_curKey = ""

			# Higher td count
			if (l_itemFound == True) and ("name" in item) and (item["name"] == "td") and (item["type"] == "StartTag"):
				l_tdCount += 1

			# artist section starts
			if (l_itemFound == True) and (l_tdCount == 2) and ("name" in item) and (item["name"] == "td") and (item["type"] == "StartTag"):
				l_artistFound = True

			# title section starts
			if (l_itemFound == True) and (l_tdCount == 3) and ("name" in item) and (item["name"] == "td") and (item["type"] == "StartTag"):
				l_titleFound = True

			# key section starts
			if (l_itemFound == True) and (l_tdCount == 4) and ("name" in item) and (item["name"] == "td") and (item["type"] == "StartTag"):
				l_keyFound = True

			# grab artist
			if (l_artistFound == True):
				if (item["type"] == "SpaceCharacters"):
					l_curArtist += " "
				if (item["type"] == "Characters"):
					l_curArtist += item["data"]

			# grab title
			if (l_titleFound == True):
				if (item["type"] == "SpaceCharacters"):
					l_curTitle += " "
				if (item["type"] == "Characters"):
					l_curTitle += item["data"]

			# grab key
			if (l_keyFound == True):
				if (item["type"] == "SpaceCharacters"):
					l_curKey += " "
				if (item["type"] == "Characters"):
					l_curKey += item["data"]

			# grab link
			if (l_itemFound == True) and ("name" in item) and (item["name"] == "a"):
				for attTupel in item["data"]:
					if ("class" in attTupel) and ("pbutton playmp3button" in attTupel):
						l_linkFound = True
				for attTupel in item["data"]:
					if ("href" in attTupel) and (l_linkFound == True):
						l_linkList.append(attTupel[1])
						l_linkFound = False

		# create tunelist
		for link, artist, title, key in zip(l_linkList, l_artistList,l_titleList, l_keyList):
			l_tuneList.append([link, artist, title, key]) 

		return l_tuneList
	# end of fetch_TuneInfo }}} #



	# function fetch_Catid -- {{{
	# @ stream
	# < list of links to info pages
	# ****************************** #
	def fetch_Catid(self, stream):
		l_itemFound = False;
		l_catidFound = False;
		l_catid = ""

		for item in stream:
			# read for catid found
			if (l_catidFound == True) and (item["type"] == "Characters"):
				return item["data"]

			# check for catid found
			if (l_itemFound == True) and (item["type"] == "Characters") and (item["data"] == "Catalog Number:"):
				l_catidFound = True

			# check for item found
			if ("name" in item) and (item["name"] == "div"):
				for attTupel in item["data"]:
					if ("class" in attTupel) and ("name" in attTupel):
						l_itemFound = True
				
		return l_catid
	# end of __init__ }}} #



	# function search -- {{{
	# @ searchterm
	# < dictionary with hit hame and the corresponding link
	# ***************************************************** #
	def search(self, term):
		# define link for search
		searchUrl = self.baseUrl + r"/sc/search?&must=" + term + r"&Type=Music"

		print(" --> searching on chemical for " + term)
		source = getWebAsStr(searchUrl)

		# create a parser, we use minidom
		p = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("dom"))
		dom_tree = p.parse(source)
		walker = treewalkers.getTreeWalker("dom")
		stream = walker(dom_tree)

		# now we can send the stream to our fetcher functions
		# find links on search result page
		l_hitLinks = self.fetch_HitLinks(stream)

		# find short info
		l_shortInfo = self.fetch_ShortInfo(stream)
		

		# create an two dimensional list
		results = []

		for link, info in zip(l_hitLinks, l_shortInfo):
			results.append([link, info]) 

		return results
	# end of search }}} #

	

	# function getReleaseInfo -- {{{
	# @ a release instance
	# < a feeded release instance
	# ****************************** #
	def getReleaseInfo(self, rel):
		
		source = getWebAsStr(rel.infopage)

		# create a parser, we use minidom
		p = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("dom"))
		dom_tree = p.parse(source)
		walker = treewalkers.getTreeWalker("dom")
		stream = walker(dom_tree)

		# get catid
		rel.catid = self.fetch_Catid(stream)

		# get tunelist
		l_tuneList = self.fetch_TuneInfo(stream)

		# build release tune list
		for tune in l_tuneList:
			temp = track()
			temp.link = tune[0]
			temp.artist = tune[1]
			temp.title = tune[2]
			temp.key = tune[3]
			rel.tunes.append(temp)

		# build links
		p = ""
		for tune in rel.tunes:
			# downloading file there links are in
			try:
				f = urllib.request.urlopen(self.baseUrl + tune.link).read()
				p = "/tmp/pymyrel-tmpinfo"
				
			except:
				print(" --> chemical.getReleaseInfo: An Error occured, while downloading linkfile")

			if p != "":
				output = open(p ,'wb')
				output.write(f)
				output.close()
				linkfile = open(p, 'r')
				for line in linkfile:
					if line.startswith("http://") == True:
						tune.link = line.strip("\n")

		if len(rel.tunes) > 0:
			print(rel)

		return rel
	# end of getReleaseInfo }}} #

# end of chemical }}} #
