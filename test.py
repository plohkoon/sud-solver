#!/usr/bin/env python3
import threading
import subprocess
import sys
from lib import debug

def test(number, difficulty, exe):
  if exe == "1":
    exe = ""

  base_path = "tests/" if exe == "" else f"tests_{exe}/"

  debug(f"Testing {difficulty} Sudoku number with exe sud2sat{exe}", number)

  base_name = f"{difficulty}_{number:02d}"
  puzzle_file_name = f"tests/puzzles/{base_name}.txt"
  cnf_file_name = f"{base_path}cnfs/{base_name}.cnf"
  assignments_file_name = f"{base_path}assignments/{base_name}.txt"
  resolutions_file_name = f"{base_path}resolutions/{base_name}.txt"
  solutions_file_name = f"{base_path}solutions/{base_name}.txt"

  with open(puzzle_file_name, "r") as puzzle:
    with open(cnf_file_name, "w") as cnf:
      with open("/dev/null", "w") as dev_null:
        sud2sat_response = subprocess.call(
          [f"./sud2sat{exe}"],
          stdin=puzzle,
          stdout=cnf,
          stderr=dev_null
        )
        if sud2sat_response != 0:
          debug(f"Sud2sat{exe} failed on test", number)
          raise Exception(f"Sud2sat{exe} failed on test", number)

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
          [f"./sat2sud{exe}"],
          stdin=assignment,
          stdout=solution,
          stderr=dev_null
        )
        if sat2sud_response != 0:
          debug(f"sat2sud{exe} failed on test", number)
          raise Exception(f"sat2sud{exe} failed on test", number)

if __name__ == "__main__":
  for i in range(50):
    t = threading.Thread(target=test, args=(i + 1, "test", "1"))
    t.start()
    t_2 = threading.Thread(target=test, args=(i + 1, "test", "2"))
    t_2.start()
    t_3 = threading.Thread(target=test, args=(i + 1, "test", "3"))
    t_3.start()
  for i in range(95):
    t = threading.Thread(target=test, args=(i + 1, "hard", "1"))
    t.start()
    t_2 = threading.Thread(target=test, args=(i + 1, "hard", "2"))
    t_2.start()
    t_3 = threading.Thread(target=test, args=(i + 1, "hard", "3"))
    t_3.start()
