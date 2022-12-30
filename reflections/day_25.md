# Part 1

I decided to come in to try day 25 expecting it to be a walk in the park.
Turns out its quite an interesting math problem.

I'm sure there's a theorem for this already, but here's what I understand from this problem regarding base n number systems.
A base n number system requires n different symbols.
While this was quite obvious looking at binary with 1 and 0 and hex with abcdef, the idea of minus and double minus implies that they don't just need to represent addition.
The places are represented by powers of n.
Again very obvious with base 10 and base 2, but the minuses again bring greater clarity why it is so.
Together with the number of symbols, each place has a certain reach.
Basically n symbols means that the nth symbol without minuses bascially is the same as timesing the current place by n, or increasing the power by one or moving to the next place.

Minus symbols are interesting.
With up to 2x the place or -2x the place, each place can reach up to the next place minus one divided by two.
With no minuses, it can reach up to the next place minus one. 
With one minus I'll make the guss that it can reach up to 75% of the next place, or 1 - 1x(1/(n-1)).
Two minuses is 1 - 2x(1/(n-1)).
I wonder how they would work with basic arithmatic or more complex mathematics?
I am hesitant to say that it'll work because representing a number is not quite the same as being able to work with it.
Would it the representation work if 0 was not included in the set?
What if there were skipped values?
Again probably not which makes the negatives all the more interesting.

Reading the numbers is quite straightforward, just count the place you're at and add or subtract the amount the symbol represents.

Converting to the number however is more complicated.
Counting up the pattern is quite easy to spot, just increase the value of each position starting from the smallest until there is nothing left to increase.
Then add 1 to the next place and set all the smaller places to double minus and continue.

Figuring out the representation for a random number is less straightforward.
I suppose what you could do is figure out how many places are required using the next place - 1 divide by two rule.
Then its either one or two otherwise you wouldn't need the next place.
The switch happens halfway up so start + 1 ((end - (start + 1)) / 2), where start is 1==... and end is 222....

The fact that you might either need to subtract or add to this means you can't go straight into a recurrsion but need to diffferenciate bewtween the two cases.