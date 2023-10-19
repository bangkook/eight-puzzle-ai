import heapq as heap
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

        #print(curState)
        depth = max(depth, curDepth)

        if curState.isGoal():
            board = curState.board
            actions.append(board)
            while board in pathTo.keys():
                board, _ = pathTo[board]
                actions.append(board)
            return actions[::-1], len(actions), expanded, depth


       
        for neighbor in curState.nextStates():
            state, direction = neighbor
            if state.board not in vis.keys():
                frontier.insert(0, (state, 1 + curDepth))
                vis[state.board] = True
                pathTo[state.board] = (curState.board, direction)

    return [], len(actions), expanded, depth


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

def ConstructPath(State):
    path = []
    while State:
        State.insert(0, (State.state, State.action))
        State = State.parent
    return path

def manhattan_distance(state):
    # Calculate Manhattan distance heuristic
    distance = 0
    for i in range(9):
        tile = int(state[i])
        goal_i, goal_j = tile // 3,tile % 3
        current_i, current_j = i // 3, i % 3
        distance = distance + abs(current_i - goal_i) + abs(current_j - goal_j)
    return distance


def aStarSearch(initialState):

    
    frontier = []
    explore = set()
    initial_node = Parent(state=initialState, parent=initialState, cost=0, heuristic=manhattan_distance(initialState.board))
    heap.heappush(frontier, (initial_node.total_cost(), initial_node)) #push in frontier: which heuristic method, cost, initial state and the path 

    while frontier:
        print("NODE: ")
        for node in heap.nsmallest(len(frontier), frontier):
            parent = node[1]  # The second element of the tuple contains the Parent object
            print(parent.state)

        _,currentState = heap.heappop(frontier)
        if(currentState.state.isGoal()):
             return ConstructPath(currentState)
        
        explore.add(currentState.state)

        for neighbor in currentState.state.nextStates():
            state, direction = neighbor
            if state not in frontier and neighbor not in explore:
                newCost = currentState.cost + 1
                neighborNode = Parent(state=state, parent=currentState.state, cost=newCost, heuristic=manhattan_distance(state.board))
                heap.heappush(frontier, (neighborNode.total_cost(), neighborNode))
                
            elif neighbor in frontier:
                if neighbor.cost < frontier[neighbor].cost: #review
                    newCost = neighbor.cost
                    neighborNode = Parent(state=state, parent=currentState.state, cost=newCost, heuristic=manhattan_distance(state.board))
                    heap.heappush(frontier, (neighborNode.total_cost(), neighborNode))     

    return [], 0, initialState, 1
        

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch