#
# SCAPY Startup File for Barefoot Academy
#
# (c) Barefoot Networks, 2018-
# All Rights Reserved
##########################################

#
# Prevent Scapy from discarding 802.1q (VLAN) tags
#
conf.use_pcap = True

#
# Load additional Scapy Modules
#
#load_contrib("bfd")
load_contrib("mpls")
load_contrib("vxlan")
#load_contrib("nvgre")
#load_contrib("erspan")
load_contrib("igmp")
load_contrib("geneve")

#
# Create convenient variables, based on available VETH or Dummy Interfaces
#
import os
global all_ports
all_ports=[]
for iface in os.listdir('/sys/class/net'):
    if iface.startswith("veth"):
        if int(iface[4:]) % 2:
            exec("{} = '{}'".format(iface, iface))
            all_ports.append(iface)
    if iface.startswith("port"):
        exec("{} = '{}'".format(iface, iface))
        all_ports.append(iface)
    if iface.startswith("cpu_"):
        exec("{} = '{}'".format(iface, iface))
        all_ports.append(iface)

def iface_num(iface):
    num = ''
    for c in iface:
        if c.isdigit():
            num += c
    return int(num)

all_ports.sort(key=iface_num)

print("""
Found the following interfaces:
{}

Created scapy.main.all_ports[] and scapy.main.veth*
To access them, type:
    from scapy.main import *
""".format(all_ports))
