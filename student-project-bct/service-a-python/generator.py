import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_csv(file_name, rows=150):
    data = []

    for _ in range(rows):
        record = {
            "name": fake.name(),
            "email": fake.email() if random.random() > 0.2 else "invalid_email",
            "age": random.randint(18, 60) if random.random() > 0.1 else None,
            
        }
        data.append(record)

    df = pd.DataFrame(data)
    df.to_csv(f"data/{file_name}", index=False)

    print(f"{file_name} created")