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

        for state in curState.nextStates():
            if state.board not in explored:
                frontier.insert(0, (state, 1 + curDepth))
                explored.add(state.board)
                parent[state.board] = curState.board

    return [], 100000000, expanded, depth


def depthFirstSearch(initialState):
    forntier = []
    explored = []
    forntier.append((initialState,0))
    parentMap = {}
    expntier = set()
    expntier.add(initialState.board)
    searchDepth=0
    while forntier:
        curr, depth = forntier.pop()
        searchDepth=max(searchDepth,depth)
        explored.append(curr.board)

        if curr.isGoal():
            return parentMap, depth, explored, searchDepth


        for neighbor in reversed(curr.nextStates()):
            if neighbor.board not in expntier:
                forntier.append((neighbor,depth+1))
                expntier.add(neighbor.board)
                parentMap[neighbor.board] = curr.board


    return [],100000000,explored,100000000



def aStarSearch(initialState, heuristic):
    frontier = []  # Priority queue (min-heap)
    frontierSet = set()  # Set to check if a state is in the frontier
    explore = set()
    parentM = dict()
    #parentM[initialState.board] = initialState.board  # Store parent states directly
    actions = list()
    # Add depth tracking
    depth = {initialState: 0}

    heap.heappush(frontier, (heuristic(initialState.board), 0, initialState))
    frontierSet.add((heuristic(initialState.board), 0, initialState))

    while frontier:
        cost, currentDepth, currentState = heap.heappop(frontier)
        frontierSet.remove((cost, currentDepth, currentState))

        if currentState.isGoal():
            print("FINAL PATH", currentState.board)
            board = currentState
            # actions.append(board)
            # while board in parentM.keys():
            #     parent_state = parentM[board]
            #     del parentM[board]
            #     actions.append(parent_state)
            #     board = parent_state
            # actions.reverse()
            # for action in actions:
            #     print("Actions:", action)
            print("Cost:", cost)
            print("Explore:", explore)
            print("Depth:", depth[currentState])
            return parentM, cost, explore, depth[currentState]

        explore.add(currentState.board)

        for state in currentState.nextStates():
            newDepth = currentDepth + 1
            newCost = newDepth + heuristic(state.board)

            if (newCost, newDepth, state) not in frontierSet and state.board not in explore:
                heap.heappush(frontier, (newCost, newDepth, state))
                frontierSet.add((newCost, newDepth, state))
                parentM[state.board] = currentState.board  # Store the parent state directly
                depth[state] = newDepth
            elif (any, newDepth, state) in frontierSet:
                print("here")
                if newCost < frontierSet[state][0]:
                    heap.heappush(frontier, (newCost, newDepth, state))
                    frontierSet.add((newCost, newDepth, state))
                    parentM[state.board] = currentState.board  # Update the parent state
                    depth[state] = newDepth

    return [], 1000000, explore, 0


    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch