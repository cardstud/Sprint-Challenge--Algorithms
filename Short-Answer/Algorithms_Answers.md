#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is:
    a.  a single loop
    b. the worst case scenario means going through whole loop
    
    Therefore this is is O(n)

b) This is:
    a. a nested loop(for i, while j) 
    b. all else are constants 
    c. dependent on n

    Therefore this is O(n^2)

c) This is:
    a. Worst case scenario (if not ==0) means you Will need to go through each element 
    
    Thefore this is O(n)

## Exercise II

My approach:

    Since there is a midpoint where higher-than-midpoint the egg will break if dropped off that floor or higher floor and if lower-than-
            midpoint the egg will not break if dropped off that floor or lower. So this looks like a divide and conquer problem.

        So to solve this:
            a. get middle floor of the building
            b. Drop egg and if it breaks then that floor and the floors above are removed
            c. Now find the middle floor of what is left
            d. Drop egg and if it breaks, then that floor and above removed and repeat
            e. When you get to where the egg does not break, remove that floor and those floors beneath
            f. Repeat this until you find the middle floor

        The time complexity of this problme is O(log n) since you are halving the set on each pass.


