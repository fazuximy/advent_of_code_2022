
# Part 1
print("Part 1")

"""
Start by figuring out the signal being sent by the CPU. The CPU has a single register, X, which starts with the value 1. It supports only two instructions:

addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
noop takes one cycle to complete. It has no other effect.
The CPU uses these instructions in a program (your puzzle input) to, somehow, tell the screen what to draw.

Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
"""

data_path = "C:/python_projects/advent_of_code_2022/Day_10/data/"
file_name = "input.txt"

with open(data_path + file_name, "r") as input_file:
    text_input_file = input_file.read()

instructions = text_input_file.splitlines()

cycle = 0
value = 1

cycle_number = [20, 60, 100, 140, 180, 220]
cycle_values = []

for instruction in instructions:

    instruction_parts = instruction.split(" ")

    if len(instruction_parts) == 1:
        cycle += 1
        if cycle in cycle_number:
            cycle_values.append(cycle*value)

    elif len(instruction_parts) == 2:
        addx = int(instruction_parts[1])
        for _ in range(0,2):
            cycle += 1
            if cycle in cycle_number:
                cycle_values.append(cycle*value)
        value += addx

print(f"The sum of the six signal strengths are: {sum(cycle_values)} \n")

# Part 2
print("Part 2")

"""
It seems like the X register controls the horizontal position of a sprite. Specifically, the sprite is 3 pixels wide, 
and the X register sets the horizontal position of the middle of that sprite. (In this system, there is no such thing as 
"vertical position": if the sprite's horizontal position puts its pixels where the CRT is currently drawing, then those pixels will be drawn.)

You count the pixels on the CRT: 40 wide and 6 high. This CRT screen draws the top row of pixels left-to-right, then 
the row below that, and so on. The left-most pixel in each row is in position 0, and the right-most pixel in each row is in position 39.

Like the CPU, the CRT is tied closely to the clock circuit: the CRT draws a single pixel during each cycle. Representing 
each pixel of the screen as a #, here are the cycles during which the first and last pixel in each row are drawn:

Cycle   1 -> ######################################## <- Cycle  40
Cycle  41 -> ######################################## <- Cycle  80
Cycle  81 -> ######################################## <- Cycle 120
Cycle 121 -> ######################################## <- Cycle 160
Cycle 161 -> ######################################## <- Cycle 200
Cycle 201 -> ######################################## <- Cycle 240

So, by carefully timing the CPU instructions and the CRT drawing operations, you should be able to determine whether 
the sprite is visible the instant each pixel is drawn. If the sprite is positioned such that one of its three pixels 
is the pixel currently being drawn, the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.).

Render the image given by your program. What eight capital letters appear on your CRT?
"""

def get_sprite_values(value):
    return [value-1,value,value+1]

cycle = 0
value = 1
sprite_value = get_sprite_values(value)

screen_output = ""

cycle_number = [40, 80, 120, 160, 200]
cycle_values = []

for instruction in instructions:

    instruction_parts = instruction.split(" ")

    if len(instruction_parts) == 1:
        cycle += 1
        if (cycle-1) % 40 in sprite_value:
            screen_output+="##"
        else:
            screen_output += ".."
        if cycle in cycle_number:
            screen_output += "\n"

    elif len(instruction_parts) == 2:
        addx = int(instruction_parts[1])
        for _ in range(0,2):
            cycle += 1
            if (cycle-1) % 40  in sprite_value:
                screen_output += "##"
            else:
                screen_output += ".."
            if cycle in cycle_number:
                screen_output += "\n"
        value += addx
        sprite_value = get_sprite_values(value)

print("These eight capital letters appear on the CRT:")
print(screen_output)