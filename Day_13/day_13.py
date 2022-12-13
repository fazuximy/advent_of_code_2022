# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:53:13 2022

@author: Fazuximy
"""

# Task 1
print("Task 1")


"""
Your handheld device must still not be working properly; the packets from the distress signal got decoded out of order. You'll need to re-order 
the list of received packets (your puzzle input) to decode the message.

Your list consists of pairs of packets; pairs are separated by a blank line. You need to identify how many pairs of packets are in the right order.

Packet data consists of lists and integers. Each list starts with [, ends with ], and contains zero or more comma-separated values 
(either integers or other lists). Each packet is always a list and appears on its own line.

When comparing two values, the first value is called left and the second value is called right. Then:

If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs 
are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, 
the inputs are the same integer; continue checking the next part of the input.
If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of 
items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. 
If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the 
comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found 
by instead comparing [0,0,0] and [2].

Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?
"""


from dataclasses import dataclass
import json
from itertools import zip_longest
from functools import cmp_to_key
import math

@dataclass
class PacketPairs:
    index: int
    packet1: list
    packet2: list
    


data_path = "Z:/python_stuff/advent_of_code_2022/Day_13/data/"
file_name = "input.XSCORE"

with open(data_path+file_name, "r") as input_file:
    text_input_file = input_file.read()
 
list_of_packet_pairs = text_input_file.split("\n\n")

packet_pair_class_list = []

for numb,packet_pair in enumerate(list_of_packet_pairs):
    packets = packet_pair.splitlines()
    packets = [json.loads(i) for i in packets]
    packet_pair_class_list.append(PacketPairs(numb+1,packets[0],packets[1]))
    

data_path = "Z:/python_stuff/advent_of_code_2022/Day_13/data/"
file_name = "test.txt"

with open(data_path+file_name, "r") as input_file:
    text_input_file = input_file.read()
 
test_packet_pairs = text_input_file.split("\n\n")

packet_pair_test_list = []

for numb,test_packet_pair in enumerate(test_packet_pairs):
    packets = test_packet_pair.splitlines()
    packets = [json.loads(i) for i in packets]
    packet_pair_test_list.append(PacketPairs(numb+1,packets[0],packets[1]))


def packet_generator(packet1, packet2):
    for subpacket1, subpacket2 in zip_longest(packet1,packet2):
            #print(subpacket1, subpacket2)
            if subpacket1 == None:
                yield True
            elif subpacket2 == None:
                yield False
            elif isinstance(subpacket1,int) and isinstance(subpacket2,int):
                if subpacket1 < subpacket2:
                    yield True
                elif subpacket1 > subpacket2:
                    yield False
                elif subpacket1 == subpacket2:
                    continue
            elif isinstance(subpacket1,list) and isinstance(subpacket2,int):
                yield from  packet_generator(subpacket1,[subpacket2])
            elif isinstance(subpacket1,int) and isinstance(subpacket2,list):
                yield from  packet_generator([subpacket1],subpacket2)
            else: 
                yield from packet_generator(subpacket1,subpacket2)
    #print("")
            
# To test on test data       
#print([all(list(packet_generator(packet_pair.packet1,packet_pair.packet2))) for packet_pair in packet_pair_test_list])

in_right_order = [packet_pair.index for packet_pair in packet_pair_class_list if list(packet_generator(packet_pair.packet1,packet_pair.packet2))[0] == True]

result_task_1 = sum(in_right_order)
print(f"The sum of the indeces of those pairs is: {result_task_1}")


# Task 2
print("Task 2")

"""
The distress signal protocol also requires that you include two additional divider packets:

[[2]]
[[6]]

Using the same rules as before, organize all packets - the ones in your list of received packets as well as 
the two divider packets - into the correct order.

Afterward, locate the divider packets. To find the decoder key for this distress signal, you need to determine the indices of the two 
divider packets and multiply them together. (The first packet is at index 1, the second packet is at index 2, and so on.) 

Organize all of the packets into the correct order. What is the decoder key for the distress signal?
"""


def sorting_packets(packet1, packet2):
    
    answer = int(list(packet_generator(packet1, packet2))[0])
    
    if answer == 1:
        return -1
    else:
        return 1

packet_list = []

for numb,packet_pair in enumerate(list_of_packet_pairs):
    packets = packet_pair.splitlines()
    [packet_list.append(json.loads(i)) for i in packets]
packet_list_with_decoders = packet_list + [[[2]],[[6]]]

sorted_packets = sorted(packet_list_with_decoders,key=cmp_to_key(sorting_packets))

result_task_2 = math.prod([j+1 for j,i in enumerate(sorted_packets) if i in [[[2]],[[6]]]])

print(f"The product of the indexes for the decoder keys is: {result_task_2}")
