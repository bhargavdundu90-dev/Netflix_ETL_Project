# 🎬 Netflix ETL Pipeline Project

A full-stack data engineering pipeline that ingests, cleans, transforms, and visualizes Netflix content metadata using Python, SQLite, and Matplotlib. Built with a virtual environment (`venv`) for clean, reproducible setup.


------------------------------------------------------------------------------


## 🚀 Features

- 📥 Data ingestion and profiling
- 🧹 Cleaning and enrichment (date parsing, country normalization)
- 🧠 SQL-based transformations using SQLite
- 📊 Visualizations with Matplotlib and Seaborn
- 🧪 Isolated environment using Python `venv`
- 📁 Modular folder structure for scalability

------------------------------------------------------------------------------

## 🧪 Environment Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate # macOS/Linux
pip install -r requirements.txt
Netflix_ETL_Project/
├── data/                  # Raw, cleaned, and output files
├── scripts/               # Python scripts for each ETL stage
│   ├── profile_data.py
│   ├── scripts_data_cleaning.py
│   ├── sql_transformation.py
│   └── visualize_data.py
├── sql/                   # Optional: standalone .sql files
├── notebooks/             # Optional: Jupyter notebooks
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

------------------------------------------------------------------------------

📦 Tech Stack
Python (pandas, matplotlib, seaborn)

SQLite (local SQL transformations)

CMD scripting for reproducible setup

Optional: AWS Glue + Athena for cloud-scale querying

------------------------------------------------------------------------------
🧠 Future Enhancements
🎭 Genre breakdown and clustering

☁️ Cloud integration with AWS Glue + Athena

📈 Interactive dashboard with Plotly or Dash

📤 Public sharing via LinkedIn and GitHub optimization
