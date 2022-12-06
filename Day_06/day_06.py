# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:33:27 2022

@author: Fazuximy
"""



# Part 1

"""
To be able to communicate with the Elves, the device needs to lock on to their signal. 
The signal is a series of seemingly-random characters that the device receives one at a time.

To fix the communication system, you need to add a subroutine to the device that detects a 
start-of-packet marker in the datastream. In the protocol being used by the Elves, the start of a 
packet is indicated by a sequence of four characters that are all different.

How many characters need to be processed before the first start-of-packet marker is detected?
"""

data_path = "Z:/python_stuff/advent_of_code_2022/Day_06/data/"
file_name = "input.XSCORE"

with open(data_path+file_name, "r") as input_file:
    text_input_file = input_file.read()
    

for char_start in range(0,len(text_input_file)-4):
    
    if len(set(text_input_file[char_start:char_start+4])) == 4:
        print(f"The number of characters needed to be processed before the first start-of-packet marker is detected is: {char_start+4}")
        break


# Part 2

"""
Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

How many characters need to be processed before the first start-of-message marker is detected?
"""

for char_start in range(0,len(text_input_file)-14):
    
    if len(set(text_input_file[char_start:char_start+14])) == 14:
        print(f"The number of characters needed to be processed before the first start-of-message marker is detected is: {char_start+14}")
        break
