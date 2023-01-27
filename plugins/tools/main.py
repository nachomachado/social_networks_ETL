# from typing import Union
import pandas as pd
# from fastapi import FastAPI
from datetime import date, datetime
from pytrends.request import TrendReq
import requests


def extract_google():
    pytrend = TrendReq()
    df_google = pytrend.trending_searches().rename(columns={0:"results"})
    df_google.to_csv('dump/data_source_google.csv')
    print('Extract from google done')

def extract_spotify():
    TOKEN = "BQAo0801YoUTliSeXqeleYwRJC7eZtx3kuTN-HeAUSFa63ckvvNycyBI9GpZrQT4oEi3FBGDVNJy5O9ulH1RPPYUz7BiiB1IdtBbF725FLV8gAPnVh65TPUTcVpjpaPOUoVHT58We74u9KU1w3GXKtvtyTp2oK6fTRyapUNw0eCm7gSlbQ" 
    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }
    r = requests.get("https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF?fields=tracks.items(track(name))", headers = headers)
    data = r.json()
    song_names = []
    for song in data['tracks']['items']:
        song_names.append(song['track']['name'])
    df_spotify = pd.DataFrame(song_names)
    df_spotify.to_csv('dump/data_source_spotify.csv')



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