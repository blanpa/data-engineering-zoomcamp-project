import paho.mqtt.client as mqtt
import time

broker_address="localhost" 
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker

"""
berlin
    cnc
        line_1
        line_2
        line_3
        cnc_amb
    electronic_assembly
        line_1
        line_2
        line_3
        electronic_assembly_amb
    mechanical_assembly
        line_1
        line_2
        line_3
        mechanical_assembly_amb
    packaging
        line_1
        line_2
        line_3
        packaging_amb
    powergenerator
        cnc_pg
        electronic_assembly_pg
        mechanical_assembly_pg
        packaging_power_pg
        powergenerator_amb
        
"""
# Site/Area/line_/xxx
reset = "Command/Reset" 
start = "Command/Start"

berlin = [
    "berlin/cnc/line_1/",
    "berlin/cnc/line_2/",
    "berlin/cnc/line_3/",
    "berlin/electronic_assembly/line_1/",
    "berlin/electronic_assembly/line_2/",
    "berlin/electronic_assembly/line_3/",
    "berlin/mechanical_assembly/line_1/",
    "berlin/mechanical_assembly/line_2/",
    "berlin/mechanical_assembly/line_3/",
    "berlin/packaging/line_1/",
    "berlin/packaging/line_2/",
    "berlin/packaging/line_3/",
]
for i in berlin:
    topic_reset = str(i)+str(reset)
    print(topic_reset)
    client.publish(topic_reset,"1")#publish
    time.sleep(2)
    topic_start = str(i)+str(start)
    print(topic_start)
    client.publish(topic_start,"1")#publish
    time.sleep(2)