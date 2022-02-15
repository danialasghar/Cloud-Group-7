// Load the Kafka library from JavaScript into an object
const { Kafka } = require("kafkajs")

run();
async function run() {

    try {
        // Establish a TCP connection with the broker
        const kafka = new Kafka({
            "clientId": "myapp",
            "brokers": ["localhost:9093", "localhost:9094", "localhost:9095"]
        })

        const consumer = kafka.consumer({
            "groupId": "test"
        });
        console.log("Connecting...")
        await consumer.connect()
        console.log("Connected!")

        console.log("Subscribing to topic");
        await consumer.subscribe({
            "topic": "topic",
            "fromBeginning": true
        })

        await consumer.run({
            "eachMessage": async result => {
                console.log(`Received Message: ${result.message.value} on partition: ${result.partition}`)
            }
        })
    } catch (ex) {
        console.log(`An Error occured ${ex}`)
    } finally {

    }
}