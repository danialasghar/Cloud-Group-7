from kafka import KafkaConsumer

group = input("Enter value for consumer group, or N \n") ##ask for user group id

if (group.lower() == "n"): ##no group id provided
    consumer = KafkaConsumer('Users', bootstrap_servers=["localhost:9093", "localhost:9094", "localhost:9095"]) ##create a consumer object with the kafka servers
else:
    consumer = KafkaConsumer('Users', group_id=group, bootstrap_servers=["localhost:9093", "localhost:9094", "localhost:9095"]) #create a consumer object with the specified group id
for message in consumer:
    # print message out
    print ("Topic= %s Partition=%d Offset=%d Key=%s Value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

consumer.close()