Added in some code into the main script to make it run the current day's solution.

Also got some advice to use poetry and an image to use the latest version of Python.
Unfortunately I am struggling to get the poetry install to work right.

# Part 1

Took a while to decide how I sould process the data before passing it to the solutions, hence the lengthy description.

I made the solution able to handle the case where there are multiple duplicates but I didn't check if it actually happens.

# Part 2

Had to combine the compartments which made me question if I should have split them in the processing.

Spent some time pondering if I should count elves with index 0 or 1.

Added a branch to handle if multiple or no duplicates where found in the rucksacks to raise an exception just in case something went wrong.