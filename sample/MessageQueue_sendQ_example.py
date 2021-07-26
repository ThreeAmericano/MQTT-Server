import pika

cred = pika.PlainCredentials('rabbit','MQ321') #MQTT계정 ID,PW를 차례로 입력
connection = pika.BlockingConnection(pika.ConnectionParameters(host='211.179.42.130',port=5672,credentials=cred)) #MQTT서버의 IP, Port를 입력

channel = connection.channel()
channel.queue_declare(queue='sensor') #사용할 토픽 입력

channel.basic_publish(exchange='',  routing_key='sensor', body='message example') #exchange, routing_key, body(message)를 차례로 입력
 
connection.close()
