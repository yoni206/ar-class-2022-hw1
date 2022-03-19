# HW 1
The tasks for this HW are found in hw1.pdf.

## Details about Question 1
### How to implement?
The SAT-solvers should be implemented in sat_solver.py.
In particular, the naive solver should be implemented in the function
``naive_solve" and the dpll solver should be implemented in the function
``dpll_solve".

### How to run?
This is how your implementation should be called:
```
python3 sat_solver.py <path-to-cnf> <algorithm>
```
where:
- <path-to-cnf> is a path to a cnf file
- <algorithm> is either "naive" or "dpll"

For example:
```
python3 sat_solver.py benchmarks/example1.cnf naive
python3 sat_solver.py benchmarks/example1.cnf dpll
```
In both cases, the result should be `sat`. 
No other output is allowed, as the implementation will be tested using scripts.

The directory `benchmarks` includes several cnf files as examples.
Your implementation will be tested on a super-set of these benchmarks.

It is highly recommended to compare your results to an off-the-shelf SAT solver,
such as `z3` in order to check that your results are correct.
When testing your implementation, I plan to compare your results to z3's results.

