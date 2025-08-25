import random

world = {
    (0, 0): ["safe"], 
    (0, 1): ["breeze"], 
    (0, 2): ["pit"], 
    (1, 0): ["stench"], 
    (1, 1): [], 
    (1, 2): ["gold"]
}

def get_percepts(pos):
    return world.get(pos, [])

def simple_reflex_agent(pos):
    percepts = get_percepts(pos)

    if "gold" in percepts:
        print("Percept: Gold. Action: Grab gold!")
        return "Grab gold!"

    elif "pit" in percepts or "stench" in percepts:
        print("Percept: Pit or Stench. Action: Flee!")
        return "Flee!"

    else:
        print("Percept: Nothing of note. Action: Move randomly.")
        return "Move randomly"

print("--- Simulating the Simple Reflex Agent ---")
position_to_test = (1, 2)
action_taken = simple_reflex_agent(position_to_test)
print(f"At position {position_to_test}, the agent's action is: {action_taken}")

print("\n--- Testing a new position ---")
position_to_test_2 = (0, 1)
action_taken_2 = simple_reflex_agent(position_to_test_2)
print(f"At position {position_to_test_2}, the agent's action is: {action_taken_2}")
