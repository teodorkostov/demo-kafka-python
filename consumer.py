from confluent_kafka import Consumer
import json
import time


c = Consumer({
  'bootstrap.servers': 'kafka',
  'group.id': 'mygroup',
  'auto.offset.reset': 'earliest'
})

c.subscribe(['my-topic-1'])


while True:
  msg = c.poll(1.0)

  if msg is None:
    continue
  if msg.error():
    print("Consumer error: {}".format(msg.error()))
    continue

  message: str = msg.value().decode('utf-8')
  value = message.split(sep=' ')[2]
  now = time.time_ns()
  lag = now - int(value)

  print('lag in ns: {}'.format(lag))


c.close()
