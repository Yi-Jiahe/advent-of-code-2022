# Part 1

I don't know if its neccessary to implement the loop in order to solve this but its a resource optimzation game.
I've been meaning to make something of the sort, maybe solving this will help me get an idea of what to do.

Its another time limited optimization problem.
I imagine it can be solved in a similar way to day 16.
The states would be defined by the the robots, resources and time avaliable I suppose.
The steps would be to create or not create a robot when possible and which type to create.

In 24 minutes with robots that take a minute to mine each resource and can cost up to 14 of a resource to craft, looks to be quite simple.
The issue might be in branching too much from the low tier robots.

Hmm I sense a possible issue caused by being able to build more than one robot a minute.
Actually if we assume the factory is busy while building a robot, it can only do one robot a minute.

I thought it would be pretty easily but its taking forever to run. 

Saw some optimizations on reddit, not building more ore robots than neccessary, capping resource amounts to improve memozation performance and building towards geode goals, breaking early.