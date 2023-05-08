from GoogleNews import GoogleNews
import json

def get_news_links(keyword):
    googlenews = GoogleNews(lang='en', period = '3d', encode = 'utf-8')
    googlenews.search(keyword)
    results = googlenews.result()

    links = []
    for result in results:
        links.append(result['link'])

    return links
