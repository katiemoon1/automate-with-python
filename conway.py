# Conway's Game of Life
import random
import time
import copy
WIDTH = 60
HEIGHT = 20

# create a list for the cells
nextCells = []
for x in range(WIDTH):
    # creates a new column
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            # add a living cell
            column.append('#')
        else:
            # add a dead cell
            column.append(' ')
        nextCells.append(column)

# main program loop
while True:
    # separate each step with new lines
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    # print currentCells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()

    # calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            # count number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == "#":
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1

            # set cell based on conway's game of life rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # living cells with 2 or 3 neighbors stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # dead cells with 3 neighbors become alive
                nextCells[x][y] = '#'
            else:
                # everything else dies or stays dead
                nextCells[x][y] = ' '
    time.sleep(1)
