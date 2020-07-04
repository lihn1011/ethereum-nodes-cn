import list
from socket import *
socket_list = []
find_list = []
for list_item in list.node_list:
    item = list_item.split("@")[1].split(":")
    ip = item[0]
    port = item[1]
    s=socket(AF_INET,SOCK_STREAM)
    s.settimeout(1)
    try:
        x = s.connect((ip,int(port)))
    except:
        pass
    else:
        find_list.append(list_item)
print("[")
for i in range(len(find_list)):
    print('"'+find_list[i]+'"'+(',' if  i<len(find_list)-1 else ''))
print("]")


