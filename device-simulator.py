"""
Python script for simulating sensor data feed. This can be:
- Raspberry Pi
- BalenaOS
- MicroPython
- Cloud-based services
"""

import random
import requests
import pycristoforo as pyc

# Replace with your API products url (get from Datacake)
url = "YOURCUSTOMDATACAKEAPIURLHERE"

# Settings
number_of_sensors = 100
serial_prefix = "level00"

# Generate real GPS coords for devices using pycristoforo
country = pyc.get_shape("Germany")
points = pyc.geoloc_generation(country, number_of_sensors, "Germany")

for device in range(1, number_of_sensors + 1):

    payload = {
        "temperature": round(random.uniform(20, 25), 2),
        "battery": round(random.uniform(2, 4), 2),
        "signal": random.randrange(70, 99),
        "level": random.randrange(20, 90),
        "location": "(" + str( points[device-1]["geometry"]["coordinates"][1] ) + "," + str( points[device-1]["geometry"]["coordinates"][0] ) +")",
        "serial": serial_prefix + str(device)
    }

    print(payload)

    r = requests.post(url, json=payload)
    print(r)