from typing import Union
import pandas as pd
from fastapi import FastAPI
from pytrends.request import TrendReq


def estract():
    app = FastAPI()
    pytrend = TrendReq()
    df_google = pytrend.trending_searches()
    df_google.to_csv('dump/data_source.csv')
    print('Estract done')

# df = pd.read_csv("test.csv")
# @app.get("/")
# def read_root():
#     return {"Hello": "World!!!"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/df")
# def read_root():
#     return {"Sample de 5 registros": df.sample()}

# @app.get("/google/{item_id}")
# def read_root(item_id: str):
#     df_google = pytrend.trending_searches(pn = item_id)
#     return {"Sample de 5 registros": df_google.sample(5)}

# @app.get("/google")
# def read_root():
#     return {"Sample de 5 registros": df_google.sample()}