from kafka import KafkaConsumer

group = raw_input("Enter value for consumer group, or N \n") 

if (group.lower() == "n"): \
    consumer = KafkaConsumer('Shayan', bootstrap_servers=["localhost:9093", "localhost:9094", "localhost:9095"]) 
else:
    consumer = KafkaConsumer('Shayan', group_id=group, bootstrap_servers=["localhost:9093", "localhost:9094", "localhost:9095"]) 
for message in consumer:
  
    print ("Topic= %s Partition=%d Offset=%d Key=%s Value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

consumer.close()