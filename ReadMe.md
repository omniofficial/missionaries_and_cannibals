## Project Instructions:

Write a Python class, MissCannibalsVariant, that defines the variant of the Missionaries & Cannibals puzzle with boat capacity = 3 (same problem from HW #1). The puzzle can be set with an arbitrary number of Missionaries and Cannibals on the left bank. Your code should be usable by a search algorithm to solve the puzzle.
The class has two instance variables, self.N1 and self.N2, which stores the total number of missionaries and the total number of cannibals starting from the left bank. These values will be set in the main function so that your class can be used to solve puzzles with different numbers of missionaries and cannibals. E.g., 3 missionaries and 2 cannibals.
Represent the state by a 3-tuple, two integers and a boolean: (m, c, onLeft), which represents the number of missionaries on the left bank (note: the number of missionaries on the right bank is then self.N1-m), the number of cannibals on the left side, and if the boat is on the left respectively.
Represent actions using strings: 'M', 'C', 'MM', 'MC', 'CC', 'MMC', … It is not necessary to represent the direction of the boat as this will be clear from the state (e.g., if the boat is on the left, then the boat will cross to the right).

## Hints:

The class must be a subclass of class Problem in the search.py code.
The class will be similar to class EightPuzzle (in structure only, the implementation will be VERY different) in search.py. Specifically, your class should have a
constructor (already completed)
method goal_test(state) (default in the Problem superclass is sufficient)
method result(state, action) that returns the new state reached from the given state and action
method actions(state) that returns a list of valid actions in the given state
I recommended implementing the methods in the order above and to test each method individually.
As the action is a string, the number of missionaries/cannibals crossing over can be calculated by just counting a 'M' or 'C'. E.g., action.count('MC').
