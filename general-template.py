#!/usr/bin/env python

# Getting file descriptors

f = open('sample', 'r')     # Replace with appropriate file name
s = open('outputfile', 'w')

# Getting input and processing



def process():
    
   
NumCases = int(f.readline().rstrip())
CaseNum = 0
N = 0
M = 0

for CaseNum != NumCases:
    N = int(readline().rstrip())
    i = 0
    while i != N:
        l = f.readline().rstrip()
        #Do Something
        i += 1
    i = 0
    while i != M:
        l = f.readline().rstrip()
        # Do Something
        i += 1
    s.write("Case #%d: %s\n"%(CaseNum,process(deck,hand)))
            


# Closing files

f.close()
s.close()