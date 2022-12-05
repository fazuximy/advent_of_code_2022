# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:56:08 2022

@author: Fazuximy
"""

from dataclasses import dataclass
import re

@dataclass
class MoveData:
    move_number:int
    from_stack: int
    to_stack: int
    
# Task 1

"""
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, 
but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, 
the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, 
the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where,
 and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input).

After the rearrangement procedure completes, what crate ends up on top of each stack?
"""



data_path = "Z:/python_stuff/advent_of_code_2022/Day_05/data/"
file_name = "input.XSCORE"

with open(data_path+file_name, "r") as input_file:
    text_input_file = input_file.read()

# Cleaning input data

stacks_and_moving_information = text_input_file.split("\n\n")


# Getting the information about the stacks of crates

stack_information_lines = stacks_and_moving_information[0].split("\n")

stack_crates = [re.findall("(\[\w\](?:\Z|\s)|\s\s\s(?:\Z|\s))", stack_line) for stack_line in stack_information_lines[:-1]]

stack_numbers = stack_information_lines[-1].split("  ")
stack_numbers = [int(number) for number in stack_numbers]

stack_dict = dict(zip(stack_numbers,[[] for _ in stack_numbers]))

for crate_stack in list(reversed(stack_crates)):
    
    for numb, crate in enumerate(crate_stack):
    
        real_crate = re.findall("\w", crate)
        
        if len(real_crate) > 0:
            
            stack_dict[(numb+1)] = stack_dict[(numb+1)] + real_crate
        


# Getting the information about the moves        

moving_information_list = stacks_and_moving_information[1].split("\n")[:-1]

moving_data_list = []

for move in moving_information_list:
    
    move_number = int(re.findall("move\s(\d+)", move)[0])
    
    from_stack = int(re.findall("from\s(\d+)", move)[0])
    
    to_stack = int(re.findall("to\s(\d+)", move)[0])
    
    moving_data_list.append(MoveData(move_number, from_stack, to_stack))
    
    

# Performing the moves on the crates
for move_data in moving_data_list:
    
    crates_to_move = stack_dict[move_data.from_stack][-(move_data.move_number):]
    
    stack_dict[move_data.from_stack] = stack_dict[move_data.from_stack][:(len(stack_dict[move_data.from_stack])-len(crates_to_move))]
    
    stack_dict[move_data.to_stack] = stack_dict[move_data.to_stack] + list(reversed(crates_to_move))
    
    
print(f'The crates that end on top are: {"".join([i[-1] for i in stack_dict.values()])}')



# Task 2

"""
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, 
and the ability to pick up and move multiple crates at once.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. 
After the rearrangement procedure completes, what crate ends up on top of each stack?
"""


# Get new dictionary for the stacks of crate to perform new movements on them

stack_dict_9001 = dict(zip(stack_numbers,[[] for _ in stack_numbers]))

for crate_stack in list(reversed(stack_crates)):
    
    for numb, crate in enumerate(crate_stack):
    
        real_crate = re.findall("\w", crate)
        
        if len(real_crate) > 0:
            
            stack_dict_9001[(numb+1)] = stack_dict_9001[(numb+1)] + real_crate
        

# Performing the new movements on the stacks of crates with the CrateMover 9001 machine

for move_data in moving_data_list:
    
    crates_to_move = stack_dict_9001[move_data.from_stack][-(move_data.move_number):]

    stack_dict_9001[move_data.from_stack] = stack_dict_9001[move_data.from_stack][:(len(stack_dict_9001[move_data.from_stack])-len(crates_to_move))]
    
    stack_dict_9001[move_data.to_stack] = stack_dict_9001[move_data.to_stack] + list(crates_to_move)
    
    
print(f'The crates that end on top with the CrateMover 9001 machine are: {"".join([i[-1] for i in stack_dict_9001.values()])}')

