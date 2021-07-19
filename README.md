# MQTT-Server
RabbitMQ 서버측 코드

## 외부 접속 방법
- 관리페이지 링크 : http://211.179.42.130:15672/
- RabbitMQ ID : admin
- RabbitMQ PW : 1234

### 관리페이지에서 도착한 메세지 조회방법
<사진>

## 예제코드 (파이썬을 통한 메세지 송신)
파이썬으로 MQTT를 사용하기 위해서는 `python -m pip install pika --upgrade` 명령을 통해 pika 라이브러리를 다운받아 미리 준비해둬야합니다.
```python
  1 import pika
  2
  3 cred = pika.PlainCredentials('admin','1234')
  4 connection = pika.BlockingConnection(pika.ConnectionParameters(host='211.179.42.130',port=5672,credentials=cred)    )
  5
  6 channel = connection.channel()
  7 channel.queue_declare(queue='icecoffe')
  8
  9 channel.basic_publish(exchange='',  routing_key='icecoffe', body='fucking webos')
 10
 11 connection.close()
```

## 참고링크
 - RabbitMQ 공식사이트 : https://www.rabbitmq.com/
 - 서버 설치설명 : http://pont.ist/rabbit-mq/
 - 서버 설치공식 : https://www.rabbitmq.com/install-debian.html
 - 클라이언트 파이썬예제 한글번역 : https://blog.storyg.co/rabbitmqs/tutorials/python/01-hellowolrd
 - Python으로 메시지 생성, 소비하기 : https://smoh.tistory.com/289
 - RabbitMQ 시행착오 모음 : https://shortstories.gitbooks.io/studybook/content/message_queue_c815_b9ac/rabbitmq-c0bd-c9c8.html
 - 파이썬 pika.connection 인자값 설명 : https://pika.readthedocs.io/en/stable/modules/parameters.html
 - Ubuntu 에서 RabbitMQ 설치하기 : https://jonnung.dev/rabbitmq/2019/01/30/rabbitmq-installation-on-ubuntu/
 - RabbitMQ 설치 및 실행 간단예 : https://yoonwould.tistory.com/157
