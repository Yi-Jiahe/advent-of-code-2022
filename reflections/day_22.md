# Part 1

Looks simple enough, I don't see anything that could be a problem yet.

The plan is to store the list of rocks and spaces as sets. 
If the next step in the path is a space, then we proceed.
If it's not, we check if its a rock.
If its a rock we continue to the next instruction.
If its not it means we are at a boundary.
We get the coordinates of the wrap around and do the same check.

Assumption is that there are no holes, i.e. any row/column only has one group of spaces and rocks.

Hmm, with sets I need to have an extra data structure to store the boundaries.
I could store the map as a nested list/list of strings and iterate through that to find the boundaries but iterating is also a pain and extra work.
I guess I could also iterate through the empty space till I find the other bound.
Its a time vs space trade-off.
I'm going to take a guess and say that iterating through to find the edge isn't going to be too costly and if so I'll just memoize it.

Made a mistake in my rollover method by forgetting to check if the position was a rock.
Fortunately my randomly selected test point had a rock and I was able to figure out the problem.
Should probably have been more through with my selection rather than leaving it to chance but if I didn't think of it while coding it.
I guess its a lesson on more care paid to thinking about test cases.

# Part 2

Okay, I'm happy with how I implemented the wrap around for part one.
If I had gone with space it would have needed to be completely redone.
At least with the current implementation I might be able to get way with just changing how the wrap around is calculated?

It's not a head banging on the wall type of question but this will require some thought.

Maybe I can split the sides up and link them. 
This uniformity will make then easier to handle, but will I lose the benefits of the originally linked sides?
But it wouldn't matter if the mapping is correct.
And the infomation would be used in mapping the sides in the first place.

