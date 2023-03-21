# Kevin Riemer
# riemerk@oregonstate.edu
# CS 325
# Homework 8: Graph Algorithms - 2
# Due: 3/6/23

def solve_puzzle(board, source, destination):
    possiblePaths = depth_first_search(board, source[0], source[1], destination, '', [])  # perform depth first search 
    # to find possible paths
    
    outputPath = []  # initialize output
    shortestPath = float('inf')  # initialize shortest path
    
    for path in possiblePaths:  # find shortest path
        shortestPath = min(len(path), shortestPath)
        
    for path in possiblePaths:  # append shortest path to output
        if len(path) == shortestPath:
            outputPath.append(path)
        
    if outputPath == []:  # check if none
        return None
    
    strings = outputPath.pop()  # pop strings off
    outputPath = []  # initialize for final path
    currentPos_x = source[0]  # initialize x pos
    currentPos_y = source[1]  # initialize y pos
    for move in strings:  # build path from strings
        if move == 'D':
            currentPos_x += 1
            outputPath.append((currentPos_x, currentPos_y))
        elif move == 'U':
            currentPos_x -= 1
            outputPath.append((currentPos_x, currentPos_y))  
        elif move == 'R':
            currentPos_y += 1
            outputPath.append((currentPos_x, currentPos_y))
        elif move == 'L':
            currentPos_y -= 1
            outputPath.append((currentPos_x, currentPos_y))
            
    outputPath.insert(0, source)  # put source at beginning
    
    overallOutPut = (outputPath, strings)  # create output tuple
    
    return overallOutPut
   

def check_move(board, x, y):
    # check if we can make the move
    output = False
    if x >= 0 and y >= 0 and x < len(board) and y < len(board[x]) and board[x][y] == '-':
        output = True
    
    return output

def depth_first_search(board, x, y, move, path, possiblePaths):
    if check_move(board, x, y) is False:
        return
    
    if move == (x, y):  # if the move is complete
        possiblePaths.append(path)
        return possiblePaths
    
    board[x][y] = '#'  # mark visited
    
    # check possible moves
    if check_move(board, x + 1, y) is True:
        depth_first_search(board, x + 1, y, move, path + 'D', possiblePaths)
        
    if check_move(board, x - 1, y) is True:
        depth_first_search(board, x - 1, y, move, path + 'U', possiblePaths)
        
    if check_move(board, x, y + 1) is True:
        depth_first_search(board, x, y + 1, move, path + 'R', possiblePaths)
        
    if check_move(board, x, y - 1) is True:
        depth_first_search(board, x, y - 1, move, path + 'L', possiblePaths)
        
    board[x][y] = '-'  # unmark because we moved
    
    return possiblePaths 
  
#puzzle = [     ['-', '-', '-', '-', '-'],     ['-', '-', '#', '-', '-'],     ['-', '-', '-', '-', '-'], 
#    ['#', '-', '#', '#', '-'], 
#    ['-', '#', '-', '-', '-'] ] 

#print(solve_puzzle(puzzle, (0, 2), (2, 2)))
#print(solve_puzzle(puzzle, (0, 0), (4, 4)))
#print(solve_puzzle(puzzle, (0,0), (4,0)))
