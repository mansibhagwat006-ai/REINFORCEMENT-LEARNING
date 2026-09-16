# Section B - Task 2: Agent State Tracker

state = {
    "location": "Restaurant",
    "orders_delivered": 0,
    "total_reward": 0.0,
    "is_available": True
}


def update_state(state, new_location, reward_earned):
    state["location"] = new_location
    state["orders_delivered"] += 1
    state["total_reward"] += reward_earned
    return state


transitions = [
    ("Zone A", 12.0),
    ("Zone B", 8.5),
    ("Zone C", 15.0),
    ("Zone D", 10.5)
]

print("Initial state:")
print(state)

for new_location, reward in transitions:
    update_state(state, new_location, reward)
    print("\nUpdated state:")
    print(state)
