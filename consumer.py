from confluent_kafka import Consumer
import json
import time


c = Consumer({
  # 'bootstrap.servers': 'lacalhost',
  'bootstrap.servers': '127.0.0.1',
  'group.id': 'mygroup',
  'auto.offset.reset': 'earliest'
})

c.subscribe(['quickstart'])


while True:
  msg = c.poll(1.0)

  if msg is None:
    continue
  if msg.error():
    print("Consumer error: {}".format(msg.error()))
    continue

  message = msg.value().decode('utf-8')
  # value = json.loads(message)
  # now = int(1000 * time.time())
  # lag = now - value['timestamp']

  print('lag: {}'.format(message))


c.close()
