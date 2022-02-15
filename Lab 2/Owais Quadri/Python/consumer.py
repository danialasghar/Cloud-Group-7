from kafka import KafkaConsumer
topic="Usernames"
consumer= KafkaConsumer(topic,bootstrap_servers=["localhost:9093","localhost:9094","localhost:9095"])

for message in consumer:
    print(message.value, " was send to partition ", message.partition)