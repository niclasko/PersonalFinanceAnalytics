import sys

sys.path.append("../")

from PersonalFinanceAnalytics.dataprep.bank_export_dataprep import BankExportDataprep
from PersonalFinanceAnalytics.dataprep.calendar import Calendar
from PersonalFinanceAnalytics.dataprep.transaction_categories import (
    TransactionCategories,
)

transactions = BankExportDataprep().prepare_data(data_path="../artefacts/data")
calendar = Calendar().create(dates=transactions["transaction_date"])
categories = TransactionCategories().create(text=transactions["text"])
transactions = transactions.merge(
    calendar[["date", "calendar_key"]], left_on="transaction_date", right_on="date", how="inner"
)
transactions = transactions.merge(
    categories[["text", "category_key"]], left_on="text", right_on="text", how="inner"
)
calendar.to_csv("../artefacts/exports/calendar.csv", index=False, header=True)
categories.to_csv("../artefacts/exports/categories.csv", index=False, header=True, sep=";")
transactions.to_csv("../artefacts/exports/transactions.csv", index=False, header=True)
