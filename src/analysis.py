def slow_queries(df, top_n=5):
    return df.sort_values(by="ResponseTime", ascending=False).head(top_n)

def frequent_queries(df, top_n=5):
    return df["Query"].value_counts().head(top_n)

