from string import digits, printable
from tabnanny import check

def row_col(position):
    row = (int(position)//9)//3
    for j in range(9):
        if not((position-j)%9):
            col = j//3
            break
    return(row,col)

def row_check(str_sudoku):
    row = [[] for i in range(9)]
    
    for i,v in enumerate(str_sudoku):
        if int(v) and (v in row[i//9]):
            return False
        else:
            row[i//9].append(v)

    # for num in row:
    #     if len(num) == 9:
    #         if duplicate(num):
    #             return False
    #     else:
    #         print("********ERROR********")
    
    return True #no row had duplicates.

def duplicate(array):
    for i,digit in enumerate(array):
        if (int(digit)) and ((digit in array[:i]) or (digit in array[i+1:])):
            return True
    return False

def column_check(str_sudoku):
    div = {i for i in range(9)}
    col = [[] for i in range(9)] 
            
    for i,v in enumerate(str_sudoku):
        for j in div:
            if not((i-j)%9):
                if int(v) and (v in col[j]):
                    return False
                else:
                    col[j].append(v)
    # for num in col:
    #     if len(num) == 9:
    #         if duplicate(num):
    #             return False #a column is not valid and has duplicate digit
    #     else:
    #         print ("***********ERROR***********")
    return True #no column has duplicate digit, all are valid

def digit_only(str_sudoku):
    for char in str_sudoku:
        if str(char) not in digits:
            return False
    return True    

def cell_check(str_sudoku):
    cells_set = {pair:lett for (pair,lett) in zip([(row,col) for row in range(3) for col in range(3)],range(9))}
    cells = [[] for i in range(9)]
    for i,digit in enumerate(str_sudoku):
        if int(digit) and (digit in cells[cells_set[row_col(i)]]):
            return False
        else:
            cells[cells_set[row_col(i)]].append(digit)
    # for num in cells:
    #     if len(num)==9:
    #         if duplicate(num):
    #             return False
    #     else:
    #         print ("***********ERROR***********")
    return True #temporary return

def check_integrity(str_sudoku, digit=True, printable = True):
    if digit and not(digit_only(str_sudoku)):
        if printable: print("Non Digit Present")
        return False
    elif not(column_check(str_sudoku)):
        if printable: print("Duplicate in a column")
        return False
    elif not(row_check(str_sudoku)):
        if printable: print("Duplicate in a row")
        return False
    elif not(cell_check(str_sudoku)):
        if printable: print("Duplicate present in a cell")
        return False
    else:
        return True

def all_empty(str_sudoku):
    size = 0
    for char in str_sudoku:
        if char == '0': size+=1
    return size

def next_attempt(str_sudoku):
    return str(int(str_sudoku) + 1).replace("0","1")

def filled_sudoku(str_sudoku, string):
    filled = ""
    string = list(string)
    for char in str_sudoku:
        if int(char):
            filled += char
        else:
            filled += string[0]
            string.pop(0)
    return filled

def brutefoce(str_sudoku):
    size = all_empty(str_sudoku)
    sudoku = "1"*size
    last = "9"*size
    count = 0
    while True:
        attempt = filled_sudoku(str_sudoku,sudoku)
        count += 1
        print("attempt: {0} | {1}".format(count,sudoku), end="\r")
        if check_integrity(attempt, digit=False, printable = False):
            print(count)
            return attempt
        elif not (sudoku is last):
            sudoku = next_attempt(sudoku)
            continue
        else:
            print ("ERROR, no solution")
            return 0

a = "367849512542713896189625437423567981956281374871394265214936758635478129798100000"
unsolved = "060800510502013006080005007003000900950081000001304260200906700600000009790102043"
solution = "367849512542713896189625437423567981956281374871394265214936758635478129798152643"
if check_integrity(unsolved):
    print(brutefoce(unsolved))
    print(solution)