# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:18:23 2022

@author: Fazuximy
"""


# Part 1
print("Part 1")

"""
You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from
 above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the 
 lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). 
Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move 
exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination 
square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could 
step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower 
                                              than the elevation of your current square.)

What is the fewest steps required to move from your current position to the location that should get the best signal?
"""


import numpy as np
import networkx as nx
import string

# Function for finding the neighbors for a positions
def get_neighbors(position, matrix, traversal_dict, matrix_row_number, matrix_column_number):
    
    neighbor_list = []
    
    position_letter = matrix[position[0]][position[1]]
    
    possible_travel_ways = traversal_dict[position_letter]
    
    # UP
    if 0 < position[0]:
        up_position = position + np.array([-1,0])
        if matrix[up_position[0]][up_position[1]] in possible_travel_ways:
            neighbor_list.append(tuple(up_position))
    
    # Down
    if (matrix_row_number-1) > position[0]:
        down_position = position + np.array([1,0])
        if matrix[down_position[0]][down_position[1]] in possible_travel_ways:
            neighbor_list.append(tuple(down_position))
        
    # Right
    if (matrix_column_number-1) > position[1]:
        right_position = position + np.array([0,1])
        if matrix[right_position[0]][right_position[1]] in possible_travel_ways:
            neighbor_list.append(tuple(right_position))
        
    # Down
    if 0 < position[1]:
        left_position = position + np.array([0,-1])
        if matrix[left_position[0]][left_position[1]] in possible_travel_ways:
            neighbor_list.append(tuple(left_position))
    
    return neighbor_list
        

data_path = "Z:/python_stuff/advent_of_code_2022/Day_12/data/"
file_name = "input.XSCORE"

with open(data_path+file_name, "r") as input_file:
    text_input_file = input_file.read()
 

# Get the positions

matrix_rows = text_input_file.splitlines()

matrix_row_number = len(matrix_rows)
matrix_column_number = len(matrix_rows[0])
        
letter_matrix_list = [[*row] for row in matrix_rows]

letter_matrix = np.array(letter_matrix_list)

list_of_positions = []
for matrix_row in range(0,matrix_row_number):
    for matrix_column in range(0,matrix_column_number):
        list_of_positions.append(np.array([matrix_row,matrix_column]))


# Get the neighbors for each position

list_of_a_z = [*string.ascii_lowercase[:26]]

possible_neighbors = [list_of_a_z[:i] for i in range(2,len(list_of_a_z)+1)]

possible_neighbors[-1] = possible_neighbors[-1] + ["E"] 

possible_neighbors.append(possible_neighbors[-1])

possible_neighbors = possible_neighbors + [[]]

possible_neighbors = [possible_neighbors[0]] + possible_neighbors
letter_position_list = ["S"] + list_of_a_z + ["E"]

traversal_dict = dict(zip(letter_position_list,possible_neighbors)) 
        
position_neighbors =  [get_neighbors(position, letter_matrix, traversal_dict, matrix_row_number, matrix_column_number) for position in list_of_positions]     


# Creating graph
path_graph = nx.DiGraph() 

tuple_positions = [(tuple(position),{"letter": str(letter_matrix[position[0]][position[1]])}) for position in list_of_positions]

# Adding nodes
path_graph.add_nodes_from(tuple_positions)

# Adding edges
for position_numb in range(len(list_of_positions)):
    for neighbor in position_neighbors[position_numb]:
        path_graph.add_edge(tuple(list_of_positions[position_numb]),neighbor)


# Get start and end positions in the graph
start_position = [node[0] for node in path_graph.nodes(data = True) if node[1]["letter"] == "S"][0]
end_position = [node[0] for node in path_graph.nodes(data = True) if node[1]["letter"] == "E"][0]

# Calculate the shortest path
shortest_path = nx.shortest_path(path_graph,start_position,end_position)

print(f"The fewest steps required to move from your current position to the location that should get the best signal are: {len(shortest_path) - 1}\n")


# Part 2
print("Part 2")

"""
To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E. However, 
the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at 
elevation a to the square marked E.

What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?
"""


# Find all "a" locations
start_position = [node[0] for node in path_graph.nodes(data = True) if node[1]["letter"] == "a"]

# Get the shortest path from "a" locations to end location
shortest_paths = []
for start in start_position:
    try:
        shortest_paths.append(nx.shortest_path(path_graph,start,end_position))
    except:
        # Catching when there is no path between the "a" location and the end location
        continue

# Get the absolutely shortest path
shortest_path = shortest_paths[np.argmin([len(i) for i in shortest_paths])]

print(f"the fewest steps required to move starting from any square with elevation a to the location that should get the best signal are: {len(shortest_path) - 1}")