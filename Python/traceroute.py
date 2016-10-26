from scapy.all import *

hostname = "google.com"

for i in range(1, 28):
    packet = IP(dst=hostname, ttl=i) / UDP(dport=33434)

    # send the packet and get reply
    reply = sr1(packet, verbose=0)
    if reply is None:
        break
    elif reply.type == 3:
        print("Done! --> " + reply.src)
        break
    else:
        print("%d hops away: %i", reply.src)
