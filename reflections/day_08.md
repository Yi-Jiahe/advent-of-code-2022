Ran into an issue with the new day script as it considered the input with leading zeros as an ocatal number.
The problem only surfaced on day 8 because 8 is the first number that diverges from base 10.

Used a stackoverflow [answer](https://stackoverflow.com/questions/8078167/printf-in-bash-09-and-08-are-invalid-numbers-07-and-06-are-fine) to treat the input as base 10. Perhaps I might use the strip leading zeros one if that doesn't work.

# Part 1

Naming the map was tricky because map is already a standard function.

Wondering if there is a neater way to iterate through up, down, left and right.

# Part 2

The direction in which I iterate through the trees in each direction matters. 
In part one I just went from top down and left to right, but now it has to move outwards.

I also rearranged the directions to make it easier to debug.

