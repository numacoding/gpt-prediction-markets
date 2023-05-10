from GoogleNews import GoogleNews
import bs4
# from urllib.request import urlopen
import requests

def get_news_links(keyword):
    googlenews = GoogleNews(lang='en', period = '3d', encode = 'utf-8')
    googlenews.search(keyword)
    results = googlenews.result()

    links = []
    for result in results:
        links.append(result['link'])

    return links

def get_text_from_news(websites):
    news_text = ''
    for w in websites:
        try:
            response = requests.get(w)
            web_content = bs4.BeautifulSoup(response.content, 'html.parser')
            text = web_content.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            news_text += text
            news_text += '\n'
        except:
            print('Invalid URL')
        
    # sentences_to_delete = ['Manage Google autocomplete predictions - Android - Google Search Help', 'Skip to main content', 
    #     'Google Search HelpSign inGoogle HelpHelp CenterCommunityGoogle SearchPrivacy PolicyTerms of ServiceSubmit feedback Send feedback on',
    #     'This help content & information', 'General Help Center experience', 'NextHelp CenterCommunityAnnouncementsGoogle Search',
    #     'Manage Google autocomplete predictions', 'With autocomplete, you can enter a Google search more quickly. You can turn off or remove certain autocomplete predictions or report issues with your predictions.',
    #     'Learn more about autocomplete.', 'Turn off Personal results', 
    #     "Important: When Personal results are off, you won't get personalized predictions or recommendations based on your past searches. If you have Web & App Activity on, your Search history is saved in your Google Account and used to give you more personalized experiences in other Google services. Learn how to find & control your Web & App Activity.", 
    #     "If you’re signed in to your Google Account and have Personal results turned on, you might also get personalized predictions and recommendations in Google Search. If you don’t want to get these predictions and recommendations, turn off Personal results.", 'Turn off trending searches',
    #     "If you don’t want to get trending searches in the Google app, you can change your settings.", 
    #     "Important: When you turn off trending searches, it turns off in the Google app on that device. If you want to turn off trending searches on google.com, update your settings in a mobile browser.", 
    #     'To turn off trending searches:', 'On your Android phone or tablet, open the Google app', 'At the top right, tap your Profile picture or initial',
    #     'Turn off Autocomplete with trending searches.', 'Turn off trending searches from a mobile browser', 'On your Android phone or tablet, open a browser like Chrome']
    
    # for sentence in sentences_to_delete:
    #     news_text = news_text.replace(sentence, '')

    return news_text


# websites = get_news_links('Ukraine')
# get_text_from_news(websites)

