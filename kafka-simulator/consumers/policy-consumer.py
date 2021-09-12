import json
import sys
from kafka import KafkaConsumer



KAFKA_TOPIC = "resultTopic"
KAFKA_BROKERS = "localhost:9092"

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=[KAFKA_BROKERS],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))

while True:
    try:
        for message in consumer:
            print(message.value)
    except KeyboardInterrupt:
        sys.exit()
