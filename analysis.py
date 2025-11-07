import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\ezhen\OneDrive\Desktop\pokequant\final_data_clean.csv")
df_rare = df["pricing.cardmarket.avg"]
print(df_rare.plot.hist())