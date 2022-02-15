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

        const admin = kafka.admin();
        console.log("Connecting...")
        admin.connect()
        console.log("Connected!")

        // CreateTopics method returns a promise so await it
        await admin.createTopics({
            // A topic is a JSON object
            "topics": [{
                "topic": "topic",
                "numPartitions": 3
            }]
        })
        console.log("Topics created successfully")
        await admin.disconnect();

    } catch (ex) {
        console.log(`An Error occured ${ex}`)
    } finally {
        process.exit();
    }
}