### Carter Person, CS 76, 20F, SA5

## Report on Results


#### Description

My GSAT algorithm works by initializing all assignments randomly. I currently have it set to 40% True 60% False, which through testing I determined to perform pretty well. From there, I then enter a loop which I set to run 500,000 times before exiting without a solution. Inside this loop, I generate a random number between 0 and 1. I then use this number to determine whether I will flip a completely random variable's value, or if I will score all of the variables to find out which one would be best to flip. When scoring the variables, I temporarily change the assignment and then check how many clauses are satisfied, then add that value into a dictionary. I do this for all of the variables, and then I sort them into a list from the dictionary, only selecting the highest valued changes. 

Back in the GSAT algorithm, I then repeat the process until I reach an assignment that satisfies all of the clauses.

My WalkSAT works in a very similar fashion. The only difference from the GSAT is the choice in candidates. Whenever I end up scoring the variables instead of choosing any random variable to change, I narrow the variables that I look at. In WalkSAT, I choose a random clause that is not satisfied and score all of the variables present in that clause in the same way as above. Then, from all of those variables, I return a list of all variables that are tied for the highest score, and then choose which variable to change randomly from that list. If it is supposed to be done without scoring, then a random variable from the selected unsatisfied clause will be flipped.


Design wise, I used a lot of lists. Because all of the variables were integers, it made it very easy to initialize and then access all of the information. I could have used a dictionary in a similar way, but there weren't any significant runtime differences with what I was doing with them, so I just stuck to lists. In addition, I decided against making the algorithm recursive, just because it was very simple to think through the problem in terms of a non-recursive algorithm and it made it convenient to set an upper limit for the amount of variables flipped. I also decided to move my probability part of WalkSAT to the helper function that returns the candidates. I did this because it was easy to cut my scoring function short and return the list of variables from the unsatisfied clause before scoring them and narrowing them down.


I laid out the problem as simply setting a basic assignment and then flipping single variables until I reached the solution.


#### Evaluation

Ultimately, I don't think that these algorithms work very well. They do find valid solutions, but it takes them a very long time to do so. They're useful, because they're very easily adjusted to make them apply to any other similar kind of question, but I have made much faster algorithms to solve sudoku in other languages in much more specific implementation.

I am fairly certain I have implemented the algorithms to be close to as efficient as they can be, I think its just the nature of the algorithms that makes it slow. With each step requiring a minimum thousands of validity checks, my algorithm is only able to flip somewhere are 120 variables per second, which is not nearly enough to be fast at finding a solution with all of the missteps inherent in the algorithm.


For testing, I found the following time durations to solve the problems with WalkSAT:

one_cell: 0.00054s
all_cells: 1.25s
rows: 2.4197s
rows_and_cols: 66.98s
rules: 58.16s
puzzle1: 331.2s
puzzle2: 64.73s


compared to runtimes with GSAT:

one_cell: .068s
all_cells: 506.55s
rows: 744s
rows_and_cols: 
rules: 
puzzle1: 
puzzle2: 


with GSAT, the times were much longer, and it was unreasonable to test it with anything beyond rows, which took multiple minutes to complete. This is because GCDF checks all of the variables against all of the clauses, leading to millions of checks with each assignment.

In addition, these runtimes changed significantly based on the p value selected, as well as the initial seeding of True/False values.






