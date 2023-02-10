#!/usr/bin/env python3
import threading
import subprocess
import sys
import time

def debug(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

def test_hard(number):
  debug("Testing Sudoku number", number)
  base_name = f"hard_{number:02d}"
  puzzle_file_name = f"tests/puzzles/{base_name}.txt"
  cnf_file_name = f"tests/cnfs/{base_name}.cnf"
  assignments_file_name = f"tests/assignments/{base_name}.txt"
  resolutions_file_name = f"tests/resolutions/{base_name}.txt"
  solutions_file_name = f"tests/solutions/{base_name}.txt"

  with open(puzzle_file_name, "r") as puzzle:
    with open(cnf_file_name, "w") as cnf:
      with open("/dev/null", "w") as dev_null:
        sud2sat_response = subprocess.call(
          ["./sud2sat"],
          stdin=puzzle,
          stdout=cnf,
          stderr=dev_null
        )
        if sud2sat_response != 0:
          debug("Sud2sat failed on test", number)
          raise Exception("Sud2sat failed on test", number)

  with open(resolutions_file_name, "w") as resolution:
    with open("/dev/null", "w") as dev_null:
      sat_response = subprocess.call(
        ["minisat", cnf_file_name, assignments_file_name],
        stdout=resolution,
        stderr=dev_null
      )
      # A success is indicated by a return code of 10. An unsatisfiable success is 10
      # 0 is error with command line args, 1 is error with input file, 3 is interrupted
      # so these are the actual failure cases
      if sat_response == 0 or sat_response == 1 or sat_response == 3:
        debug("minisat failed on test", number)
        raise Exception("minisat failed on test", number)

  with open(assignments_file_name, "r") as assignment:
    with open(solutions_file_name, "w") as solution:
      with open("/dev/null", "w") as dev_null:
        sat2sud_response = subprocess.call(
          ["./sat2sud"],
          stdin=assignment,
          stdout=solution,
          stderr=dev_null
        )
        if sat2sud_response != 0:
          debug("sat2sud failed on test", number)
          raise Exception("sat2sud failed on test", number)

if __name__ == "__main__":
  debug("Hello, world!")
  for i in range(95):
    t = threading.Thread(target=test_hard, args=(i + 1,))
    t.start()
