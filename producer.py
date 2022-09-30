import reactivex as rx
import reactivex.operators as ops
import time
import json
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'kafka'})

rx.interval(1).pipe(
  ops.map(lambda index: f'rx,tag=me index={index} {time.time_ns()}')
).subscribe(lambda message: producer.produce(topic='my-topic-1', value=message))

time.sleep(15)
