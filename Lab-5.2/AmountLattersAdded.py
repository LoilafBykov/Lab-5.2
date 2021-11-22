import csv
import sys
large=0
space=0
catalog2=[]
catalog1=[]
my_file="FairyTale.txt"
row=[]
fd=open(my_file,'r', encoding='utf8')
row=fd.readlines()
fd.close()
for part in row:
    large=large+len(part)
    part=part[0:-2]
    print(part)
    space=space+part.count(' ')
    words=part.split(' ')
    catalog1.append(words)
#print(catalog1[3])
print('Space=',space)
print('Large=',large)
P1=len(catalog1)
P2=0
all_words=0
sole_words=0
for i in range(P1):
    P2=len(catalog1[i])
    for j in range(P2):
        part=catalog1[i][j]
        all_words=all_words+1
        if part in catalog2:
            continue
        else:
            catalog2.append(part)
P1=len(catalog2)
sole_words=len(catalog2)
print('All words=',all_words)
print('Unique words=', sole_words)
input()