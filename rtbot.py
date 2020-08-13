#!/usr/bin/env python

# Importing libraries

import sys 
import socket 
import string 
import os            # Temporary?

# Config params

HOST='irc.freenode.org'
PORT=6667  
NICK='ChiptuneDale'                # The bot's nickname 
IDENT='Chiptune_Dale' 
REALNAME='cool_bro' 
OWNER='H3MLOCK'                    # The bot owner's nick 
CHANNELINIT='#reddit-r4r'          # The default channel for the bot 
readbuffer=''                      # Message storage 

# Connecting

s=socket.socket( )               # Create the socket 
s.connect((HOST, PORT))          # Connect to server 
s.send('NICK '+NICK+'n')         # Send the nick to server 

s.send('USER '+IDENT+' '+HOST+' bla :'+REALNAME+'n') #Identify to server 

# Listening

while 1: 

    line=s.recv(500) 
    print line

    if line.find('MOTD')!=-1:
        s.send('JOIN '+CHANNELINIT+'n')

    if line.find('PRIVMSG')!=-1:

        parsemsg(line)                  ### WRITE FUNCTION FOR THIS
        line=line.rstrip()              # Remove trailing 'rn' 
        line=line.split() 

        if(line[0]=='PING'):            # If server pings then pong 
            s.send('PONG '+line[1]+'n') 