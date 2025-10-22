## 🎬 Netflix ETL Pipeline — End-to-End Data Engineering Project

A full-stack ETL pipeline built for Netflix content metadata, showcasing your expertise in environment isolation, data profiling, PySpark transformations, and visual storytelling.

---

### 🧱 1. Environment Setup with CMD + `venv`

You created a **virtual environment using CMD scripting**, ensuring:
- 🔒 **Dependency isolation** for reproducibility
- ⚙️ Easy activation via `Scripts/activate` for Windows
- 📦 Controlled installation of packages via `requirements.txt`

This guarantees that anyone cloning your repo can replicate the exact setup without dependency conflicts.

---

### 📥 2. Data Ingestion & Profiling

- Downloaded raw Netflix metadata as `.csv`
- Used a **profiling script** to:
  - Count broken rows
  - Identify missing values
  - Flag anomalies in date, country, and category fields

This step ensures data quality before transformation begins.

---

### 🔄 3. Transformation with PySpark

- Implemented a **PySpark-based transformation script** to:
  - Normalize country names
  - Parse and standardize date formats
  - Handle nulls and duplicates efficiently

Using PySpark adds scalability and parallelism, ideal for larger datasets or future cloud migration.

---

### 📊 4. Visualization with Matplotlib

- Activated the virtual environment
- Used **Matplotlib** (and optionally Seaborn) to create:
  - Content distribution charts
  - Genre breakdowns
  - Time-series trends of releases

These visuals make the data insights recruiter-friendly and presentation-ready.

---

### 🧠 Bonus: Modular Structure

 repo includes:
- `data/` for raw and cleaned files
- `scripts/` for each ETL stage
- `sql/` for optional SQL transformations
- `notebooks/` for exploratory analysis
- `README.md` for documentation

