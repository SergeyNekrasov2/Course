from math import ceil


def investment_bank(month: str, transactions: list[dict[str, any]], limit: int) -> float:
    cashback = 0
    for trans in transactions:
        for k,v in trans.items():
            if k[0:7] == month and v > 0:
                cashback += round((ceil(v/limit)) * limit - v, 2)
    return cashback
