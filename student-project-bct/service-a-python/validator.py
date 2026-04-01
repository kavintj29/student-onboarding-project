import pandas as pd
import re
import os

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", str(email))

def validate_csv(file_path):
    df = pd.read_csv(file_path)

    valid_rows = []
    invalid_rows = []

    for _, row in df.iterrows():
        if pd.isna(row["age"]) or not is_valid_email(row["email"]):
            invalid_rows.append(row)
        else:
            valid_rows.append(row)

    valid_df = pd.DataFrame(valid_rows)
    invalid_df = pd.DataFrame(invalid_rows)

    # Create output folder if not exists
    os.makedirs("output", exist_ok=True)

    valid_df.to_csv("output/valid.csv", index=False)
    invalid_df.to_csv("output/invalid.csv", index=False)

    print(f"Valid records: {len(valid_df)}")
    print(f"Invalid records: {len(invalid_df)}")
    return valid_df.to_dict(orient="records"), invalid_df.to_dict(orient="records")