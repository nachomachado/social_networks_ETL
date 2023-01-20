

# pytrends = TrendReq(hl='en-US', tz=360)

# result = pytrends.trending_searches() 

# print(result.head()) 
from typing import Union
import pandas as pd
from fastapi import FastAPI
from pytrends.request import TrendReq



app = FastAPI()
pytrend = TrendReq()
df_google = pytrend.trending_searches()
df_google.to_csv('data_source.csv')
print('Estract done')