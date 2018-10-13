"""
Launch the others script to display values on terminal
"""
import os
import sys
from all_mqtt_pub import *
num = sys.argv[2]
qos = sys.argv[3]
if int(qos) not in [0, 1, 2]:
	print ("Error: QoS [0 1 2]")
	exit()
topic = sys.argv[4]
iface = sys.argv[5]
length = int(sys.argv[6])
res = sender_function(num, qos, topic, iface, length)
if sys.argv[1] == "simple":
	if len(sys.argv) < 7:
		print("Parameters: Num_Message QoS topic iface length") 
		sys.exit()
	num = sys.argv[2]
	qos = sys.argv[3]
	if int(qos) not in [0, 1, 2]:
		print ("Error: QoS [0 1 2]")
		exit()
	topic = sys.argv[4]
	iface = sys.argv[5]
	length = int(sys.argv[6])
	res = sender_function(num, qos, topic, iface, length)
	print('\n\n //////:Average RTT = '+str(res['rtt'])+'; STD _DEV = '+str(res['std']))

if sys.argv[1] == "netem":
    if len(sys.argv) < 9:
        print("Parameters: Num_Message QoS topic iface length packet_loss_ratio delay_ms") 
        sys.exit()
	packet_loss = sys.argv[7]
	delay = sys.argv[7]
    os.system("sudo tc qdisc add dev wlo1 root netem delay 0ms")
    os.system("sudo tc qdisc add dev wlo1 root netem loss 0.01%")
    os.system('sudo tc qdisc change dev wlo1 root netem loss '+packet_loss+'%')
    os.system('sudo tc qdisc change dev wlo1 root netem delay '+delay+'ms')
    res = sender_function(num, qos, topic, iface, length)
    print('\n\n //////:Average RTT = '+str(res['rtt'])+'; STD _DEV = '+str(res['std']))

