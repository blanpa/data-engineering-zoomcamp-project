import paho.mqtt.client as mqtt
import time

broker_address="localhost" 
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker

"""
berlin
    packaging
        line_1
        line_2
        line_3
    cnc
        line_1
        line_2
        line_3
"""
# Site/Area/line_/xxx
reset = "Command/Reset" 
start = "Command/Start"

berlin = [
    "berlin/packaging/line_1/",
    "berlin/packaging/line_2/",
    "berlin/packaging/line_3/",
    "berlin/cnc/line_1/",
    "berlin/cnc/line_2/",
    "berlin/cnc/line_3/",
]
for i in berlin:
    topic_reset = str(i)+str(reset)
    print(topic_reset)
    client.publish(topic_reset,"1")#publish
    time.sleep(1)
    topic_start = str(i)+str(start)
    print(topic_start)
    client.publish(topic_start,"1")#publish
    time.sleep(1)