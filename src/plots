import matplotlib.pyplot as plt
import pandas as pd

def plot_correlation_matrix_transposed(data):
    flat_data = [(key1, key2, key3, value3[0][0], value3[1][0], value3[2][0]) for key1, value1 in data.items() 
                 for key2, value2 in value1.items() for key3, value3 in value2.items()]

    df = pd.DataFrame(flat_data, columns=['Group', 'Variable', 'Statistic', 'Correlation', 'P-Value_Uncorrected', 'P-Value_Corrected'])
    
    correlation_matrices = {}

    for group in df['Group'].unique():
        group_df = df[df['Group'] == group]
        pivot_table = pd.pivot_table(group_df, values='Correlation', index='Statistic', columns='Variable')
        desired_order = ['rest1_s200', 'rest2_s200'] + [col for col in pivot_table.columns if col not in ['rest1_s200', 'rest2_s200']]
        pivot_table = pivot_table.reindex(columns=desired_order)
        selected_rows = pivot_table.loc[['std_raw', 'roc_raw_squared', 'se', 'mse', 'fe']]
        pivot_table = pivot_table.drop(index=['std_raw', 'roc_raw_squared', 'se', 'mse', 'fe'])
        pivot_table = pd.concat([selected_rows, pivot_table])
        correlation_matrices[group] = pivot_table

    for group, matrix in correlation_matrices.items():
        plt.figure(figsize=(8, 6))
        plt.title(f'Correlation matrix for group "{group}"')

        mask = df[(df['Group'] == group) & (df['P-Value_Corrected'] < 0.05)]

        transposed_matrix = matrix.T

        plt.matshow(transposed_matrix, cmap='coolwarm', vmin=-1, vmax=1, fignum=False)

        for i in range(transposed_matrix.shape[0]):
            for j in range(transposed_matrix.shape[1]):
                tasks = transposed_matrix.index[i]
                entropie = transposed_matrix.columns[j]

                masked_data = mask[(mask['Variable'] == tasks) & (mask['Statistic'] == entropie)]
                
                if not masked_data.empty:
                    plt.gca().text(j, i, f'{transposed_matrix.iloc[i, j]:.2f}', ha='center', va='center', 
                                   fontweight='bold', color='black')
                else:
                    plt.gca().text(j, i, f'{transposed_matrix.iloc[i, j]:.2f}', ha='center', va='center', 
                                   color='black')

        plt.gca().xaxis.set_ticks_position('bottom')  
        plt.xlabel('Variability and Complexity', fontsize = 14)
        plt.ylabel('Tasks', fontsize = 14)
        plt.xticks(range(transposed_matrix.shape[1]), ['SD', 'MSSD', 'SE', 'MSE', 'FE'], rotation=90, fontsize = 12)
        plt.yticks(range(transposed_matrix.shape[0]), ['REST1', 'REST2', 'EMOTION', 'GAMBLING', 'LANGUAGE', 'MOTOR', 'RELATIONAL', 'SOCIAL', 'WM'], fontsize = 12)
        plt.colorbar(label='Correlation', shrink=0.8)
        plt.show()

def plot_data_gender_networks():
# Code funktioniert nicht richtig. für Boxplot von z.B. FE muss FE auch am ende der entropy liste stehen!! weil es male/female numbers nur von dem letzten dings nimmt. Selbes für durchgang

    entropies = ['std_raw', 'roc_raw_squared', 'fe', 'mse', 'se']
    durchgang = [rest1_s200, rest2_s200, emotion_s200, gambling_s200, language_s200, motor_s200, relational_s200, social_s200, wm_s200]
    key2 = 'M'
    key3 = 'F'

    NETWORKS_SCHAEFER_200 = {'VIS': [(0, 11), (100, 111)],
                        'SMN':[(12, 27), (112, 129)],
                        'DAN':[(28, 38), (130, 140)],
                        'VAN':[(39, 49), (141, 155)],
                        'LIM':[(50, 55), (156, 163)],
                        'CON':[(56, 73), (164, 182)],
                        'DMN':[(74, 97), (183, 195)],
                        'Temp':[(98, 99), (196, 199)], 
                        }

    entropies = ['mse', 'se', 'std_raw', 'roc_raw_squared','fe'] #'mse'
    durchgang = [rest2_s200, emotion_s200, social_s200, rest1_s200, wm_s200,motor_s200,relational_s200,language_s200,gambling_s200]
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

            
                    # Calculate Pearson correlation and store the result
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
                    # Create a key for the result using the naming convention

                    new_dict = {'0': male_numbers,
                                '1': female_numbers
                               }

                    wholebrain_values[network] = new_dict

                whole_brain_variables[entropie] = wholebrain_values

            slicedbrain[item_name] = whole_brain_variables

    return slicedbrain

def plot_nested_boxplot_gender_network(data_x, ylabel): 

    runs = []
    variability = []
    correlation = []

    df = pd.DataFrame()
    
    for run, values in data_x.items():
        for ent, entropie in values.items():
            for network, networks in entropie.items():
                for gender_item, gender_values in networks.items():
                    df_cat = pd.DataFrame({'gender_values': gender_values})
                    df_cat['gender'] = gender_item
                    df_cat['variability'] = ent
                    df_cat['run'] = run
                    df_cat['network'] = network
                    df = df.append(df_cat, ignore_index=True)

    # You have to change what variability and what task you want to plot here!
    rest1_df = df[(df['variability'] == 'fe') & (df['run'] == 'gambling_s200')]
    overall_mean = rest1_df['gender_values'].mean()
    

    print(rest1_df)
    
    plt.figure()
    sns.boxplot(data=rest1_df, x='network', y='gender_values', hue='gender', dodge=True, palette = "bright")
    mean_line = mlines.Line2D([], [], color='red', linestyle='--', label='Overall Mean')
    orange_patch = mpatches.Patch(color='orange', label='Orange Box')
    blue_patch = mpatches.Patch(color='blue', label='Blue Box')
    #labels=['VIS', 'SMN', 'DAN', 'GAMBLING', 'LANGUAGE', 'MOTOR', 'RELATIONAL', 'SOCIAL', 'WM']
    plt.gca().add_line(mean_line)
    plt.xlabel('Networks')
    plt.ylabel('FE values - GAMBLING', fontsize = 12)
    plt.legend(title='Run')
    plt.axhline(y=overall_mean, color='r', linestyle='--', label='Overall Mean')
    plt.xticks(rotation = 90, fontsize = 12)
    plt.legend()
    plt.legend(title='Gender', labels = ["Overall Mean", 'Male', 'Female' ], handles=[mean_line,blue_patch, orange_patch], loc='best', bbox_to_anchor=(1, 1))  # Adjust legend position
    plt.tight_layout()
    #plt.ylim(0.6, 1.4)
    plt.show()
