from confluent_kafka import Consumer
import json
import ccloud_lib


if __name__ == '__main__':

    # Read arguments and configurations and initialize
    args = ccloud_lib.parse_args()
    config_file = args.config_file
    topic = args.topic
    conf = ccloud_lib.read_ccloud_config(config_file)

    group = input("Enter value for consumer group, or N\n") ##ask for user group id
    
    # Create Consumer instance
    # 'auto.offset.reset=earliest' to start reading from the beginning of the
    #   topic if no committed offsets exist
    consumer_conf = ccloud_lib.pop_schema_registry_params_from_config(conf)

    if (group.lower() == "n"):
        consumer_conf['group.id'] = 'test'
        consumer_conf['auto.offset.reset'] = 'earliest'
        consumer = Consumer(consumer_conf)
    else:
        consumer_conf['group.id'] = group
        consumer_conf['auto.offset.reset'] = 'earliest'
        consumer = Consumer(consumer_conf)

    # Subscribe to topic
    consumer.subscribe([topic])

    # Process messages
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            elif msg.error():
                print('error: {}'.format(msg.error()))
            else:
                # Check for Kafka message
                record_key = msg.key()
                record_value = msg.value()
                partition = msg.partition()
                print("Consumed record with key: ", record_key, " Value: ", record_value, " Partition: ", partition)
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()
