Fixed the init problem by adding a flag to the poetry install line.

Puzzle input is non-homogenous and requires parsing an ascii art diagram. 
The easiest solution is probably not to parse the input at all but to hardcode it in somewhere.
The issue is how to modify the boilerplate to accept extra inputs.

It would have been more convinent if they had provided the stacks in row form.

# Part 1

Actually, hardcoding the stacks was quite tedious too.

# Part 2

Based on the solution in part 1, modifying the stacks in part 1 will affect the results of part 2.
The solution was to create a deepcopy of the stacks for working on.