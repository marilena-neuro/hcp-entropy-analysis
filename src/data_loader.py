import numpy as np
import os

def load_npz(file_path):
    return np.load(file_path)


def load_all_tasks(base_path):
    tasks = [
        "EMOTION", "GAMBLING", "LANGUAGE", "MOTOR",
        "RELATIONAL", "REST1", "REST2", "SOCIAL", "WM"
    ]

    data = {}

    for task in tasks:
        path = os.path.join(base_path, task, f"Variability_s200_{task}_LR.npz")
        data[task] = np.load(path)

    return data
