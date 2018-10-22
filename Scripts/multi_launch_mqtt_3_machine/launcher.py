"""
Launch the others script for MQTT and CoAP
@Parameters : type num_messages qos topic iface length port ip [ packet_loss delay result_file ]
"""
import os
import sys
from all_mqtt_pub import *

if sys.argv[1] == "analyse":
    analyse()
    sys.exit()

num = sys.argv[2]
qos = sys.argv[3]
if int(qos) not in [0, 1, 2]:
	print ("Error: QoS [0 1 2]")
	exit()
topic = sys.argv[4]
iface = sys.argv[5]
length = int(sys.argv[6])
port = sys.argv[7] if len(sys.argv) > 7 else "27000"
ip = sys.argv[8] if len(sys.argv) > 8 else "192.168.1.2"

"""def netem_send(delay, packet_loss):
    if len(sys.argv) < 8:
        print("Parameters: Num_Message QoS topic iface length packet_loss_ratio delay_ms") 
        sys.exit()
    proc = subprocess.Popen('sudo tc qdisc change dev '+iface+' root netem loss '+str(packet_loss)+'%', shell=True, stderr = subprocess.STDOUT)
    subprocess.Popen('sudo tc qdisc change dev '+iface+' root netem delay '+str(delay)+'ms', shell=True)
    return sender_function(num, qos, topic, iface, length, port, ip)"""

def analyse():
    res = analyse_function()
    print('\n\n //////:Average RTT = '+str(res['rtt'])+'; STD _DEV = '+str(res['std']))
    return res

if sys.argv[1] == "simple":
	if len(sys.argv) < 7:
		print("Parameters: Num_Message QoS topic iface length") 
		sys.exit()
	print(sender_function(num, qos, topic, iface, length, port, ip))

if sys.argv[1] == "send-and-print":
    file_res = open(sys.argv[11], "a+")
    packet_loss = sys.argv[9]
    delay = sys.argv[10]
    print('\n\n\n //////LOSS : '+str(packet_loss)+' DELAY  '+str(delay)+"\n\n\n")
    sender_function(num, qos, topic, iface, length, port, ip)
    res = analyse_function()
    file_res.write(str(packet_loss)+" "+str(delay)+" "+str(res['rtt'])+ " "+str(res['std'])+"\n")
    sys.exit()

if sys.argv[1] == "netem-analyse":
    netem_send()
    analyse()   
    sys.exit()

"""if sys.argv[1] == "multi-launch-loss":
    file_res = open("res_multi_launch_loss", "a+")
    for packet_loss in [0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]:
        netem_send(0, str(packet_loss))
        res = analyse()
        file_res.write(str(packet_loss)+" "+str(res['rtt'])+ " "+str(res['std'])+"\n")
    sys.exit()

if sys.argv[1] == "multi-launch-delay":
    file_res = open("res_multi_launch_delay", "a+")
    for packet_delay in [0.1, 0.5, 0.5, 1, 2, 5, 10, 15, 20, 50, 60, 70, 80, 90, 100, 110, 120, 130]:
        netem_send(str(packet_delay), 0.001)
        res = analyse()
        file_res.write(str(packet_delay)+" "+str(res['rtt'])+ " "+str(res['std'])+"\n")
    sys.exit()
"""