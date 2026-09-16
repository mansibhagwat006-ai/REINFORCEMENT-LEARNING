# Section C - Mini Capstone: Food Delivery RL Concept Simulator

class FoodDeliveryRLSimulator:
    def __init__(self):
        self.agent_state = {
            "current_location": "Restaurant",
            "orders_delivered": 0,
            "total_reward": 0.0
        }

        self.total_episodes = 0
        self.total_reward_all_episodes = 0.0

        self.reward_map = {
            "accept_order": 2,
            "navigate_to_customer": 1,
            "request_directions": 0,
            "deliver_order": 10,
            "wait": -1
        }

    def reset_episode_state(self):
        self.agent_state["current_location"] = "Restaurant"

    def take_action(self, action):
        reward = self.reward_map.get(action, -5)

        if action == "accept_order":
            self.agent_state["current_location"] = "Restaurant"

        elif action == "navigate_to_customer":
            self.agent_state["current_location"] = "Customer"

        elif action == "request_directions":
            self.agent_state["current_location"] = "On Route"

        elif action == "deliver_order":
            self.agent_state["orders_delivered"] += 1
            self.agent_state["current_location"] = "Customer"

        elif action == "wait":
            self.agent_state["current_location"] = self.agent_state["current_location"]

        self.agent_state["total_reward"] += reward
        return reward

    def start_episode(self):
        self.reset_episode_state()

        actions = [
            "accept_order",
            "navigate_to_customer",
            "request_directions",
            "navigate_to_customer",
            "deliver_order",
            "wait"
        ]

        episode_reward = 0
        episode_log = []

        print("\n========== NEW DELIVERY EPISODE ==========")

        for step, action in enumerate(actions, start=1):
            reward = self.take_action(action)
            episode_reward += reward

            episode_log.append({
                "step": step,
                "action": action,
                "reward": reward,
                "cumulative_reward": episode_reward
            })

            print(
                f"Step {step}: {action} | "
                f"Reward: {reward:+d} | "
                f"Cumulative: {episode_reward} | "
                f"State: {self.agent_state}"
            )

        self.total_episodes += 1
        self.total_reward_all_episodes += episode_reward

        print("\n---------- Episode Summary ----------")
        for entry in episode_log:
            print(
                f"Step {entry['step']}: {entry['action']} | "
                f"Reward: {entry['reward']:+d} | "
                f"Cumulative: {entry['cumulative_reward']}"
            )

        print(f"Total episode reward: {episode_reward}")
        print(f"Agent state: {self.agent_state}")

    def view_stats(self):
        average = (
            self.total_reward_all_episodes / self.total_episodes
            if self.total_episodes > 0 else 0
        )

        print("\n========== AGENT STATS ==========")
        print(f"Total episodes run: {self.total_episodes}")
        print(f"Total reward earned: {self.total_reward_all_episodes}")
        print(f"Average reward per episode: {average:.2f}")
        print(f"Orders delivered: {self.agent_state['orders_delivered']}")
        print(f"Current location: {self.agent_state['current_location']}")
        print(f"Agent cumulative reward: {self.agent_state['total_reward']}")


def main():
    simulator = FoodDeliveryRLSimulator()

    while True:
        print("\n========== FOOD DELIVERY RL SIMULATOR ==========")
        print("1. Start New Delivery Episode")
        print("2. View Agent Stats")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            simulator.start_episode()

        elif choice == "2":
            simulator.view_stats()

        elif choice == "3":
            print("Exiting Food Delivery RL Simulator.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
