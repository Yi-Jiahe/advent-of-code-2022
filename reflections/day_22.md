# Part 1

Looks simple enough, I don't see anything that could be a problem yet.

The plan is to store the list of rocks and spaces as sets. 
If the next step in the path is a space, then we proceed.
If it's not, we check if its a rock.
If its a rock we continue to the next instruction.
If its not it means we are at a boundary.
We get the coordinates of the wrap around and do the same check.