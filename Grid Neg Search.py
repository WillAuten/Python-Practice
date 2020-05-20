from grid import Grid
from random import randrange

negative = randrange(-10,0)
number = randrange(0,10)

table = Grid(10,10,number)
table[number][number] = -2
print(table)

for row in range(table.getHeight()):
    for column in range(table.getWidth()):
        if table[row][column] < 0:
            print("The negative number is at row " + str(row) + " and column " + str(column))
            break

print("We have " + str(row) + " rows and " + str(column) + " columns")
