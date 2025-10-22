import pandas as pd
import os

# === 1. Load raw data ===
RAW_PATH = os.path.join("data", "netflix_titles.csv")
df_raw = pd.read_csv(RAW_PATH)
print(f"🔢 Rows before cleaning: {len(df_raw)}")

# === 2. Standardize column names ===
df_raw.columns = df_raw.columns.str.strip().str.lower().str.replace(" ", "_")

# === 3. Drop duplicates ===
df = df_raw.drop_duplicates()

# === 4. Handle missing values ===
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['director'] = df['director'].fillna('N/A')
df['cast'] = df['cast'].fillna('N/A')

# Drop rows with missing 'title' or 'type'
df = df.dropna(subset=['title', 'type'])

# === 5. Convert date_added to datetime ===
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# === 6. Normalize genres (listed_in) ===
df['listed_in'] = df['listed_in'].str.replace(', ', '|')

# === 7. Extract year/month for SQL analysis ===
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

# === 8. Save cleaned data ===
CLEANED_PATH = os.path.join("data", "cleaned_netflix_data.csv")
df.to_csv(CLEANED_PATH, index=False)

# === 9. Log summary ===
print(f"✅ Data cleaning complete.")
print(f"🔢 Rows after cleaning: {len(df)}")
print(f"📁 Cleaned file saved to: {CLEANED_PATH}")
print(f"📋 Final columns: {df.columns.tolist()}")
