#!/usr/bin/env python

# Importing modules


# Defining Global Variables


# Defining Classes

class HtmlFile(object):
    """ Class object of an html file """
    
    def __init__(self, fd):
        """ Constructor to import the file as a string """
        self.file = fd.read()
    
    def notags(self):
        """ Function to remove all html tags and definitions from code """
        self.lefts = self.file.split('>')
        self.ends = []
        self.stg = []
        for s in self.lefts:
            self.ends.append(s.split('</')[0])
        for s in self.ends:
            if '<' in s:
                self.stg.append(s.split('<')[0])
        return ''.join(self.stg)
        
    def __str__(self):
        """ String Representation of file """
        return self.file
        
    def __repr__(self):
        """ Representation operand pointing to __str__ """
        return self.__self__()
        
# Defining Global Functions

def main():
    """ Main function of program """
    
    fd = open('/Users/zachariahaslam/Desktop/FileT', 'r')
    newFile = HtmlFile(fd)
    fd.close()
    
    ft = open('/Users/zachariahaslam/Desktop/ft', 'w')
    ft.write(newFile.notags())
    ft.close()

# Running program

main()
