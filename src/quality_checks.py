import numpy as np

def check_nan_inf(datasets, keys):
    results = {}

    for name, dataset in datasets.items():
        results[name] = {}

        for key in keys:
            if key in dataset:
                arr = dataset[key]
                results[name][key] = {
                    "nan": np.isnan(arr).any(),
                    "inf": np.isinf(arr).any()
                }

    return results
