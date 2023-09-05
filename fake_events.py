import json
import random
from time import sleep
from tqdm import tqdm

from kafka import KafkaProducer
from kafka.errors import KafkaError

NUM_EVENTS = 500

input_topic_name = 'web_events'
localhost_bootstrap_server = 'localhost:19092'
producer = KafkaProducer(bootstrap_servers=[localhost_bootstrap_server])

# Add data to input topic
users = [
    {'user_id': 'a12', 'email': 'joe@mail.com'},
    {'user_id': 'a34', 'email': 'jane@mail.com'},
    {'user_id': 'a56', 'email': 'you@mail.com'},
    {'user_id': 'a78', 'email': 'the@mail.com'},
    {'user_id': 'a99', 'email': 'employee@bytewax.io'},
]
event_types = ['click', 'post', 'comment', 'login']
try:
    for _ in tqdm(range(NUM_EVENTS)):
        event = random.choice(users)
        event['type'] = random.choice(event_types)
        event_ = json.dumps(event).encode()
        producer.send(input_topic_name, value=event_)
        sleep(0.1)
    print(f'input topic "{input_topic_name}" populated successfully with {NUM_EVENTS} sample events')
except KafkaError:
    print('A kafka error occurred')
