def solve_sudoku(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                for num in range(1, 5):
                    valid = True
                    for k in range(4):
                        if matrix[i][k] == num or matrix[k][j] == num:
                            valid = False
                    box_i, box_j = (i//2)*2, (j//2)*2
                    for x in range(2):
                        for y in range(2):
                            if matrix[box_i+x][box_j+y] == num:
                                valid = False
                    if valid:
                        matrix[i][j] = num
                        if solve_sudoku(matrix):
                            return True
                        matrix[i][j] = 0
                return False
    return True

matrix = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4]
]

solve_sudoku(matrix)
for row in matrix:
    print(''.join(map(str, row)))
