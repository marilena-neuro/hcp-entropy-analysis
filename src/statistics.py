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

def whole_brain():

    entropies = ['std_raw', 'roc_raw_squared', 'se', 'fe', 'mse']
    durchgang = [rest1_s200, rest2_s200, emotion_s200, gambling_s200, language_s200, motor_s200, relational_s200, social_s200, wm_s200]
    variables = [ages, fluid_Unadj, fluid_Adj, crystal_Unadj, crystal_Adj, total_Unadj, total_Adj]
    
    wholebrain = {}
    for variable, variable_name in zip(variables, ['ages', 'fluid_Unadj', 'fluid_Adj', 'crystal_Unadj', 'crystal_Adj', 'total_Unadj', 'total_Adj']):
        whole_brain_variables = {}
        for item, item_name in zip(durchgang, ['rest1_s200', 'rest2_s200', 'emotion_s200', 'gambling_s200', 'language_s200', 'motor_s200', 'relational_s200', 'social_s200', 'wm_s200']): 
            wholebrain_values = {}
            for entropie in entropies: 

                if item_name == 'emotion_s200' and entropie == 'mse':
                    network_mean_data = np.nanmean(item[entropie], axis = 1)
                else: 
                    network_mean_data = np.nanmean(item[entropie], axis=1)
                    
                correlation, p_values = pearsonr(variable, network_mean_data)   
                m = 5
                corrected_p_values = p_values * m
                corrected_p_values = min(corrected_p_values, 1.0)

                wholebrain_values[entropie] = [[correlation], [p_values], [corrected_p_values]]
                
            whole_brain_variables[item_name] = wholebrain_values

        wholebrain[variable_name] = whole_brain_variables

    return wholebrain

def slice_entropies():
    NETWORKS_SCHAEFER_200 = {'VIS': [(0, 11), (100, 111)],
                        'SMN':[(12, 27), (112, 129)],
                        'DAN':[(28, 38), (130, 140)],
                        'VAN':[(39, 49), (141, 155)],
                        'LIM':[(50, 55), (156, 163)],
                        'CON':[(56, 73), (164, 182)],
                        'DMN':[(74, 97), (183, 195)],
                        'Temp':[(98, 99), (196, 199)], 
                        }

    entropies = ['std_raw','roc_raw_squared', 'se','fe', 'mse']
    durchgang = [rest1_s200, rest2_s200, emotion_s200, gambling_s200, language_s200, motor_s200, relational_s200, social_s200, wm_s200]
    variables = [ages, fluid_Unadj, fluid_Adj, crystal_Unadj, crystal_Adj, total_Unadj, total_Adj]
    
    slicedbrain = {}
    for variable, variable_name in zip(variables, ['ages', 'fluid_Unadj', 'fluid_Adj', 'crystal_Unadj', 'crystal_Adj', 'total_Unadj', 'total_Adj']):
        whole_brain_variables = {}
        for item, item_name in zip(durchgang, ['rest1_s200', 'rest2_s200', 'emotion_s200', 'gambling_s200', 'language_s200', 'motor_s200', 'relational_s200', 'social_s200', 'wm_s200']): 
            wholebrain_values = {}
            for entropie in entropies: 
                network_data = {}
                for network, indices in NETWORKS_SCHAEFER_200.items():
                    sliced_list = []
                    
                    for start, end in indices:
                        sliced_columns = np.array([row[start:end+1] for row in item[entropie]])
                        sliced_list.append(sliced_columns)
                        
                    concatenated_array = np.concatenate(sliced_list, axis=1)
                    #concatenated_array = concatenated_array.tolist()
                
                    row_means = np.nanmean(concatenated_array, axis=1)
                    correlation, p_values = pearsonr(variable, row_means)
                    m = 17
                    corrected_p_values = p_values * m
                    corrected_p_values = min(corrected_p_values, 1.0)
                
                    network_data[network] = [[correlation], [p_values], [corrected_p_values]]

                wholebrain_values[entropie] = network_data
                
            whole_brain_variables[item_name] = wholebrain_values

        slicedbrain[variable_name] = whole_brain_variables

    return slicedbrain

def whole_brain_gender():

    entropies = ['std_raw', 'roc_raw_squared', 'se', 'fe', 'mse']
    durchgang = [rest1_s200, rest2_s200, emotion_s200, gambling_s200, language_s200, motor_s200, relational_s200, social_s200, wm_s200]
    variables = [complete_data_gender] 
    
    wholebrain = {}
    for variable, variable_name in zip(variables, ['Gender']):
        whole_brain_variables = {}
        for item, item_name in zip(durchgang, ['rest1_s200', 'rest2_s200', 'emotion_s200', 'gambling_s200', 'language_s200', 'motor_s200', 'relational_s200', 'social_s200', 'wm_s200']): 
            wholebrain_values = {}
            for entropie in entropies: 
                if item_name == 'emotion_s200' and entropie == 'mse':
                    network_mean_data = np.nanmean(item[entropie], axis = 1)  
                else:
                    network_mean_data = np.mean(item[entropie], axis=1)
                male_numbers = [num for g, num in zip(complete_data_gender, network_mean_data) if g == 'M']
                female_numbers = [num for g, num in zip(complete_data_gender, network_mean_data) if g == 'F']
                # Perform independent t-test
                t_statistic, p_value = stats.ttest_ind(male_numbers, female_numbers)
                
                m = 5
                corrected_p_values = m * p_value
                corrected_p_values = min(corrected_p_values, 1.0)

                wholebrain_values[entropie] = [[t_statistic], [p_value], [corrected_p_values], [male_numbers], [female_numbers]]
                
            whole_brain_variables[item_name] = wholebrain_values

        wholebrain[variable_name] = whole_brain_variables

    return wholebrain

def slice_entropies_gender():
    NETWORKS_SCHAEFER_200 = {'VIS': [(0, 11), (100, 111)],
                        'SMN':[(12, 27), (112, 129)],
                        'DAN':[(28, 38), (130, 140)],
                        'VAN':[(39, 49), (141, 155)],
                        'LIM':[(50, 55), (156, 163)],
                        'CON':[(56, 73), (164, 182)],
                        'DMN':[(74, 97), (183, 195)],
                        'Temp':[(98, 99), (196, 199)], 
                        }

    entropies = ['std_raw', 'roc_raw_squared', 'se', 'fe', 'mse']
    durchgang = [rest1_s200, rest2_s200, emotion_s200, gambling_s200, language_s200, motor_s200, relational_s200, social_s200, wm_s200]
    variables = [complete_data_gender]
    
    slicedbrain = {}
    for variable, variable_name in zip(variables, ['Gender']):
        whole_brain_variables = {}
        for item, item_name in zip(durchgang, ['rest1_s200', 'rest2_s200', 'emotion_s200', 'gambling_s200', 'language_s200', 'motor_s200', 'relational_s200', 'social_s200', 'wm_s200']): 
            wholebrain_values = {}
            for entropie in entropies: 
                network_data = {}
                for network, indices in NETWORKS_SCHAEFER_200.items():
                    sliced_list = []
                    
                    for start, end in indices:
                        sliced_columns = np.array([row[start:end+1] for row in item[entropie]])
                        sliced_list.append(sliced_columns)
                        
                    concatenated_array = np.concatenate(sliced_list, axis=1)
                    #concatenated_array = concatenated_array.tolist()
                
                    row_means = np.nanmean(concatenated_array, axis=1)

                    p_value_t_test = []
                    statistics = []

                    male_numbers = [num for g, num in zip(complete_data_gender, row_means) if g == 'M']
                    female_numbers = [num for g, num in zip(complete_data_gender, row_means) if g == 'F']
                    # Perform independent t-test
                    t_statistic, p_value = stats.ttest_ind(female_numbers, male_numbers) # für FE positiv: erst female_numbers, male_number
                    #t_statistic, p_value = ttest_ind(complete_data_gender, reshaped_sds[i])
                    statistics.append(t_statistic)
                    p_value_t_test.append(p_value)
            
                    m = 17
                    corrected_p_values = p_value * m
                    corrected_p_values = min(corrected_p_values, 1.0)
                
                    network_data[network] = [[t_statistic], [p_value], [corrected_p_values], [male_numbers], [female_numbers]]  

                wholebrain_values[entropie] = network_data

            whole_brain_variables[item_name] = wholebrain_values

        slicedbrain[variable_name] = whole_brain_variables

    return slicedbrain
