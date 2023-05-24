import pandas as pd                        
from trend_capturer import TrendCapturer
from news_capturer import get_news_links, get_text_from_news
from gpt_prompter import get_prediction_markets
import json
import streamlit as st

trendcapt = TrendCapturer()

raw_trends = trendcapt.main_searches()

list_of_trends = list(raw_trends['searches'])


trends = st.multiselect('Trend selector', raw_trends['searches'])

col1, col2, col3 = st.columns(3)
with col2:
    context = st.button('Need more context to decide')

if context:
    st.dataframe(trendcapt.main_searches_suggestions(raw_trends))

with col3:
    trigger = st.button('Generate Prediction Markets')

if trigger:
    trend_dict = {}
    progress_text = 'Processing the information and generating the PMs. Please wait'
    my_bar = st.progress(0, text=progress_text)
    percentage = 0
    for trend in trends:
        print(trend)
        news_links = get_news_links(trend)
        text = get_text_from_news(news_links)
        prediction_markets = get_prediction_markets(text)
        if prediction_markets[0] == '[':
            prediction_markets = json.loads(prediction_markets)
        trend_dict[trend] = prediction_markets
        operation_percentage = 1/len(trends)
        percentage += operation_percentage
        my_bar.progress(percentage, text=progress_text)
        # if len(prediction_markets)>1:
        #     for pm in prediction_markets:
        #         st.checkbox(str(pm))
        # else:
        #     st.checkbox(str(prediction_markets))

    

    st.write (trend_dict)

    save_file = open('prediction-markets.json', 'w')
    json.dump(trend_dict, save_file)
    save_file.close()

    # for pm in trend_dict:
    #     if json.dumps(pm):
    #         st.checkbox(pm)