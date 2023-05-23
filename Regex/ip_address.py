import re

ip_pattern = r"^(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}$"

ip_address = "192.168.0.1"

if re.match(ip_pattern, ip_address):
    print("Valid IP address")
else:
    print("Invalid IP address")
