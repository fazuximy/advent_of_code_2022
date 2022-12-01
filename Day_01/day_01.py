# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:33:29 2022

@author: Fazuximy
"""


from dataclasses import dataclass

@dataclass
class ElfCalories:
    elf_id: int
    elf_calories: list
    summed_elf_calories: int


# Part 1

"""
The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. 
that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's 
inventory (if any) by a blank line.

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

data_path = "Z:/python_stuff/advent_of_code_2022/Day_01/data/"
file_name = "input.XSCORE"

with open(data_path+file_name, "r") as input_file:
    text_input_file = input_file.read()
    
elf_dataclass_list = []

calorie_list = text_input_file.split("\n\n")

for elf_id, elf_calories in enumerate(calorie_list):
    
    elf_calorie_list = [int(calorie) for calorie in elf_calories.split("\n") if calorie != ""]
    
    elf_dataclass_list.append(ElfCalories(elf_id,elf_calorie_list,sum(elf_calorie_list)))
    

top_1 = max([dataclass.summed_elf_calories for dataclass in elf_dataclass_list])
    
print(f"The total calories carried by the Elf that carries the most calories are: {top_1}")

# Part 2

"""
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most 
Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top 
three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.
"""
    
top_3_summed = sum(sorted([dataclass.summed_elf_calories for dataclass in elf_dataclass_list])[-3:])

print(f"The total calories carried by the top 3 Elves that carries the most calories are: {top_3_summed}")