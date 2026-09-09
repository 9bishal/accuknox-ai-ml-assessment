# Problem Statement 1 — Python, API, Database & Data Visualization

This section contains the implementation of the three tasks provided in
the AccuKnox AI/ML technical assessment.

## Tasks

### 1. API Data Retrieval and Storage

**File:** `01_api_to_sqlite.py`

The program retrieves book information from the Open Library REST API,
processes the JSON response, stores the relevant fields in a local
SQLite database, and displays the stored records.

#### Data Flow

REST API → JSON → Python → SQLite → SQL Query → Terminal Output

#### Fields Stored

- Book title
- Author
- Publication year

#### Assumption

Since the assessment did not specify a particular books API, the
Open Library public search API was selected.

---

### 2. Student Score Processing and Visualization

**File:** `02_student_scores.py`

The program retrieves student records from a public REST API, processes
the data, calculates the average test score, and generates a bar chart
using Matplotlib.

#### Data Flow

REST API → JSON → Student Data → Average Calculation → Matplotlib

#### Output

The generated visualization is saved as:

`student_scores.png`

#### Assumption

The assessment did not specify a particular student-score API.
Therefore, a publicly accessible API was used to retrieve student
records. Since the selected API does not provide examination scores,
representative scores were assigned to the retrieved records to
demonstrate the required score-processing and visualization workflow.

---

### 3. CSV Data Import to SQLite

**File:** `03_csv_to_sqlite.py`

The program reads user information from a CSV file, validates the
basic fields, inserts the records into a local SQLite database, and
displays the stored records.

#### Input

`../sample_data/users.csv` (resolved via `Path(__file__).parent` — works from any working directory)

#### Data Flow

CSV → Python CSV Reader → Validation → SQLite → SQL Query → Terminal Output

#### Fields Stored

- Name
- Email

---

## Technologies Used

- Python
- REST API
- JSON
- SQLite
- SQL
- CSV
- Matplotlib
- Requests

## How to Run

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Run the individual programs (from either repository root or `problem_statement_1/`):

```bash
# From repository root
python3 problem_statement_1/01_api_to_sqlite.py
python3 problem_statement_1/02_student_scores.py
python3 problem_statement_1/03_csv_to_sqlite.py

# Or from inside the folder
cd problem_statement_1
python3 01_api_to_sqlite.py
python3 02_student_scores.py
python3 03_csv_to_sqlite.py
```
Database

SQLite is used because it is lightweight, serverless, requires no
separate database setup, and is suitable for local data storage.

The programs create the following databases:

books.db
users.db

These databases are generated automatically when the programs are run.

## Error Handling

The implementations include basic error handling for:

- Failed API requests
- Empty API responses
- Missing data fields
- Empty CSV records
- Duplicate database records (`INSERT OR IGNORE` + `UNIQUE` constraints)
- Missing CSV file
- Path resolution via `pathlib.Path` for cwd-independent execution

## Author

Bishal Kumar Shah — see root `README.md` for portfolio links and resume.
```
