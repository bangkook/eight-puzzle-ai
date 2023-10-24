from eightpuzzle import *

puzzles = [[ 1,2,5,3,4,0,6,7,8], [1,4,2,6,5,8,7,3,0], [1,0,2,7,5,4,8,6,3], [8,0,6,5,4,7,2,3,1]]

# abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch

functions = [bfs, dfs, astar]
heuristics = [manhattanHeuristic, euclideanHeuristic]

TRIALS = 5

def run_puzzle1():
    state = EightPuzzleState(puzzles[0])
    for fn in functions:
        for h in heuristics:
            print('---------------------------------------------------')
            total_time = 0
            cost = depth = expanded_nodes = 0
            path, actions = None, None
            for i in range(TRIALS):
                agent = EightPuzzleAgent(state, fn, h)
                path, actions = agent.getPath()
                cost = agent.getCost()
                expanded_nodes = len(agent.getExpandedNodes())
                depth = agent.getDepth()
                total_time += agent.getTime()
            
            print(fn.__name__)
            if len(actions) < 30:
                print("path", actions)
            print('Expanded Nodes = ', expanded_nodes)
            print('Cost/Depth = ', cost)
            print('Max Search Depth = ', depth)
            print('Total Time = ', total_time / TRIALS)

            if fn.__name__ != 'aStarSearch':
                break

            print(h.__name__)

def run_puzzle2():
    state = EightPuzzleState(puzzles[1])
    for fn in functions:
        for h in heuristics:
            print('---------------------------------------------------')
            total_time = 0
            cost = depth = expanded_nodes = 0
            path, actions = None, None
            for i in range(TRIALS):
                agent = EightPuzzleAgent(state, fn, h)
                path, actions = agent.getPath()
                cost = agent.getCost()
                expanded_nodes = len(agent.getExpandedNodes())
                depth = agent.getDepth()
                total_time += agent.getTime()
            
            print(fn.__name__)
            if len(actions) < 30:
                print("path", actions)
            print('Expanded Nodes = ', expanded_nodes)
            print('Cost/Depth = ', cost)
            print('Max Search Depth = ', depth)
            print('Total Time = ', total_time / TRIALS)

            if fn.__name__ != 'aStarSearch':
                break

            print(h.__name__)


def run_puzzle3():
    state = EightPuzzleState(puzzles[2])
    for fn in functions:
        for h in heuristics:
            print('---------------------------------------------------')
            total_time = 0
            cost = depth = expanded_nodes = 0
            path, actions = None, None
            for i in range(TRIALS):
                agent = EightPuzzleAgent(state, fn, h)
                path, actions = agent.getPath()
                cost = agent.getCost()
                expanded_nodes = len(agent.getExpandedNodes())
                depth = agent.getDepth()
                total_time += agent.getTime()
            
            print(fn.__name__)
            if len(actions) < 30:
                print("path", actions)
            print('Expanded Nodes = ', expanded_nodes)
            print('Cost/Depth = ', cost)
            print('Max Search Depth = ', depth)
            print('Total Time = ', total_time / TRIALS)

            if fn.__name__ != 'aStarSearch':
                break

            print(h.__name__)

def run_puzzle4():
    state = EightPuzzleState(puzzles[3])
    for fn in functions:
        for h in heuristics:
            print('---------------------------------------------------')
            total_time = 0
            cost = depth = expanded_nodes = 0
            path, actions = None, None
            for i in range(TRIALS):
                agent = EightPuzzleAgent(state, fn, h)
                path, actions = agent.getPath()
                cost = agent.getCost()
                expanded_nodes = len(agent.getExpandedNodes())
                depth = agent.getDepth()
                total_time += agent.getTime()
            
            print(fn.__name__)
            if len(actions) < 30:
                print("path", actions)
            print('Expanded Nodes = ', expanded_nodes)
            print('Cost/Depth = ', cost)
            print('Max Search Depth = ', depth)
            print('Total Time = ', total_time / TRIALS)

            if fn.__name__ != 'aStarSearch':
                break

            print(h.__name__)


if __name__ == '__main__':
    run_puzzle1()

    print('===========================================================')

    run_puzzle2()

    print('===========================================================')

    run_puzzle3()

    print('===========================================================')
    
    run_puzzle4()

    print('===========================================================')


    