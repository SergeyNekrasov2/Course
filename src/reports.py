from datetime import datetime
from typing import Optional

import pandas as pd
from dateutil.relativedelta import relativedelta

from utils import xlsx_converting


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Function for filter transactions by category of spending"""
    last_day = pd.to_datetime(date, dayfirst=True) if date else datetime.today()
    first_day = last_day - relativedelta(months=3)
    transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"])
    filtered_trans_by_date = transactions[
        (transactions["Дата операции"] >= first_day) & (transactions["Дата операции"] <= last_day)
    ]
    filtered_trans_by_cat = filtered_trans_by_date[filtered_trans_by_date["Категория"] == category]
    return filtered_trans_by_cat


df = xlsx_converting("operations.xlsx")

print(spending_by_category(df, "Супермаркеты", "30.05.2020 14:10:18"))
