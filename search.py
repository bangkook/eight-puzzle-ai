import heapq as heap
import sys
sys.path.append('../')

"""
    Each search function:
    1- takes state as input.
    2- Performs the search.
    3- Returns the path to goal (list of actions), expanded nodes, and depth of the search.
"""

def breadthFirstSearch(initialState):
    explored = set()
    frontier = []
    frontier.insert(0, (initialState, 0)) # (state, depth)
    explored.add(initialState.board)
    actions = list()
    parent = dict()
    expanded = []
    depth = 0

    while len(frontier) > 0:
        curState, curDepth = frontier.pop()
        
        expanded.append(curState.board)

        depth = max(depth, curDepth)

        if curState.isGoal():
            return parent, curDepth, expanded, depth

        #print(curState)
        for state, action in curState.nextStates():
            if state.board not in explored:
                #print(state)
                frontier.insert(0, (state, 1 + curDepth))
                explored.add(state.board)
                parent[state.board] = (curState.board, action)
        #print("FINISHED")

    return [], 100000000, expanded, depth


def depthFirstSearch(initialState):
    forntier = []
    explored = []
    forntier.append((initialState, 0))
    parentMap = {}
    expntier = set()
    expntier.add(initialState.board)
    searchDepth = 0

    while forntier:
        curr, depth = forntier.pop()
        searchDepth = max(searchDepth, depth)

        explored.append(curr.board)

        if curr.isGoal():
            return parentMap, depth, explored, searchDepth

        #print(curr)
        for neighbor, action in reversed(curr.nextStates()):
            if neighbor.board not in expntier:
                expntier.add(curr.board)
                forntier.append((neighbor, depth + 1))
                parentMap[neighbor.board] = (curr.board, action)

        #print("FINISHED")
    return [], 100000000, explored, searchDepth



def aStarSearch(initialState, heuristic):
    frontier = []  # Priority queue (min-heap)
    frontierSet = set()  # Set to check if a state is in the frontier
    explore = set()
    parentM = dict()
    actions = list()
    searchDepth = 0

    heap.heappush(frontier, (heuristic(initialState.board), 0, initialState))
    frontierSet.add(initialState.board)

    while frontier:
        cost, currentDepth, currentState = heap.heappop(frontier)
        frontierSet.remove(currentState.board)

        searchDepth = max(searchDepth, currentDepth)

        explore.add(currentState.board)

        if currentState.isGoal():
            return parentM, currentDepth, explore, searchDepth

        #print(currentState)
        for state, action in currentState.nextStates():
            newDepth = currentDepth + 1
            newCost = newDepth + heuristic(state.board)

            if state.board not in frontierSet and state.board not in explore:
                heap.heappush(frontier, (newCost, newDepth, state))
                frontierSet.add(state.board)
                parentM[state.board] = (currentState.board, action)  # Store the parent state directly
                #print(1, state)
            elif state.board in frontierSet:
                #print(2, state)
                decreaseKey(frontier, state, newDepth, newCost, parentM, currentState.board, action)
        #print("FINISHED")
    return [], 1000000, explore, searchDepth


def decreaseKey(frontier, state, depth, cost, parentMap, parent, action):
    for i, (c, d, s) in enumerate(frontier):
        if s.board != state.board:
            continue
        #print(1)
        if c <= cost :
            break
        #print(2)
        frontier[i] = (cost, depth, state)
        parentMap[state.board] = (parent, action)
        heap.heapify(frontier)
        