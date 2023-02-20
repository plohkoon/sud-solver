def get_dimension_from_vars(vars):
  return int(len(vars) ** (1/3))

# @param variable_num: An integer representing a variable
# @return: A tuple representing the cell and value that the variable represents
def convert_to_cell(variable_num, dimension):
  variable_num -= 1
  value = variable_num % dimension
  column = (variable_num // dimension) % dimension
  row = (variable_num // dimension ** 2) % dimension

  return row, column, value

# @param vars: A list of strings representing the variables in the solution
# @return: A list of integers representing the assignments in a solution
def get_assignments(vars):
  # If it's positive it is an assignment and we want to
  # reject the final 0 anyway
  return [
    int(var)
    for var in vars
    if int(var) > 0
  ]

# @param assignments: A list of integers representing the assignments in a solution
# @param dimension: The dimension of the puzzle
# @return: A string representing the puzzle in a raw format
def assign_values(assignments, dimension):
  puzzle = "." * (dimension ** 2)

  for assignment in assignments:
    row, column, value = convert_to_cell(assignment, dimension)
    puzzle = puzzle[:row * dimension + column] + str(value + 1) + puzzle[row * dimension + column + 1:]

  return puzzle

# @param puzzle: A string representing a solved puzzle
# @param dimension: The dimension of the puzzle
# @return: A formatted string to pretty print the puzzle
def format_puzzle(puzzle, dimension):
  sub_dimension = int(dimension ** (1/2))

  with_spaces = [
    " ".join([
      puzzle[sub_row * dimension + sub_col * sub_dimension : sub_row * dimension + (sub_col + 1) * sub_dimension]
      for sub_col in range(sub_dimension)
    ])
    for sub_row in range(dimension)
  ]

  with_blanklines = "\n\n".join([
    "\n".join(
      with_spaces[row * sub_dimension : (row + 1) * sub_dimension]
    )
    for row in range(sub_dimension)
  ])

  return with_blanklines
