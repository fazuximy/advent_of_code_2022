# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 15:19:09 2022

@author: Fazuximy
"""

# Part 1
print("Part 1")

"""
Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. 
If the head moves far enough away from the tail, the tail is pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able to model the positions 
of the knots on a two-dimensional grid. Then, by following a hypothetical series of motions 
(your puzzle input) for the head, you can determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) 
and tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching):

Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?
"""

import numpy as np

data_path = "C:/python_projects/advent_of_code_2022/Day_09/data/"
file_name = "input.XSCORE"

with open(data_path+file_name, "r") as input_file:
    text_input_file = input_file.read()
    
head_movements = text_input_file.split("\n")[:-1]

def get_neighbors(position):
    
    x = position[0]
    y = position[1]
    
    neighbor_list = []
    
    for x_add in range(-1,2):
        for y_add in range(-1,2):
            neighbor_list.append((x + x_add, y + y_add))
            
    return neighbor_list
    

head_position = (0,0)
tail_position = (0,0)

head_positions = []
head_positions.append(head_position)
tail_positions = []
tail_positions.append(tail_position)


for head_movement in head_movements:
    
    movement_input = head_movement.split(" ")
    
    movement_direction = movement_input[0]
    
    movement_times = int(movement_input[1])
    
    for single_move in range(0,movement_times):
        
        list_head_position = list(head_position)
        if movement_direction == "U":
            list_head_position[1] = list_head_position[1] + 1
            new_head_position = tuple(list_head_position)
        elif movement_direction == "D":
            list_head_position[1] = list_head_position[1] + -1
            new_head_position = tuple(list_head_position)
        elif movement_direction == "R":
            list_head_position[0] = list_head_position[0] + 1
            new_head_position = tuple(list_head_position)
        elif movement_direction == "L":
            list_head_position[0] = list_head_position[0] - 1
            new_head_position = tuple(list_head_position)
            
        head_positions.append(new_head_position)
        
        if new_head_position not in get_neighbors(tail_position):
            tail_position = head_position
            
        tail_positions.append(tail_position)
        
        head_position = new_head_position
            
    
print(f"The number of positions the tail of the rope visits at least once: {len(set(tail_positions))}\n")


# Part 2
print("Part 2")

"""
Rather than two knots, you now must simulate a rope consisting of ten knots. One knot is still the head of the rope and moves according 
to the series of motions. Each knot further down the rope follows the knot in front of it using the same rules as before.

Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?
"""

def not_same_column_or_row(position1,position2):
    return (position1[0] != position2[0]) and (position1[1] != position2[1])


def update_knot_position(current_knot,previous_knot,movement_direction):
    if previous_knot not in get_neighbors(current_knot):
        if not_same_column_or_row(previous_knot,current_knot) == True:
            list_current_knot = list(current_knot)
            if previous_knot[0] > current_knot[0] and previous_knot[1] > current_knot[1]:
                list_current_knot[0] = list_current_knot[0] + 1
                list_current_knot[1] = list_current_knot[1] + 1
                updated_knot = tuple(list_current_knot)
            elif previous_knot[0] < current_knot[0] and previous_knot[1] > current_knot[1]:
                list_current_knot[0] = list_current_knot[0] - 1
                list_current_knot[1] = list_current_knot[1] + 1
                updated_knot = tuple(list_current_knot)
            elif previous_knot[0] < current_knot[0] and previous_knot[1] < current_knot[1]:
                list_current_knot[0] = list_current_knot[0] - 1
                list_current_knot[1] = list_current_knot[1] - 1
                updated_knot = tuple(list_current_knot)
            elif previous_knot[0] > current_knot[0] and previous_knot[1] < current_knot[1]:
                list_current_knot[0] = list_current_knot[0] + 1
                list_current_knot[1] = list_current_knot[1] - 1
                updated_knot = tuple(list_current_knot)
            else:
                print("Error")
                
        else:
            list_current_knot = list(current_knot)
            list_previous_knot = list(previous_knot)

            list_current_knot[0] += (list_current_knot[0] != list_previous_knot[0]) * np.sign(list_previous_knot[0] - list_current_knot[0])
            list_current_knot[1] += (list_current_knot[1] != list_previous_knot[1]) * np.sign(list_previous_knot[1] - list_current_knot[1])

            updated_knot = tuple(list_current_knot)

    else:
        updated_knot = current_knot
        
    return updated_knot


head_position = (0,0)
tail_position = (0,0)

head_positions = []
head_positions.append(head_position)
tail_positions = []
tail_positions.append(tail_position)

position_2 = (0,0)
position_3 = (0,0)
position_4 = (0,0)
position_5 = (0,0)
position_6 = (0,0)
position_7 = (0,0)
position_8 = (0,0)
position_9 = (0,0)


for head_movement in head_movements:
    
    movement_input = head_movement.split(" ")
    
    movement_direction = movement_input[0]
    
    movement_times = int(movement_input[1])
    
    for single_move in range(0,movement_times):
        
        list_head_position = list(head_position)
        if movement_direction == "U":
            list_head_position[1] = list_head_position[1] + 1
            head_position = tuple(list_head_position)
        elif movement_direction == "D":
            list_head_position[1] = list_head_position[1] - 1
            head_position = tuple(list_head_position)
        elif movement_direction == "R":
            list_head_position[0] = list_head_position[0] + 1
            head_position = tuple(list_head_position)
        elif movement_direction == "L":
            list_head_position[0] = list_head_position[0] - 1
            head_position = tuple(list_head_position)
            
        head_positions.append(head_position)
        
        position_2 = update_knot_position(position_2,head_position,movement_direction)
        position_3 = update_knot_position(position_3,position_2,movement_direction)
        position_4 = update_knot_position(position_4,position_3,movement_direction)
        position_5 = update_knot_position(position_5,position_4,movement_direction)
        position_6 = update_knot_position(position_6,position_5,movement_direction)
        position_7 = update_knot_position(position_7,position_6,movement_direction)
        position_8 = update_knot_position(position_8,position_7,movement_direction)
        position_9 = update_knot_position(position_9,position_8,movement_direction)
        tail_position = update_knot_position(tail_position,position_9,movement_direction)
                                            
        tail_positions.append(tail_position)

print(f"The number of positions the tail of the ten-knot rope visits at least once: {len(set(tail_positions))}\n")
