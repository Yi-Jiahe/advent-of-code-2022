# Part 1

The naive solution seems quite easy to implement so long as there's no duplicates.

Unfortunately, a quick scan of the input shows thay there are quite a number of duplicates (~1/3).

With a bit of modification, I managed to implement the naive solution.
Had a bit of trouble with the modulo-ing but otherwise was straightforward.

# Part 2

Amazing what a big difference large numbers can make.

After implementing the modulo operations, I realised that even just multiplying out the data is already too much.
Fortunately the solution was simple.
Just don't multiply out the values till you need the final answer.