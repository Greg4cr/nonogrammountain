from random import *

height = 15
width = 15

# Initialize an empty grid

grid = [[0]*width for i in range(height)]

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

col_sequences = [0 for i in range(width)]
labels_x = [[] for i in range(width)]
labels_y = ['0' for i in range(height)]

for row in range(height):
    label = ''
    sequence = 0
    for index in range(len(grid[row])):
        if grid[row][index] == 1:
            sequence += 1
            col_sequences[index] += 1
        else:
            if sequence > 0:
                label += (str(sequence) + ' ')
            if col_sequences[index] > 0:
                labels_x[index].append(str(col_sequences[index]))

            sequence = 0
            col_sequences[index] = 0

    if sequence > 0:
        label += (str(sequence) + ' ')

    labels_y[row] = label[:-1]

for index in range(width):
    if col_sequences[index] > 0:
        labels_x[index].append(str(col_sequences[index]))


# Print resulting nonogram

longest_x = 1
for label in labels_x:
    if len(label) > longest_x:
        longest_x = len(label)

longest_y = 1
for label in labels_y:
    if len(label) > longest_y:
        longest_y = len(label)

divider = '         '
for spacer in range(longest_y):
    divider += ' '
out_x = [[] for i in range(longest_x)]
for label in range(len(labels_x)):
    for index in range(len(labels_x[label])):
        out_x[index].append(labels_x[label][index])
    for index in range(len(labels_x[label]), longest_x):
        out_x[index].append(' ')

for line in range(longest_x):
    print(divider + str(out_x[line]).replace(',','').replace('[','').replace(']','').replace('\'',''))

divider = '---------'
for spacer in range(longest_y):
    divider += '-'
for spacer in range(width):
    divider += '--'
print(divider)

for row in range(height):
    divider = ''
    for space in range(longest_y - len(labels_y[row])):
        divider += ' '
    
    print(labels_y[row] + divider + '    |    ' + str(grid[row]).replace(',','').replace('[','').replace(']','').replace('0',' ').replace('1','•'))
