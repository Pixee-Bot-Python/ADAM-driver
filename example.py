from AdamClient import AdamClient

ADAM_IP = "172.18.120.250"
client = AdamClient(ADAM_IP, thermocouple_type="K")

try:
    converted_values = client.read_and_convert()
    print(converted_values)
except Exception as e:
    print(f"Error: {e}")