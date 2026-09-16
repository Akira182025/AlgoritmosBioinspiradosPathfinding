import numpy as np
from config import MAX_STEPS


def random_moves(rng, length=MAX_STEPS):
    return rng.integers(0, 4, size=length).astype(int)


def random_vector(rng, length=MAX_STEPS):
    return rng.uniform(0.0, 4.0, size=length)


def clip_vector(x):
    return np.clip(x, 0.0, np.nextafter(4.0, 0.0))
