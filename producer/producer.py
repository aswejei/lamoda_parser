import time

from kafka.producer import KafkaProducer
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers='kafka:29092', api_version=(0, 11, 5))
    page = requests.get("https://www.lamoda.by/c/17/shoes-men/?sitelink=topmenuM&l=3")
    soup = BeautifulSoup(page.text, 'html.parser')
    cards = soup.find_all('div', 'x-product-card__card')
    cards = [card.text.replace('\n', '') for card in cards]
    for card in cards:
        print(card)
        producer.send('test', key=b'shoes', value=card.encode('UTF-8'))
        time.sleep(5)
        print('success')
