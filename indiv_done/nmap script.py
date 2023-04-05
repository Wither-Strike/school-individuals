import os
ip_Addr=[]

with open("indiv_done/test.txt", "r") as file:
    for line in file:
        line = line.strip()
        ip_Addr.append(line)

for ipaddr in ip_Addr:
    os.system(f"nmap -sCV {ipaddr} -oN indiv_done/{ipaddr}.txt --unprivileged")
