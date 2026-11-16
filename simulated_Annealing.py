def count_conflicts(positions):
    """
    Positions is a list where index represents the row, 
    and the value represents the column position of the queen in that row.
    """
    n = len(positions)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Check same column
            if positions[i] == positions[j]:
                conflicts += 1
            # Check diagonals
            elif abs(positions[i] - positions[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def print_board(positions):
    n = len(positions)
    for row in range(n):
        line = ""
        for col in range(n):
            if positions[row] == col:
                line += " Q "
            else:
                line += " . "
        print(line)

def solve_n_queens(n):
    # Simple backtracking solver to find a 0-conflict configuration
    solutions = []
    def backtrack(row, current_path):
        if row == n:
            solutions.append(current_path.copy())
            return True
        for col in range(n):
            # Check if placing a queen at (row, col) is valid
            safe = True
            for r, c in enumerate(current_path):
                if c == col or abs(c - col) == abs(r - row):
                    safe = False
                    break
            if safe:
                current_path.append(col)
                if backtrack(row + 1, current_path):
                    return True
                current_path.pop()
        return False
    
    backtrack(0, [])
    return solutions[0] if solutions else None

# 1. Get Board Size
try:
    n = int(input("Enter the number of queens (N): "))
    
    # 2. Ask user for column positions row by row
    print(f"\nEnter column indexes (0 to {n-1}) for each row:")
    user_positions = []
    for i in range(n):
        col = int(input(f"Row {i} queen column: "))
        user_positions.append(col)
    
    # 3. Print user board and conflicts
    print("\n--- Your Board ---")
    print_board(user_positions)
    conflicts = count_conflicts(user_positions)
    print(f"\nNumber of conflicts: {conflicts}")
    
    # 4. Show a 0-conflict diagram if possible
    if conflicts > 0:
        print("\nSearching for a 0-conflict solution...")
        solution = solve_n_queens(n)
        if solution:
            print(f"\n--- 0-Conflict Solution Diagram for {n}-Queens ---")
            print_board(solution)
            print(f"Solution positions: {solution}")
        else:
            print(f"No solution exists for {n}-Queens.")
except ValueError:
    print("Please enter valid integers.")