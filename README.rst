==============================================================================
Interview Screening
==============================================================================
**Johan going to the church and there are n stairs to reach to Prayer hall.**
**Johan can move either 1 step, 2 step or 3 steps at a time.**
**Implement a method to count how many possible ways Johan can run up the stairs.**


SOLUTION
--------

- I am going to solve this using Dynamic Programming apprach.
- HINT : Possible ways Johran can run up to n stairs is sum of (possible ways to reach n stair with 1 step and 2 step) + (possible ways to reach (n-3) stairs with 1, 2 step and 3 step) 

Illustration 
------------
- when n = 4


+------------+------------+-----------+------------+------------+-----------+
| []         | 0          | 1         | 2          | 3          | 4         |
+============+============+===========+============+============+===========+
| [no steps] | 1 ways     | 0 ways    | 0 ways     | 0 ways     | 0 ways    |
+------------+------------+-----------+------------+------------+-----------+
| [1]        | 1 ways     | 1 ways    | 1 ways     | 1 ways     | 1 ways    |
+------------+------------+-----------+------------+------------+-----------+
| [1,2]      | 1 ways     | 1 ways    | 2 ways     | 2 ways     | 3 ways    |
+------------+------------+-----------+------------+------------+-----------+
| [1,2,3]    | 1 ways     | 1 ways    | 2 ways     | 4 ways     | 4 ways    |
+------------+------------+-----------+------------+-----------+------------+
