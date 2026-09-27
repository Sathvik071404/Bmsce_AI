import copy

class PuzzleState:
    def __init__(self, board, parent=None, move="", depth=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        
    def __eq__(self, other):
        return self.board == other.board if other else False

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))

    def find_blank(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    return r, c

    def get_neighbors(self):
        neighbors = []
        r, c = self.find_blank()
        moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
        
        for dr, dc, move_name in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_board = copy.deepcopy(self.board)
                new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
                neighbors.append(PuzzleState(new_board, self, move_name, self.depth + 1))
        return neighbors

    def print_path(self):
        path = []
        current = self
        while current:
            path.append(current)
            current = current.parent
        path.reverse()
        
        print(f"Total Moves: {len(path) - 1}")
        for idx, state in enumerate(path):
            if idx > 0:
                print(f"--- Move {idx}: {state.move} ---")
            else:
                print("--- Initial State ---")
            for row in state.board:
                print(row)
        print("---------------------\n")


def depth_limited_search(state, goal_board, limit, visited):
    """Recursive helper function for Depth-Limited Search."""
    if state.board == goal_board:
        return state
        
    if state.depth >= limit:
        return None
        
    visited.add(state)
    
    for neighbor in state.get_neighbors():
        if neighbor not in visited:
            # Create a path-specific copy for accurate backtracking exploration
            local_visited = visited.copy()
            result = depth_limited_search(neighbor, goal_board, limit, local_visited)
            if result:
                return result
    return None


def ids(start_board, goal_board):
    """Solves the 8-puzzle by incrementally deepening the search depth constraint."""
    start_state = PuzzleState(start_board)
    depth = 0
    
    while True:
        visited = set()
        result = depth_limited_search(start_state, goal_board, depth, visited)
        if result:
            return result
        depth += 1


# Execute IDS
if __name__ == "__main__":
    initial = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    print("--- Running Iterative Deepening Search (IDS) ---")
    solution = ids(initial, goal)
    if solution:
        solution.print_path()
    else:
        print("No solution found.")
