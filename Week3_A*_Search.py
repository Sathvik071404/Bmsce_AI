import heapq


def heuristic(state, goal):

    distance = 0

    for i in range(9):

        if state[i] == 0:
            continue

        current_row = i // 3
        current_col = i % 3

        goal_index = goal.index(state[i])
        goal_row = goal_index // 3
        goal_col = goal_index % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):

    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col


            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors



def a_star(start, goal):

    priority_queue = []


    g = 0

    f = g + heuristic(start, goal)

    heapq.heappush(
        priority_queue,
        (f, g, start, [start])
    )

    visited = {}

    while priority_queue:

        f, g, state, path = heapq.heappop(priority_queue)

        if state == goal:
            return path

        if state in visited and visited[state] <= g:
            continue

        visited[state] = g


        for new_state in get_neighbors(state):

            new_g = g + 1


            h = heuristic(new_state, goal)

            new_f = new_g + h

            heapq.heappush(
                priority_queue,
                (
                    new_f,
                    new_g,
                    new_state,
                    path + [new_state]
                )
            )

    return None


start = (
    2, 8, 3,
    1, 6, 4,
    7, 0, 5
)


goal = (
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
)


solution = a_star(start, goal)


if solution:

    print("Solution Found!")
    print("Number of moves:", len(solution) - 1)
    print()

    for state in solution:

        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
        print()

else:

    print("No solution found.")
