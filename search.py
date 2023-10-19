import heapq as heap
import sys
sys.path.append('../')
import heuristics
"""
    Each search function:
    1- takes state as input.
    2- Performs the search.
    3- Returns the path to goal (list of actions), expanded nodes, and depth of the search.
"""

def breadthFirstSearch(initialState):
    vis = dict()
    frontier = []
    frontier.insert(0, (initialState, 0)) # (state, depth)
    vis[initialState.board] = True
    actions = list()
    pathTo = dict()
    expanded = []
    depth = 0

    while len(frontier) > 0:
        curState, curDepth = frontier.pop()
        
        expanded.append(curState.board)

        depth = max(depth, curDepth)

        if curState.isGoal():
            board = curState.board
            actions.append(board)
            print("finish",board)
            while board in pathTo.keys():
                board = pathTo[board]
                actions.append(board)
            return actions[::-1], len(actions) - 1, expanded, depth

        for state in curState.nextStates():
            if state.board not in vis.keys():
                frontier.insert(0, (state, 1 + curDepth))
                vis[state.board] = True
                pathTo[state.board] = curState.board

    return [], 100000000, expanded, depth


def depthFirstSearch(initialState):
    # TO BE IMPLEMNTED
    pass


class Parent:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def total_cost(self):
        return self.cost + self.heuristic
    
    def __lt__(self, other): # to sort the heap
        return self.total_cost() < other.total_cost()

# def ConstructPath(State):
#     path = []
#     while State:
#         State.insert(0, (State.state, State.action))
#         State = State.parent
#     return path

def aStarSearch(initialState):
    frontier = []  # Priority queue (min-heap)
    frontierSet = set()  # Set to check if a state is in the frontier
    explore = set()
    path = []

    initial_node = Parent(state=initialState, parent=initialState, cost=0, heuristic=heuristics.manhattanHeuristic(initialState.board))
    heap.heappush(frontier, (initial_node.total_cost(), initial_node))
    frontierSet.add((initial_node.total_cost(), initial_node))

    while frontier:
        print("1")
        cost, currentState = heap.heappop(frontier)
        frontierSet.remove((cost, currentState))
        if currentState.state.isGoal():
            print("FINAL PATH", currentState.state.board)
            return [], 0, initialState, 1

        explore.add(currentState.state.board)

        for state in currentState.state.nextStates():
            s = Parent(state=state, parent=currentState, cost=currentState.cost + 1, heuristic=heuristics.manhattanHeuristic(state.board))
            if (s.total_cost, s) not in frontierSet and state.board not in explore:
                newCost = currentState.cost + 1
                neighborNode = Parent(state=state, parent=currentState.state, cost=newCost, heuristic=heuristics.manhattanHeuristic(state.board))
                heap.heappush(frontier, (neighborNode.total_cost(), neighborNode))
                frontierSet.add((neighborNode.total_cost(), neighborNode))
            elif (s.total_cost, s) in frontierSet:
                print("here")
                costOfState = heuristics.manhattanHeuristic(state.board)
                if costOfState < frontierSet[state].total_cost(): #review
                    newCost = costOfState + 1
                    neighborNode = Parent(state=state, parent=currentState.state, cost=newCost, heuristic=heuristics.manhattanHeuristic(state.board))
                    heap.heappush(frontier, (neighborNode.total_cost(), neighborNode))
                    frontierSet.add((neighborNode.total_cost(), neighborNode))

    return [], 0, initialState, 1

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch