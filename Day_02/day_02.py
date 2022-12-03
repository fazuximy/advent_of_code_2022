# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 22:47:35 2022

@author: Fazuximy
"""

from dataclasses import dataclass

@dataclass
class StrategyGuide:
    oppenent: str
    play: str
    result: int
    score: int
    
    
# Part 1

"""
Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. 
"The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" 
Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. 
Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for 
the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

What would your total score be if everything goes exactly according to your strategy guide?
"""

data_path = "Z:/python_stuff/advent_of_code_2022/Day_02/data/"
file_name = "input.XSCORE"

with open(data_path+file_name, "r") as input_file:
    text_input_file = input_file.read()

match_strategy_list = []

matches = text_input_file.split("\n")

win_dict = {"A":"Y", "B":"Z", "C":"X"}

equal_dict = {"A":"X", "B":"Y", "C":"Z"}

lose_dict = {"A":"Z", "B":"X", "C":"Y"}

play_score_dict = {"X":1,"Y":2,"Z":3}

result_score_dict = {-1:0,0:3,1:6}

for match in matches:
    
    match_result_list = match.split(" ")

    clean_match_result_list = [i for i in  match_result_list if i != ""]
    
    if len(clean_match_result_list) > 0:
        
        if equal_dict[clean_match_result_list[0]] == clean_match_result_list[-1]:
            result = 0
            
        elif win_dict[clean_match_result_list[0]] == clean_match_result_list[-1]:
            result = 1  
            
        else:
            result = -1
        
        
        score = play_score_dict[clean_match_result_list[1]] + result_score_dict[result]
        
        match_strategy_list.append(StrategyGuide(clean_match_result_list[0],clean_match_result_list[-1],result,score))
    

print(f"The total score if everything goes according to your strategy guide is: {sum([match.score for match in match_strategy_list])}")
    
    

# Part 2

"""
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, 
Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. 
The example above now goes like this:
    
Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
"""

updated_match_strategy_list = []

match_result_dict = {"X":-1,"Y":0,"Z":1}

for match in match_strategy_list:
    
    match.result = match_result_dict[match.play]
    
    if match.result == 0:
        match.play = equal_dict[match.oppenent]
    elif match.result == -1:
        match.play = lose_dict[match.oppenent]
    elif match.result == 1:
        match.play = win_dict[match.oppenent]
    
    match.score = play_score_dict[match.play] + result_score_dict[match.result]
    
    updated_match_strategy_list.append(match)



print(f"Following the elf, The total score if everything goes according to your strategy guide is: {sum([match.score for match in updated_match_strategy_list])}")
    