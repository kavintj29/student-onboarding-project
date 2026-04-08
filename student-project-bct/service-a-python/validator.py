import pandas as pd
import re
import os

def validate_csv(file_path):
    df = pd.read_csv(file_path)

    valid = []
    invalid = []

    for _, row in df.iterrows():
        email = str(row.get("email", ""))
        age = row.get("age")

      #check the data
        if pd.isna(age) or not re.match(r".+@.+\..+", email):
            invalid.append(row)
        else:
            valid.append(row)

    # dataframe (converation of valid and in valid data into dataframe)
    valid_df = pd.DataFrame(valid)
    invalid_df = pd.DataFrame(invalid)

    # create folder (os lib is used to create a folder)
    os.makedirs("output", exist_ok=True)

    # save files(dataframe is save into csv )
    valid_df.to_csv("output/valid.csv", index=False)
    invalid_df.to_csv("output/invalid.csv", index=False)

    return valid_df.to_dict(orient="records"), invalid_df.to_dict(orient="records")