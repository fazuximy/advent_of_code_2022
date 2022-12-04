# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:37:48 2022

@author: Fazuximy
"""

from dataclasses import dataclass
import string

@dataclass
class RucksackData:
    content: str
    first_pouch: str
    second_pouch: str
    item_in_both_pouches: str
    priority_score: int

    
# Task 1

"""
The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. 
Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in 
each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the 
characters represent items in the second compartment.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
"""

item_list = [i for i in string.ascii_lowercase + string.ascii_uppercase]
    
item_priority_dictionary = dict(zip(item_list, list(range(1,len(item_list)+1))))



data_path = "Z:/python_stuff/advent_of_code_2022/Day_03/data/"
file_name = "input.XSCORE"

with open(data_path+file_name, "r") as input_file:
    text_input_file = input_file.read()

rucksack_data_list = []

rucksacks = text_input_file.split("\n")
rucksacks = rucksacks[:-1]

for rucksack in rucksacks:
    
    content = rucksack
    
    first_pouch = rucksack[:int(len(rucksack)/2)]
    second_pouch = rucksack[int(len(rucksack)/2):]
    
    item_in_both_pouches = set(first_pouch).intersection(second_pouch)
    
    if len(item_in_both_pouches) != 1:
        print(f"Oh no! item_in_both_pouches is: {item_in_both_pouches}")
    else:
        item_in_both_pouches = str(list(item_in_both_pouches)[0])
        
        priority_score = item_priority_dictionary[item_in_both_pouches]
        
        rucksack_data_list.append(RucksackData(content,first_pouch, second_pouch, item_in_both_pouches, priority_score))
        
        
summed_priority_score = sum([rucksack_data.priority_score for rucksack_data in rucksack_data_list])
        
print(f"The sum of the priority scores of the items that appear in both compartments is: {summed_priority_score}")    


# Part 2   

"""
For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. 
For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. 
That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, 
and at most two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges 
need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item 
type is the right one is by finding the one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item 
type.

Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
"""

group_index = list(range(0,len(rucksack_data_list),3))
badge_priority_list = []

for group_start in group_index:
    group_badge = set.intersection(*map(set,[rucksack_data.content for rucksack_data in rucksack_data_list[group_start:group_start+3]]))
    badge_priority = item_priority_dictionary[list(group_badge)[0]]
    badge_priority_list.append(badge_priority)

print(f"The sum of the priority scores of the group badges is: {sum(badge_priority_list)}")



