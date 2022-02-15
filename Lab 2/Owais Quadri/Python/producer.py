from sys import argv
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=["localhost:9093","localhost:9094","localhost:9095"])
topic="Usernames"
message=argv[1]

if message[0] > 'N':
    producer.send(topic,bytearray(message.encode()),partition=1)
    print("Message sent to partition 1")
else:
    producer.send(topic,bytearray(message.encode()),partition=0)
    print("Message sent to partition 0")
