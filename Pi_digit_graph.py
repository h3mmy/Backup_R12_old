#!/usr/bin/env python

"""
Created by Zachariah Aslam
Copyright 2011 Infinitude Enterprises. All rights reserved.
"""

# Importing modules

import matplotlib.pyplot as plt

# Defining functions

def Handle(User_Input, b):
    """
    This function Processes The User input
    """
    if b == '' or b == '\n':
        b = 'ro-'
    
    if False not in [i not in User_Input for i in 'yn']:
        print "Error"
        main()
    elif User_Input == 'y':
        print "Will plot using matplotlib.pyplot"
        plot_graph(raw_input("Enter your number: "), b)
    else:
        print "Importing math module\n"
        
        import math
        
        print "Math module imported"
        print "Plotting with math.pi"
        plot_graph(math.pi, b)
    
def plot_graph(Num, bubble='ro-'):
    """
    This Function plots all the digits of the given number (Num)
    """
    
    Digit_list = [digit for digit in str(Num)]
    if '.' in Digit_list:
        Digit_list.remove('.')
    plt.plot([i for i in range(0,len(Digit_list), 1)],Digit_list, bubble)
    plt.show()
    
def main():
    
    Handle(raw_input("Would you like to enter your own number? "), raw_input("Bubble customization(Leave blank for deault): "))

main()