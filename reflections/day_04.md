# Part 1

Added in a test for the fully_contains method because my answer was too high and I wasn't sure if I had covered all the cases.
I was trying to make the code clearer to reason if it covered all the cases but the test was more reassuring. 
I added in more digits to the test in-case that was the issue since the example specifically drew my attention to that but it wasn't the issue.

I checked Reddit for help where I saw this [post](https://www.reddit.com/r/adventofcode/comments/zc89gu/2022_day_4_my_experience_in_a_nutshell/) complaining about input parsing.
It occured to me that the comparison wasn't being done between numeric types so I added a cast for the input to int which solved it.
Trying to stuff the parsing into one line also got a big lengthy, especially since map returns an iterator which I had to convert to a list.

# Part 2

Part 2 was easier than I expected.
I was expecting it to ask for comparisions to be made between pairs but instead all the was required was to find overlaps instead of if ranges fully contained another.
