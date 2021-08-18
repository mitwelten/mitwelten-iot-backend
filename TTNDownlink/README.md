# TTN Downlink

A Python script to push downlink messages to a TTN Node.

## Installation

Install pip
```sh
sudo apt install python3-pip
```

Install [paho-mqtt](https://www.eclipse.org/paho/index.php?page=clients/python/index.php)
```sh
pip3 install paho-mqtt
```

## Downlink Message Structure

See [documentation](https://www.thethingsindustries.com/docs/integrations/mqtt/#publishing-downlink-traffic)

The command is hardcoded in [get_paxcounter_battery.py](get_paxcounter_battery.py):
```json
{
    "downlinks": [
        {
            "f_port": 2,
            "frm_payload": "gw==",
            "priority": "HIGH",
            "confirmed": false
        }
    ]
}
```
The field `frm_payload` is encoded in base64. A nice tool to convert the payload is [here](https://base64.guru/converter/encode/hex).

## Configuration

The configuration is stored in a [JSON file](config.json).

The file must contain:

Parameter|Description
-|-
username|TTN MQTT-Integration username
password|TTN MQTT-Integration password
broker|TTN MQTT-Integration broker url
port|TTN MQTT-Integration broker port
topicprefix|Prefix of the topic to publish to
topicsuffix|Suffix of the topic (after DeviceId)
devices|List of DeviceId's

The Topic Structure to send a downlink message is:
```
v3/<APPLICATION-NAME>@ttn/devices/<DEVICE-ID>/down/push
```

## Schedule the script using crontab

Open the crontab configuration
```sh
crontab -e
```

Append the job to the file:
```
0 */4 * * * /usr/bin/python3 /home/ubuntu/TTNDownlink/get_paxcounter_battery.py
```
The schedule expression `0 */4 * * * ` executes the script every four hours. 

[crontab.guru](https://crontab.guru/) is helpful to create the schedule expression.

