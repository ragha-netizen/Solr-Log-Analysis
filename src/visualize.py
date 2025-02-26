import matplotlib.pyplot as plt
import seaborn as sns

def plot_response_time_distribution(df):
    plt.figure(figsize=(10, 5))
    sns.histplot(df["ResponseTime"], bins=20, kde=True)
    plt.title("Query Response Time Distribution")
    plt.xlabel("Response Time (ms)")
    plt.ylabel("Frequency")
    plt.show()

def plot_query_performance_over_time(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x=df.index, y="ResponseTime")
    plt.title("Query Response Time Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Response Time (ms)")
    plt.xticks(rotation=45)
    plt.show()

