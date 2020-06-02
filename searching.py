# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:05:39 2020

@author: Lenovo
"""

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
search=pd.read_csv("google.csv")
print(search.Year.value_counts().sort_values(ascending = False).head(100))
sns.kdeplot(data=search['Year'], shade=True)
print(search.Age.value_counts())
sns.countplot(x='Age', data=search)
print(search['google'].value_counts())
sns.countplot(x='google', data=search)
sns.pairplot(data=search)

