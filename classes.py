import numpy as np
import pygame
import gym
from gym import spaces
from stable_baselines3 import PPO


# game congig
WINDOW_SIZE = 400
GRID_SIZE = 20
CELL_SIZE = WINDOW_SIZE // GRID_SIZE


class SnakeEnv(gym.Env):
    def __init__(self):
        super(SnakeEnv, self).__init__()
        self.action_space = spaces.Discrete(4)  # up, down, left, right
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(GRID_SIZE, GRID_SIZE, 3), dtype=np.float32)
        self.reset()
    
    def _place_food(self):
            while True:
                food = (np.random.randint(0, GRID_SIZE),
                        np.random.randint(0, GRID_SIZE))
                if food not in self.snake:
                    return food

    def _get_observation(self):
            obs = np.zeros((GRID_SIZE, GRID_SIZE, 3), dtype=np.float32)
            for x, y in self.snake:
                obs[y, x, 0] = 1
            fx, fy = self.food
            obs[fy, fx, 1] = 1

            return obs

    def reset(self):
        self.snake = [(GRID_SIZE // 2, GRID_SIZE // 2)]
        self.food = self._place_food()
        self.direction = 0
        self.score = 0
        self.game_over = False

        return self._get_observation()
    
    def step(self, action):
        if action == (self.direction + 2) % 4:
            action = self.direction
        
        self.direction = action
        head_x, head_y = self.snake[0]

        if action == 0:  # up
            head_y -= 1
        elif action == 1:  # right
            head_x += 1
        elif action == 2:  # down
            head_y += 1
        elif action == 3:  # left
            head_x -= 1

        new_head = (head_x, head_y)

        # check for collision
        if (new_head in self.snake) or\
        head_x < 0 or head_x >= GRID_SIZE or\
        head_y < 0 or head_y >= GRID_SIZE:
            self.game_over = True
            reward = -15
        else:
            self.snake.insert(0, new_head)
            if new_head == self.food:
                self.food = self._place_food()
                reward = 10
                self.score += 1
            else:
                self.snake.pop()
                reward = -0.1
        print(f'Длина змейки: {len(self.snake)}')
        return self._get_observation(), reward, self.game_over, {}
    
    def render(self, mode = 'human'):
        if mode == 'human':
            pygame.init()
            screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
            screen.fill((0, 0, 0))
            for x, y in self.snake:
                pygame.draw.rect(
                    screen, (0, 255, 0),
                    (x * CELL_SIZE,
                     y * CELL_SIZE,
                     CELL_SIZE,
                     CELL_SIZE))
                fx, fy = self.food
                pygame.draw.rect(
                    screen, (255, 0, 0),
                    (fx * CELL_SIZE,
                     fy * CELL_SIZE,
                     CELL_SIZE,
                     CELL_SIZE))
                pygame.display.flip()
                pygame.time.wait(100)
