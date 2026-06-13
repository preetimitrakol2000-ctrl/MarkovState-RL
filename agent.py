class QLearningAgent:
    def __init__(self, states_count=4):
        self.q_table = [0.0] * states_count  # Flat value map representation
        self.learning_rate = 0.5
        self.discount_factor = 0.9

    def apply_bellman_update(self, current_state, next_state, reward):
        """Applies an explicit Bellman optimality equation shortcut."""
        old_value = self.q_table[current_state]
        future_optimal = self.q_table[next_state]
        
        # Temporal difference tracking calculation
        self.q_table[current_state] = old_value + self.learning_rate * (reward + self.discount_factor * future_optimal - old_value)
