from random import *

height = 15
width = 15

# Initialize an empty grid

grid = [[0]*width for i in range(height)]
labels_x = ['0' for i in range(width)]
labels_y = ['0' for i in range(height)]

# Fill grid

# Generate a random nonogram at first
for row in range(height):
    for column in range(width):
        grid[row][column] = randrange(2)

# Heuristically prune the nonogram to be more 'realistic'
# Rule 1: Nonograms should not have standalone pixels (only clusters)
for row in range(height):
    # For debugging
    #if row != 0:
    #    print(grid[row-1])
    #print(grid[row])
    #if row +1 != height:
    #    print(grid[row + 1])

    for column in range(width):
        if grid[row][column] == 1:
            neighbor = False
            if row != 0:    
                if column != 0 and grid[row - 1][column - 1] == 1: # Top-left
                        neighbor = True
                if grid[row - 1][column] == 1: # Top
                        neighbor = True
                if column + 1 != width and grid[row - 1][column + 1] == 1: # Top-right
                        neighbor = True
            if column != 0 and grid[row][column - 1] == 1: # Left
                neighbor = True
            if column + 1 != width and grid[row][column + 1] == 1: # Right
                neighbor = True         
            if row + 1 != height:    
                if column != 0 and grid[row + 1][column - 1] == 1: # Bottom-left
                        neighbor = True
                if grid[row + 1][column] == 1: # Bottom
                        neighbor = True
                if column + 1 != width and grid[row + 1][column + 1] == 1: # Bottom-right
                        neighbor = True

            if neighbor == False:
                grid[row][column] = 0

# Calculate labels

# Print resulting nonogram

longest_y = 1
for label in labels_y:
    if len(label) > longest_y:
        longest_y = len(label)

divider = '         '
for spacer in range(longest_y):
    divider += ' '
print(divider + str(labels_x).replace(',','').replace('[','').replace(']','').replace('\'',''))

divider = '---------'
for spacer in range(longest_y):
    divider += '-'
for spacer in range(width):
    divider += '--'
print(divider)

for row in range(height):
    print(labels_y[row] + '    |    ' + str(grid[row]).replace(',','').replace('[','').replace(']','').replace('0','').replace('1','•'))
