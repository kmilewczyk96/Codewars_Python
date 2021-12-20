########################################################################################################################
# Sudoku is a game played on a 9x9 grid.
# The goal of the game is to fill cells of the grid with digits from 1 to 9,
# so that each column, each row, and each of the nine 3x3 sub-grids
# (also known as blocks) contain all the digits from 1 to 9.
#
# Write a function validSolution/ValidateSolution/valid_solution()
# that accepts a 2D array representing a Sudoku board,
# and returns true if it is a valid solution, or false otherwise.
# The cells of the sudoku board may also contain 0's, which will represent empty cells.
# Boards containing one or more zeroes are considered to be invalid solutions.
#
# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
########################################################################################################################
def valid_solution(board):
    for row in board:
        repetition_check = {0}
        repetition_check.update(row)
        if sum(repetition_check) != 45:
            return False

    for i in range(0, 9):
        current_values = 0
        for row in board:
            current_values += row[i]
        if current_values != 45:
            return False

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            square_sum = 0
            for x in board[r: r + 3]:
                for column in range(c, c + 3):
                    square_sum += x[column]
            if square_sum != 45:
                return False

    return True


if __name__ == '__main__':
    print(valid_solution([
      [5, 3, 4, 6, 7, 8, 9, 1, 2],
      [6, 7, 2, 1, 9, 5, 3, 4, 8],
      [1, 9, 8, 3, 4, 2, 5, 6, 7],
      [8, 5, 9, 7, 6, 1, 4, 2, 3],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 6, 1, 5, 3, 7, 2, 8, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]))

    print(valid_solution([
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]))
