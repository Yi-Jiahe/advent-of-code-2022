# Part 1

It's another intcode computer.
I wonder if it will need to be extended on later dates.

Off by one errors are a little confusing to deal with because the middle of the cycle is basically the end of the last one.
Trying to make the generator function run in the middle of the loop is a bit messier than just skipping the first cycle because the value in the middle of the first cycle is always the initial value.