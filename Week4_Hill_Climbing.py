import random


def heuristic(state):

    conflicts = 0

    for i in range(4):
        for j in range(i + 1, 4):

            if state[i] == state[j]:
                conflicts += 1

            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def get_neighbors(state):

    neighbors = []

    for row in range(4):

        for col in range(4):

            if col != state[row]:

                new_state = state.copy()
                new_state[row] = col

                neighbors.append(new_state)

    return neighbors


def hill_climbing():

    while True:

        current = [
            random.randint(0, 3),
            random.randint(0, 3),
            random.randint(0, 3),
            random.randint(0, 3)
        ]

        while True:

            current_h = heuristic(current)

            if current_h == 0:
                return current

            neighbors = get_neighbors(current)

            best = current
            best_h = current_h

            for neighbor in neighbors:

                h = heuristic(neighbor)

                if h < best_h:
                    best = neighbor
                    best_h = h

            if best_h >= current_h:
                break

            current = best

def print_board(state):

    for row in range(4):

        for col in range(4):

            if state[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

solution = hill_climbing()

print("Solution:", solution)
print("Heuristic:", heuristic(solution))
print()

print_board(solution)
