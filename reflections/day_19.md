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

I think I made a mistake with when the robot is ready to contribute to the new resources.
When its just made it still needs another minute to generate new resources.
Keeping track of this further increases the search space however.
Hmm there is still a bug somewhere.
Oh even the previously existing robots's resources can only be added after testing if new robots can be built.

I thought it would be pretty easily but its taking forever to run. 

Saw some optimizations on reddit, not building more ore robots than neccessary, capping resource amounts to improve memozation performance and building towards geode goals, breaking early.

I think breaking early will make a significant difference because every minute more given to time avaliable is an exponential increase in time taken.
What's a good way of estimating if the solution will be able to break the record or not though?
It takes 3 minutes for a robot to contribute resources from the minute it is built.
This means that a geode robot will only be useful if built with at least 3 minutes to spare.
An obsidian robot must be built with at leasts 5 minutes to spare to allow one more geode robot to be built in time.
A clay robot has to be built with at least 7 minutes to spare to allow an obsidian robot to allow a geode robot to be useful.
Same for ore if its the limiting producer.
Not sure if this constraint does much.

I saw someone make the arguement that if you can make an geode robot you should always do that.
Not sure how certain that is, but I'll accept it.
I think based on the time available its likely that doing so will maximise geode production, but if we had more time, would building obsidian robots first to make sure we can produce geode robots at one per minute be better?

I wonder if it extends to obsidian robots too?
If you can't make a geode robot, should you make an obsidian robot?
The only issue I can see with this approach is if ore is the choke point but will it be?