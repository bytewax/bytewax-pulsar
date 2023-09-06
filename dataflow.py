import json
from json.decoder import JSONDecodeError

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
    try:
        key = json.loads(key_bytes) if key_bytes else None
    except JSONDecodeError:
        key = key_bytes
    try:
        payload = json.loads(payload_bytes) if payload_bytes else None
    except JSONDecodeError:
        payload = payload_bytes
    return key, payload


flow.map(deserialize)
flow.output('out', StdOutput())
