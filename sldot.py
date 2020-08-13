#!/usr/bin/env python

# Importing necessary modules

import urllib
import string

# Download homepage for slashdot.org

page = urllib.urlretrieve('http://www.slashdot.org/', 'page.html')

# Write html code to file

## Done already

# Opening file(s)

file = open(page[0], 'r')
checkr = open('quotes', 'r')

# Filter out the <div class="rightcontent"> <small>TAGLINE</small> </div> tagline element

linelist = file.read()         # Reading webpage into a string
file.close()

codeline = ' '.join(linelist.split())     # Removing whitespace

seglist = codeline.split('</blockquote>')

for item in seglist:                              # Getting wanted section
    if "<blockquote class=\"msg grid_24\"" in item:
        Reqline = item

tagline = Reqline.split('<blockquote class="msg grid_24" cite="http://slashdot.org"><p>')[1].split('</p>')[0]


# Check last extract

last = checkr.readlines().pop()
checkr.close()
writ = open('quotes', 'a')

if str(tagline + "\n") != str(last):
    writ.write(tagline + "\n")
    print tagline


# If new, add to file/database

# Repeat as cron job or import the time module and go repeat? 