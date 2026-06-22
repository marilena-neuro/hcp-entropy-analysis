import numpy as np
from scipy.stats import pearsonr
from scipy import stats
from statsmodels.stats.multitest import multipletests

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

def t_test(entropie, variable): 
    p_value_t_test = []
    statistics = []

    network_mean_data = np.nanmean(entropie, axis = 1)  
    male_numbers = [num for g, num in zip(complete_data_gender, network_mean_data) if g == 'M']
    female_numbers = [num for g, num in zip(complete_data_gender, network_mean_data) if g == 'F']
    
    t_statistic, p_value = stats.ttest_ind(male_numbers, female_numbers)
    #t_statistic, p_value = ttest_ind(complete_data_gender, reshaped_sds[i])
    statistics.append(t_statistic)
    p_value_t_test.append(p_value)

    m = 5
    corrected_p_values = m * p_value
    corrected_p_values = min(corrected_p_values, 1.0)

    results = [p_value_t_test, corrected_p_values, statistics, male_numbers, female_numbers]

    return results
