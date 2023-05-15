import pandas as pd


df = pd.read_csv("exercicios/data/fifa_audience.csv")

print(df.loc[df["population_share"] > 2])
