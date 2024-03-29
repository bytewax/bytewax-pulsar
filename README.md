# Bytewax on Pulsar PoC implementation

To easily use Bytewax on Pulsar you can take advantage of the kafka protocol adaptor that comes with the standalone Pulsar package. Nothing needs to change for the Bytewax dataflow.

To get this running on your local machine, follow the commands below.

Install the bytewax library with kafka connector (and tqdm for a simple progressbar for fake events generator):
```
pip install bytewax[kafka]==0.17 tqdm
```

Spin up the Apache Pulsar container
```
docker-compose up
```
the image size for Apache Pulsar container is around 2.5Gb

Produce some events
```
python fake_events.py
```

Run the dataflow
```
python -m bytewax.run dataflow:flow
```

If you didn't change anything in the `fake_events.py` you should see 500 lines similar to this:
```text
(None, {'user_id': 'a99', 'email': 'employee@bytewax.io', 'type': 'comment'})
(None, {'user_id': 'a12', 'email': 'joe@mail.com', 'type': 'click'})
(None, {'user_id': 'a99', 'email': 'employee@bytewax.io', 'type': 'post'})
(None, {'user_id': 'a12', 'email': 'joe@mail.com', 'type': 'click'})
...
```
