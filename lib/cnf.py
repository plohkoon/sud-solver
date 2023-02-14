from . import debug

# @param row: The row of the cell
# @param column: The column of the cell
# @param value: The value of the cell
# @param dimension: The dimension of the sudoku puzzle
# @param sgn: The sign of the variable
# @return: A number representing the CNF variable in the range of 1 - dimension^3
def convert_to_cnf_term(row, column, value, dimension, sgn):
  return sgn * (row * (dimension ** 2) + column * dimension + value + 1)

# @param dimension: The dimension of the puzzle
# @return: A CNF representing the statement "every cell must have a value"
def build_cell_cnf(dimension):
  debug("Building the cell CNF")
  return [
    [convert_to_cnf_term(row, column, value, dimension, 1) for value in range(dimension)]
    for row in range(dimension)
    for column in range(dimension)
  ]

# @param dimension: The dimension of the puzzle
# @return: A CNF representing the statement "every row contains each value once"
def build_row_cnf(dimension):
  debug("Building the row CNF")
  return [
    [
      convert_to_cnf_term(row, column1, value, dimension, -1),
      convert_to_cnf_term(row, column2, value, dimension, -1)
    ]
    for row in range(dimension)
    for value in range(dimension)
    for column1 in range(dimension - 1)
    for column2 in range(column1 + 1, dimension)
  ]

# @param dimension: The dimension of the puzzle
# @return: A CNF representing the statement "every column contains each value once"
def build_column_cnf(dimension):
  debug("Building the column CNF")
  return [
    [
      convert_to_cnf_term(row1, column, value, dimension, -1),
      convert_to_cnf_term(row2, column, value, dimension, -1)
    ]
    for column in range(dimension)
    for value in range(dimension)
    for row1 in range(dimension - 1)
    for row2 in range(row1 + 1, dimension)
  ]

# @param dimension: The dimension of the puzzle
# @return: A CNF representing the statement "every box contains each value once"
def build_box_cnf(dimension):
  debug("Building the box CNF")
  box_dimension = int(dimension ** 0.5)

  # @param row_of_box: The row of the box
  # @param column_of_box: The column of the box
  # @param cell1_of_box: The cell inside the box
  # @param cell2_of_box: The cell inside the box
  # @param value: The value being checked by the conjunct
  # @return: A disjunct representing the statement "these two cells in the box do not share a value"
  def build_conjunct(row_of_box, column_of_box, cell1_of_box, cell2_of_box, value):
    # Integer division and modulo are used to figure out how far down and right to move
    row1 = row_of_box * box_dimension + cell1_of_box // box_dimension
    column1 = column_of_box * box_dimension + cell1_of_box % box_dimension

    row2 = row_of_box * box_dimension + cell2_of_box // box_dimension
    column2 = column_of_box * box_dimension + cell2_of_box % box_dimension

    return [
      convert_to_cnf_term(row1, column1, value, dimension, -1),
      convert_to_cnf_term(row2, column2, value, dimension, -1)
    ]

  return [
    build_conjunct(row_of_box, column_of_box, cell1_of_box, cell2_of_box, value)
    # Scan over each box
    for row_of_box in range(box_dimension)
    for column_of_box in range(box_dimension)
    # Scan over each value
    for value in range(dimension)
    # Scan over each cell in the box
    for cell1_of_box in range(dimension)
    for cell2_of_box in range(cell1_of_box + 1, dimension)
  ]

# @param sudoku: A string representing the sudoku puzzle
# @param dimension: The dimension of the sudoku puzzle
# @return: A CNF representing a conjuction of singletons matching the
#          constraints of the input
def build_constraints_cnf(sudoku, dimension):
  debug("Building the constraints CNF")
  return [
    [convert_to_cnf_term(row, column, int(value), dimension, 1)]
    for row in range(dimension)
    for column in range(dimension)
    if (value := sudoku[row * dimension + column]) != '.'
  ]

# ---- Efficient and Extended Encoding Starts Here ----
#
# Extended Encoding CNF #1
# @param dimension: The dimension of the puzzle
# @return: A CNF representing the statement "every cell has at most 1 value"
def build_cell_max_cnf(dimension):
  debug("Bulding cell max CNF")

  return [
    [
      convert_to_cnf_term(row, column, value1, dimension, -1),
      convert_to_cnf_term(row, column, value2, dimension, -1)
    ]
    for row in range(dimension)
    for column in range(dimension)
    for value1 in range(dimension - 1)
    for value2 in range(value1 + 1, dimension)
  ]

# ---- Efficient Encoding ends Here ----
# From here on out it's just the extended encoding

# Extended Encoding CNF #2
# @param dimension: The dimension of the puzzle
# @return: A CNF representing the statement "every value appears at least once in each row"
def build_value_in_column_cnf(dimension):
  debug("Building value in row CNF")
  
  return[
    [convert_to_cnf_term(row, column, value, dimension, 1) for row in range(dimension)]
    for column in range(dimension)
    for value in range(dimension)
  ]

# Extended Encoding CNF #3
# @param dimension: The dimension of the puzzle
# @return: A CNF representing the statement "every value appears at least once in each column"
def build_value_in_row_cnf(dimension):
  debug("Building value in row CNF")
  
  return[
    [convert_to_cnf_term(row, column, value, dimension, 1) for column in range(dimension)]
    for row in range(dimension)
    for value in range(dimension)
  ]

# Extended Encoding CNF #4
# @param dimension: The dimension of the puzzle
# @return: A CNF representing the statement "every value appears at least once in each box"
def build_value_in_box_cnf(dimension):
  debug("Building value in box CNF")
  box_dimension = int(dimension ** 0.5)
  
  return[
    [convert_to_cnf_term(box_dimension*b + v, box_dimension*a + u, value, dimension, 1)
      for u in range(box_dimension)
      for v in range(box_dimension)
    ]
    for value in range(dimension)
    for a in range(box_dimension)
    for b in range(box_dimension)
  ]

