

% README.txt, 2010-12-06 -- The REMETA script


*******************
* 1. Introduction *
*******************

You can use this script to rename your sound file with a specified
pattern. First, remeta tries to fetch the information from tags.
If some wanted information is not found, as it will be for the 
harmonic keys, it tries to fetch the information from the web.

To use the script simply clone the repository with
	
	git clone git://github.com/Sighter/remeta.git

Then make a link to a folder which is present in your PATH
variable.

	ln -s path/to/git/repo/remeta.py path/to/your/bin/PATH/remeta



************
* 2. Usage *
************

Synopsis: remeta [ -c ] [ -p pattern ] [ -s term ] file1 file2 ...
  -c	| --copy     make a copy of original files before copying
  -h	| --help     print this help
  -p	| --pattern  specify pattern for renaming
  -w	|            use Cemelot format for keys
  -s	| --search   search for release, to append this to the cache

Keys for patterns:
%a - Artist
%t - Title
%n - Track number
%k - Harmonic key

Examples:
	
	remeta -c -p "%a - %t - %k" nicemusic.mp3

	This fetches artist, title and key for the given file, but makes
	a copy of the original files.


	remeta -c -p -s "secure search" "%a - %t - %k" *.mp3

	This fetches artist, title and key for the given files (the current working dir), makes
	a copy of the original files, and searches for "secure search" first. So if a release is
	found, it is appended to the cache. After that all over files will be searched in this
	release first. This is good if want to gather information about an album and the first
	title does not match this album with the search.



*******************
* 3. Dependencies *
*******************
	id3ed
	python3-html5lib-hg




*********************
* 4. Known Problems *
*********************

 - if no tags are present, nothing can be found.
 - some tags do not work with id3ed
 - only mp3 can be read for now


