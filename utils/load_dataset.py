from datasets import load_dataset
import pandas as pd
import numpy as np

def load_huggingface_dataset(name: str) -> pd.DataFrame:
    print(f"Loading {name} ...")
    raw = load_dataset(name)
    print(raw)

    # Use the test split for evaluation; fall back to train if test is absent
    split = "test" if "test" in raw else list(raw.keys())[0]
    df = raw[split].to_pandas()

    print(f"\nUsing split : '{split}'")
    print(f"Rows        : {len(df):,}")
    print(f"Columns     : {df.columns.tolist()}")
    df.head(3)
    return df