from scipy.stats import pearsonr
import numpy as np

def compute_correlations(data, variable):
    r_vals, p_vals = [], []

    for i in range(data.shape[0]):
        r, p = pearsonr(variable, data[i])
        r_vals.append(r)
        p_vals.append(p)

    return np.array(r_vals), np.array(p_vals)
