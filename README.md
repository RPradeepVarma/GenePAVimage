
# GenePAVimage

The script will parse the tab-delimited input file with genes in rows and accessions in columns. The gene presence and absence are indicated in the binary matrix (0/1) format.

Note
Image dimensions are static and need to change accordingly in script

# Input
file meanids.txt

g10120  0       0       0       0

g10104  0       0       0       0

g1010   0       0       1       1

g10085  1       0       0       0

g10084  0       0       0       1

g10080  1       1       0       0

g10078  0       1       1       1

# Output
![PAV image](https://github.com/pradeepruperao/GenePAVimage/blob/master/PAV.jpg)
PAV.jpg

# Usage
python PAVimage.py meanids.txt


