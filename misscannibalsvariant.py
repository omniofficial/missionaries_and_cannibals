from search import *


class MissCannibalsVariant(Problem):
    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)

    def result(self, state, action):
        """Apply an action and return the resulting state."""
        m, c, boat_left = state
        m_count = action.count("M")
        c_count = action.count("C")

        if boat_left:  # move from left to right
            m -= m_count
            c -= c_count
        else:  # move from right to left
            m += m_count
            c += c_count

        return (m, c, not boat_left)

    def actions(self, state):
        """Return valid actions for the current state."""
        # All possible moves with boat capacity = 3
        possible_moves = ["M", "C", "MM", "CC", "MC", "MMM", "CCC", "MMC", "MCC"]
        valid_actions = []

        for move in possible_moves:
            new_state = self.result(state, move)
            if self.is_valid_state(new_state):
                if self.can_take(move, state):
                    valid_actions.append(move)

        return valid_actions

    def can_take(self, move, state):
        """Check if the move is possible given who's on the boat side."""
        m, c, boat_left = state
        m_count = move.count("M")
        c_count = move.count("C")

        if boat_left:  # taking from left
            return m_count <= m and c_count <= c
        else:  # taking from right
            return m_count <= (self.N1 - m) and c_count <= (self.N2 - c)

    def is_valid_state(self, state):
        """Check missionaries are never outnumbered unless none are present."""
        m_left, c_left, _ = state
        m_right = self.N1 - m_left
        c_right = self.N2 - c_left

        # Non negative counts
        if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
            return False

        # Missionaries safe on left
        if m_left > 0 and c_left > m_left:
            return False

        # Missionaries safe on right
        if m_right > 0 and c_right > m_right:
            return False

        return True


if __name__ == "__main__":
    mc = MissCannibalsVariant(4, 4)
    print(mc.actions((3, 3, True)))  # should return something like ['MC', 'MMM']

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)
