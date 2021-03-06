# importing system module for reading files
import sys

# in what follows, a *formula* is a collection of clauses,
# a clause is a collection of literals,
# and a literal is a non-zero integer.

# input path:  a path to a cnf file
# output: the formula represented by the file, 
#         the number of variables, 
#         and the number of clauses
def parse_dimacs_path(path):
  return [], 0, 0

# input cnf: a formula
# input n_vars: the number of variables in the formula
# input n_clauses: the number of clauses in the formula
# output: True if cnf is satisfiable, False otherwise
def naive_solve(cnf, n_vars, n_clauses):
  return True

# input cnf: a formula
# input n_vars: the number of variables in the formula
# input n_clauses: the number of clauses in the formula
# output: True if cnf is satisfiable, False otherwise
def dpll_solve(cnf, n_vars, n_clauses):
  return True


######################################################################

# get path to cnf file from the command line
path = sys.argv[1]

# get algorithm from the command line
algorithm = sys.argv[2]

# make sure that algorithm is either "naive" or "dpll"
assert(algorithm in ["naive", "dpll"])

# parse the file
cnf, num_vars, num_clauses = parse_dimacs_path(path)

# check satisfiability based on the chosen algorithm
# and print the result
if algorithm == "naive":
  print("sat" if naive_solve(cnf, num_vars, num_clauses) else "unsat")
else:
  print("sat" if dpll_solve(cnf, num_vars, num_clauses) else "unsat")
