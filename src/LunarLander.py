import gymnasium as gym
from gymnasium.envs import registry

# optional - check available environment
for env_id in registry.keys():
    if "LunarLander" in env_id:
        print(env_id)

env = gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset()

episode_over = False
while not episode_over:
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)

    episode_over = terminated or truncated

env.close()