import pandas as pd 

#for testing
df = pd.read_csv('measuring_hate_speech.csv')

def lowercase_text(df):
    df['text'] = df['text'].str.lower()
    return df

#Before
print(df['text'].head(5))

#After
lowercase_df = lowercase_text(df)
print(lowercase_df['text'].head(5))