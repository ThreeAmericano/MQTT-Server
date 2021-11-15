# REST 방식으로 MQTT 정보 가져오기
RabbitMQ 서버에 직접 접속하지않고, 인터넷 관리 페이지를 통하여 접근하는 방식. (POST)  
RabbitMQ REST Doc : https://pulse.mozilla.org/api/index.html  

<br/>

### 기대응답 예시

test321 큐에 있는 메세지 2개를 확인한 모습. (내용1 : direct messsssssssage, 내용2 : messageeeeeee)  
```sh
 $ python3 MQTT_rest_test.py
Response :[{"payload_bytes":21,"redelivered":true,"exchange":"","routing_key":"test321","message_count":1,"properties":[],"payload":"direct messsssssssage","payload_encoding":"string"},{"payload_bytes":13,"redelivered":true,"exchange":"","routing_key":"test321","message_count":0,"properties":[],"payload":"messageeeeeee","payload_encoding":"string"}]
```

<br/>

# 예제

## Linux CURL 예제

```sh
curl -i -X POST http://rabbit:MQ321@<<SERVER IP>>:<<SERVER PORT>>/api/queues/%2f/test321/get  -H "Content-Type: application/json" -d '{"count":5,"requeue":true,"encoding":"auto","truncate":50000,"ackmode":"ack_requeue_true"}'
```

<br/>

## Python3 Request 예제

```python
  1 # importing the requests library
  2 import requests
  3
  4 # defining the api-endpoint
  5 API_ENDPOINT = "http://<<SERVER IP>>:<<SERVER PORT>>/api/queues/%2f/test321/get"
  6
  7 headers = {'content-type': 'application/json'}
  8 # data to be sent to api
  9 pdata = {'count':'5','requeue':'true','encoding':'auto','truncate':'50000','    ackmode':'ack_requeue_true'}
 10
 11 # sending post request and saving response as response object
 12 r = requests.post(url = API_ENDPOINT ,auth=('rabbit', 'MQ321'), json = pdata    , headers=headers)
 13
 14 # extracting response text
 15 pastebin_url = r.text
 16 print("Response :%s"%pastebin_url)
 17
```

<br/>

## HTML/JS 예제

```html
<!DOCTYPE html>
<html>
<body>
<h2>RabbitMQ REST API - Get Queue Message</h2>

URL/API Call: <input type="text" id="theurl" value="http://<<SERVER IP>>:<<SERVER PORT>>/api/queues/%2f/"  size = "50" /> <br><br>
Queue Name:   <input type="text" id="qname" value="test321"/> <br><br>
Requeue: <input type="text" id="rq" value="true" /> (false = remove old values)<br><br>
Message Count: <input type="text" id="mcount" value="5"/> <br><br>
<button type="button" onclick="sendoutput()">Get Message(s)</button>
<br>

<hr>
<p id="demo"></p>

<script>
function sendoutput() {
	// RabbitMQ username and password
	var username = "rabbit";
	var password = "MQ321";
	var xhttp = new XMLHttpRequest();
	
    var fullurl = document.getElementById("theurl").value + document.getElementById("qname").value + "/get";
	
	xhttp.open("POST", fullurl, true,username,password);
	
	// change to your Auth username and password

	xhttp.setRequestHeader("Content-Type","application/jsonp");

	var rq = document.getElementById("rq").value;
	var mcount = document.getElementById("mcount").value;
	var params = JSON.stringify({"count":mcount,"requeue":rq,"encoding":"auto","truncate":"50000","ackmode":"ack_requeue_true"});
	// Define a handler function when the response comes back
	xhttp.onreadystatechange = function() {
		// Get the response and put on it the screen
		if (this.readyState == 4 ) {	
			document.getElementById("demo").innerHTML = "Result=" +xhttp.responseText;
		}
	}

	xhttp.send(params);
}

</script>
</body>
</html>
```

<br/>
