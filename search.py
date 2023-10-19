import heapq as heap
from sre_constants import SUCCESS
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


def neighbors(state):
    # TO BE IMPLEMNTED
    return 

def aStarSearch(initialState, heuristic):
    # TO BE IMPLEMNTED
    
    initialState = initialState.board
    frontier = []
    explore = set()
    
    heap.heappush(frontier, (heuristic(initialState), 0, initialState, [])) #push in frontier: which heuristic method, cost, initial state and the path 

    while frontier:
        _,cost, currentState, path = heap.heappop(frontier)

        if(isGoal(currentState)):
            return path

        explore.add(currentState)

        for neighbor in neighbors(currentState):
            if neighbor not in frontier and neighbor not in explore:
                newCost = cost + 1
                heap.heappush(frontier, (newCost + heuristic(initialState), newCost , neighbor, path + [neighbor]))

            elif neighbor in frontier:
                frontier.decreaseKey(neighbor)

    return "FAILURE"            

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch