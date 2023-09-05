import json

from bytewax.dataflow import Dataflow
from bytewax.connectors.kafka import KafkaInput
from bytewax.connectors.stdio import StdOutput


flow = Dataflow()
flow.input(
    'aqi_state',
    KafkaInput(
        brokers=['localhost:19092'],
        topics=['web_events'],
    ),
)


# Deserialize input for processing
def deserialize(key_bytes__payload_bytes):
    key_bytes, payload_bytes = key_bytes__payload_bytes
    key = json.loads(key_bytes) if key_bytes else None
    sensor_data = json.loads(payload_bytes) if payload_bytes else None
    return key, sensor_data


flow.map(deserialize)
flow.output('out', StdOutput())
