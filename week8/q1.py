import numpy as np

def sample(a, b):
    assert a < b, "a must < b!"
    return a + np.random.random()*(b-a)

if __name__ == '__main__':
    print(sample(5, 7))