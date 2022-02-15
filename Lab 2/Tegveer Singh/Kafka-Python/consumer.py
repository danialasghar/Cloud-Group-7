import json
from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'topic',
        bootstrap_servers=['localhost:9093', 'localhost:9094', 'localhost:9095'],
        auto_offset_reset='earliest'
    )
    for message in consumer:
        print(json.loads(message.value))