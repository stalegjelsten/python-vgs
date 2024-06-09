# Write your code here :-)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SOCR-HeightWeight.csv", sep=",", skiprows=0, index_col="Index")
df["Høyde (cm)"]  = df["Height(Inches)"] * 2.54
df["Vekt (kg)"] = df["Weight(Pounds)"] * 0.45359237
df.drop(labels=["Height(Inches)", "Weight(Pounds)"], axis="columns", inplace=True)
df["Høyde (cm)"].hist()
df["BMI"] = df["Vekt (kg)"]/((df["Høyde (cm)"]/100)**2)

fig,ax = plt.subplots()
ax.scatter(df["Høyde (cm)"], df["BMI"])
plt.show()
