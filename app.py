import pandas as pd                        
from trend_capturer import TrendCapturer
from news_capturer import get_news_links, get_text_from_news
from gpt_prompter import get_prediction_markets
import json

trendcapt = TrendCapturer()

raw_trends = trendcapt.main_searches()

list_of_trends = list(raw_trends['searches'])
print(list_of_trends[0])

trend_dict = {}
for trend in list_of_trends[:1]:
    news_links = get_news_links(list_of_trends[0])
    text = get_text_from_news(news_links)
    prediction_markets = get_prediction_markets(text)
    trend_dict[trend] = prediction_markets


save_file = open('prediction-markets.json', 'w')
json.dump(trend_dict, save_file)
save_file.close()