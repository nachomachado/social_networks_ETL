from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=360)

result = pytrends.trending_searches() 

print(result.head()) 