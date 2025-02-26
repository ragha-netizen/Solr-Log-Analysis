import random
from datetime import datetime, timedelta

# Define queries and statuses
queries = ["product", "customer", "order", "transaction", "invoice", "database", "search", "error", "user", "analytics"]
statuses = [200, 200, 200, 200, 500]  # 80% success, 20% errors

# Start time for logs
start_time = datetime(2024, 2, 25, 12, 0, 0)

# Generate a large dataset of logs
log_entries = []
for i in range(5000):  # Generate 5000 log entries
    timestamp = start_time + timedelta(seconds=i * random.randint(1, 5))
    query = random.choice(queries)
    rows = random.randint(5, 50)
    response_time = random.randint(100, 1500)  # Response time in milliseconds
    status = random.choice(statuses)

    log_entry = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}, INFO Query: q={query}&rows={rows}&start=0, Response Time: {response_time}ms, Status: {status}"
    log_entries.append(log_entry)

# Save to file
with open("data/sample_large_logs.txt", "w") as file:
    file.write("\n".join(log_entries))

print("✅ Large sample log file created: data/sample_large_logs.txt")