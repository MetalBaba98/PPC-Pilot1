from newspaper import Article #pip3 install newspaper
import  nltk #pip3 install nltk
from bs4 import BeautifulSoup #pip3 install BeautifulSoup4
import urllib.request
import re
import csv #pip3 install csv
import time
from datetime import datetime
list = []

main_url = "https://timesofindia.indiatimes.com/sports/football/champions-league/champions-league-messis-barcelona-knock-manchester-united-out/articleshow/68915295.cms"

html_page = urllib.request.urlopen(main_url)
soup = BeautifulSoup(html_page)
links = []

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))

links.append(main_url)

print(links)

nltk.download('punkt')

for url in links:

    # For different language newspaper refer above table
    toi_article = Article(url, language="en")  # en for English

    # To download the article
    toi_article.download()

    # To parse the article
    toi_article.parse()

    # To perform natural language processing ie..nlp
    toi_article.nlp()

    # To extract title
    print("Article's Title:")
    title = toi_article.title
    print(title)
    print("n")

    # To extract keywords
    print("Article's Keywords:")
    key = toi_article.keywords
    print(key)

    if 'messi' in key:
        list.append((url,title,key))

    time.sleep(.75)


with open('../new.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    for url,title,key in list:
        writer.writerow(url,title,key)
