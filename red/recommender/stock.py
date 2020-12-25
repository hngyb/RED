def gold_cross(stock_name, stock_data, lst):
    temp = stock_data.iloc[-2, :]
    if (temp["ma5"] < temp["ma20"]) & (temp["ma5"] > temp["ma60"]) & (temp["ma5"] > temp["ma120"]):
        if (stock_data.iloc[-1, :]["ma5"] >= stock_data.iloc[-1, :]["ma20"]) & (
            stock_data.iloc[-1, :]["일수익률"] >= 2
        ):
            lst.append([stock_name, stock_data.iloc[-1, :]["close price"], "g"])


def r_sigma(stock_name, stock_data, lst):
    temp = stock_data.iloc[-2, :]
    if (temp["williams"] < -80) & (temp["sigma"] < -2) & (temp["ma20"] < temp["ma60"]):
        if stock_data.iloc[-1, :]["일수익률"] >= 2.5:
            lst.append([stock_name, stock_data.iloc[-1, :]["close price"], "r"])


def long_candle(stock_name, stock_data, lst):
    temp = stock_data.iloc[-1, :]
    cond1 = temp["close price"] > temp["pre_close_price"] * (1 + (5 / 100))
    cond2 = temp["high price"] > temp["low price"] * (1 + (5 / 100))
    cond3 = temp["amount"] > temp["amount_ma5"]

    if cond1 and cond2 and cond3:
        lst.append([stock_name, temp["close price"], "long_candle"])


def mfi_checker(stock_name, stock_data, lst):
    temp1 = stock_data.copy()
    temp2 = temp1.iloc[-2, :]

    if temp2["MFI"] <= 0.2:
        if temp1.iloc[-1, :]["MFI"] > 0.2:
            lst.append([stock_name, stock_data.iloc[-1, :]["close price"], "mfi"])


def rsi_sto_cross(stock_name, stock_data, lst):
    temp1 = stock_data.iloc[-1, :]
    temp2 = stock_data.iloc[-2, :]

    cond1 = temp2["fast_k"] < temp1["fast_k"]
    cond2 = temp1["fast_k"] > 20

    cond3 = temp2["fast_k"] < temp2["slow_d"]
    cond4 = temp1["fast_k"] > temp1["slow_d"]

    cond5 = temp2["rsi"] < 0.3

    if (cond1 and cond2) or (cond3 and cond4) or (cond5):
        lst.append([stock_name, temp1["close price"], "rsi_sto"])