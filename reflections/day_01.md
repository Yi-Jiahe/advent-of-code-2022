Most of my effort on day 1 was spent trying to figure out how I wanted to setup the workflow for starting and finishing up a new challenge.

The main change I made over the previous Python repositories was to consolidate the solution running to the root directory by running the main script.

One of the things I'm still debating on is how to setup the method to read the data from the input. 
It might be faster to do whatever processing required to get to the answer as each line is read to reduce the number of iterations.
However, unless the solution is O(n) I don't think one extra iteration to ingest the data will make a big difference.
Some level of processing common between parts 1 and 2 would be good to include in the ingestion step if only to reduce duplicated work.
However it would change the function signitures of both the ingestion method and part methods. 
Fortunately Python does not require fixed types so it doesn't cause any errors so long as the part method is able to process the output of the ingestion method.
I'm just a bit concerned about the reasoning part.
Perhaps the ingestion method shouldn't be too concerned about processing given that its purpose is just to ingest? 
Well I left it as it was anyway because it seemed unnecessary to add too many intermediatry steps.

# Part 1
This is an example where a single pass would be sufficient to get the answer so ingestion would raise the time complexity from O(n) to O(2n) but I guess its too simple a problem for it to matter.

# Part 2
I was considering using a priority queue to store the top 3 answers and pop the lowest when a new entry was found. 
However sorting the whole list once and taking the top 3 was a far simpler solution so I went with that.
I also updated part one to make use of the sorted ingested data.