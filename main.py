from src.log_parser import parse_logs
from src.analysis import slow_queries, frequent_queries
from src.visualize import plot_response_time_distribution, plot_query_performance_over_time

# Load and parse logs
log_file = "data/sample_logs.txt"
df = parse_logs(log_file)

# Analyze Logs
print("\n🔹 Slowest Queries:")
print(slow_queries(df))

print("\n🔹 Most Frequent Queries:")
print(frequent_queries(df))

# Visualizations
plot_response_time_distribution(df)
plot_query_performance_over_time(df)

