import numpy as np

def compute_sd(data):
    return [np.std(data[i], axis=-1) for i in range(200)]
