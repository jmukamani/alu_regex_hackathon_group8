
import re

ip_address = ['192.168.43.1']    #Replace with your actual IP address

ip_pattern = r"^(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}$"
ip address_match = re.match(ip pattern,ip_address)

if ip_address:
    print(ip_address.group(0))
else:
    print("The IP address does not match the pattern")
