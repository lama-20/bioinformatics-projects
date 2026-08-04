import pandas as pd

before = pd.read_csv("tables/before_filter_final.tsv", sep="\t")
after = pd.read_csv("tables/after_filter_final.tsv", sep="\t")

for df in [before, after]:
    df["QUAL"] = pd.to_numeric(df["QUAL"], errors="coerce")
    df["DP"] = pd.to_numeric(df["DP"], errors="coerce")

    df["TRUE_FALSE"] = (
        (df["QUAL"] > 50) & (df["DP"] > 20)
    ).map({True: "TRUE", False: "FALSE"})

with pd.ExcelWriter("tables/variant_tables.xlsx") as writer:
    before.to_excel(writer, sheet_name="Before_Filter", index=False)
    after.to_excel(writer, sheet_name="After_Filter", index=False)

print("Excel file created successfully")
