# Part 1

Sounds pretty straightforward.
I'm thinking of having a dictionary of monkey names to numbers/operations for constant time lookup and then just recur through the operations till the root is solved.

# Part 2

Are there values which are used more than once?
If so this could be more complicated.
Otherwise working backwords would be the only challenge.

Fortunately it doesn't seem to be the case.

A quick check has also confirmed that humn for my input affects the left value and the value to match is 122624242469304.
Further testing shows that the value changes quite unpredictably with changes of humn.
Its unlikely that brute forcing a solution out will work but its worth a shot.

Brute forcing the answer out from the range -99999 to 99999 isn't working as expected and also takes extermely long.

The most obvious optimization I can think of is to identify which values change as a result of changing humn and only recalcuate those.
Also if I've managed to identify which values are affected by humn I could just feed the whole equation to a constraint solver.

Plugged the problem into z3 and yup, brute force would not have worked.