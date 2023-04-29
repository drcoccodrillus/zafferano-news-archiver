import time
import requests
import psycopg2
from bs4 import BeautifulSoup

#Database connection
conn = psycopg2.connect(user="postgres",
                        password="mysecretpassword",
                        host="172.16.0.2",
                        port="5432",
                        database="zafferano")

#Request session
session = requests.Session()

#---Il Cameo - Links
#Get all pages links and titles from "Il Cameo" section
cur = conn.cursor()
page_titles = []
page_urls = []
page_url = 'https://zafferano.news/il-cameo'
while True:
    response = session.get(page_url)
    print('Working on --> ' + str(response.url))
    print('Response: ' + str(response.status_code))

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    for article in articles:
        title = article.find('h2', class_='colordarkgreen').text.strip()
        link = article.find('a')['href']

        #---Database
        #Insert title and url of the article into the database
        cur.execute("INSERT INTO news (title, url) VALUES (%s, %s)", (title, f'https://zafferano.news{link}'))
        #---End Database

        page_urls.append(link)

    #---Paginator
    #Get next page link
    next_page = soup.find('a', class_='page-link colordarkgreen', string='»')
    if not next_page:
        break
    page_url = f'https://zafferano.news/il-cameo{next_page["href"]}'
    #---End Paginator

    time.sleep(2)

conn.commit()
cur.close()
#---End Il Cameo - Links

cur = conn.cursor()
#---Il Cameo - Content
#Get for each article the description and the content
for page_url in page_urls:
    response = session.get(f'https://zafferano.news{page_url}')
    soup = BeautifulSoup(response.content, 'html.parser')
    description = soup.find('div', class_='post-desccription').text.strip()
    content = soup.find('div', class_='post-content').text.strip()

    #---Database
    #Update description and content for each article
    cur.execute('UPDATE news SET description=%s, content=%s WHERE url=%s', (description, content, f'https://zafferano.news{page_url}'))
    #---End Database

    time.sleep(1)

conn.commit()
cur.close()

#Close database connection
conn.close()
#---End Il Cameo - Content
