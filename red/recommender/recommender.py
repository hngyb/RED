from . import stock
from . import etf
import os
import pandas as pd


class Recommender:
    def __init__(self, path, stock_path, etf_path):
        self.path = path
        self.stock_path = stock_path
        self.etf_path = etf_path

    def rec_stock(self):
        recommend_lst = []
        print("추천 주식 종목 찾는 중...")
        for i in os.listdir(self.stock_path):
            stock_data = pd.read_csv(self.stock_path + "/" + i, encoding="cp949")
            stock_name = i[:-4]
            stock.gold_cross(stock_name, stock_data, recommend_lst)
            stock.r_sigma(stock_name, stock_data, recommend_lst)
            stock.long_candle(stock_name, stock_data, recommend_lst)
            stock.mfi_checker(stock_name, stock_data, recommend_lst)
            stock.rsi_sto_cross(stock_name, stock_data, recommend_lst)

        return recommend_lst

    def rec_etf(self):
        lst1 = []  # 채권 etf
        lst2 = []  # 그외 etf
        print("추천 ETF 찾는 중...")
        etfs = pd.read_csv(self.path + "/data/etf_list.csv", encoding="cp949")
        bonds = etfs[etfs["etfTabCode"] == "채권"]["itemname"].values

        for i in os.listdir(self.etf_path):
            etf_data = pd.read_csv(self.etf_path + "/" + i, encoding="cp949")
            etf.momentum(i, etf_data, lst1, lst2, bonds)

        lst1.sort(key=lambda x: x[1])
        lst2.sort(key=lambda x: x[1])
        lst1.sort(key=lambda x: x[2], reverse=True)
        lst2.sort(key=lambda x: x[2], reverse=True)
        return lst1[:20], lst2[:20]