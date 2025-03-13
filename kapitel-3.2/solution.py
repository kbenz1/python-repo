import pandas as pd

df = pd.read_csv("personen.csv")

df_gefiltert = df[df["Alter"] > 25]
df_gefiltert.to_csv("personen_ueber_25.csv")

df2 = pd.read_csv("personen_ueber_25.csv")
print(df2)