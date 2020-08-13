#!/usr/bin/env python

# Getting file descriptors

f = open('sample', 'r')     # Replace with appropriate file name
s = open('outputfile', 'w')

# Defining functions

def process(d, s):
    print d
    print s
    return 1
    

# Getting input and processing

LineNum = 0
CaseNum = 0
Dataline = 1
N = 0
M = 0
dct = []
tackleorder = ""

for line in f:
    if LineNum == 0:
        NumCases = int(line)
        LineNum += 1
    else:
        print line
        if LineNum == Dataline:
            N = int(line.split()[0])
            M = int(line.split()[1])
            dct = []
            LineNum +=1
        elif (LineNum-Dataline<=N):
            dct.append(line.rstrip())
            LineNum += 1
        elif (LineNum-Dataline<=N+M):
            tackleorder = line
            LineNum += 1
        else:
            s.write("Case #%d: %s\n"%(CaseNum,process(dct,tackleorder)))
            CaseNum += 1
            Dataline = LineNum +1
            LineNum += 1
        


# Closing files

f.close()
s.close()