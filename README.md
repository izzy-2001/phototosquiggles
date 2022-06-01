# phototosquiggles
Converts a .pgm file into a "Szpakowski-like" line drawing. Work in progress. 

Image gets output to "ouput.eps". Do not alter "backup.eps".

To change the image, change where it says "FNAME = mona-lisa-face.pgm" to be the name of your own image (including the filepath, if necessary). 

resources for generating low resolution pgm files from a source image:
-use https://www.reduceimages.com/ to reduce the size of your image. Make sure to make the size 5-20% and the quality 100%. This way it reduces the resolution but does not use compression.
-use https://convertio.co/jpg-pgm/ to convert the small image to a .pgm file
