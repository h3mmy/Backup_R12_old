#!/usr/bin/env python

# Importing modules

import os

# Defining functions

def GetCSV(InFile):
    """
    Gets InFile and adds item(s) into a list
    """
    OutList =[]
    fd = open(InFile, 'r')
    for line in fd:
        OutList.append(line)
        #print line
    return OutList

def ProcCSV(lst):
    """
    Processes lst for delimiters and sorts them into a multi-dimensional array
    """
    OutList = []
    MegaList = []
    for element in lst:
        for item in element.split(",,"):
            OutList.append(item.strip("\n"))
    for item in OutList:
        MegaList.append(item.split(","))     
    return MegaList

def GoogleUP(lst):
    """
    Add lst to Google Contacts (after some tweaks)
    """

    for n in range(0,len(lst)-7,1):           # Fixing Last Name ScrewUP {ADAPT}
        if n % 2 == 1:
            lst[n][0], lst[n][1] = lst[n][1], lst[n][0]
    
    # Another small adjustment in the list to fix Coaches
    for item in lst:
        if 'Coach' in item[0]:
            item.insert(1,'')
    
    # Constructing commands
    commandlist = []
    for item in lst:
        commandlist.append("google contacts add '%s %s, %s'"%(item[0],item[1],item[2]))
    for command in commandlist:
        os.system(command)
    
    
def main():
    PM = ProcCSV(GetCSV('/Users/zachariahaslam/Downloads/team.csv'))
    GoogleUP(PM)



# Processing

main()

# Output