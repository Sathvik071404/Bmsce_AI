class SimpleReflexVacuumAgent:
    def __init__(self):
        pass

    def perceive_and_act(self, location, status):
        """
        Decision-making based strictly on the current state.
        location: 'A' or 'B'
        status: 'Dirty' or 'Clean'
        """
        print(f"[Reflex Agent] Percept - Location: {location}, Status: {status}")
        
        # Rule 1: If the current location is dirty, suck the dirt.
        if status == 'Dirty':
            return 'Suck'
        # Rule 2: If in location A and it is clean, move right to B.
        elif location == 'A':
            return 'Right'
        # Rule 3: If in location B and it is clean, move left to A.
        elif location == 'B':
            return 'Left'

# --- Simulation ---
environment = {
    'A': 'Dirty',
    'B': 'Dirty'
}

agent = SimpleReflexVacuumAgent()
current_location = 'A'

print("--- Starting Simple Reflex Agent Simulation ---")
for step in range(4):
    status = environment[current_location]
    action = agent.perceive_and_act(current_location, status)
    print(f"Action Taken: {action}")
    
    if action == 'Suck':
        environment[current_location] = 'Clean'
    elif action == 'Right':
        current_location = 'B'
    elif action == 'Left':
        current_location = 'A'
    print(f"Environment State: {environment}\n")
