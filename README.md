# Sudoku Solver

Python Implementation to convert sudoku problems to CNF form for `minisat` and in turn convert a satisfying assignment of the CNF to a solved Sudoku board.

## Running the Tests

`minisat` needs to be installed to run the tests. On mac install it with `brew install minisat`. Windows and linux are installable [here](http://minisat.se/MiniSat.html).

To run the basic tests run `python3 test.py` and it will fork and run itself against all the standard tests.

To run the hard tests run `python3 hard_test.py` and it will fork and run itself against all of the "hard" tests.
