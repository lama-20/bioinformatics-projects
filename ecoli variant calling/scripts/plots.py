import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("tables/after_filter_final.tsv", sep="\t")

df["QUAL"] = pd.to_numeric(df["QUAL"], errors="coerce")
df["DP"] = pd.to_numeric(df["DP"], errors="coerce")
df["POS"] = pd.to_numeric(df["POS"], errors="coerce")

# Scatter Plot
plt.figure(figsize=(7,5))
plt.scatter(df["DP"], df["QUAL"])
plt.xlabel("DP")
plt.ylabel("QUAL")
plt.title("Scatter Plot: DP vs QUAL")
plt.tight_layout()
plt.savefig("plots/scatter_plot.png")
plt.close()

# Histogram
plt.figure(figsize=(7,5))
plt.hist(df["QUAL"].dropna(), bins=20)
plt.xlabel("QUAL")
plt.ylabel("Frequency")
plt.title("Histogram of QUAL")
plt.tight_layout()
plt.savefig("plots/histogram.png")
plt.close()

# Heatmap
corr = df[["POS", "QUAL", "DP"]].corr()

plt.figure(figsize=(6,5))
sns.heatmap(corr, annot=True)
plt.title("Heatmap")
plt.tight_layout()
plt.savefig("plots/heatmap.png")
plt.close()

print("Plots created successfully")
