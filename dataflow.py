import json

from bytewax.dataflow import Dataflow
from bytewax.execution import run_main
from bytewax.inputs import KafkaInputConfig
from bytewax.window import TumblingWindowConfig, EventClockConfig
from bytewax.outputs import StdOutputConfig

flow = Dataflow()
flow.input(
    "aqi_state", 
    KafkaInputConfig(
        brokers=["localhost:19092"], 
        topic="web_events",
        starting_offset = "beginning",
        tail = False
        )
    )

# Deserialize input for processing
def deserialize(key_bytes__payload_bytes):
    key_bytes, payload_bytes = key_bytes__payload_bytes
    key = json.loads(key_bytes) if key_bytes else None
    sensor_data = json.loads(payload_bytes) if payload_bytes else None
    return key, sensor_data

flow.map(deserialize)
flow.capture(StdOutputConfig())

if __name__ == '__main__':
    run_main(flow)