# 🚀 Hugging Face ETL Pipeline

A production-ready ETL (Extract, Transform, Load) pipeline built in Python that extracts machine learning model metadata from the Hugging Face API, transforms the data using Pandas, and loads it into CSV and SQLite formats for analysis.

---

## 📌 Project Overview

This project demonstrates a complete ETL workflow following software engineering best practices.

The pipeline:

* Extracts model metadata from the Hugging Face API
* Cleans and transforms the raw data
* Stores processed data as CSV
* Loads data into a SQLite database
* Generates detailed logs for monitoring
* Uses a modular project structure for maintainability

This project simulates a real-world data engineering pipeline and highlights API integration, data processing, database loading, logging, configuration management, and automation.

---

## 🛠 Tech Stack

* Python 3
* Pandas
* Requests
* SQLite3
* JSON
* Logging
* Git & GitHub

---

## 📂 Project Structure

```
HuggingFace_ETL_Pipeline/
│
├── data/
│   ├── raw_models.json
│   └── cleaned_models.csv
│
├── database/
│   └── huggingface.db
│
├── logs/
│   └── pipeline.log
│
├── scripts/
│   ├── config.py
│   ├── logger.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ ETL Workflow

### 1️⃣ Extract

* Connects to the Hugging Face REST API
* Downloads metadata for machine learning models
* Stores the raw JSON response

### 2️⃣ Transform

* Selects required columns
* Handles missing values
* Converts data into a Pandas DataFrame
* Creates an `is_popular` flag based on download count
* Sorts models by downloads

### 3️⃣ Load

* Exports transformed data to CSV
* Loads the dataset into SQLite
* Creates the `huggingface_models` table
* Enables SQL-based analysis

---

## 📊 Dataset

The pipeline collects information such as:

* Model Name
* Downloads
* Likes
* Pipeline Tag
* Last Modified
* Popularity Flag

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/misingh27/HuggingFace_ETL_Pipeline.git
cd HuggingFace_ETL_Pipeline
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate it

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute the Pipeline

```bash
python scripts/main.py
```

---

## 📁 Output Files

After execution, the pipeline generates:

```
data/raw_models.json
data/cleaned_models.csv
database/huggingface.db
logs/pipeline.log
```

---

## 📈 Sample SQL Query

```sql
SELECT model_name,
       downloads
FROM huggingface_models
ORDER BY downloads DESC
LIMIT 10;
```

---

## ✨ Features

* Modular ETL architecture
* Configuration management
* Centralized logging
* Exception handling
* SQLite integration
* CSV export
* API integration
* Reusable code structure
* Easy to extend and maintain

---

## 🚀 Future Enhancements

* Incremental data loading
* API pagination support
* Docker containerization
* Airflow orchestration
* Scheduling using Cron
* Unit testing with PyTest
* Environment variable support using `.env`
* Cloud database integration
* CI/CD using GitHub Actions

---

## 📚 Skills Demonstrated

* Data Engineering
* ETL Development
* Python Programming
* REST API Integration
* Data Transformation
* Pandas
* SQL
* SQLite
* Logging
* Software Engineering Best Practices
* Git & GitHub

---

## 👩‍💻 Author

**Mitali Singh**

GitHub: https://github.com/misingh27

LinkedIn: *(Add your LinkedIn profile URL here)*

---

## ⭐ If you found this project useful, consider giving it a star!
