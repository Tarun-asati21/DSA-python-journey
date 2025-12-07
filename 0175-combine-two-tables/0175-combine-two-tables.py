import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # left join used
    a = pd.merge(person, address, on="personId", how="left")
    return a[["firstName","lastName","city","state"]]