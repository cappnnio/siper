MONGO_CONNECTION_STRING = 'mongodb://172.16.26.139:27017'
MONGO_DB_NAME = 'movies'
MONGO_CONNECTION_NAME = 'movies'

import pymongo
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s:%(message)s')
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'

url = 'https://spa1.scrape.center'
html = requests.get(url).text
print(html)

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies']
collection = db['movies']


def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


LIMIT = 10


def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)


DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'


def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)
    print(url)


TOTAL_PAGE = 10


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)
            sava_data(detail_data)
            logging.info('data save successfully')


if __name__ == '__main__':
    main()


def sava_data(data):
    collection.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    }, upsert=True)
