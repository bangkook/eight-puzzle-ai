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
    explored = set()
    forntier.append((initialState,0))
    parentMap = []
    parentMap.append((initialState.board,initialState.board))
    expntier = set()
    expntier.add(initialState.board)
    searchDepth=0
    while forntier:
        curr, depth = forntier.pop()
        searchDepth=max(searchDepth,depth)

        if curr.isGoal():
            return parentMap, depth, explored, searchDepth

        explored.add(curr.board)
        for neighbor in reversed(curr.nextStates()):
            if neighbor.board not in expntier:
                forntier.append((neighbor,depth+1))
                expntier.add(neighbor.board)
                parentMap.append((neighbor.board,curr.board))


    return [],100000000,explored,100000000







# class Parent:
#     def __init__(self, state, parent=None, cost=0, heuristic=0):
#         self.state = state
#         self.parent = parent
#         self.cost = cost
#         self.heuristic = heuristic

#     def total_cost(self):
#         return self.cost + self.heuristic
    
#     def __lt__(self, other): # to sort the heap
#         return self.total_cost() < other.total_cost()

# def ConstructPath(State):
#     path = []
#     while State:
#         State.insert(0, (State.state, State.action))
#         State = State.parent
#     return path

# def aStarSearch(initialState):
#     frontier = []  # Priority queue (min-heap)
#     frontierSet = set()  # Set to check if a state is in the frontier
#     explore = set()
#     path = []

#     initial_node = Parent(state=initialState, parent=initialState, cost=0, heuristic=heuristics.manhattanHeuristic(initialState.board))
#     heap.heappush(frontier, (initial_node.total_cost(), initial_node))
#     frontierSet.add((initial_node.total_cost(), initial_node))

#     while frontier:
#         print("1")
#         cost, currentState = heap.heappop(frontier)
#         frontierSet.remove((cost, currentState))
#         if currentState.state.isGoal():
#             print("FINAL PATH", currentState.state.board)
#             return [], 0, initialState, 1

#         explore.add(currentState.state.board)

#         for state in currentState.state.nextStates():
#             s = Parent(state=state, parent=currentState, cost=currentState.cost + 1, heuristic=heuristics.manhattanHeuristic(state.board))
#             if (s.total_cost, s) not in frontierSet and state.board not in explore:
#                 newCost = currentState.cost + 1
#                 neighborNode = Parent(state=state, parent=currentState.state, cost=newCost, heuristic=heuristics.manhattanHeuristic(state.board))
#                 heap.heappush(frontier, (neighborNode.total_cost(), neighborNode))
#                 frontierSet.add((neighborNode.total_cost(), neighborNode))
#             elif (s.total_cost, s) in frontierSet:
#                 print("here")
#                 costOfState = heuristics.manhattanHeuristic(state.board)
#                 if costOfState < frontierSet[state].total_cost(): #review
#                     newCost = costOfState + 1
#                     neighborNode = Parent(state=state, parent=currentState.state, cost=newCost, heuristic=heuristics.manhattanHeuristic(state.board))
#                     heap.heappush(frontier, (neighborNode.total_cost(), neighborNode))
#                     frontierSet.add((neighborNode.total_cost(), neighborNode))

#     return [], 0, initialState, 1



def aStarSearch(initialState):
    frontier = []  # Priority queue (min-heap)
    frontierSet = set()  # Set to check if a state is in the frontier
    explore = set()
    parentM = {}
    parentM[initialState] = (initialState, heuristics.manhattanHeuristic(initialState.board))
    actions = list()
    # Add depth tracking
    depth = {initialState: 0}
    
    heap.heappush(frontier, (heuristics.manhattanHeuristic(initialState.board), 0, initialState))
    frontierSet.add((heuristics.manhattanHeuristic(initialState.board), 0, initialState))
    
    while frontier:
        cost, currentDepth, currentState = heap.heappop(frontier)
        frontierSet.remove((cost, currentDepth, currentState))
        
        if currentState.isGoal():
            print("FINAL PATH", currentState.board)
            board = currentState
            actions.append(board)
            while board in parentM.keys():
                parent_state, _ = parentM[board]
                del parentM[board]
                actions.append(parent_state)
                board = parent_state
            actions.reverse()  
            for action in actions:
                print("Actions:", action)
            print("Cost:", cost)
            print("Explore:", explore)
            print("Depth:", depth[currentState])
            return actions, cost, explore, depth[currentState]
        
        explore.add(currentState.board)

        for state in currentState.nextStates():
            newDepth = currentDepth + 1
            newCost = newDepth + heuristics.manhattanHeuristic(state.board)
            
            if (newCost, newDepth, state) not in frontierSet and state.board not in explore:
                heap.heappush(frontier, (newCost, newDepth, state))
                frontierSet.add((newCost, newDepth, state))
                parentM[state] = (currentState, newCost)
                depth[state] = newDepth
            elif (any, newDepth, state) in frontierSet:
                print("here")
                if newCost < frontierSet[state][0]:
                    heap.heappush(frontier, (newCost, newDepth, state))
                    frontierSet.add((newCost, newDepth, state))
                    parentM[state] = (currentState, newCost)
                    depth[state] = newDepth

    return [], 1000000, explore, 0

    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch