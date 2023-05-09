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
        print(w)
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
            
        

    return news_text


# websites = get_news_links('Ukraine')
# get_text_from_news(websites)