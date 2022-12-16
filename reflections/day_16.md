# Part 1

Oh boy today looks like a hard problem. 
There are two things to optimize for, time and size.
The larger valves need to be opened first because they will give the most payout over time.
This can be large enough to ignore the ones which don't release enough.
0 pressure valves are clearly passages, but low valued ones can also be passthroughs to get to the larger ones first.

The example is small enough to solve as a logical puzzle but the actual case has so many more valves.
Most of them only have 2 links though meaning its not super inter-connected.
Furthermore most of them have 0 flow rate, meaning they can be simplified into a weighted edge.
The problem is that it would be very easy to miss out possibilities doing it by hand.

I guess the first order of business is to form the graph.

Next I think its a dynamic programming problem, the states are a function of current position, time left and opened valves?

Considered optimizing the problem by converting valves with 0 flow rate and only 2 neighbours into weighted edges but not knowing what part 2 was I decided against it.
Not sure how much benefit the optimization will offer anyway.

Opening a valve takes 1 minute, meaning the flow rate from the valve to be opened cannot be added in the step when it is opened.