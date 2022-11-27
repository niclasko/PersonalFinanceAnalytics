import numpy as np
import pandas as pd


class Calendar:
    def create(self, dates: pd.Series) -> pd.DataFrame:
        """Create a calendar dimension from a set of dates.

        Args:
            dates: A Pandas series of dates.

        Returns:
            A dataframe.
        """
        date_range = pd.date_range(start=dates.min(), end=dates.max())
        return pd.DataFrame(
            {
                "calendar_key": np.arange(len(date_range)),
                "date": pd.to_datetime(date_range.date),
                "dayname": date_range.day_name(),
                "day_number": date_range.day_of_week,
                "monthname": date_range.month_name(),
                "month_number": date_range.month,
                "year": date_range.year,
            }
        )
