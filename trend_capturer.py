import pandas as pd                        
from pytrends.request import TrendReq
from deep_translator import GoogleTranslator


class TrendCapturer:
    pytrend = TrendReq()
    def __init__(self, countries=None):
        '''
        countries       list
                        a list of countries.
        '''
        if countries != None:
            self.countries = [x.lower() for x in countries]
        else:
            self.countries = ['united_states']

    def translate_string(self, text, target = 'en', source='auto'):
        translated = GoogleTranslator(source = source, target = target).translate(text)
        return translated

    def main_searches(self, target = 'en', source = 'auto'):
        searches = pd.DataFrame([])
        for country in self.countries:
            df = TrendCapturer.pytrend.trending_searches(pn=country)
            df['country'] = country
            searches = pd.concat([searches, df], ignore_index=True)

        searches.reset_index(inplace=True)
        searches.columns = ['old_index', 'searches', 'country']        
        searches['searches'] = searches['searches'].apply(lambda x: self.translate_string(x, target))
        searches = searches.drop(columns = 'old_index')
        
        return searches

    def searches_grouped(self, main_searches_df, more_than = 1):
        searches_grouped = main_searches_df.groupby('searches').size().reset_index(name='counts').sort_values('counts', ascending=False)
        return searches_grouped[searches_grouped['counts']>more_than]

    def main_searches_suggestions(self, main_searches_df):
        main_searches_suggestions = pd.DataFrame([]) 
        for row in range(len(main_searches_df)):
            try:
                keywords = TrendCapturer.pytrend.suggestions(keyword= main_searches_df['searches'][row])
                temp = pd.DataFrame(keywords)
                temp = temp.drop(columns= 'mid')   # This column makes no sense
                temp['country'] = main_searches_df['country'][row]
            except:
                temp = pd.DataFrame(main_searches_df.iloc[row, :]).T
                temp.columns = ['title', 'country']
            main_searches_suggestions = pd.concat([main_searches_suggestions, temp], ignore_index=True)

        return main_searches_suggestions

    def grouped_main_searches_suggestions(self, suggestions_df, more_than = 1):
        grouped_searches_suggestions = suggestions_df.groupby(['title', 'type'])['country'].size().reset_index(name='counts').sort_values('counts', ascending=False)
        return grouped_searches_suggestions[grouped_searches_suggestions['counts']>more_than]