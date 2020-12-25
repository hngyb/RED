import requests
import json
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup
import re


def get_etf_list():
    """'https://finance.naver.com/'에서 ETF 리스트를 스크래핑합니다.
    Returns: etf list를 dataframe으로 반환합니다.
    """
    # 네이버 금융 API로부터 ETF 데이터 갖고오기
    url = "https://finance.naver.com/api/sise/etfItemList.nhn"
    json_data = json.loads(requests.get(url).text)
    df = json_normalize(json_data["result"]["etfItemList"])

    # etf 데이터프레임 정제
    # etfTabCode = {1: 국내 시장지수, 4: 해외 주식, 6: 채권}
    etf_df = df[["itemcode", "etfTabCode", "itemname", "섹터"]]
    etf_df = etf_df[etf_df["etfTabCode"].isin([1, 4, 6])]

    etf_df["etfTabCode"].loc[etf_df["etfTabCode"] == 1] = "국내시장지수"
    etf_df["etfTabCode"].loc[etf_df["etfTabCode"] == 4] = "해외주식"
    etf_df["etfTabCode"].loc[etf_df["etfTabCode"] == 6] = "채권"
    return etf_df
