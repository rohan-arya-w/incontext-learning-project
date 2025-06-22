import pandas as pd
from sklearn.datasets import fetch_california_housing, load_iris
# src/preprocessor/preprocessor.py

def load_dataset(name):
    if name == "iris":
        from sklearn.datasets import load_iris
        return load_iris(as_frame=True).frame
    elif name == "california":
        from sklearn.datasets import fetch_california_housing
        return fetch_california_housing(as_frame=True).frame
    else:
        raise ValueError(f"Unsupported dataset: {name}")