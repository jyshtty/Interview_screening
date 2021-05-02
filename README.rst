Johan going to the church and there are n stairs to reach to Prayer hall.
Johan can move either 1 step, 2 step or 3 steps at a time.
Implement a method to count how many possible ways Johan can run up the stairs.


+------------+------------+-----------+------------+------------+-----------+
| []	       | 0		      | 1		      | 2		       | 3		      | 4		      |
+============+============+===========+============+============+===========+
| [no steps] | 1 ways  	  | 0 ways    | 0 ways     | 0 ways     | 0 ways    |
+------------+------------+-----------+------------+------------+-----------+
| [1] 		   | 1 ways	    | 1 ways	  | 1 ways	   | 1 ways     | 1 ways    |
+------------+------------+-----------+------------+------------+-----------+
| [1,2]		   | 1 ways	    | 1 ways	  | 2 ways	   | 2 ways     | 3 ways    |
+------------+------------+-----------+------------+------------+-----------+
| [1,2,3] 	 | 1 ways	    | 1 ways	  | 2 ways	   | 4 ways     | 4 ways    |
+------------+------------+-----------++------------+-----------+-----------+