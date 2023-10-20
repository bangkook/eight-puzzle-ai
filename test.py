import heapq as heap
import sys
sys.path.append('../')
import heuristics
def aStarSearch(initialState):
    frontier = []  # Priority queue (min-heap)
    frontierSet = set()  # Set to check if a state is in the frontier
    explore = set()
    parentM = {}
    parentM[initialState] = (initialState,heuristics.manhattanHeuristic(initialState.board))
    heap.heappush(frontier, (heuristics.manhattanHeuristic(initialState.board), initialState))
    frontierSet.add((heuristics.manhattanHeuristic(initialState.board), initialState))
    
    while frontier:
        cost, currentState = heap.heappop(frontier)
        frontierSet.remove((cost, currentState))
        if currentState.isGoal():
            print("FINAL PATH", currentState.board)
            return [], 0, initialState, 1 
        explore.add(currentState.board)

        for state in currentState.nextStates():
            if (cost + heuristics.manhattanHeuristic(state.board), state) not in frontierSet and state.board not in explore:
                newCost = cost + 1 + heuristics.manhattanHeuristic(state.board)
                heap.heappush(frontier, (newCost , state))
                frontierSet.add((newCost , state))
                parentM[state] = (currentState,newCost)
    return [], 0, initialState, 1
