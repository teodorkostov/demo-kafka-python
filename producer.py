import reactivex as rx
import reactivex.operators as ops
import time
import json
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'broker'})

rx.interval(1).pipe(
  # ops.map(lambda index: {"name": str(index), "timestamp": int(1000 * time.time())})
  # ops.map(lambda index: f'rx,tag=me index={index} {int(1000 * time.time())}')
  ops.map(lambda index: f'rx,tag=me index={index}')
# ).subscribe(lambda message: producer.produce(topic='quickstart', value=json.dumps(message)))
).subscribe(lambda message: producer.produce(topic='quickstart', value=message))

time.sleep(15)
