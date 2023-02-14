# Sudoku Solver

Python Implementation to convert sudoku problems to CNF form for `minisat` and in turn convert a satisfying assignment of the CNF to a solved Sudoku board.

## Running The Executables

There are eight primary executables in the project:
1. `sud2sat`
2. `sat2sud`
3. `sud2sat1`
4. `sat2sud1`
5. `sud2sat2`
6. `sat2sud2`
7. `sud2sat3`
8. `sat2sud3`

In theory each of these executables are runnable simply by `./sud2sat` (or whatever the appropriate number is). The scripts use a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) directive at the top of the script to resolve your local install of python3 and execute in that environment.

*NOTE: If the executables themselves do not work they are also runnable with `python3 ./sud2sat`. That is by simply prepending the run command with `python3`. This should not be necessary in any standard Unix based environment.*

## Project Layout

### The Lib folder

Inside of the lib folder you will find the main code of the project. There are 4 primary files in this folder:
1. `reader`: Functions associated with transforming strings read from standard in to appropriate formats.
2. `writer`: Functions associated with transforming parsed data into strings to be written out
3. `cnf`: Functions associated with converting a puzzle to CNF form
4. `sat`: Functions associated with converting a SAT assignment to a complete solution to a puzzle.

### Tests

The tests are arranged into multiple folders:
1. `tests`: This is the folder with the output of the standard `sat2sud` executables. This also contains the files for the individual strings.
2. `tests_2`: This is the folder with the output of tests ran with `sud2sat2` and `sat2sud2`
2. `tests_3`: This is the folder with the output of tests ran with `sud2sat3` and `sat2sud3`

### Report

The LaTeX and PDF file of the associated Report.

## Running the Tests

`minisat` needs to be installed to run the tests. On mac install it with `brew install minisat`. Windows and linux are installable [here](http://minisat.se/MiniSat.html).

To run the tests run `./test.py`, this will run all the tests against each of the three executable cases.

*Note: The test script will fail on windows as windows cannot understand shebang lines*
