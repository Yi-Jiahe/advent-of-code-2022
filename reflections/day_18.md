# Part 1

Seems simple enough, just create a set of all the cubes, iterate each cube and count the side if its not adjacent to another cube.
I imagine the challenge is either in part 2 or in a ridiculous number of cubes.

~3000 cubes is not a small amount but with 6 faces a cube its at most ~24000 checks.

# Part 2

Have to identify pockets of air inside the lava droplet.

Considering that the lava droplet resides within a ~22x22x22 cube, the search space is only about ~15k spaces max.
Doing a dfs on all air spaces shouldn't be a huge deal?

Actually the number of airspaces on the inside is insufficient; how they are arranged also affects the result.

Since I have already implemented a search from the outside which checks adjacent positions, I can just add any detected surfaces to the list of exterior surfaces.