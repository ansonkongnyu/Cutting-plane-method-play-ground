If you want to test with ray running locally: 
    ray start --head

Start the training process: bash train_ray.sh

Key Components:

Algorithm Design:
The project involves various components, including pre-processing, policy gradient, LSTM and attention networks, exploration, and evolutionary strategies (ES).
Pre-processing:
The algorithm normalizes the inputs, constraints, and available cuts before feeding them into the policy network.
Policy Gradient:
The policy gradient method is employed in reinforcement learning, updating the policy network after every episode based on the discounted reward.
LSTM and Attention Networks:
LSTM and attention networks are used to generate an embedded representation of the inputs, which is then passed through a dense linear network to generate probability distribution for actions.
Exploration:
Exploration rate is set at 0.5 initially and decays with each iteration. Actions are sampled based on the probability distribution rather than choosing the action with the highest probability.
Evolutionary Strategies (ES):
The algorithm follows the paper's approach to implementing evolutionary strategies, adding a random factor to the discounted reward.
Experiments and Results:

Four different model configurations were tested, varying LSTM hidden dimensions, dense hidden dimensions, exploration, and evolutionary strategies.
The models showed good performance during training, with some variation in performance based on the complexity of the problem.
Conclusion:
The project demonstrates that the reinforcement learning model from the paper effectively addresses cutting plane problems and becomes more stable when exploration is added.
