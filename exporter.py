def export_csv(df, path):
    df.to_csv(path, index=False)
    print(f"✅ Cleaned data exported to {path}")
