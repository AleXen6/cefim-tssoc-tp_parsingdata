from pprint import pprint
import re
import json

with open("access.log", "r") as file_pointer:
    lines = file_pointer.readlines()

regex = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+ (\d{3}) \d"

access_data = []
for line in lines:
    data = re.findall(regex, line)[0]
    access_data.append(data)

#print(access_data)

ip_list = [ip for ip, status_code in access_data]

#print(ip_list)

ipaddress = {}

for ip in ip_list:
    if ip not in ipaddress:
        ipaddress[ip] = 1
    else:
        ipaddress[ip] += 1
#print(ipaddress)

final_data = {}

for ip, status_code in access_data:
    final_data[ip] = {}
for ip, status_code in access_data:
    if status_code not in final_data[ip]:
        final_data[ip][status_code] = 1
    else:
        final_data[ip][status_code] += 1
pprint(final_data)

with open("venv/access.json", "w") as json_file_pointer:
    json.dump(final_data, json_file_pointer)












