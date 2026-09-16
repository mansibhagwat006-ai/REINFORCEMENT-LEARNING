# Section B - Task 4: Simple RL Environment Simulator

class DeliveryEnvironment:
    def __init__(self):
        self.current_state = {
            "location": "Restaurant",
            "pending_orders": 3
        }
        self.total_reward = 0
        self.step_count = 0

    def step(self, action):
        self.step_count += 1

        if action == "deliver_order":
            if self.current_state["pending_orders"] > 0:
                self.current_state["pending_orders"] -= 1
                self.current_state["location"] = "Customer"
                reward = 10
            else:
                reward = -2

        elif action == "wait":
            reward = -1

        elif action == "navigate_to_zone":
            self.current_state["location"] = "Delivery Zone"
            reward = 2

        else:
            reward = -5

        self.total_reward += reward

        print(
            f"Step {self.step_count}: Action = {action} | "
            f"State = {self.current_state} | Reward = {reward:+d}"
        )
        return reward


env = DeliveryEnvironment()

episode_actions = [
    "navigate_to_zone",
    "deliver_order",
    "wait",
    "navigate_to_zone",
    "deliver_order",
    "deliver_order"
]

for action in episode_actions:
    env.step(action)

print("\nFinal Results")
print(f"Final state: {env.current_state}")
print(f"Total reward: {env.total_reward}")
print(f"Total steps: {env.step_count}")
