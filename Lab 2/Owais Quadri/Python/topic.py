from kafka.admin import KafkaAdminClient, NewTopic
topic="Usernames"
admin=KafkaAdminClient(
    bootstrap_servers=["localhost:9093","localhost:9094","localhost:9095"],
    client_id='myapp'
)
print("Creating Topic ",topic)
topic_list = [NewTopic(name=topic, num_partitions=2, replication_factor=2)]
admin.create_topics(new_topics=topic_list, validate_only=False)
print("Topic '",topic,"' Created.")