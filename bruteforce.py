from Sudoku.functools import *

unsolved = "060800510502013006080005007003000900950081000001304260200906700600000009790102043"
solved = "367849512542713896189625437423567981956281374871394265214936758635478129798152643"

def main():
    while True:
        #input("Sudoku: ")
        unsolved = unsolved
        if check_integrity(unsolved):
            solution = bruteforce(unsolved)
            print(f"Solution of sudoku is :{solution}") 
        else:
            print("Invalid sudoku, enter valid sudoku")
    #retrieve unsolved sudoku array
    #brute force solutions
    #check solution to respect for rules.
    #temp check with actual solution.

if __name__ == "__main__":
    main()