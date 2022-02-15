from kafka import KafkaProducer


##Method with optional settings prompt
def withOptionals():
    try:
        userMsg = input("Enter User name message: ") ##enter the sending message
        userMsgEncoded = str.encode(userMsg) ##Encode string into byte array
        producer = KafkaProducer(bootstrap_servers=["localhost:9093", "localhost:9094", "localhost:9095"]) ##create a producer with our brokers
        userChoice = input("Enter 1: Partition or 2: Key \n") ##choose which optional user wants
        if (int(userChoice) == 1):
            userPartition = input("Enter the partition: 0, 1, 2 \n") ##ask partition
            producer.send('Users', userMsgEncoded, partition=int(userPartition)) ##async call specifying the partition the message should go to
        if (int(userChoice) == 2):
            userKey = input("Enter the key: \n") ##ask for key
            userKeyEncoded = str.encode(userKey) ##convert into bytes
            producer.send('Users', userMsgEncoded, key=userKeyEncoded) ##async call specifying the key 
        print("Sent successfully!") ##success message
        producer.close() ##close the producer instance
    except:
        print("Exception occured during Sending") ##handling exception
        

##Method without any optional settings
def withoutOptionals():
    try:
        userMsg = input("Enter User name message: ") ##enter the sending message
        userMsgEncoded = str.encode(userMsg) ##Encode string into byte array
        producer = KafkaProducer(bootstrap_servers=["localhost:9093", "localhost:9094", "localhost:9095"]) ##create a producer with our brokers
        producer.send('Users',userMsgEncoded) ##async send call
        print("Sent successfully!") ##success message
        producer.close() ##close the producer instance
    except:
        print("Exception occured during Sending") ##handling exception


val = input("Do you want to enter a key/partition? Y or N \n")

##Start the method with optionals if user wants to input key/partition
if (val.lower() == "y"):
    withOptionals()

##Start method without any extra optionals
if (val.lower() == "n"):
    withoutOptionals()
