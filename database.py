import pandas as pd

def create_database_from_csv(uploaded_file, engine):
    df = pd.read_csv(uploaded_file)
    df.to_sql("data", engine, if_exists="replace", index=False)
