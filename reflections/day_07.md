# Part 1

Commands are basically a DFS into the filesystem. The filesystem can probably be recreated using a tree with the leaf nodes being directories.

I don't need to know which command was run when looking at stdout because there are only two commands and only ls writes to stdout.

Precalculating the directory sizes without doing another DFS is reliant on the way the search is performed in the input.
Especially the way directories are exited to continue the search and the final exit.

Spent a bit of extra time adding a print method to the nodes to allow visual inspection of the data ingestion.

# Part 2

Had to expand the print method in order to do debugging on the actual input because of the size.

As expected the size calcuation had to be fixed. 