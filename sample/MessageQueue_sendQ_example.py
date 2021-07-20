import pika

cred = pika.PlainCredentials('admin','1234')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='211.179.42.130',port=5672,credentials=cred)    )

channel = connection.channel()
channel.queue_declare(queue='sensor')

channel.basic_publish(exchange='',  routing_key='sensor', body='fucking hot')
 
connection.close()
