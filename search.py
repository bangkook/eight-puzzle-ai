import heapq as heap
from sre_constants import SUCCESS
from eightpuzzle import isGoal
"""
    Each search function:
    1- takes state as input.
    2- Performs the search.
    3- Returns the path to goal (list of actions), expanded nodes, and depth of the search.
"""

def breadthFirstSearch(initialState):
    # TO BE IMPLEMNTED
    pass

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