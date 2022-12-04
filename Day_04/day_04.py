# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:49:29 2022

@author: Fazuximy
"""

from dataclasses import dataclass

@dataclass
class CleanUpPairs:
    elf_1_sections:list
    elf_2_sections:list
    wholly_within: bool
    overlapping_sections: list
    number_of_overlapping_sections: int
    
# Task 1

"""
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned 
the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. 
To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

In how many assignment pairs does one range fully contain the other?
"""


data_path = "Z:/python_stuff/advent_of_code_2022/Day_04/data/"
file_name = "input.XSCORE"

with open(data_path+file_name, "r") as input_file:
    text_input_file = input_file.read()

clean_up_pair_data_list = []

clean_up_pairs = text_input_file.split("\n")[:-1]

for clean_up_pair in clean_up_pairs:
    
    pairs = clean_up_pair.split(",")
    
    elf_1_range = [int(numb) for numb in pairs[0].split("-")]
    
    elf_1_sections = list(range(elf_1_range[0],elf_1_range[1]+1))
    
    elf_2_range = [int(numb) for numb in pairs[1].split("-")]
    
    elf_2_sections = list(range(elf_2_range[0],elf_2_range[1]+1))
    
    if set(elf_1_sections).issubset(elf_2_sections) or set(elf_2_sections).issubset(elf_1_sections):
        wholly_within = True
    else:
        wholly_within = False
        
    overlapping_sections = list(set(elf_1_sections).intersection(elf_2_sections))
    
    number_of_overlapping_sections = len(overlapping_sections)
        
    clean_up_pair_data_list.append(CleanUpPairs(elf_1_sections, elf_2_sections, wholly_within, overlapping_sections, number_of_overlapping_sections))
    
    
number_of_fully_contrained_ranges = sum([int(clean_up_pair_data.wholly_within) for clean_up_pair_data in clean_up_pair_data_list])

print(f"The number of assigment pairs where one is fully contrained by the other is: {number_of_fully_contrained_ranges}")


# Task 2

"""
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In how many assignment pairs do the ranges overlap?
"""

pairs_with_overlapping_ranges = sum([int(clean_up_pair_data.number_of_overlapping_sections > 0) for clean_up_pair_data in clean_up_pair_data_list])

print(f"The number of assignment pairs where the ranges overlap is: {pairs_with_overlapping_ranges}")


