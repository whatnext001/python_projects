import csv

ip_marker = """
 __      __.__            __                          __   
/  \    /  \  |__ _____ _/  |_  ____   ____ ___  ____/  |_ 
\   \/\/   /  |  __     __\/    \_/ __   \/  /\   __ 
 \        /|   Y  \/ __ \|  | |   |  \  ___/ >    <  |  |  
  \__/\  / |___|  (____  /__| |___|  /\___  >__/\_ \ |__|  
       \/       \/     \/          \/     \/      \/       
"""
print(ip_marker)

empty_ip = []

print("The List of IP address is listed below:")
with open('ip_lists', 'r') as ip_collections:
    ip_reader = csv.reader(ip_collections)
    #print(list(ip_reader))

    for ip_info in ip_reader:
        empty_ip.append(ip_info[0])

for items in empty_ip:
    print(items)