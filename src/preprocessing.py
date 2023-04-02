"""
Created on Sun Apr  2 20:49:11 2023

@author: Raghul S
"""
# -*- coding: utf-8 -*-
import pandas as pd 
import numpy as np

data = pd.read_csv("../data/mldata.csv")

target = "Suggested Job Role"

cols = data.columns.tolist();
numerical_cols = data.select_dtypes(include=np.number).columns.tolist()
categorical_cols= data.select_dtypes(include=['object']).columns.tolist()

unique_values={}
for i in data:
    unique_values[i] = data[i].unique().tolist()

Dict={}
for i in data[categorical_cols]:
    data[i] = data[i].astype('category')
    data[i+"_code"] = data[i].cat.codes
    
    Dict[i]={}
    for j in range(0,len(data.axes[0])):
        Dict[i][data[i].iloc[j]] = data[i+"_code"].iloc[j]
    data[i]= data[i+"_code"]
    data= data.drop(i+"_code", axis=1)
    
    

