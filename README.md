# Adam-driver

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
