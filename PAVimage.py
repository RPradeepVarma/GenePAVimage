
from PIL import Image, ImageDraw
import sys
import operator
import numbers
from collections import defaultdict


str=defaultdict(list) # Structure values
ann=defaultdict(list) # Annotation data
origin=[]
im = Image.new('RGB', (5500, 30500), (255, 255, 255))
draw = ImageDraw.Draw(im)

def getstructure():
	with open(sys.argv[1]) as f:
		for line in f:
			line = line.strip('\n')
			linedata = line.split('\t')
			#linedata2=linedata.split('\t')
			#print( linedata[2])
			str[linedata[0]].append(linedata[1:])
			

def drawimg(name):
	print("Creating image")
	#(maxval,minval)=getrange(val)
	row=20
	#ecol=0
	for id in str: # Each structure ID and values in list
		scol=20
		i=1
		for vallist in str[id]: # List of values for above id
			#print(id, vallist, "++++++++")
			for val in range(1,len(vallist)):
				ecol=scol+15 # Set width of feature plot
				if(int(vallist[val]) == 1):
					(r,g,b)=255,0,0
					(r, g, b) = 255,127,80
					draw.line((scol, row, ecol, row), fill=(r, g, b), width=5)
					#print(vallist[val])
				else:
					(r,g,b)=0,0,255
					#print(vallist[val])
					draw.line((scol, row, ecol, row), fill=(r, g, b), width=20)

				scol=ecol
				i=i+20 # Set colours
				
		row=row + 1


	
	#lines.add(dwg.line(start=(800, 800), end=(1000, 800),  stroke=svgwrite.rgb(237,185,185, '%'), stroke_width=8))
	im.save('PAVplot.jpg', quality=95)

# ======================
getstructure()
print("Finished parsing structure data")
drawimg('PAV.svg')
print("Image ready")

'''
Usage: python PAVimage.py meanids.txt

meanids.txt
g10120  0       0       0       0
g10104  0       0       0       0
g1010   0       0       1       1
g10085  1       0       0       0
g10084  0       0       0       1
g10080  1       1       0       0
g10078  0       1       1       1
g10077  0       1       1       0
g1007   0       0       0       0
g10061  0       1       1       1
g10060  1       1       1       1
g10052  0       1       1       0
g10046  1       0       1       1
g10045  1       0       1       1
g10033  0       0       0       0
g10026  0       0       0       0
g10014  1       1       1       1
g10013  0       1       0       0
g10010  1       0       0       0
g10008  1       1       0       1




'''