import heapq as heap
import sys
sys.path.append('../')

"""
    Each search function:
    1- takes state as input.
    2- Performs the search.
    3- Returns the path to goal (list of actions), expanded nodes, and depth of the search.
"""

def breadthFirstSearch(initial_state):
    explored = set()
    frontier = []
    frontier.insert(0, (initial_state, 0)) # (state, depth)
    explored.add(initial_state.board)
    actions = list()
    parent = dict()
    expanded = []
    max_search_depth = 0

    while len(frontier) > 0:
        cur_state, cur_depth = frontier.pop()
        
        expanded.append(cur_state.board)

        if cur_state.isGoal():
            return parent, cur_depth, expanded, max_search_depth

        for state, action in cur_state.nextStates():
            if state.board not in explored:
                frontier.insert(0, (state, 1 + cur_depth))
                explored.add(state.board)
                parent[state.board] = (cur_state.board, action)
                max_search_depth = max(max_search_depth, 1 + cur_depth)

    return [], 100000000, expanded, max_search_depth


def depthFirstSearch(initial_state):
    forntier = []
    explored = []
    forntier.append((initial_state, 0))
    parent_map = {}
    expntier = set()
    expntier.add(initial_state.board)
    max_search_depth = 0

    while forntier:
        curr, depth = forntier.pop()

        explored.append(curr.board)

        if curr.isGoal():
            return parent_map, depth, explored, max_search_depth

        for neighbor, action in reversed(curr.nextStates()):
            if neighbor.board not in expntier:
                expntier.add(neighbor.board)
                forntier.append((neighbor, depth + 1))
                parent_map[neighbor.board] = (curr.board, action)
                max_search_depth = max(max_search_depth, depth + 1)

    return [], 100000000, explored, max_search_depth



def aStarSearch(initial_state, heuristic):
    frontier = []  # Priority queue (min-heap)
    frontier_set = set()  # Set to check if a state is in the frontier
    explore = set()
    parentM = dict()
    actions = list()
    max_search_depth = 0

    heap.heappush(frontier, (heuristic(initial_state.board), 0, initial_state))
    frontier_set.add(initial_state.board)

    while frontier:
        cost, current_depth, current_state = heap.heappop(frontier)
        frontier_set.remove(current_state.board)

        max_search_depth = max(max_search_depth, current_depth)

        explore.add(current_state.board)

        if current_state.isGoal():
            return parentM, current_depth, explore, max_search_depth

        #print(currentState)
        for state, action in current_state.nextStates():
            new_depth = current_depth + 1
            new_cost = new_depth + heuristic(state.board)

            if state.board not in frontier_set and state.board not in explore:
                heap.heappush(frontier, (new_cost, new_depth, state))
                frontier_set.add(state.board)
                parentM[state.board] = (current_state.board, action)  # Store the parent state directly
                max_search_depth = max(max_search_depth, new_depth)
            elif state.board in frontier_set:
                depth = decreaseKey(frontier, state, new_depth, new_cost, parentM, current_state.board, action)
                max_search_depth = max(max_search_depth, new_depth)

    return [], 1000000, explore, max_search_depth


def decreaseKey(frontier, state, depth, cost, parentMap, parent, action):
    for i, (c, d, s) in enumerate(frontier):
        if s.board != state.board:
            continue
        if c <= cost :
            return d
        frontier[i] = (cost, depth, state)
        parentMap[state.board] = (parent, action)
        heap.heapify(frontier)
        return depth
        