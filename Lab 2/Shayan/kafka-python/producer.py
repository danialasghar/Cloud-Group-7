from kafka import KafkaProducer



def withOptionals():
    try:
        userMsg = raw_input("Enter User name message: ")
        userMsgEncoded = str.encode(userMsg)
        producer = KafkaProducer(bootstrap_servers=["localhost:9093", "localhost:9094", "localhost:9095"]) ##create a producer with our brokers
        userChoice = raw_input("Enter 1: Partition or 2: Key \n") ##choose which optional user wants
        if (int(userChoice) == 1):
            userPartition = raw_input("Enter the partition: 0, 1, 2 \n") ##ask partition
            producer.send('Shayan', userMsgEncoded, partition=int(userPartition)) 
        if (int(userChoice) == 2):
            userKey = raw_input("Enter the key: \n") 
            userKeyEncoded = str.encode(userKey) 
            producer.send('Shayan', userMsgEncoded, key=userKeyEncoded)  
        print("Sent successfully!") ##success message
        producer.close() 
    except:
        print("Exception occured during Sending") ##exception
        
##no optional setting
def withoutOptionals():
    try:
        userMsg = raw_input("Enter User name message: ") 
        userMsgEncoded = str.encode(userMsg) 
        producer = KafkaProducer(bootstrap_servers=["localhost:9093", "localhost:9094", "localhost:9095"]) 
        producer.send('Shayan',userMsgEncoded) 
        print("Sent successfully!") 
        producer.close() 
    except:
        print("Exception occured during Sending") ##exception


val = raw_input("Do you want to enter a key/partition? Y or N \n")


if (val.lower() == "y"):
    withOptionals()

if (val.lower() == "n"):
    withoutOptionals()