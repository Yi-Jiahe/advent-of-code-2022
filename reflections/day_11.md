# Part 1

Wow they're getting more and more complicated aren't they.

Parsing the input manually seems easier than parsing it programatically.
But I think it shouldn't be too complicated to do it programmatically.

It was kind of tedious but it worked out in the end.
Debugging the regex was probably good experience.
The hardest part was figuring a way to assign the operation.
I made use of a few cheats based on assumptions made from the input, e.g. test is only division, operation is only + and *.

# Part 2

Clearly brute forcing it isn't going to work.

I wonder if its the number of iterations, 30-ish items shared among 8 monkeys for 10000 rounds for potentially 30*8*10000, or approximately 400000 operations probably wouldn't take that long right.
Meaning its the size of the numbers.
I guess the hint was that worry levels need to be managed.
Sounds like math.

I had some help from the subreddit to figure this one out, namely using the mod of all the test values to keep the worry_levels bounded.
Modulo arithmatic I think its called?