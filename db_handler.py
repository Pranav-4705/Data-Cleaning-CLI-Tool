import mysql.connector

def upload_to_mysql(df, table_name='cleaned_data'):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pranav123*"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS data_cleaner_db")
    cursor.execute("USE data_cleaner_db")

    # Create table if not exists
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY
    )
    """
    cursor.execute(create_table_query)

    # Add columns dynamically if not present
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    existing_columns = [col[0] for col in cursor.fetchall()]

    for col in df.columns:
        if col not in existing_columns:
            cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN `{col}` VARCHAR(255)")

    # Insert cleaned data
    for _, row in df.iterrows():
        placeholders = ', '.join(['%s'] * len(df.columns))
        columns = ', '.join(f"`{col}`" for col in df.columns)
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Data uploaded successfully to '{table_name}' in MySQL database 'data_cleaner_db'.")
