==============================================================================
Interview Screening
==============================================================================
**Johan going to the church and there are n stairs to reach to Prayer hall.**
**Johan can move either 1 step, 2 step or 3 steps at a time.**
**Implement a method to count how many possible ways Johan can run up the stairs.**


SOLUTION
--------

- I am going to solve this using Dynamic Programming apprach.
- HINT : 
1.Possible ways Johran can run up to n stairs is sum of (possible ways to reach n stair with 1 step and 2 step) + (possible ways to reach (n-3) stairs with 1, 2 step and 3 step) 

2. Unique ways Johan can run up to 0 stairs is always 1.

3. *Sub Problem* - Find all the unique ways when the stairs are range(n) with all step 0 , step 1, step 2 and step 4.

4. *Solution* - Value in the last column.

Illustration 
------------
- when n = 4

1. Find how many unique ways Johan can run up to 0 stairs. Using HINT 2 fill up the first column as 1.
2. When there is no step all the value to 0.
3. Now using HINT 1 fill up all the column.
4. **4 ways** is solution since it is in last column.


+------------+------------+-----------+------------+------------+-----------+
| []         | 0 Stairs   | 1 Stairs  | 2 Stairs   | 3 Stairs   | 4 Stairs  |
+============+============+===========+============+============+===========+
| [no steps] | 1 way      | 0 way     | 0 way      | 0 way      | 0 way     |
+------------+------------+-----------+------------+------------+-----------+
| [1]        | 1 way      | 1 way     | 1 way      | 1 way      | 1 way     |
+------------+------------+-----------+------------+------------+-----------+
| [1,2]      | 1 way      | 1 way     | 2 ways     | 2 ways     | 3 ways    |
+------------+------------+-----------+------------+------------+-----------+
| [1,2,3]    | 1 way      | 1 way     | 2 ways     | 4 ways     | 4 ways    |
+------------+------------+-----------+------------+------------+-----------+
