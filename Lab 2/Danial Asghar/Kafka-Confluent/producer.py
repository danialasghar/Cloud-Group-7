from confluent_kafka import Producer, KafkaError
import json
import ccloud_lib


if __name__ == '__main__':

    # Read arguments and configurations and initialize
    args = ccloud_lib.parse_args()
    config_file = args.config_file
    topic = args.topic
    conf = ccloud_lib.read_ccloud_config(config_file)

    # Create Producer instance
    producer_conf = ccloud_lib.pop_schema_registry_params_from_config(conf)
    producer = Producer(producer_conf)

    ##Method with optional settings prompt
    def withOptionals():
        try:
            userMsg = input("Enter User name message:") ##enter the sending message
            userMsgEncoded = str.encode(userMsg) ##Encode string into byte array
            userChoice = input("Enter 1: Partition or 2: Key \n") ##choose which optional user wants
            if (int(userChoice) == 1):
                userPartition = input("Enter the partition: 0, 1, 2 \n") ##ask partition
                producer.produce('Users', userMsgEncoded, partition=int(userPartition)) ##async call specifying the partition the message should go to
            if (int(userChoice) == 2):
                userKey = input("Enter the key: \n") ##ask for key
                producer.produce('Users', userMsgEncoded, key=userKey) ##async call specifying the key 
            print("Sent successfully!") ##success message
            producer.flush()
        except:
            print("Exception occured during Sending") ##handling exception
            

    ##Method without any optional settings
    def withoutOptionals():
        try:
            userMsg = input("Enter User name message:") ##enter the sending message
            userMsgEncoded = str.encode(userMsg) ##Encode string into byte array
            producer.produce('Users',userMsgEncoded) ##async send call
            print("Sent successfully!") ##success message
            producer.flush()
        except:
            print("Exception occured during Sending") ##handling exception

    val = input("Do you want to enter a key/partition? Y or N\n")

    ##Start the method with optionals if user wants to input key/partition
    if (val.lower() == "y"):
        withOptionals()

    ##Start method without any extra optionals
    if (val.lower() == "n"):
        withoutOptionals()

    
   
