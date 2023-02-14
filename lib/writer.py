
# @param sub_cnfs: A list of CNF forms that are to be combined
# @param dimension: The dimension of the sudoku puzzle
# @return: A string representing the CNF form of the combined CNFs
def build_cnf_string(sub_cnfs, dimension):
  list_of_clauses = [
    " ".join(map(str, clause + [0])) for cnf in sub_cnfs for clause in cnf
  ]
  cnf_string = "\n".join(list_of_clauses)

  number_of_clauses = len(list_of_clauses)
  number_of_variables = dimension ** 3

  return f"p cnf {number_of_variables} {number_of_clauses}\n{cnf_string}"
