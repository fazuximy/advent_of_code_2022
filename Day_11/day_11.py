# Task 1

print("Task 1")

"""
To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful observation,
you realize the monkeys operate based on how worried you are about each item.

You take some notes (your puzzle input) on the items each monkey currently has, how worried you are about those items,
and how the monkey makes decisions based on your worry level. For example:

Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
Each monkey has several attributes:

Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.
Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5 means that
your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)
Test shows how the monkey uses your worry level to decide where to throw an item next.
If true shows what happens with an item if the Test was true.
If false shows what happens with an item if the Test was false.
After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't
damage the item causes your worry level to be divided by three and rounded down to the nearest integer.

The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the items
it is holding one at a time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each monkey has
had one turn. The process of each monkey taking a single turn is called a round.

When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that starts
a round with no items could end up inspecting and throwing many items by the time its turn comes around. If a monkey is holding
no items at the start of its turn, its turn ends.

Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of monkey business after
20 rounds of stuff-slinging simian shenanigans?
"""

from dataclasses import dataclass
import re
import numpy as np

data_path = "C:/python_projects/advent_of_code_2022/Day_11/data/"
file_name = "input.txt"

@dataclass
class Monkey:
    number:int
    items: list[int]
    number_of_inspecs: int
    operation_math: str
    operation_value: str
    test_divisible_by: int
    test_true_to_monkey: int
    test_false_to_monkey: int


    def operation(self, old, lcm = None):
        if self.operation_math == "*":
            if self.operation_value == "old":
                new = old * old
            else:
                int_value = int(self.operation_value)
                new = old * int_value
        else:
            if self.operation_value == "old":
                new = old + old
            else:
                int_value = int(self.operation_value)
                new = old + int_value
        if lcm != None:
            if new > lcm:
                remainder = new % lcm
                new = lcm + remainder
        return new

    def test(self, x):
        return self.test_true_to_monkey if x % self.test_divisible_by == 0 else self.test_false_to_monkey


with open(data_path + file_name, "r") as input_file:
    text_input_file = input_file.read()

monkey_list = text_input_file.split("\n\n")

monkey_class_list = []


for monkey_data in monkey_list:
    monkey_data_list = monkey_data.splitlines()
    monkey_number = int(re.findall("\d+",monkey_data_list[0])[0])
    monkey_items = [int(numb) for numb in re.findall("\d+",monkey_data_list[1])]

    monkey_operation = re.findall(r"\= old (.*)$", monkey_data_list[2])[0].split(" ")
    monkey_operation_math = monkey_operation[0]
    monkey_operation_value = monkey_operation[1]

    test_divisible_by = int(re.findall("\d+",monkey_data_list[3])[0])
    test_true_to_monkey = int(re.findall("\d+",monkey_data_list[4])[0])
    test_false_to_monkey = int(re.findall("\d+",monkey_data_list[5])[0])

    monkey_class_list.append(Monkey(monkey_number,monkey_items,0,monkey_operation_math,monkey_operation_value,test_divisible_by,test_true_to_monkey,test_false_to_monkey))

for round in range(0,20):
    for monkey in monkey_class_list:
        for item in monkey.items:
            new_item = monkey.operation(item)
            monkey.number_of_inspecs += 1
            relief_item = new_item//3
            send_to_monkey = monkey.test(relief_item)
            item_list = monkey_class_list[send_to_monkey].items
            monkey_class_list[send_to_monkey].items = item_list+[relief_item]
        monkey.items = []

print(f"The level of monkey business after 20 rounds is: {np.prod(sorted(monkey.number_of_inspecs for monkey in monkey_class_list)[-2:])}\n")


# Task 2

print("Task 2")

"""
You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage 
an item no longer causes your worry level to be divided by three.

Unfortunately, that relief was all that was keeping your worry levels from reaching ridiculous levels. You'll need to find another 
way to keep your worry levels manageable.

At this rate, you might be putting up with these monkeys for a very long time - possibly 10000 rounds!

Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable. 
Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?
"""

monkey_class_list = []

for monkey_data in monkey_list:
    monkey_data_list = monkey_data.splitlines()
    monkey_number = int(re.findall("\d+",monkey_data_list[0])[0])
    monkey_items = [int(numb) for numb in re.findall("\d+",monkey_data_list[1])]

    monkey_operation = re.findall(r"\= old (.*)$", monkey_data_list[2])[0].split(" ")
    monkey_operation_math = monkey_operation[0]
    monkey_operation_value = monkey_operation[1]

    test_divisible_by = int(re.findall("\d+",monkey_data_list[3])[0])
    test_true_to_monkey = int(re.findall("\d+",monkey_data_list[4])[0])
    test_false_to_monkey = int(re.findall("\d+",monkey_data_list[5])[0])

    monkey_class_list.append(Monkey(monkey_number,monkey_items,0,monkey_operation_math,monkey_operation_value,test_divisible_by,test_true_to_monkey,test_false_to_monkey))

least_common_multiple = 1
for monkey_class in monkey_class_list:
    least_common_multiple *= monkey_class.test_divisible_by

for round in range(0,10000):
    for monkey in monkey_class_list:
        for item in monkey.items:
            new_item = monkey.operation(item, least_common_multiple)
            monkey.number_of_inspecs += 1
            send_to_monkey = monkey.test(new_item)
            item_list = monkey_class_list[send_to_monkey].items
            monkey_class_list[send_to_monkey].items = item_list+[new_item]
        monkey.items = []

sorted_monkey_inspections = sorted(monkey.number_of_inspecs for monkey in monkey_class_list)

print(f"The level of monkey business after 10000 rounds is: {sorted_monkey_inspections[-2]*sorted_monkey_inspections[-1]}\n")