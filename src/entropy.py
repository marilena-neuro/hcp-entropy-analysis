import numpy as np
import neurokit2 as nk

def sample_entropy(data):
    data = data.T
    entropies = [
        nk.entropy_sample(data[i], delay=1, dimension=2, tolerance='sd')[0]
        for i in range(200)
    ]
    return entropies


def fuzzy_entropy(data):
    data = data.T
    entropies = [
        nk.entropy_fuzzy(data[i], delay=1, dimension=2, tolerance='sd')[0]
        for i in range(200)
    ]
    return entropies


def multiscale_entropy(data):
    data = data.T
    entropies = [
        nk.entropy_multiscale(data[i], scale='default', dimension=3, tolerance='sd')[0]
        for i in range(200)
    ]
    return entropies
