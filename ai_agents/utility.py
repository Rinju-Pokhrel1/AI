import random

world = {
    (0, 0): ["safe"],
    (0, 1): ["breeze"],
    (0, 2): ["pit"],
    (1, 0): ["stench"],
    (1, 1): [],
    (1, 2): ["gold"]
}

UTILITY_TABLE = {
    "safe": 10,
    "breeze": -20,
    "stench": -50,
    "gold": 1000,
    "pit": -1000,
}

def get_percepts(pos):
    return world.get(pos, [])

def utility_based_agent(pos):
    percepts = get_percepts(pos)
    
    current_utility = sum(UTILITY_TABLE.get(p, 0) for p in percepts)
    print(f"Current state utility at {pos}: {current_utility}")

    if "gold" in percepts:
        print("Percept: Gold! Action: Grab Gold!")
        return "Grab gold!"

    if "safe" in percepts or len(percepts) == 0:
        print("Percept: Safe. Action: Explore a new cell.")
        return "Explore a new cell"

    if "pit" in percepts or "stench" in percepts:
        print("Percept: Pit or Stench. Action: Flee! (Highest utility action to avoid large penalty)")
        return "Flee!"
        
    return "Stall"

print("--- Simulating the Utility-Based Agent ---")
position_to_test = (1, 2)
action_taken = utility_based_agent(position_to_test)
print(f"At position {position_to_test}, the agent's action is: {action_taken}")

print("\n--- Testing a new position ---")
position_to_test_2 = (0, 1)
action_taken_2 = utility_based_agent(position_to_test_2)
print(f"At position {position_to_test_2}, the agent's action is: {action_taken_2}")

print("\n--- Testing a dangerous position ---")
position_to_test_3 = (0, 2)
action_taken_3 = utility_based_agent(position_to_test_3)
print(f"At position {position_to_test_3}, the agent's action is: {action_taken_3}")
