import pandas as pd                        
from trend_capturer import TrendCapturer
from news_capturer import get_news_links
from gpt_prompter import get_prediction_markets
import json

trendcapt = TrendCapturer()

raw_trends = trendcapt.main_searches()

list_of_trends = list(raw_trends['searches'])
print(list_of_trends[0])

trend_dict = {}
for trend in list_of_trends[:4]:
    news_links = get_news_links(list_of_trends[0])
    prediction_markets = get_prediction_markets(news_links)
    trend_dict[trend] = prediction_markets


save_file = open('prediction-markets.json', 'w')
json.dump(trend_dict, save_file, indent=1)
save_file.close()