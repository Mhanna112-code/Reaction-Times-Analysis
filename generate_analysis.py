import duckdb
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1️⃣ File paths
#DATA_DIR = os.path.join(os.path.dirname(__file__), '/data')
#OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '/output')
#os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_DIR = 'output/'
csv_file = os.path.join('data/', 'drawings.csv')

# 2️⃣ Connect to DuckDB (in-memory)
con = duckdb.connect(database=':memory:')

# 3️⃣ Load CSV into DuckDB table
con.execute(f"""
CREATE TABLE drawings AS
SELECT *
FROM read_csv_auto('{csv_file}');
""")

# 4️⃣ Concept distribution
concept_distribution_query = """
SELECT
    concept,
    COUNT(*) AS drawing_count
FROM drawings
GROUP BY concept
ORDER BY drawing_count DESC;
"""
df_concept = con.execute(concept_distribution_query).fetchdf()
df_concept.to_csv(os.path.join(OUTPUT_DIR, 'concept_distribution.csv'), index=False)

# 5️⃣ Reaction time over trials
reaction_time_query = """
SELECT
    trial_index,
    AVG(rt) AS avg_reaction_time
FROM drawings
GROUP BY trial_index
ORDER BY trial_index;
"""
df_rt = con.execute(reaction_time_query).fetchdf()
df_rt.to_csv(os.path.join(OUTPUT_DIR, 'reaction_time_over_trials.csv'), index=False)

# 6️⃣ Plot Concept Distribution
plt.figure(figsize=(10,6))
plt.bar(df_concept['concept'].head(20), df_concept['drawing_count'].head(20))
plt.xticks(rotation=45, ha='right')
plt.ylabel('Drawing Count')
plt.title('Top 20 Concepts')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'concept_distribution.png'))
plt.close()

# 7️⃣ Plot Reaction Time over Trials
plt.figure(figsize=(10,6))
plt.plot(df_rt['trial_index'], df_rt['avg_reaction_time'], marker='o')
plt.xlabel('Trial Index')
plt.ylabel('Average Reaction Time (ms)')
plt.title('Reaction Time over Trials')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'reaction_time_over_trials.png'))
plt.close()

# 8️⃣ Close connection
con.close()

print("✅ CSVs and PNGs generated in the 'output' folder!")
