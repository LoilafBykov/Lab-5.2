import csv
import sys
large=0
space=0
catalog=[]
my_file="FairyTale.txt"
fd=open(my_file,'r')
reader=csv.reader(fd, delimiter="\n")
for series in fd:
    space=space+series.count(' ')
    large=large+len(series)
    words=series.split(' ')
    catalog.append(words)
fd.close()
print(large)
print(space)
print('words=',len(catalog))
print(my_file[0])
input()