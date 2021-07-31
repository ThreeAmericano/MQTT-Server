#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 사용할 exchange 이름과 type(direct, topic, fanout ..)을 입력합니다.
channel.exchange_declare(exchange='test321', exchange_type='direct')

message = "info: Hello World!"
channel.basic_publish(exchange='test321', routing_key='amqtest', body=message)
print(" [x] Sent %r" % message)
connection.close()
