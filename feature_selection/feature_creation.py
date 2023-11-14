# -*- coding: utf-8 -*-
"""feature_creation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YJZVoRZZZTzQtpv48fEvarmLacdGfOVJ
"""

import pandas as pd

def feature_creation(df):
  # 'Score' feature for 'hate_speech_score' column
  df['Score'] = df['hate_speech_score'].astype(float)

  # 'Comments' feature for 'text' column
  df['Comments'] = df['text'].str.len()


# Load the CSV file into a DataFrame
df = pd.read_csv('measuring_hate_speech.csv')


# Checking to see if the new created features exits
if 'Comments' and 'Score' in df.columns:
    print("The 'Comments' and 'Score' features exists in the DataFrame.")
else:
    print("The 'Comments' and 'Score' features does not exist in the DataFrame.")

# Printing all the columns in the dataframe.
# The 'Comments' and 'Score' feature are created at the end
print(df.columns)