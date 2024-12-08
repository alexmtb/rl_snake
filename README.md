# Snake game with Reinforcement Learning

## Description

This is a simple implementation of the Snake game with Reinforcement Learning using the [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3) library.
Snake is controlled by a RL algorithm. The objective is to collect as many cubes as possible and to avoid collisions with the walls and itself body

### Features:
- Snake is controlled using reinforcement learning (e.g., PPO, DQN).
- The snake grows longer upon eating food.
- Food spawns randomly on the game field.
- The game ends when the snake collides with a wall or itself.
- Rewards and penalties are used to train the RL agent.

---

## ⚙️ Requirements
Before you start, ensure you have the following dependencies installed:

- Python 3.8+ (I used Python 3.11)
- Python libraries:
  - pygame (for graphical interface)
  - numpy (for array operations)
  - stable-baselines3 (for reinforcement learning)
  - gym (for game environment implementation)

Install the dependencies with:

```bash | PowerShell
pip install pygame numpy stable-baselines3 gym

