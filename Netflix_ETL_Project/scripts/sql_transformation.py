import pandas as pd
import sqlite3
import os

# === 1. Load cleaned data ===
CLEANED_PATH = os.path.join("data", "cleaned_netflix_data.csv")
df = pd.read_csv(CLEANED_PATH)

# === 2. Create SQLite DB ===
conn = sqlite3.connect("data/netflix.db")
df.to_sql("netflix_titles", conn, if_exists="replace", index=False)
print("✅ Data loaded into SQLite")

# === 3. Run SQL Queries ===
cursor = conn.cursor()

# 🎬 Count of Movies vs TV Shows
cursor.execute("""
    SELECT type, COUNT(*) AS count
    FROM netflix_titles
    GROUP BY type
""")
print("\n🎬 Content Type Breakdown:")
for row in cursor.fetchall():
    print(row)

# 📅 Titles added per year
cursor.execute("""
    SELECT year_added, COUNT(*) AS count
    FROM netflix_titles
    WHERE year_added IS NOT NULL
    GROUP BY year_added
    ORDER BY year_added
""")
print("\n📅 Titles Added Per Year:")
for row in cursor.fetchall():
    print(row)

# 🌍 Top 10 Countries by Content
cursor.execute("""
    SELECT country, COUNT(*) AS count
    FROM netflix_titles
    WHERE country != 'Unknown'
    GROUP BY country
    ORDER BY count DESC
    LIMIT 10
""")
print("\n🌍 Top Countries by Content:")
for row in cursor.fetchall():
    print(row)

conn.close()
