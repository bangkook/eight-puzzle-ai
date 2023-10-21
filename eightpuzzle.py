import time
from search import breadthFirstSearch, aStarSearch
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
        directions = ['up', 'right', 'down', 'left']
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(len(directions)):
            newX = x + dx[i]
            newY = y + dy[i]
            if(self._isValid(newX, newY)):
                nextStates.append(self._applyMove(3 * newX + newY))
        
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
    def __init__(self, initialState, searchFunc):
        self.startTime = time.time() 
        self.parentMap, self.cost, self.expandedNodes, self.depth = searchFunc(initialState)
        self.endTime = time.time()
        
    def getPath(self):
        path = []
        board = self.expandedNodes[-1]
        path.append(board)
        while board in self.parentMap.keys():
            board = self.parentMap[board]
            path.append(board)
        return path[::-1] # reverse of path

    def getCost(self):
        return self.cost 

    def getExpandedNodes(self):
        return self.expandedNodes

    def getDepth(self):
        return self.depth

    def getTime(self):
        return self.endTime - self.startTime

if __name__ == '__main__':
    puzzle =  [1, 2, 3, 4, 5, 0, 6, 7, 8]

    state = EightPuzzleState(puzzle)

    function = breadthFirstSearch
    #function = aStarSearch
    agent = EightPuzzleAgent(state, function)
    for board in agent.getPath():
        print(asciiBoard(board))
    
    #print(state)

    # for state in actions:
    #     print(asciiBoard(state))

    # print(actions[-1])

    # print("Cost = ", agent.getCost())

    # print("Expanded Nodes = ", agent.getExpandedNodes())

    # print("Search Depth = ", agent.getDepth())
    # print("Total Time = ", agent.getTime())
    