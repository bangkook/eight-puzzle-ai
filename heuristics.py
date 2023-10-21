def manhattanHeuristic(state):
    distance = 0
    for i in range(9):
        tile = int(state[i])
        goal_i, goal_j = tile // 3,tile % 3
        current_i, current_j = i // 3, i % 3
        distance = distance + abs(current_i - goal_i) + abs(current_j - goal_j)
    return distance


def euclideanHeuristic(state):
    distance = 0
    for i in range(9):
        tile = int(state[i])
        goal_i, goal_j = tile // 3,tile % 3
        current_i, current_j = i // 3, i % 3
        distance = distance + ((current_i - goal_i) ** 2 + (current_j - goal_j) ** 2) ** 0.5
    return distance

