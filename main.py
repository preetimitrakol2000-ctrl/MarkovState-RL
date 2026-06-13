from environment import GridWorldMatrix
from agent import QLearningAgent
from policy_run import verify_transition

if __name__ == "__main__":
    print("🤖 Launching Adjacency Matrix MarkovState-RL Engine Environment...")

    world = GridWorldMatrix()
    smart_agent = QLearningAgent()

    # Simulation: Agent transitions from State 1 to State 2
    step_start = 1
    step_end = 2

    if verify_transition(world, step_start, step_end):
        immediate_reward = world.rewards[step_end]
        smart_agent.apply_bellman_update(step_start, step_end, immediate_reward)
        
        print(f"📥 Transition Step Validated: State [{step_start}] -> State [{step_end}]")
        print(f"   📊 Collected Reward Modifier: {immediate_reward}")
        print(f"🔮 Updated Agent Expected Utility Table: {smart_agent.q_table}")
    else:
        print("❌ Invalid Move Attempted via Matrix Constraints.")
