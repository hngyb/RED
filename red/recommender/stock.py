def gold_cross(stock_name, stock_data, lst):
    temp = stock_data.iloc[-2, :]
    s = abs(stock_data.iloc[1:-1, :]['std'].mean()) / stock_data.iloc[-1, :]["close price"]
    if (temp["ma5"] < temp["ma20"]) & (temp["ma5"] > temp["ma60"]) & (temp["ma5"] > temp["ma120"]):
        if (stock_data.iloc[-1, :]["ma5"] >= stock_data.iloc[-1, :]["ma20"]) & (
            stock_data.iloc[-1, :]["일수익률"] >= 2
        ):
            lst.append([stock_name, stock_data.iloc[-1, :]["close price"], 5,"g", 2.1,s])


def r_sigma(stock_name, stock_data, lst):
    temp = stock_data.iloc[-2, :]
    s = abs(stock_data.iloc[1:-1, :]['std'].mean()) / stock_data.iloc[-1, :]["close price"]
    if (temp["williams"] < -80) & (temp["sigma"] < -2) & (temp["ma20"] < temp["ma60"]):
        if stock_data.iloc[-1, :]["일수익률"] >= 2.5:
            lst.append([stock_name, stock_data.iloc[-1, :]["close price"], 40, "r", 1.95,s])


def long_candle(stock_name, stock_data, lst):
    temp = stock_data.iloc[-1, :]
    s = abs(stock_data.iloc[1:-1, :]['std'].mean()) / stock_data.iloc[-1, :]["close price"]
    cond1 = temp["close price"] > temp["pre_close_price"] * (1 + (5 / 100))
    cond2 = temp["high price"] > temp["low price"] * (1 + (5 / 100))
    cond3 = temp["amount"] > temp["amount_ma5"]

    if cond1 and cond2 and cond3:
        lst.append([stock_name, temp["close price"], 5, "long_candle", 2.16,s])


def mfi_checker(stock_name, stock_data, lst):
    temp = stock_data.iloc[-1, :]
    s = abs(stock_data.iloc[1:-1, :]['std'].mean()) / stock_data.iloc[-1, :]["close price"]
    if temp["MFI"] <= 0.2:
        lst.append([stock_name, stock_data.iloc[-1, :]["close price"], 40, "mfi", 1.65,s])


def rsi_sto_cross(stock_name, stock_data, lst):
    temp1 = stock_data.iloc[-1, :]
    temp2 = stock_data.iloc[-2, :]
    s = abs(stock_data.iloc[1:-1, :]['std'].mean()) / stock_data.iloc[-1, :]["close price"]
    cond1 = temp2["fast_k"] < temp1["fast_k"]
    cond2 = temp1["fast_k"] > 20

    cond3 = temp2["fast_k"] < temp2["slow_d"]
    cond4 = temp1["fast_k"] > temp1["slow_d"]

    cond5 = temp2["rsi"] < 0.3

    if (cond1 and cond2) or (cond3 and cond4) or (cond5):
        lst.append([stock_name, temp1["close price"], 20, "rsi_sto", 1.8,s] )