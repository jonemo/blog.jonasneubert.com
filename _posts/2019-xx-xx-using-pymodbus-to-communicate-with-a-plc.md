---
layout: post
title: "Using pymodbus to communicate with a PLC"
tags:
 - factorytech
 - plc
published: false
date: November TODO, 2019
---

*This post is part 4 of [a series]({{ site.url }}/2019/10/27/what-is-a-plc-and-how-do-i-talk-python-to-id).*


## Modbus: Two PLCs talking to each other


Modbus is a server/client protocol, i.e. unidirectional.[^1]


## pymodbus as Modbus client

```
pip install pymodbus
```

```python
from pymodbus.client.sync import ModbusTcpClient

PLC_IP = "192.168.1.9"

client = ModbusTcpClient(PLC_IP)
print(client.read_holding_registers(0, 12))
```

This outputs:

```
[500, 0, 300, 0, 100, 0, 300, 0, 700, 0, 50]
```

```python
# continued from above
client.write.registers(0, [10, 0])
print(client.read_holding_registers(0, 12))
```

This outputs:

```python
[10, 0, 300, 0, 100, 0, 300, 0, 700, 0, 50]
```

## pymodbus as Modbus server

```python

# TODO: copy and paste demose/pymodbus/server.py
```

The output updates with a new line added every time the PLC sends a new Modbus message.
In my on-stage demo I have the PLC program set up to publish a message whenever the traffic signal state changes.
With a little bit of Python formatting code, this results in output like this for each pedestrian crossing cycle:

```
# TODO stdout output of server example
```


---

###### Footnotes:

[^1]: The Modbus protocol specifications show how dated they are by still using the "master and slave" terminology of yesteryear.
