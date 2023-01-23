# from typing import Union
import pandas as pd
# from fastapi import FastAPI
from datetime import date
from pytrends.request import TrendReq


def extract():
    pytrend = TrendReq()
    df_google = pytrend.trending_searches().rename(columns={0:"results"})
    df_google.to_csv('dump/data_source.csv')
    print('Extract done')

def letter_count(**kwargs):
    today=date.today()
    dict = {}
    print('1')
    list_API = pd.read_csv(f"dump/{kwargs['file_name']}").loc[:,"results"].tolist()
    print('leido')
    str_API=''.join(list_API).lower()
    str_API=str_API.replace(" ","")
    print('modif')
    for i in str_API:
        dict[i] = str_API.count(i)
    df_final=pd.DataFrame.from_dict(dict, orient='index')
    print('dict a df')
    df_final=df_final.sort_index().rename(columns={0:'char_count'})
    print('df ordenado')
    df_final.to_csv(f"stagging/API_{kwargs['API_name']}/{today}_char_count.csv")
    print('df a stagging')