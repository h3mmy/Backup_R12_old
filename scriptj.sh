#!/bin/bash


if [ $(ioreg -l | awk '/ExternalConnected/ {print $NF}') == "Yes" ]; then
  
 if [ $(expr $(expr $(ioreg -l | awk '/AvgTimeToFull/ {print $NF}') / 2) / 60) -ne 0 ]; then
  say $(expr $(expr $(ioreg -l | awk '/AvgTimeToFull/ {print $NF}') / 2) / 60) Hours
 fi
 if [ $(expr $(expr $(ioreg -l | awk '/AvgTimeToFull/ {print $NF}') / 2) % 60) -ne 0 ]; then 
  say $(expr $(expr $(ioreg -l | awk '/AvgTimeToFull/ {print $NF}') / 2) % 60) Minutes remaining
 fi
  say $(ioreg -l | grep -i capacity | tr '\n' ' | ' | awk '{printf("%.2f%%", $10/$5 * 100)}')
  say "until FULL"

else 
 
 if [ $(expr $(ioreg -l | awk '/AvgTimeToEmpty/ {print $NF}') / 60) -ne 0 ]; then
 say $(expr $(ioreg -l | awk '/AvgTimeToEmpty/ {print $NF}') / 60) Hours
 fi 
 if [ $( expr $(ioreg -l | awk '/AvgTimeToEmpty/ {print $NF}') % 60) -ne 0 ]; then 
 say $( expr $(ioreg -l | awk '/AvgTimeToEmpty/ {print $NF}') % 60) Minutes
 fi 
 say "Remaining"
 say $(ioreg -l | grep -i capacity | tr '\n' ' | ' | awk '{printf("%.2f%%", $10/$5 * 100)}')
 say "to EMPTY"

fi


