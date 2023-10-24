import unittest
from eightpuzzle import *

puzzles = [[ 1,2,5,3,4,0,6,7,8], [1,4,2,6,5,8,7,3,0], [1,0,2,7,5,4,8,6,3], [8, 0, 6, 5, 4, 7, 2, 3, 1]]

# abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch

class TestEightPuzzle(unittest.TestCase):
    TRIALS = 5

    # Test solvability
    def test_solvable_puzzle(self):
        self.assertEqual(solvable(puzzles[3]), True)
    
    def test_unSolvable_puzzle(self):
        unsolvable_puzzle = [1, 2, 4, 5, 7, 3, 8, 6, 0]
        self.assertEqual(solvable(unsolvable_puzzle), False)

    # Test every algorithm with puzzle 1 (close to goal)

    def test_bfs_puzzle1(self):
        state = EightPuzzleState(puzzles[0])
        
        agent = EightPuzzleAgent(state, bfs)
        path, actions = agent.getPath()
        cost = agent.getCost()
        expanded_nodes = len(agent.getExpandedNodes())
        depth = agent.getDepth()
        total_time = agent.getTime()

        self.assertEqual(cost, 3)
        self.assertEqual(expanded_nodes, 16)
        self.assertEqual(depth, 4)
        self.assertEqual(actions, ['up', 'left', 'left'])
        

    def test_dfs_puzzle1(self):
        state = EightPuzzleState(puzzles[0])
        
        agent = EightPuzzleAgent(state, dfs)
        path, actions = agent.getPath()
        cost = agent.getCost()
        expanded_nodes = len(agent.getExpandedNodes())
        depth = agent.getDepth()
        total_time = agent.getTime()

        self.assertEqual(cost, 27)
        self.assertEqual(expanded_nodes, 28)
        self.assertEqual(depth, 27)
        self.assertEqual(actions, ['left', 'left', 'up', 'right', 'right', 'down', 
        'left', 'left', 'up', 'right', 'right', 'down', 'left', 'left', 'up', 
        'right', 'right', 'down', 'left', 'left', 'up', 'right', 'right', 'down', 
        'left', 'left', 'up'])

    def test_astar_man_puzzle1(self):
        state = EightPuzzleState(puzzles[0])

        agent = EightPuzzleAgent(state, astar, heuristic=manhattanHeuristic)
        path, actions = agent.getPath()
        cost = agent.getCost()
        expanded_nodes = len(agent.getExpandedNodes())
        depth = agent.getDepth()
        total_time = agent.getTime()

        self.assertEqual(cost, 3)
        self.assertEqual(expanded_nodes, 4)
        self.assertEqual(depth, 3)
        self.assertEqual(actions, ['up', 'left', 'left'])


    def test_astar_euc_puzzle1(self):
        state = EightPuzzleState(puzzles[0])
        
        agent = EightPuzzleAgent(state, astar, heuristic=euclideanHeuristic)
        path, actions = agent.getPath()
        cost = agent.getCost()
        expanded_nodes = len(agent.getExpandedNodes())
        depth = agent.getDepth()
        total_time = agent.getTime()

        self.assertEqual(cost, 3)
        self.assertEqual(expanded_nodes, 4)
        self.assertEqual(depth, 3)
        self.assertEqual(actions, ['up', 'left', 'left'])

    ### A state optimal for dfs (less expanded nodes than bfs)
    # The goal is the leftmost node
    def test_dfs_puzzle_optimal(self):
        puzzle = [3, 1, 2, 4, 5, 0, 6, 7, 8]
        state = EightPuzzleState(puzzle)

        agent = EightPuzzleAgent(state, dfs)
        path, actions = agent.getPath()
        cost = agent.getCost()
        expanded_nodes = len(agent.getExpandedNodes())
        depth = agent.getDepth()
        total_time = agent.getTime()

        self.assertEqual(cost, 3)
        self.assertEqual(expanded_nodes, 4)
        self.assertEqual(depth, 3)
        self.assertEqual(actions, ['left', 'left', 'up'])        

    def test_bfs_puzzle2(self):
        state = EightPuzzleState(puzzles[1])

        agent = EightPuzzleAgent(state, bfs)
        path, actions = agent.getPath()
        cost = agent.getCost()
        expanded_nodes = len(agent.getExpandedNodes())
        depth = agent.getDepth()
        total_time = agent.getTime()

        self.assertEqual(cost, 8)
        self.assertEqual(expanded_nodes, 244)
        self.assertEqual(depth, 9)
        self.assertEqual(actions, ['up', 'left', 'down', 'left', 'up', 'right', 'up', 'left'])

    def test_astar_man_puzzle2(self):
        state = EightPuzzleState(puzzles[1])
        
        agent = EightPuzzleAgent(state, astar, heuristic=manhattanHeuristic)
        path, actions = agent.getPath()
        cost = agent.getCost()
        expanded_nodes = len(agent.getExpandedNodes())
        depth = agent.getDepth()
        total_time = agent.getTime()

        self.assertEqual(cost, 8)
        self.assertEqual(expanded_nodes, 13)
        self.assertEqual(depth, 8)
        self.assertEqual(actions, ['up', 'left', 'down', 'left', 'up', 'right', 'up', 'left'])

        
    def test_astar_euc_puzzle2(self):
        state = EightPuzzleState(puzzles[1])
        
        agent = EightPuzzleAgent(state, astar, heuristic=euclideanHeuristic)
        path, actions = agent.getPath()
        cost = agent.getCost()
        expanded_nodes = len(agent.getExpandedNodes())
        depth = agent.getDepth()
        total_time = agent.getTime()

        self.assertEqual(cost, 8)
        self.assertEqual(expanded_nodes, 13)
        self.assertEqual(depth, 8)
        self.assertEqual(actions, ['up', 'left', 'down', 'left', 'up', 'right', 'up', 'left'])


    # Test with a puzzle where the cost of some unexplored
    # nodes in the frontier is upated with less cost

    def test_bfs_puzzle3(self):
        state = EightPuzzleState(puzzles[2])
        total_time = 0
        cost = depth = expanded_nodes = 0
        path, actions = None, None
        
        agent = EightPuzzleAgent(state, bfs)
        path, actions = agent.getPath()
        cost = agent.getCost()
        expanded_nodes = len(agent.getExpandedNodes())
        depth = agent.getDepth()
        total_time += agent.getTime()

        self.assertEqual(cost, 23)
        self.assertEqual(depth, 24)
        self.assertEqual(actions, ['right', 'down', 'left', 'down', 'right', 'up', 
        'left', 'down', 'left', 'up', 'right', 'right', 'up', 'left', 'left', 'down', 
        'right', 'right', 'down', 'left', 'left', 'up', 'up'])

    def test_astar_man_puzzle3(self):
        state = EightPuzzleState(puzzles[2])
        
        agent = EightPuzzleAgent(state, astar, manhattanHeuristic)
        path, actions = agent.getPath()
        cost = agent.getCost()
        expanded_nodes = len(agent.getExpandedNodes())
        depth = agent.getDepth()
        total_time = agent.getTime()

        self.assertEqual(cost, 23)
        self.assertEqual(depth, 23)
        self.assertEqual(actions, ['right', 'down', 'left', 'down', 'right', 'up', 
        'up', 'left', 'down', 'down', 'left', 'up', 'right', 'up', 'left', 'down', 
        'right', 'right', 'down', 'left', 'left', 'up', 'up'])

    def test_astar_euc_puzzle3(self):
        state = EightPuzzleState(puzzles[2])
        
        agent = EightPuzzleAgent(state, astar, euclideanHeuristic)
        path, actions = agent.getPath()
        cost = agent.getCost()
        expanded_nodes = len(agent.getExpandedNodes())
        depth = agent.getDepth()
        total_time = agent.getTime()

        self.assertEqual(cost, 23)
        self.assertEqual(depth, 23)
        self.assertEqual(actions, ['right', 'down', 'left', 'down', 'right', 'up', 
        'up', 'left', 'down', 'down', 'left', 'up', 'right', 'up', 'left', 'down', 
        'right', 'right', 'down', 'left', 'left', 'up', 'up'])

if __name__ == '__main__':
    unittest.main()