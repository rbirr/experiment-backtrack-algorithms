

def check_vector(vector):
    existing_values = []
    for i in vector:
        if i not in existing_values:
            existing_values.append(i)
        else:
            if i != 0: # 0 is a value not entered
                return 0
    return 1


def is_solution(board):
    # check rows
    for r in board:
        if check_vector(r) != 1:
            return 0
    # check columns
    for i in range (0, 9):
        column = get_column(board, i)
        if check_vector(column) != 1:
            return 0
    # check sub-matrizes
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            vector = get_submatrix_as_vector(board, i, j)
            if check_vector(vector) != 1:
                return 0
            j += 3
        i += 3
    return 1


def get_column(matrix, i):
    return [row[i] for row in matrix]


def get_submatrix_as_vector(matrix, x, y):
    """
    :param matrix: the 9x9 matrix
    :param i: which matrix [1,2,3,4,5,6,7,8,9] starting from top left
    :return: the 3x3 submatrix as vector [row1, row2, row3]
    """
    vector = []
    for row in matrix[y:y+3]:
        vector += row[x:x + 3]
    return vector


def get_next_empty_cell(matrix, pos):
    for i in range(0, 9):
        for j in range(0, 9):
            if matrix[i][j] == 0:
                pos[0]=i
                pos[1]=j
                return True
    return False


def print_board(board):
    for r in board:
        for c in r:
            print(c, end=" ")
        print()
    return 1


def check_position(board, row, col, value):
    copy_board = board
    copy_board[row][col]=value
    if is_solution(copy_board):
        return True
    return False


def solve(board):
    pos = [0, 0]
    if not get_next_empty_cell(board, pos):
        return True;
    else:
        row = pos[0]
        col = pos[1]
        for value in range(1, 10): # try every value from 0, 9 in that position
            if check_position(board, row, col, value):
                board[pos[0]][pos[1]] = value
                if solve(board):
                    return True
        board[pos[0]][pos[1]] = 0 # reset
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    if solve(board):
        print_board(board)
    else:
        print("Not solvable")

