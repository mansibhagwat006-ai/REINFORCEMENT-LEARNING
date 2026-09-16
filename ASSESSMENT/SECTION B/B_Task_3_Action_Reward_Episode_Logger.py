# Section B - Task 3: Action-Reward Episode Logger

actions = [
    "accept_order",
    "request_directions",
    "navigate_to_restaurant",
    "accept_order",
    "request_directions",
    "mark_delivered"
]

reward_map = {
    "accept_order": 2,
    "reject_order": -1,
    "request_directions": 0,
    "mark_delivered": 10
}

# navigate_to_restaurant is included in the episode sequence.
# It is given 0 reward so every action in the sequence has a defined reward.
reward_map["navigate_to_restaurant"] = 0

cumulative_reward = 0

for step, action in enumerate(actions, start=1):
    reward = reward_map[action]
    cumulative_reward += reward

    print(
        f"Step {step}: Action = {action} | "
        f"Reward = {reward:+d} | "
        f"Cumulative Reward = {cumulative_reward}"
    )

print(f"\nTotal episode reward: {cumulative_reward}")
