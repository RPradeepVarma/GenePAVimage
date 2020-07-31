
# GenePAVimage

The script will parse the tab-delimited input file with genes in rows and accessions in columns. The gene presence and absence are indicated in the binary matrix (0/1) format.

Note
Image dimensions are static and need to change accordingly in script

Output: PAV.svg

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
