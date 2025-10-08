def validate_data(df):
    assert 'email' in df.columns, "Email column missing!"
    assert df['age'].between(0, 120).all(), "Invalid ages found!"
    return True
