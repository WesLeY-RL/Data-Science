# -*- coding: utf-8 -*-
"""padasipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14WjlUf-hjPgJtslumxuSGzAojORZ-8Fc
"""

!pip install ydata-profiling
#!pip install --upgrade pandas-profiling

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

data = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/winequality-red.csv", sep = ";")

data.info()

data.head()

data["quality"].describe()

data['quality'] = data['quality'].astype('category',copy=False)



qualidade  =  data["quality"].values
for i in qualidade:
  print(i)

from ydata_profiling import ProfileReport

profile = ProfileReport(data, title="Wine Quality")
profile

#como exportar os dados profile

profile.to_file(output_file="/content/dataframe_report.html")

