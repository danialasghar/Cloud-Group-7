import time
import json
import random
from kafka import KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=['localhost:9093', 'localhost:9094', 'localhost:9095'],
    value_serializer=serializer
)

if __name__ == '__main__':
    while True:
        producer.send('topic', 'This is a random message')
        time.sleep(3)
