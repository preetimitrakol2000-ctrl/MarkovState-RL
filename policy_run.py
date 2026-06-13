def verify_transition(env, current, target):
    return env.adjacency_matrix[current][target] == 1
