from string import digits

def row_col(position):
    """give the section position(3x3) of the given cell"""
    row = (int(position)//9)//3
    for j in range(9):
        if not((position-j)%9):
            col = j//3
            break
    return(row,col)

def row_check(str_sudoku):
    """check for duplicates in row of a sudoku. Return True if there are no duplicates, False if there are."""
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
    """check for duplicates in array
    Possibly depracated"""
    for i,digit in enumerate(array):
        if (int(digit)) and ((digit in array[:i]) or (digit in array[i+1:])):
            return True
    return False

def column_check(str_sudoku):
    """Check for duplicated in column of given sudoku string. Returns True if there are no duplicates, False if there are"""
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
    """Ensure that only digits are in the string and no other symbol"""
    for char in str_sudoku:
        if str(char) not in digits:
            return False
    return True    

def cell_check(str_sudoku):
    """Check that there are no duplicates in the section of the cell. Return True if there are no duplicates, False if there are."""
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
    """Go through the different check to ensure that no duplicate is found and that Sudoku is still valid. Return True if there are no duplicates, False if there are.
        Additional feature is toggle to check that there only digits (Toggle off after initial input check) and toggle to print where the duplicate was found at each call."""
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
    """Return how many empty slots/cells there are in the sudoku"""
    size = 0
    for char in str_sudoku:
        if char == '0': size+=1
    return size

def next_smart_attempt(str_sudoku,possibilities):
    """Gives you the next possible sudoku solution for the smart brute force, by checking for all possibilities of empy slots and loops the array from the right.
        Return the new updated sudoku solution to check.
        
        TODO: Find a way to put a check in place and return 0 in case that there is no possible solution."""
    matrix = possibilities[::-1]
    str_sudoku = str_sudoku[::-1]
    return_sudoku = ""
    remainder = True
    for i in range(len(str_sudoku)):
        if len(matrix[i]) == 1 or not(remainder):
            return_sudoku += str_sudoku[i]
        elif remainder:
            for j,digit in enumerate(matrix[i]):
                if digit == str_sudoku[i]:
                    if j < len(matrix[i])-1:
                        return_sudoku += matrix[i][j+1]
                        remainder = False
                    else:
                        return_sudoku += matrix[i][0]
                        remainder = True
                    break
    return return_sudoku[::-1]                   

def next_dumb_attempt(str_sudoku):
    """Return the next attempt of the dumb bruteforce by incresing the string of digits for each empty slot, needed in the filled_sudoku function"""
    return str(int(str_sudoku) + 1).replace("0","1")

def filled_sudoku(str_sudoku, string):
    """Fill the empy slots with string of numbers. Returned filled sudoku string. Needed in dumb bruteforce."""
    filled = ""
    string = list(string)
    for char in str_sudoku:
        if int(char):
            filled += char
        else:
            filled += string[0]
            string.pop(0)
    return filled

def maxi(array):
    """Globalise REVERSED string of the lenght of possibilities for all the slots.
    Possibily DEPRACATEED"""
    global maxi_cell
    maxi_cell = ""
    for cell in array:
        maxi_cell+=str(len(cell))
    maxi_cell[::-1]
    return 0

def smart_brute(str_sudoku):
    """Initialise the smart bruteforce of the sudoku string."""
    possibilities = [[] for i in range(len(str_sudoku))]
    for cell,char in enumerate(str_sudoku):
        if int(char):
            possibilities[cell].append(char)
        else:
            for i in range(1,10):
                if check_integrity(str_sudoku[:cell]+str(i)+str_sudoku[cell+1:], digit = False, printable= False): 
                    possibilities[cell].append(str(i))
    
    first_attempt = ""
    for array in possibilities:
        first_attempt += array[0]
    maxi(possibilities)
    return (first_attempt,possibilities)

def dumb_brute(str_sudoku):
    """Brute forcing in a dumb way the sudoky string."""
    sudoku = "1"*all_empty(str_sudoku)
    last = int("9"*all_empty(str_sudoku))
    count = 0
    while True:
        attempt = filled_sudoku(str_sudoku,sudoku)
        count += 1
        print("attempt: {0} | {1}".format(count,sudoku), end="\r")
        if check_integrity(attempt, digit=False, printable = False):
            print(count)
            return attempt
        elif int(sudoku) < last:
            sudoku = next_dumb_attempt(sudoku) #see how to implement this function
            continue
        else:
            print ("ERROR, no solution")
            return 0

def bruteforce(str_sudoku, smart=True):
    """Bruteforce function to solve a given sudoku in string format. Smart toggle allows for the choice between extremely inefficient dumb bruteforce and the more efficient method which is bruteforcing the solution by limiting attempts to only possible choices in slots (not all 1 to 9)"""
    if smart:
        sudoku,possibilities = smart_brute(str_sudoku)
    else:
        return dumb_brute(str_sudoku)
    count = 0
    while True:
        count += 1
        # print("attempt: {0} | {1}".format(count,sudoku), end="\r")
        if check_integrity(sudoku, digit=False, printable = False):
            #print(count)
            return sudoku
        else:
            sudoku = next_smart_attempt(sudoku,possibilities) #see how to implement this function
            print(f"{count}\t{sudoku}",end="\n")
            if not(sudoku):
                print("ERROR === NO SOLUTION FOUND")
                return 0
        

a = "367849012542703806009625437023500900006280304871390265204036750630478129798100000"
unsolved = "060800510502013006080005007003000900950081000001304260200906700600000009790102043"
solution = "367849512542713896189625437423567981956281374871394265214936758635478129798152643"
if check_integrity(a):
    solved = bruteforce(a,smart=True)
    print()
    print(solved)
    print(solution)
    print(solution==solved)