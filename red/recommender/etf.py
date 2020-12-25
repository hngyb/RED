def momentum(etf_name, etf_data, lst1, lst2, bonds):
    try:
        profit6 = round(
            (etf_data.iloc[-1, :]["close price"] - etf_data.iloc[-60, :]["close price"])
            / etf_data.iloc[-60, :]["close price"],
            2,
        )
        profit12 = round(
            (etf_data.iloc[-1, :]["close price"] - etf_data.iloc[-120, :]["close price"])
            / etf_data.iloc[-120, :]["close price"],
            2,
        )

        if etf_name[:-4] in bonds:
            lst1.append([etf_name[:-4], etf_data.iloc[-1, :]["close price"], (profit6 + profit12)])
        else:
            etf_data["slope1"] = (etf_data["ma20"] - etf_data["ma20"].shift(10)) / etf_data["ma20"]
            if (etf_data.iloc[-1, :]["slope1"] > 0.02) & (
                etf_data.iloc[-1, :]["ma20"] > etf_data.iloc[-1, :]["ma60"]
            ):  # 중기적으로 상향세일때
                lst2.append(
                    [etf_name[:-4], etf_data.iloc[-1, :]["close price"], (profit6 + profit12)]
                )

    except IndexError:
        return
