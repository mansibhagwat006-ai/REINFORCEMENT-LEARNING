# Section B - Task 1: Delivery Reward Function

def calculate_reward(delivery_time, is_on_time, customer_rating):

    if is_on_time:
        reward += 10
    else:
        reward -= 5

    reward += customer_rating
    return reward


tests = [
    (25, True, 5),
    (40, False, 3),
    (30, True, 2),
]

for delivery_time, is_on_time, customer_rating in tests:
    reward = calculate_reward(delivery_time, is_on_time, customer_rating)
    print(
        f"Delivery time: {delivery_time} min | "
        f"On time: {is_on_time} | Rating: {customer_rating} | "
        f"Final reward: {reward}"
    )

ans = calculate_reward(30, True, 4)