import time

from kafka.consumer import KafkaConsumer

from card_parser import Parser


if __name__=="__main__":
    consumer = KafkaConsumer(bootstrap_servers='kafka:29092', api_version=(0, 11, 5))
    consumer.subscribe(['test'])
    print('aaaaa')
    for card in consumer:
        card = card.value.decode('UTF-8')
        card_parser = Parser(card)
        card_parsed = card_parser.get_current_card_parsed()
        with open('cards.txt', 'a') as file:
            print(card_parsed, file=file)
            print(card_parsed)