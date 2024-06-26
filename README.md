# ADAM-driver

![alt text](/image/ADAM.png "ADAM Driver")

This is a reader for the ADAM-6018+ TC reader.

To use, include the AdamClient.py file in your project.
The output of this code is a list of thermocouples 1-8.

# Example
```python
from AdamClient import AdamClient

ADAM_IP = "172.18.120.250"
client = AdamClient(ADAM_IP, thermocouple_type="K")

try:
    converted_values = client.read_and_convert()
    print(converted_values)
except Exception as e:
    print(f"Error: {e}")
```

With one thermocouple attached to input 1, and the thermocouple installed in a coffee, the output will be:
```
[48.37, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

# Configuring ADAM devices

The ADAM devices only connect through Ethernet, _and don't respond to ping_. Yeah, have fun with that. They must be configured using the [Advantech ADAM/APAX Utility](https://www.advantech.com/en-us/support/details/utility?id=1-2AKUDB) using a Windows box.

To use the Advantech ADAM Utility, plug the ADAM device into Ethernet. On the same network, run the ADAM Utility on a Windows machine. In the ADAM Utility, select Tools -> Search Device, and hopefully the ADAM device will show up in the left hand column. From there, change the IP / subnet / gateway to something that works. I would suggest using static IP. Have fun.
