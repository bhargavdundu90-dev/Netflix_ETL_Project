import pandas as pd

df = pd.read_csv('data/netflix_titles.csv')

print("🔢 Shape:", df.shape)
print("📋 Columns:", df.columns.tolist())
print("🧼 Nulls:\n", df.isnull().sum())
print("🔍 Dtypes:\n", df.dtypes)
print("🔁 Duplicates:", df.duplicated().sum())
print("🧪 Sample rows:\n", df.sample(5))
