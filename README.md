# Bytewax on Pulsar

To easily use Bytewax on Pulsar you can take advantage of the kafka protocol adaptor that comes with the standalone Pulsar package. Nothing needs to change for the Bytewax dataflow.

To get this running on your local machine, follow the commands below.

`pip install bytewax kafka-python`

`docker-compose up`

`python fake_events.py`

`python dataflow.py` 
