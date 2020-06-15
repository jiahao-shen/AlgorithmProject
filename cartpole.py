import gym
from dqn import *
from tqdm import trange


def train():
    env = gym.make('CartPole-v0')
    agent = DQN(4, 2)

    episode = 1000
    batch_size = 16

    for e in trange(episode):
        state = env.reset().reshape((1, 4))
        score = 0

        while True:
            # env.render()

            action = agent.act(state)
            new_state, reward, done, info = env.step(action)
            new_state = np.reshape(new_state, (1, 4))

            agent.memorize(state, action, reward, new_state, done)
            agent.replay(batch_size)

            state = new_state
            score += reward

            if done:
                break

        print('Episode:', e, '/', episode, ', value:', agent.epsilon,
              ', score:', score, file=open('logs/cartpole.log', 'a'))

        agent.save('models/CartPole.h5')
    
    env.close()


if __name__ == '__main__':
    train()