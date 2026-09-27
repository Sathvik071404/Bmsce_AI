import copy

class PuzzleState:
    def __init__(self, board, parent=None, move="", depth=0):
        self.board = board       # 3x3 list
        self.parent = parent     # Pointer to parent state
        self.move = move         # Move that led here ("Up", "Down", etc.)
        self.depth = depth       # Current depth level
        
    def __eq__(self, other):
        return self.board == other.board if other else False

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))

    def find_blank(self):
        """Locates the 0 tile."""
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    return r, c

    def get_neighbors(self):
        """Generates all legal adjacent states."""
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
        """Prints the path from initial state to goal."""
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


def dfs(start_board, goal_board, max_depth=30):
    """Solves the 8-puzzle using a depth-limited DFS approach to prevent stack overflows."""
    start_state = PuzzleState(start_board)
    goal_state = PuzzleState(goal_board)
    
    stack = [start_state]
    visited = set()
    
    while stack:
        current = stack.pop()
        
        if current.board == goal_state.board:
            return current
            
        if current not in visited and current.depth < max_depth:
            visited.add(current)
            for neighbor in current.get_neighbors():
                if neighbor not in visited:
                    stack.append(neighbor)
    return None


# Execute DFS
if __name__ == "__main__":
    initial = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    print("--- Running Depth-First Search (DFS) ---")
    solution = dfs(initial, goal)
    if solution:
        solution.print_path()
    else:
        print("No solution found within depth limit.")
