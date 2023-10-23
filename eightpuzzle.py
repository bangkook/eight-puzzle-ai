import copy
import time
from search import *
from heuristics import *

class EightPuzzleState:
    def __init__(self, puzzle): # puzzle is 1d for simplicity, convert to 2d in init
        self.board = ""
        for i in range(9):
            self.board = self.board + str(puzzle[i])
            if(puzzle[i] == 0):
                self.blankPosition = i

    # Check if given coordinates are valid
    def _isValid(self, x, y):
        return x >= 0 and x < 3 and y >= 0 and y < 3

    def __lt__(self, other):
        return True
    def nextStates(self):
        """
            Returns list of next (state, move) for this state.
        """
        x = self.blankPosition // 3
        y = self.blankPosition % 3

        # List of tuples (state, direction)
        nextStates = []
        directions = ['up', 'down', 'left', 'right']
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(len(directions)):
            newX = x + dx[i]
            newY = y + dy[i]
            if(self._isValid(newX, newY)):
                nextStates.append((self._applyMove(3 * newX + newY), directions[i]))
        
        return nextStates

    # Return a new state after changing the blank's cell position to (newX, newY)
    def _applyMove(self, newPos):
        newState = EightPuzzleState([0]*9)
        puzzle = list(self.board) 
        pos = self.blankPosition
    
        puzzle[newPos] = self.board[pos]
        puzzle[pos] = self.board[newPos]

        newState.board = ''.join(puzzle)
        newState.blankPosition = newPos

        return newState
        
    # A goal is reached when the cell value equals the cell index in 1d array
    def isGoal(self):
        return self.board == '012345678'

    def __str__(self):
        return asciiBoard(self.board)

def asciiBoard(board):
    lines = []
    lines.append("-------------")
    for x in range(3):
        line = '|'
        for y in range(3):
            value = board[3 * x + y]
            if value == '0':
                value = ' '
            line = line + ' ' + value.__str__() + ' |'
        lines.append(line)
        lines.append("-------------")
    return "\n".join(lines)

def solvable(puzzle):
    inversion_count = 0
    p=copy.deepcopy(puzzle)
    p.remove(0)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                inversion_count += 1

    return inversion_count % 2 == 0

class EightPuzzleGame:
    def __init__(self, initialState):
        self.initialState = initialState
  
    def getNeighbours(self, state):
        return state.nextStates()

    def getInitialState(self):
        return self.initialState

    def isGoalState(self, state):
        return state.isGoal()

class EightPuzzleAgent:
    def __init__(self, initialState, fn, heuristic=lambda x : 0):
        if fn.__name__ == 'aStarSearch':
            self.searchFunc = lambda x : fn(x, heuristic)
        else:
            self.searchFunc = fn

        self.startTime = time.time()
        self.parentMap, self.cost, self.expandedNodes, self.depth = self.searchFunc(initialState)
        self.endTime = time.time()
        
    def getPath(self):
        path = []
        actions = []
        board = '012345678' #self.expandedNodes[-1]
        path.append(board)
        while board in self.parentMap.keys():
            board, action = self.parentMap[board]
            path.append(board)
            actions.append(action)
        return path[::-1], actions[::-1] # reverse

    def getCost(self):
        return self.cost 

    def getExpandedNodes(self):
        return self.expandedNodes

    def getDepth(self):
        return self.depth

    def getTime(self):
        return self.endTime - self.startTime



if __name__ == '__main__':
    #puzzle = [1,4,2,6,5,8,7,3,0]
    #print(solvable(puzzle))
    #state = EightPuzzleState(puzzle)
    puzzles = [[8, 0, 6, 5, 4, 7, 2, 3, 1], [ 1,2,5,3,4,0,6,7,8], [1,4,2,6,5,8,7,3,0], [1,0,2,7,5,4,8,6,3]]
    #function = breadthFirstSearch
    #function = aStarSearch
    
        

    