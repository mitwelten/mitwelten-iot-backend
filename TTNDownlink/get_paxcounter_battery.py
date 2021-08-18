import paho.mqtt.client as mqtt
import ssl
import json

# send payload 0x83 to the node
command = """
            {
            "downlinks": [{
                "f_port": 2,
                "frm_payload": "gw==",
                "priority": "HIGH",
                "confirmed": false
            }]
            }
"""

f = open("/home/ubuntu/TTNDownlink/config.json", "r")
config = json.loads(f.read())
f.close()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


client = mqtt.Client()
client.username_pw_set(config["username"], config["password"])
client.on_connect = on_connect


client.connect(config["broker"], config["port"], 60)

for device in config["devices"]:
    client.publish(config["topicprefix"] + device + config["topicsuffix"], command, 2)
