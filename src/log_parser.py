import pandas as pd
import re

def parse_logs(file_path):
    log_entries = []
    with open(file_path, "r") as file:
        for line in file:
            match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}), INFO Query: q=(.*)&rows=\d+&start=\d+, Response Time: (\d+)ms', line)
            if match:
                log_entries.append([match.group(1), match.group(2), int(match.group(3))])

    df = pd.DataFrame(log_entries, columns=["Timestamp", "Query", "ResponseTime"])
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df.set_index("Timestamp", inplace=True)
    
    return df

