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

