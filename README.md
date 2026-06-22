# fMRI Variability and Complexity Analysis
This project analyses fMRI data from the Human Connectome Project (HCP) and investigates neural variability and complexity. 

The goal is to understand how these measures relate to individual traits such as age, intelligence or gender. 

## Project Overview
Brain variability is inherently variable and complex. This project explores two core concepts: 
- **Neural variability** (SD, MSSD)
- **Neural complexity/entropy** (Sample Entropy, Fuzzy Entropy, Multiscale Entropy)

Then we analyse how these measure relate to: 
- Age
- Fluid intelligence
- Crystallized intelligence
- Gender

## Key Results
- Neural variability decreases with age
- Entropy measures show mixed relationships with age
- Variability is higher in resting-state, entropy is higher during tasks
- Cognitive variables show task-specific correlations

## Methods

### Variability Measures
- Standard Deviation (SD)
- Mean Squared Successive Difference (MSSD)

### Complexity Measures
- Sample Entropy (SE)
- Fuzzy Entropy (FE)
- Multiscale Entropy (MSE)

## Data Specifics

This project uses data from the **Human Connectome Project (HCP)** (WU-Minn Consortium).

### Dataset
- **HCP Young Adult 1200 release**: Subsample of 330 participants

### Data Structure
- 2 resting-state sessions
- 7 task-based fMRI scans
- each scan acquired with two phase encoding directions (Left-to-Right (LR) serves as primary dataset; Right-to-Left (RL) serves as replication sample)

### Notes on Data Availability
Due to HCP data usage restrictions, the raw dataset is **not included in this repository**.  
Access can be requested via the official HCP platform:
https://www.humanconnectome.org

## Repository Structure
- 'src/' > core analysis functions
- 'notebooks/' > exploratory analysis & visualization
- 'data/' > dataset structure (HCP data not included)
- 'results/' > figures and outputs
- 'reports/' > thesis and summary

## Reproducibility 
Data used: 
- Subset of Human Connectome Project (HCP) Young Adult 1200 release by Washington University of Minnesota (330 individuals)
- For the preprocessing of data see Wehrheim, M. H., Faskowitz, J., Schubert, A. & Fiebach, C. J. (2024). Reliability of variability and complexity measures for task and task‐free BOLD fMRI. Human Brain Map-
ping, 45(10). https://doi.org/10.1002/hbm.26778
