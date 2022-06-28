from matminer.datasets import load_dataset

df = load_dataset("dielectric_constant")

print("drop前：")
print(df.describe())
print("--" * 20)
cleaned_df = df.drop(["nsites", "space_group", "e_electronic", "e_total"], axis=1)
print("drop后")
print(cleaned_df.describe())
df['poly_ionic'] = df['poly_total']-df['poly_electronic']
print(df['poly_ionic'])