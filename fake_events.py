import json
import random
import socket
import time

from confluent_kafka import Producer
from tqdm import tqdm


NUM_EVENTS = 500
SLEEP_BETWEEN_MESSAGES = 0.01

# Add data to input topic
users = [
    {'user_id': 'a12', 'email': 'joe@mail.com'},
    {'user_id': 'a34', 'email': 'jane@mail.com'},
    {'user_id': 'a56', 'email': 'you@mail.com'},
    {'user_id': 'a78', 'email': 'the@mail.com'},
    {'user_id': 'a99', 'email': 'employee@bytewax.io'},
]
event_types = ['click', 'post', 'comment', 'login']

# setup producer, see
# https://docs.confluent.io/kafka-clients/python/current/overview.html
TOPIC = 'web_events'
BROKER = 'localhost:19092'
conf = {
    'bootstrap.servers': BROKER,
    'client.id': socket.gethostname(),
}
producer = Producer(conf)


if __name__ == '__main__':
    for msg_id in tqdm(range(NUM_EVENTS)):
        event = random.choice(users)
        event['msg_id'] = msg_id
        event['type'] = random.choice(event_types)
        producer.produce(
            TOPIC,
            value=json.dumps(event).encode(),
        )
        time.sleep(SLEEP_BETWEEN_MESSAGES)
