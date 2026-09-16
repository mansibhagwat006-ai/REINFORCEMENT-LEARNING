# Section A — Concept Application

## Task 1: Reinforcement Learning for Food Delivery Dispatch

Reinforcement Learning (RL) is suitable because the delivery dispatch system must make decisions repeatedly and improve from the results of those decisions. Traditional programming requires manually written rules, while RL can learn a better decision policy through interaction with the delivery environment.

The key characteristic is **learning through trial and error using rewards and penalties**. The agent takes an action, observes the result, receives a reward, and uses that experience to improve future decisions. Therefore, it does not require a labelled dataset containing the correct dispatch decision for every situation.

## Task 2: Supervised Learning vs Reinforcement Learning

A supervised learning model learns from historical examples where the input and desired output are already provided. For example, past restaurant orders can be used to train a model to predict a recommendation based on known historical outcomes.

An RL agent learns differently. It interacts with the environment, selects recommendations, receives rewards based on customer responses or other outcomes, and updates its policy over time. The fundamental difference is that supervised learning learns from labelled examples, whereas RL learns from **actions, feedback, and rewards**. This makes RL useful for a recommendation engine that needs to continuously adapt.

## Task 3: RL vs Unsupervised Learning

Both methods can work without labelled data, but their learning objectives are different. Unsupervised learning, such as clustering, discovers patterns or groups in existing data without a reward signal.

RL actively chooses actions and learns from the consequences of those actions. For delivery zones, an RL agent could assign riders to zones, observe outcomes such as delivery efficiency, and receive rewards or penalties. It can therefore continuously improve its policy based on real delivery outcomes, while clustering mainly identifies patterns in the available data.

## Task 4: Components of the Delivery Dispatch RL System

- **Agent:** The delivery dispatch AI system that decides which rider should receive an incoming order.
- **Environment:** The food delivery platform and real-world delivery situation, including orders, riders, locations, traffic, and delivery outcomes.
- **Actions:** Possible rider assignments, such as assigning the order to Rider A, Rider B, Rider C, or another eligible rider.
- **Reward:** A numerical value representing the quality of the dispatch outcome.

A suitable reward should combine useful delivery outcomes, such as on-time delivery and customer satisfaction, while avoiding shortcuts. For example, rewarding only speed could encourage unsafe or unrealistic behaviour. A better reward should consider delivery time, successful completion, customer rating, and penalties for undesirable outcomes.

## Task 5: Game AI and Food Delivery RL

In game AI, an RL agent observes the game state, chooses an action, receives a reward or penalty, and uses the experience to improve its future actions. For example, a chess-playing agent can learn that some actions lead to better game outcomes.

Food delivery follows the same principle even though it is not a game. The delivery agent observes the current delivery state, chooses a dispatch or delivery action, receives feedback from the resulting outcome, and uses that feedback to improve future decisions. The environment is different, but the basic RL loop of **state → action → reward → learning** remains the same.

## Task 6: RL in Recommendation Systems

Reinforcement Learning can be used in recommendation systems by treating recommendations as actions and user responses as feedback. For example, a system may recommend a meal, observe whether the customer views, orders, skips, or rates it, and use this feedback to improve later recommendations.

An RL-based system can adapt as customer preferences change because it continues learning from new interactions. A model trained once on historical data may continue reflecting older behaviour unless it is retrained. RL can therefore support continuous adaptation by using current interaction outcomes as feedback.
