# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 18:00:29 2022

@author: Fazuximy
"""

# Part 1

"""
The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a 
previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count 
the number of trees that are visible from outside the grid when looking directly along a row or column.

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider 
trees in the same row or column; that is, only look up, down, left, or right from any given tree.

Consider your map; how many trees are visible from outside the grid?
"""

import numpy as np

data_path = "Z:/python_stuff/advent_of_code_2022/Day_08/data/"
file_name = "input.XSCORE"

with open(data_path+file_name, "r") as input_file:
    text_input_file = input_file.read()
    

process_matrix = ";".join(text_input_file.split("\n"))

input_matrix = np.matrix(" ".join(process_matrix[:-1]))

matrix_shape = np.shape(input_matrix)

node_list = []

numbers_of_trees_hidden = 0

for y in range(0,matrix_shape[0]):
    for x in range(0,matrix_shape[1]):
        
        if x != 0 and x != 98 and y != 0 and y != 98:
            
            three_height = input_matrix[y,x]
                
            from_down = input_matrix[y+1:,x].flatten()
            from_down_hidden = any([tree >= three_height for tree in from_down.tolist()[0]])
            
            from_up = input_matrix[:y,x].flatten()
            from_up_hidden = any([tree >= three_height for tree in from_up.tolist()[0]])
            
            from_right = input_matrix[y,x+1:].flatten()
            from_right_hidden = any([tree >= three_height for tree in from_right.tolist()[0]])
            
            from_left = input_matrix[y,:x].flatten()
            from_left_hidden = any([tree >= three_height for tree in from_left.tolist()[0]])
            
            if all([from_left_hidden,from_right_hidden,from_up_hidden,from_down_hidden]) == True:
                numbers_of_trees_hidden += 1
                
print(f"The number of trees visible from outside the grid is: {99*99 - numbers_of_trees_hidden}")


# Part 2

"""
Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: 
    they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an 
edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the 
edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large 
eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

Consider each tree on your map. What is the highest scenic score possible for any tree?
"""

from itertools import takewhile

scenic_score_list = []

for y in range(0,matrix_shape[0]):
    for x in range(0,matrix_shape[1]):
        
        # Since the scenic scores of the outmost ones whould be 0 anyway, they are left out here as well
        if x != 0 and x != 98 and y != 0 and y != 98:
            
            three_height = input_matrix[y,x]
                
            from_down = input_matrix[y+1:,x].flatten()
            from_down_visible_trees = [*takewhile(lambda k: k < three_height, from_down.tolist()[0])]
            if len(from_down_visible_trees) == len(from_down.tolist()[0]):
                from_down_scenic_tree = len(from_down_visible_trees)
            else:
                from_down_scenic_tree = len(from_down_visible_trees) + 1
            
            from_up = input_matrix[:y,x].flatten()
            from_up_visible_trees = [*takewhile(lambda k: k < three_height,  list(reversed(from_up.tolist()[0])))]
            if len(from_up_visible_trees) == len(from_up.tolist()[0]):
                from_up_scenic_tree = len(from_up_visible_trees)
            else:
                from_up_scenic_tree = len(from_up_visible_trees) + 1
            
            from_right = input_matrix[y,x+1:].flatten()
            from_right_visible_trees = [*takewhile(lambda k: k < three_height, from_right.tolist()[0])]
            if len(from_right_visible_trees) == len(from_right.tolist()[0]):
                from_right_scenic_tree = len(from_right_visible_trees)
            else:
                from_right_scenic_tree = len(from_right_visible_trees) + 1
            
            from_left = input_matrix[y,:x].flatten()
            from_left_visible_trees = [*takewhile(lambda k: k < three_height, list(reversed(from_left.tolist()[0])))]
            if len(from_left_visible_trees) == len(from_left.tolist()[0]):
                from_left_scenic_tree = len(from_left_visible_trees)
            else:
                from_left_scenic_tree = len(from_left_visible_trees) + 1
            
            total_scenic_score = from_down_scenic_tree*from_up_scenic_tree*from_right_scenic_tree*from_left_scenic_tree
            
            scenic_score_list.append(total_scenic_score)
            
print(f"The highest scenic score for any possible tree is: {max(scenic_score_list)}")
