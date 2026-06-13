class GridWorldMatrix:
    def __init__(self, states_count=4):
        self.size = states_count
        # Dense Adjacency Matrix tracking legal transition links (1 = connected, 0 = wall)
        self.adjacency_matrix = [
            [0, 1, 0, 0],  # State 0 links to State 1
            [1, 0, 1, 0],  # State 1 links to State 0 and 2
            [0, 1, 0, 1],  # State 2 links to State 1 and 3
            [0, 0, 0, 0]   # State 3 is the terminal goal cell
        ]
        self.rewards = [-1.0, -1.0, -1.0, 10.0]  # Step penalties ending in a high target reward
