#%%
# -*- coding: utf-8 -*-
# /Users/user/.spyder-py3
#%% 
### LOAD RELEVANT MODULES
import os
import pandas as pd
import numpy as np
#%%%
### READ IN THE GAP DATASET FROM GITHUB 
# https://github.com/google-research-datasets/gap-coreference
# GAP CONTAINS 3 SEPERATE FILES: 
#    (1) gap-development.tsv - for model development
#    (2) gap-test.tsv - for model evaluation
#    (3) gap-validation.tsv - for parameter tuning

# OBTAIN RELEVANT URLs 
url_dev = 'https://raw.githubusercontent.com/google-research-datasets/gap-coreference/master/gap-development.tsv'
url_tes = 'https://raw.githubusercontent.com/google-research-datasets/gap-coreference/master/gap-test.tsv'
url_val = 'https://raw.githubusercontent.com/google-research-datasets/gap-coreference/master/gap-validation.tsv'

gap_dev = pd.read_csv(url_dev, delimiter="\t")
gap_tes = pd.read_csv(url_tes, delimiter="\t")
gap_val = pd.read_csv(url_val, delimiter="\t")

#%% 
### UNDERSTAND THE DATAFILES 
# GET COLUMN NAMES
list(gap_dev.columns)
list(gap_tes.columns)
list(gap_val.columns)

# DOUBLE CHECK DIMENSIONS
print(gap_dev.shape)
print(gap_tes.shape)
print(gap_val.shape)

# LOOK INTO FIRST 5 ROWS PER FILE
pd.set_option('display.max_columns', None)
print(gap_dev.head())
print(gap_tes.head())
print(gap_val.head())

ß


