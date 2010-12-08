

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

Synopsis: remeta file1 file2 ... [ -c ] [ -p pattern ]
  -c	| --copy     make a copy of original files before copying
  -h	| --help     print this help
  -p	| --pattern  specify pattern for renaming

Keys for patterns:
%a - Artist
%t - Title
%n - Track number
%k - Harmonic key

Examples:
	
	remeta -c -p "%a - %t - %k" nicemusic.mp3

	This fetches artist, title and key for the given file, but makes
	a copy of the original files.



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


