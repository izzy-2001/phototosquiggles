from turtle import back
import random

PXSIZE = 30
FNAME = "mona-lisa-face.pgm"
DIV = 7 #what it takes to divide a number into a range of 0 to 36

def preamble(file, rows, cols):
    width = cols*PXSIZE
    height = rows*PXSIZE
    file.write("%!PS-Adobe-3.0 EPSF-3.0\n%%BoundingBox: " + str(0) + " " +str(0) + " " + str(width+PXSIZE*2) + " " + str(height+PXSIZE*2) + "\n")
    file.write("/pxsize " + str(PXSIZE) + " def\n" )
    file.write("pxsize pxsize translate\n")
    print()

def Pixel(file, pixelNumber, x, y, d):
    file.write( str((y*PXSIZE- PXSIZE)/2) + " " + str((x*PXSIZE)/2) + " " + str(d) + " pixel" + str(pixelNumber) + "\n")

def fileEnd(file):
    file.write("showpage\n" + "%"+"EOF")



def main():
    print("===========================================================")
    print("phototosquiggles.py. Created by Izzy Snyder in May-June 2022. Converts a pgm file into a 'Szpakowski-like' line drawing.")
    print("===========================================================")

    f = open(FNAME, "rb")
    
    f.readline()
    firstLine = f.readline()
    firstLineList = firstLine.split()
    NUMCOLS = int(firstLineList[0])
    NUMROWS = int(firstLineList[1])
    f.readline()

    out = open("output.eps", "w")
    preamble(out, NUMROWS, NUMCOLS)

    out = open("output.eps", "a")
    backup = open("backup.eps", "r+")
    for line in backup:
        # append content to second file
        out.write(line)
    out.write("\n")

    #on even rows, go left to right. On odd rows, go right to left
    for y in range(NUMROWS):
        for x in range(NUMCOLS):
            gray = f.read(1)
            if gray != "":
                gray = ord(gray)+1
                gray = int(gray/DIV)
                gray = 36-gray                  
                
                """ if gray <= 9:
                    pixnum = random.choice([24, 25, 26, 34, 35])

                elif gray <= 13:
                    pixnum = random.choice([28, 31])

                elif gray <= 14:
                    pixnum = 39
                
                elif gray <= 17:
                    pixnum = random.choice([21,27,30,36])

                elif gray <= 21:
                    pixnum = random.choice([18,19,20,29,32,33])

                elif gray <= 22:
                    pixnum = 38

                elif gray <= 28:
                    pixnum = 23

                elif gray <= 29:
                    pixnum = 22

                elif gray <= 30:
                    pixnum = 37

                else:
                    pixnum = 40
                    
                if x == 0: #start pixels
                    if y%2 == 0: #left start
                        Pixel(out,pixnum,x,NUMROWS-y, 0)
                    else: #right start
                        #leftRowEndPixel(out,pixel,x,NUMROWS-y)
                        Pixel(out,pixnum,x,NUMROWS-y, 0)
                elif x == NUMCOLS-1: #end pixels
                    if y%2 == 0: #right end
                        #rightRowEndPixel(out,pixel,x,NUMROWS-y)
                        Pixel(out,pixnum,x,NUMROWS-y, 0)
                    else: #left end
                        #rightRowBeginPixel(out,pixel,x,NUMROWS-y)
                        Pixel(out,pixnum,x,NUMROWS-y, 0)
                else: #middle pixels """

            if gray <= 9:
                pixnum = random.choice([0, 0, 0, 0, 10, 12])

            elif gray <= 11:
                pixnum = random.choice([10, 12])

            elif gray <= 13:
                pixnum = random.choice([8, 9, 11, 17])

            elif gray <= 15:
                pixnum = random.choice([6, 7, 13, 14])
            
            elif gray <= 20:
                pixnum = 15

            elif gray <= 21:
                pixnum = random.choice([1,2,3,18,19])

            elif gray <= 25:
                pixnum = 4

            elif gray <= 26:
                pixnum = random.choice([5, 16])

            else:
                pixnum = random.choice([5, 18, 18, 18])

            #genericPixel(out,pixel,x,NUMROWS-y)
            Pixel(out,pixnum,x,NUMROWS-y, 0)
    fileEnd(out)


main()