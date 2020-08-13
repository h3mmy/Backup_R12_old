#!/bin/bash

# Defining functions

function runwifi {

## Assigning variables

ssid=$(airport -I | awk '/SSID/' | awk "NR==2{print;exit}" | awk -F':' '{ print $2 }')
agrctlrssi=$(airport -I | awk '/agrCtlRSSI/' | awk -F':' '{ print $2 }')
ssidcount=$(echo $ssid | wc -m)
signalstr=$(expr 100 + $agrctlrssi)

## Performing Action

[ $ssidcount == 0 ] && say "Not Associated" || say Associated with $ssid with signal strength $signalstr 

}

# Assigning variables

split=$(airport -I | awk '/Off/')
count=$(echo $split | wc -m)
count=$(expr $count - 1)

# Performing Action

[ $count != 0 ] && say "Airport is Off" || runwifi
