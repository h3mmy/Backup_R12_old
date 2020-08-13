#!/usr/bin/env python

# Getting file descriptors

f = open('input-1.in', 'r')     # Replace with appropriate file name
s = open('outputfile', 'w')

# Getting input and processing

LineNum = 0

for line in f:
    if LineNum == 0:
        NumCases = int(line)
        LineNum += 1
    else:
        s.write("Case #%d: %s\n"%(LineNum,process(line)))
        LineNum += 1


# Closing files

f.close()
s.close()