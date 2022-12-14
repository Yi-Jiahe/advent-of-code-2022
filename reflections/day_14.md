# Part 1

Maybe I should have a standard test case for the input parsing?

For now I wrote a visualizer for the map.

Hmm I didn't check the results of the map properly and the inputs were also missing a couple of cases where the paths were not completed to the last rock.

# Part 2

The twist sounded quite straightforward; just stop the grains if they reach the new bottom.
But I can't figure out where they are leaking.
I'm still pretty confused about where I was doing my checks but I got the answer.

It took like 30mins to get the answer for part 2 of about ~20000 grains.
Each grain took longer than the last.

I saw an optimization on reddit about memomization so I think I'll give that a try.