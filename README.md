# Reaction Times Analysis

This project analyzes a dataset of drawing trials and generates summary statistics and visualizations for:

* Concept distribution (number of drawings per concept)
* Average reaction time across trials

The analysis uses **DuckDB**, **Pandas**, and **Matplotlib** to process a CSV dataset and generate both **CSV outputs** and **PNG visualizations**.

---

**Files**

* `generate_analysis.py` – main script that runs the full analysis pipeline
* `data/drawings.csv` – dataset containing drawing trials
* `output/` – generated CSV summaries and visualization images

---

# Requirements

Install the required Python packages:

```
pip install duckdb pandas matplotlib
```


# Running the Analysis

Run the script:

```
python generate_analysis.py
```

The script will:

1. Load the `drawings.csv` dataset using DuckDB.
2. Compute the **concept distribution** (number of drawings per concept).
3. Compute the **average reaction time per trial index**.
4. Save the results as CSV files.
5. Generate visualization plots and save them as PNG images.

---

# Output Files

After running the script, the following files will be generated:

| File                              | Description                               |
| --------------------------------- | ----------------------------------------- |
| `concept_distribution.csv`        | Counts of drawings for each concept       |
| `reaction_time_over_trials.csv`   | Average reaction time by trial index      |
| `top_10_concept_distribution.png` | Bar chart of most common drawing concepts |
| `reaction_time_over_trials.png`   | Line chart showing reaction time trends   |

These files will appear in the `output/` directory.

---

# Example Visualizations

The script produces two plots:

**Concept Distribution**

Shows the most frequently drawn concepts.

**Reaction Time Over Trials**

Shows how average reaction time changes as trials progress.

---

# Reproducing the Results

To reproduce the results:

```
git clone https://github.com/<your-username>/Reaction-Times-Analysis.git
cd Reaction-Times-Analysis
pip install -r requirements.txt
python generate_analysis.py
```

The output CSV files and PNG visualizations will be generated automatically.

---

# Technologies Used

* DuckDB – fast analytical SQL queries on CSV data
* Pandas – data manipulation
* Matplotlib – data visualization
* Python – scripting and automation
