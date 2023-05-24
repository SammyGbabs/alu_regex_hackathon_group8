
import re

ip_address = ['192.168.43.1']   

ip_pattern = re.compile(r"^(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}$")

ip_address_match = ip_pattern.findall(ip_address)

for address in ip_address_match:
    print (address)
