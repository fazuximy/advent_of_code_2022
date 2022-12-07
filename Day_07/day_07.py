# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 17:47:20 2022

@author: Fazuximy
"""

# Task 1

"""
The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. 
You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.


Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
"""

from functools import reduce
import numpy as np

def add_values_to_dict(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value
    
def get_nested_values(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from get_nested_values(v)
    else:
      yield v
      
def find_nested_dict_based_on_keys(dictionary, *keys):
    return reduce(lambda d, key: d.get(key) if d else None, keys, dictionary)

data_path = "Z:/python_stuff/advent_of_code_2022/Day_07/data/"
file_name = "input.XSCORE"

with open(data_path+file_name, "r") as input_file:
    text_input_file = input_file.read()

command_and_results_list = text_input_file.split("$ ")[1:]

directory_dict = {}

directory_path_list = []

dir_total_file_sizes = 0

all_directory_paths = []

for command_and_results in command_and_results_list:
    
    command_and_results_divided = command_and_results.split("\n")[:-1]
    
    # List commands
        # Is it a list command?
    if len(command_and_results_divided) > 1 and command_and_results_divided[0] == "ls":
        
        dir_name_list = []
        file_size_list = []
        file_name_list = []
            
        dir_and_files = command_and_results_divided[1:]
        
        for dir_or_file in dir_and_files:
            if dir_or_file[:3] == "dir":
                dir_name = dir_or_file[4:]
                dir_name_list.append(dir_name)
            else:
                dir_or_file_split = dir_or_file.split(" ")
                file_size = int(dir_or_file_split[0])
                file_size_list.append(file_size)
                file_name = dir_or_file_split[1]
                file_name_list.append(file_name)
                
        if len(directory_path_list) > 0:

            for dir_name in dir_name_list:
                add_values_to_dict(directory_dict, directory_path_list,{dir_name:{}})
            for file_index in range(0,len(file_name_list)):
                add_values_to_dict(directory_dict, directory_path_list, {"file_size":sum(file_size_list)})
                 
        else:
            for dir_name in dir_name_list:
                directory_dict[dir_name] = {}

            
             
        # Is it a change directory command
    elif len(command_and_results_divided) == 1 and command_and_results_divided[0][0:2] == "cd":
        change_dir_to = command_and_results_divided[0][3:]
        
        # Go back
        if change_dir_to == "..":
            directory_path_list = directory_path_list[:-1]
        
        # Go to the start
        elif change_dir_to == "/":
            
            directory_path_list = []
            
        # Go to this directory    
        else:
            directory_path_list.append(change_dir_to)
            all_directory_paths.append(directory_path_list.copy())
        
        # To catch if something do not goes as expected
    else:
        print(f"Something went wrong. The input is: {command_and_results_divided}")
        break

unique_paths = list(np.unique(all_directory_paths))

directory_file_size_dict = [{str(path):sum(list(get_nested_values(find_nested_dict_based_on_keys(directory_dict, *path))))} for path in unique_paths]

dir_size_less_or_equal_to_value = [list(directory_file_size.values())[0] for directory_file_size in directory_file_size_dict if list(directory_file_size.values())[0] <= 100000]

print(f"The total value of all of the directories with a total size of at most 100000: {sum(dir_size_less_or_equal_to_value)}")


# Part 2

"""
The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000.
You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; 
this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. 
Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
"""

total_available_space = 70000000
need_space = 30000000

used_space = sum(list(get_nested_values(directory_dict)))

space_to_free = used_space - (total_available_space - need_space)

large_enough_dirs = [list(i.values())[0] for i in directory_file_size_dict if list(i.values())[0] > space_to_free]

print(f"The smallest directory that would free up space if deleted is this total size: {sorted(large_enough_dirs)[0]}")
