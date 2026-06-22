# Data

This project uses data from the Human Connectome Project (HCP).

Due to data access restrictions, **neither raw nor processed data are included in this repository**.

## Structure

- `raw/` → original fMRI data (not provided)
- `processed/` → preprocessed data used in analysis (not provided)

## Data Access

To access the dataset, request permission via:
https://www.humanconnectome.org

Dataset used:
- HCP Young Adult 1200 release

## Preprocessing Notes

- Data preprocessing was performed using established pipelines (HCP pipeline + additional processing steps)
- The preprocessing was **not performed by the author of this repository**
- Preprocessing was done by: Wehrheim, M. H., Faskowitz, J., Schubert, A. & Fiebach, C. J. (2024). Reliability of variabil-
ity and complexity measures for task and task‐free BOLD fMRI. Human Brain Map-
ping, 45(10). https://doi.org/10.1002/hbm.26778
- Due to computational constraints, the veriability and entropy calculations were not entirely performed on local hardware. Preprocessed datasets used in this project were provided by a supervisor. However, the implemented functions in this repository demonstrate the full computation pipeline.

## Reproducing the Analysis

To reproduce the results:
1. Request access to the HCP dataset
2. Apply preprocessing pipeline (see references)
3. Run analysis scripts provided in `src/` and `notebooks/`
