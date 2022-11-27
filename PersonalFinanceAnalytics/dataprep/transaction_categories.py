import numpy as np
import pandas as pd


class TransactionCategories:
    def create(self, text: pd.Series) -> pd.DataFrame:
        """Create a transaction category dimension dataframe.

        Args:
            text: A Pandas series of transaction text.

        Returns:
            A dataframe.
        """
        text = pd.Series(text.unique())
        return pd.DataFrame(
            {
                "category_key": np.arange(len(text)),
                "text": text,
                "category": self._categorise(text=text),
            }
        )

    def _categorise(self, text: pd.Series) -> pd.Series:
        """Categorise transaction text.

        Args:
            text: A Pandas series of transaction text.

        Returns:
            A Pandas series of categories.
        """
        text_lower = text.str.lower()
        category = pd.Series(np.repeat("Other", len(text_lower)))
        category[text_lower.str.contains("rema|kiwi|meny|joker|coop")] = "Groceries"
        category[text_lower.str.contains("ruter")] = "Public transport"
        category[text_lower.str.contains("vipps\\*4service facilit")] = "Work lunch"
        category[text_lower.str.contains("pizza")] = "Pizza takeaway"
        category[text_lower.str.contains("(mcdonald|mcd )")] = "McDonalds"
        category[text_lower.str.contains("treffen")] = "Treffen"
        category[text_lower.str.contains("kaffe|stockfleth|steam|fransken|starbucks")] = "Kaffe"
        category[text_lower.str.contains("overf\\.")] = "Transfer"
        category[text_lower.str.contains("paypal")] = "Paypal"
        category[text_lower.str.contains("apple")] = "Apple"
        return category
