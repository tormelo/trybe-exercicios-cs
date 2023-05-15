import pandas as pd


df = pd.read_csv("exercicios/data/fifa_audience.csv")

print(
    df.groupby("confederation")["country"]
    .count()
    .reset_index(name="countries")
)
