from classes import *

# agent learning
env = SnakeEnv()
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=20000)

# playing
obs = env.reset()

if __name__ == '__main__':
    for _ in range(5000):
        action, _ = model.predict(obs)
        obs, reward, game_over, _ = env.step(action)
        env.render()
        if game_over:
            obs = env.reset()

