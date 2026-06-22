from scipy.stats import pearsonr
import numpy as np

def pearson1(entropie, variable): 
    coefficient = []
    p_values = []

    entropie = entropie.T

    for i in range(len(entropie)):  
        correlation_coefficient, p_value = pearsonr(variable,entropie[i])
        coefficient.append(correlation_coefficient)
        p_values.append(p_value)

    alpha = 0.05
    reject_null, corrected_p_values, _, _ = multipletests(p_values, alpha=alpha, method='bonferroni')

    mean_p_value = np.mean(p_values)

    results = [p_values, corrected_p_values, mean_p_value]
    
    return results
