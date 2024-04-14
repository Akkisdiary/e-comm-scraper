import os
from datetime import datetime

import pandas as pd


PROJECT_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def to_csv(data, file_name: str = None):
    df = pd.DataFrame(data)

    if file_name is None:
        file_name = datetime.now().isoformat()

    abs_file_path = os.path.join(PROJECT_BASE, file_name)
    df.to_csv(abs_file_path, index=False)
