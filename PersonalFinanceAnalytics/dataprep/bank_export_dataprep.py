import os
from datetime import datetime
from pathlib import Path
from typing import Iterator

import pandas as pd

HEADERS = {
    "transaction_date": datetime,
    "interest_date": datetime,
    "text": str,
    "amount": float,
    "balance": float,
}


class BankExportDataprep:
    def prepare_data(self, data_path: str) -> pd.DataFrame:
        """Prepare a dataframe of bank transactions from exported bank transaction files.

        Args:
            data_path: Path to a directory of exported transaction files.

        Returns:
            A dataframe.
        """
        return pd.concat(list(self._prepare_data(data_path=data_path)))

    def _prepare_data(self, data_path: str) -> Iterator[pd.DataFrame]:
        """Prepare dataframes of bank transactions from exported bank transaction files.

        Args:
            data_path: Path to a directory of exported transaction files.

        Returns:
            An Iterator of dataframes.
        """
        for filename in os.listdir(path=data_path):
            yield pd.read_excel(
                Path(data_path, filename),
                header=None,
                names=list(HEADERS.keys()),
                dtype=HEADERS,
                engine="openpyxl",
            ).assign(source=filename)
