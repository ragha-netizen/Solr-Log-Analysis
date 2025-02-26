# solr_log_analysis.py

import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Log File Path
log_file = "logs/solr_query_logs.txt"

# Read and Parse Log File
log_entries = []
with open(log_file, "r") as file:
    for line in file:
        match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}), INFO Query: q=(.*)&rows=\d+&start=\d+, Response Time: (\d+)ms', line)
        if match:
            log_entries.append([match.group(1), match.group(2), int(match.group(3))])

# Create DataFrame
df = pd.DataFrame(log_entries, columns=["Timestamp", "Query", "ResponseTime"])

# Convert Timestamp to Datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df.set_index("Timestamp", inplace=True)

# Display the first few rows
print(df.head())

# Find top 10 slowest queries
slow_queries = df.sort_values(by="ResponseTime", ascending=False).head(10)
print("\n🔹 Slowest Queries:")
print(slow_queries)

# Count most frequent queries
query_counts = df["Query"].value_counts().head(10)
print("\n🔹 Most Frequent Queries:")
print(query_counts)

# Response Time Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df["ResponseTime"], bins=20, kde=True)
plt.title("Query Response Time Distribution")
plt.xlabel("Response Time (ms)")
plt.ylabel("Frequency")
plt.savefig("visuals/response_time_distribution.png")
plt.show()

# Query Performance Over Time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x=df.index, y="ResponseTime")
plt.title("Query Response Time Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Response Time (ms)")
plt.xticks(rotation=45)
plt.savefig("visuals/query_performance_over_time.png")
plt.show()

