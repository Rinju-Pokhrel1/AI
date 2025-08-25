from collections import deque
import sys

class EightPuzzleProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.cost = 1

    def actions(self, state):
        possible_actions = ["up", "down", "left", "right"]
        blank_index = state.index(0)

        if blank_index % 3 == 0:
            possible_actions.remove("left")
        if blank_index % 3 == 2:
            possible_actions.remove("right")
        if blank_index < 3:
            possible_actions.remove("up")
        if blank_index >= 6:
            possible_actions.remove("down")

        return possible_actions

    def result(self, state, action):
        new_state = list(state)
        blank_index = new_state.index(0)

        if action == "up":
            swap_index = blank_index - 3
        elif action == "down":
            swap_index = blank_index + 3
        elif action == "left":
            swap_index = blank_index - 1
        elif action == "right":
            swap_index = blank_index + 1

        new_state[blank_index], new_state[swap_index] = new_state[swap_index], new_state[blank_index]
        return tuple(new_state)

    def goal_test(self, state):
        return state == self.goal_state


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost

    def solution_path(self):
        path = []
        node = self
        while node:
            path.append(node.state)
            node = node.parent
        return list(reversed(path))


def dfs(problem):
    root = Node(problem.initial_state)
    if problem.goal_test(root.state):
        return root.solution_path()

    frontier = [root]  # stack for DFS
    explored = set()

    while frontier:
        node = frontier.pop()  # pop from stack
        explored.add(node.state)

        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)
            if child_state not in explored and all(n.state != child_state for n in frontier):
                child_node = Node(child_state, node, action, 1)
                if problem.goal_test(child_state):
                    return child_node.solution_path()
                frontier.append(child_node)

    return None


def read_state(prompt):
    raw_input = input(prompt).split()
    nums = []
    for x in raw_input:
        if x == "_":
            nums.append(0)
        else:
            try:
                nums.append(int(x))
            except ValueError:
                print("Invalid input. Enter numbers 0-8 or _ for blank.")
                sys.exit()
    if len(nums) != 9 or set(nums) != set(range(9)):
        print("Error: Enter exactly 9 unique numbers from 0 to 8 (use _ for blank).")
        sys.exit()
    return tuple(nums)


def is_solvable(state):
    nums = [n for n in state if n != 0]
    inversions = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                inversions += 1
    return inversions % 2 == 0


# MAIN PROGRAM
initial = read_state("Enter the initial state (9 numbers, use _ for blank): ")
goal = read_state("Enter the goal state (9 numbers, use _ for blank): ")

if not is_solvable(initial):
    print("The given initial state is NOT solvable.")
    sys.exit()

problem = EightPuzzleProblem(initial, goal)
solution = dfs(problem)

if solution:
    print("Solution found in", len(solution) - 1, "moves:")
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i], state[i+1], state[i+2])
        print()
else:
    print("No solution found.")
