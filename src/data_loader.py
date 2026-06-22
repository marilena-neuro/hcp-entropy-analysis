import os
import nibabel as nib

def load_nifti(file_path):
    img = nib.load(file_path)
    return img.get_fdata().squeeze()


def average_runs(data1, data2):
    return ((data1 + data2) / 2).T


def extract_file_paths(base_path, file_path, exclude_ids):
    paths = []

    for subject in os.listdir(base_path):
        if subject not in exclude_ids:
            subj_path = os.path.join(base_path, subject, file_path)
            if os.path.exists(subj_path):
                for file in os.listdir(subj_path):
                    if file.startswith('schaefer200'):
                        paths.append(os.path.join(subj_path, file))
    return paths
