from kafka import KafkaAdminClient
from kafka.admin import NewTopic

try:
    admin = KafkaAdminClient(bootstrap_servers=['localhost:9093', 'localhost:9094', 'localhost:9095'])
    topic = NewTopic(name='Shayan', num_partitions=3, replication_factor=3)
    admin.create_topics([topic])
    print("Topic created") 
except:
    print("Already created")