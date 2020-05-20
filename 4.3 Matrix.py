from grid import Grid

matrix = Grid(3,3)

for row in range(matrix.getHeight()):
    for column in range(matrix.getWidth()):
        print(matrix)
        matrix[row][column] = row * column

print(matrix)
