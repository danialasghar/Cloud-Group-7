// Load the Kafka library from JavaScript into an object
const { Kafka } = require("kafkajs")
const msg = process.argv[2]; // Index 2 is the first argument

run();
async function run() {

    let partition = 0;
    if (msg[0] <= "O" && msg[0] >= "I") {
        partition = 1
        console.log(`Sending to partition ${partition} due to ${msg[0]}`);
    } else if (msg[0] <= "Z" && msg[0] >= "P") {
        partition = 2;
        console.log(`Sending to partition ${partition} due to ${msg[0]}`);
    } else {
        partition = 0;
        console.log(`Sending to partition ${partition} due to ${msg[0]}`);
    }

    try {
        // Establish a TCP connection with the broker
        const kafka = new Kafka({
            "clientId": "myapp",
            "brokers": ["localhost:9093", "localhost:9094", "localhost:9095"]
        })

        const producer = kafka.producer();
        console.log("Connecting...")
        await producer.connect()
        console.log("Connected!")

        const result = await producer.send({
            "topic": "topic",
            "messages": [
                {
                    "value": msg,
                    "partition": partition
                }
            ]
        })
        console.log(`Message ${JSON.stringify(result)} sent successfully`)
        await producer.disconnect();

    } catch (ex) {
        console.log(`An Error occured ${ex}`)
    } finally {
        process.exit();
    }
}