import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# === Load cleaned data ===
df = pd.read_csv("data/cleaned_netflix_data.csv")

# === Plot 1: Titles Added Per Year ===
year_counts = df['year_added'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.barplot(x=year_counts.index, y=year_counts.values, palette="viridis")
plt.title("Titles Added Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/plot_titles_per_year.png")
plt.show()

# === Plot 2: Content Type Distribution ===
type_counts = df['type'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140, colors=["#66b3ff", "#ff9999"])
plt.title("Content Type Distribution")
plt.tight_layout()
plt.savefig("data/plot_content_type.png")
plt.show()

# === Plot 3: Top 10 Countries ===
top_countries = df[df['country'] != 'Unknown']['country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="magma")
plt.title("Top 10 Countries by Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("data/plot_top_countries.png")
plt.show()
