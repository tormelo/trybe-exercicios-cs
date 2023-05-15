import pandas as pd


df = pd.read_csv("exercicios/data/fifa_audience.csv")

uefa_tv_audience_mean = df.loc[df["confederation"] == "UEFA"][
    "tv_audience_share"
].mean()

print(f"{uefa_tv_audience_mean:.2f}")
