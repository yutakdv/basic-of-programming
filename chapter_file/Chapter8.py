##sudoku_4x4.py
import random

def initialize_board_4x4():
    row0 = [1, 2, 3, 4]
    random.shuffle(row0)
    row1 = row0[2:4] + row0[0:2]
    row2 = [row0[1], row0[0], row0[3], row0[2]]
    row3 = row2[2:4] + row2[0:2]
    return [row0, row1, row2, row3]

def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

def transpose(board):
    transposed = []
    size = len(board)
    for _ in range(size):
        transposed.append([])
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed 

def create_solution_board_4x4():
    board = initialize_board_4x4()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

def copy_board(board):
    board_clone = []
    for row in board:
        board_clone.append(row[:])
    return board_clone

def get_level():
    print("Enter your level.")
    level = input("Beginner = 1, Intermediate = 2, Advanced = 3:")
    while level not in ("1", "2", "3"):
        level = input("Beginner = 1, Intermediate = 2, Advanced = 3:")
    if level == "1":
        return 6
    elif level == "2":
        return 8
    else:
        return 10

def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1
    return board

def show_board(board):
    for row in board:
        for entry in row:
            if entry == 0:
                print(".", end = " ")
            else:
                print(entry, end = " ")
        print()

def get_integer(message, i, j):
    number = input(message)
    while not (number.isdigit() and i <= int(number) <= j):
        number = input(message)
    return int(number)

def sudoku_mini():
    solution_board = create_solution_board_4x4()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    show_board(puzzle_board)
    while no_of_holes > 0:
        i = get_integer("Row#(1, 2, 3, 4): ", 1, 4) - 1
        j = get_integer("Column#(1, 2, 3, 4): ", 1, 4) - 1
        if puzzle_board[i][j] != 0:
            print("Not empty!")
            continue
        n = get_integer("Number(1, 2, 3, 4): ", 1, 4)
        if n == solution_board[i][j]:
            puzzle_board[i][j] = solution_board[i][j]
            show_board(puzzle_board)
            no_of_holes -= 1
        else:
            print(n, ": Wrong number! Try again.")
    print("Well done! Come again.")

##sudoku_6x6.py
import random

def initialize_board_6x6():
    row0 = [1, 2, 3, 4, 5, 6]
    random.shuffle(row0)
    row1 = row0[3:] + row0[:3]
    row2 = [row1[5]] + row1[3:5] + [row1[2]] + row1[:2]
    row3 = row2[3:] + row2[:3]
    row4 = [row2[5]] + [row2[3]] + [row2[4]] + [row2[2]] + [row2[0]] + [row2[1]]
    row5 = row4[3:] + row4[:3]
    return [row0, row1, row2, row3, row4, row5]

def shuffle_ribbons(board):
    top = board[:3]
    bottom = board[3:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

def transpose(board):
    transposed = []
    size = len(board)
    for _ in range(size):
        transposed.append([])
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed

def create_solution_board_6x6():
    board = initialize_board_6x6()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

def copy_board(board):
    board_clone = []
    for row in board:
        board_clone.append(row[:])
    return board_clone

def get_level():
    print("Enter your level.")
    level = input("Beginner = 1, Intermediate = 2, Advanced = 3:")
    while level not in ("1", "2", "3"):
        level = input("Beginner = 1, Intermediate = 2, Advanced = 3:")
    if level == "1":
        return 8
    elif level == "2":
        return 10
    elif level == "3":
        return 12

def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0, 5)
        j = random.randint(0, 5)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1
    return board

def show_board(board):
    for row in board:
        for entry in row:
            if entry == 0:
                print(".", end = " ")
            else:
                print(entry, end = " ")
        print()

def get_integer(message, i, j):
    number = input(message)
    while not (number.isdigit() and i <= int(number) <= j):
        number = input(message)
    return int(number)

def sudoku_6x6():
    solution_board = create_solution_board_6x6()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    show_board(puzzle_board)
    while no_of_holes > 0:
        i = get_integer("Row#(1, 2, 3, 4, 5, 6): ", 1, 6) - 1
        j = get_integer("Column#(1, 2, 3, 4, 5, 6): ", 1, 6) - 1
        if puzzle_board[i][j] != 0:
            print("Not empty!")
            continue
        n = get_integer("Number(1, 2, 3, 4, 5, 6): ", 1, 6)
        if n == solution_board[i][j]:
            puzzle_board[i][j] = solution_board[i][j]
            show_board(puzzle_board)
            no_of_holes -= 1
        else:
            print(n, ": Wrong number! Try again.")
    print("Well done! Come again.")

#sudoku_6x6()

##sudoku_9x9.py
import random

def initialize_board_9x9():
    row0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(row0)
    row1 = row0[3:6] + row0[6:] + row0[:3]
    row2 = row1[3:6] + row1[6:] + row1[:3]
    row3 = [row2[4]] + [row2[5]] + [row2[3]] + [row2[7]] + [row2[8]] + [row2[6]] + [row2[1]] + [row2[2]] + [row2[0]]
    row4 = row3[3:6] + row3[6:] + row3[:3]
    row5 = row4[3:6] + row4[6:] + row4[:3]
    row6 = [row5[4]] + [row5[5]] + [row5[3]] + [row5[7]] + [row5[8]] + [row5[6]] + [row5[1]] + [row5[2]] + [row5[0]]
    row7 = row6[3:6] + row6[6:] + row6[:3]
    row8 = row7[3:6] + row7[6:] + row7[:3]
    return [row0, row1, row2, row3, row4, row5, row6, row7, row8]

def shuffle_ribbons(board):
    part1 = board[:3]
    part2 = board[3:6]
    part3 = board[6:]
    random.shuffle(part1)
    random.shuffle(part2)
    random.shuffle(part3)
    return part1 + part2 + part3

def transpose(board):
    transposed = []
    size = len(board)
    for _ in range(size):
        transposed.append([])
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed

def create_solution_board_9x9():
    board = initialize_board_9x9()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

def copy_board(board):
    board_clone = []
    for row in board:
        board_clone.append(row[:])
    return board_clone

def get_level():
    print("Enter your level.")
    level = input("Beginner = 1, Intermediate = 2, Advanced = 3:")
    while level not in ("1", "2", "3"):
        level = input("Beginner = 1, Intermediate = 2, Advanced = 3:")
    if level == "1":
        return 10
    elif level == "2":
        return 12
    else:
        return 14

def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1
    return board

def show_board(board):
    for row in board:
        for entry in row:
            if entry == 0:
                print(".", end = " ")
            else:
                print(entry, end = " ")
        print()

def get_integer(message, i, j):
    number = input(message)
    while not (number.isdigit() and i <= int(number) <= j):
        number = input(message)
    return int(number)

def sudoku_9x9():
    solution_board = create_solution_board_9x9()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    show_board(puzzle_board)
    while no_of_holes > 0:
        i = get_integer("Row#(1, 2, 3, 4, 5, 6, 7, 8, 9): ", 1, 9) - 1
        j = get_integer("Column#(1, 2, 3, 4, 5, 6, 7, 8, 9: ", 1, 9) - 1
        if puzzle_board[i][j] != 0:
            print("Not empty!")
            continue
        n = get_integer("Number(1, 2, 3, 4, 5, 6, 7, 8, 9): ", 1, 9)
        if n == solution_board[i][j]:
            puzzle_board[i][j] = solution_board[i][j]
            show_board(puzzle_board)
            no_of_holes -= 1
        else:
            print(n, ": Wrong number! Try again.")
    print("Well done! Come again.")

sudoku_9x9()