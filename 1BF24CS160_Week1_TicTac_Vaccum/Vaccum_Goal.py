class GoalBasedVacuumAgent:
    def __init__(self, all_locations):
        # Goal: All rooms in this list must register as 'Clean'
        self.goal_state = {loc: 'Clean' for loc in all_locations}
        
        # Internal Model / Memory of the world
        self.model = {loc: 'Unknown' for loc in all_locations}

    def perceive_and_act(self, location, status):
        # 1. Update internal model based on current percept
        self.model[location] = status
        print(f"[Goal Agent] Model updated: {self.model}")

        # 2. Check if the goal is already achieved
        if self.model == self.goal_state:
            return 'Stop (Goal Achieved)'

        # 3. Choose action that moves closer to the goal
        if status == 'Dirty':
            return 'Suck'
        
        # If current location is clean but the goal isn't met, find the dirty room
        for loc, state in self.model.items():
            if state == 'Dirty' or state == 'Unknown':
                if loc == 'B' and location == 'A':
                    return 'Right'
                elif loc == 'A' and location == 'B':
                    return 'Left'
                
        return 'Explore'

# --- Simulation ---
environment = {
    'A': 'Dirty',
    'B': 'Dirty'
}

agent = GoalBasedVacuumAgent(all_locations=['A', 'B'])
current_location = 'A'

print("--- Starting Goal-Based Agent Simulation ---")
while True:
    status = environment[current_location]
    action = agent.perceive_and_act(current_location, status)
    print(f"Action Taken: {action}")
    
    if action == 'Stop (Goal Achieved)':
        print("Agent shut down safely.")
        break
    elif action == 'Suck':
        environment[current_location] = 'Clean'
    elif action == 'Right':
        current_location = 'B'
    elif action == 'Left':
        current_location = 'A'
    print(f"Environment State: {environment}\n")
