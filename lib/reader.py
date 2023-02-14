import re
import sys

# @param raw_puzzle: A string representing the puzzle to be solved
# @return: A string representing the puzzle in a standardized format
def clean(raw_puzzle):
  single_line = re.sub(r'\s+', '', raw_puzzle)
  cleaned = single_line.strip()
  standardized = cleaned.translate(str.maketrans('0.*?123456789', '....012345678'))

  return standardized

def read_assignment():
  read_string = sys.stdin.read().split("\n")

  if read_string[0] == "UNSAT":
    print("No solution found")
    exit(1)

  if read_string[0] != "SAT" or len(read_string) < 2:
    print("Unexpected output from solver")
    exit(1)

  return read_string[1].split()
