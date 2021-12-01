# ping-pong
Simple server for checking http transport. It can be useful when debugging a network or infrastructure by type:
```
(client) --> [cloud_application_load_balance] --> [cloud_vpc]
```
### Run
```
lomaha@ping-pong % python3 main.py -a=127.0.0.1 -p=9090
```
### Use
#### Client side:
```
lomaha@home-test % curl -G http://localhost:9090/ping
pong
```
#### Server side:
```
Server started http://127.0.0.1:9090
127.0.0.1 - - [01/Dec/2021 12:10:11] "GET /ping HTTP/1.1" 200 -
Request headers:
Host: localhost:9090
User-Agent: curl/7.64.1
Accept: */*
```
