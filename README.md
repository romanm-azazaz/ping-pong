# ping-pong
Simple server for checking http transport. It can be useful when debugging a network or infrastructure by type:
```
(client) --> [cloud_application_load_balance] --> [cloud_instance]
```
### Run
```
lomaha@ping-pong % python3 main.py -a=0.0.0.0 -p=80
```
### Use
#### Client side:
```
lomaha@home-test % curl -G https://demo.example.io/ping
pong
```
#### Server side:
```
127.0.0.2 - - [01/Dec/2021 15:43:03] "GET /ping HTTP/1.1" 200 -
Request headers:
X-Forwarded-For: 127.0.0.1
X-Forwarded-Proto: https
X-Forwarded-Port: 443
Host: demo.example.io
X-Amzn-Trace-Id: Root=1-420-yc784y587yw9f58
user-agent: curl/7.64.1
accept: */*
```
