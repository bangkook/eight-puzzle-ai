import time
from search import aStarSearch

class EightPuzzleState:
    def __init__(self, puzzle): # puzzle is 1d for simplicity, convert to 2d in init
        self.board = []
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append(puzzle[3*i+j])
                if(self.board[i][j] == 0):
                    self.blankPosition = (i, j)

    # Check if given coordinates are valid
    def _isValid(self, x, y):
        return x >= 0 and x < 3 and y >= 0 and y < 3


    def nextStates(self):
        """
            Returns list of next (state, move) for this state.
        """
        x, y = self.blankPosition

        # List of tuples (state, direction)
        nextStates = []
        directions = ['up', 'right', 'down', 'left']
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(len(directions)):
            newX = x + dx[i]
            newY = y + dy[i]
            if(self._isValid(newX, newY)):
                nextStates.append((self._applyMove(newX, newY), directions[i]))
        
        return nextStates

    # Return a new state after changing the blank's cell position to (newX, newY)
    def _applyMove(self, newX, newY):
        newState = EightPuzzleState([0]*9)
        newState.board = [row[:] for row in self.board]
        x, y = self.blankPosition

        newState.board[newX][newY] = self.board[x][y]
        newState.board[x][y] = self.board[newX][newY]
        newState.blankPosition = (newX, newY)

        return newState
        
    # A goal is reached when the cell value equals the cell index in 1d array
    def isGoal(self):
        for i in range(3):
            for j in range(3):
                if(self.board[i][j] != 3*i + j):
                    return False
        return True

    def __str__(self):
        lines = []
        lines.append("-------------")
        for row in self.board:
            line = '|'
            for value in row:
                if value == 0:
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
        self.actions, self.expandedNodes, self.depth = searchFunc(initialState)
        self.endTime = time.time()

    def getActions(self):
        return self.actions

    def getCost(self):
        return len(self.actions) 

    def getExpandedNodes(self):
        return self.expandedNodes

    def getDepth(self):
        return self.depth

    def getTime(self):
        return self.endTime - self.startTime

if __name__ == '__main__':
    puzzle = [0, 2, 3, 1, 4, 5, 6, 7, 8]
    state = EightPuzzleState(puzzle)
    print(state)
    #for s, d in state.nextStates():
    #    print(s, d)
    aStarSearch(state)
    """
    function = bfs
    agent = EightPuzzleAgent(state, function)
    actions = agent.getActions()

    print(state)
    for action in actions:
        state = state.nextState(action)
        print(action, state)

    print("Cost = ", agent.getCost())
    print("Expanded Nodes = ", agent.getExpandedNodes())
    print("Search Depth = ", agent.getDepth())
    print("Total Time = ", agent.getTime())
    """
