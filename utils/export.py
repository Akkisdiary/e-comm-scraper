import os
from datetime import datetime

import pandas as pd


PROJECT_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def add_csv_extension(file_path: str):
    base, ext = os.path.splitext(file_path)
    
    if ext.lower() == '.csv':
        return file_path
    
    return f"{base}.csv"


def to_csv(data, file_name: str = None, verbose: bool = True):
    if file_name is None:
        file_name = datetime.now().isoformat(timespec='seconds')

    abs_file_path = os.path.join(PROJECT_BASE, file_name)
    file_path = add_csv_extension(abs_file_path)

    if verbose:
        print(f"Exporting to file: {file_path}")

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
