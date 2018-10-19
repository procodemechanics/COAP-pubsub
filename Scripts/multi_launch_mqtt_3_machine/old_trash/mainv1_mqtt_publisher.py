import os
import sys
import subprocess
import numpy as np
""" 
Argument 1 <int>Number of messages sent;
Argument 2 <int> QoS (0,1,2);
Argument 3 <float> Packet loss in percentage;
Argument 4 <int> Delay in ms;
Compute the average rtt over the n mqtt messages sent n being the first parameter when launching;
!!! Must be launched as sudo !!!
tshark, tcpdump, mosquitto_pub need to be installed"""
os.system("sudo tc qdisc add dev wlo1 root netem delay 0ms")
os.system("sudo tc qdisc add dev wlo1 root netem loss 0.01%")
os.system( 'sudo tc qdisc change dev wlo1 root netem loss '+str(sys.argv[3])+'%')
os.system('sudo tc qdisc change dev wlo1 root netem delay '+str(sys.argv[4])+'ms')
for i in range(int(sys.argv[1])):
	os.system('mosquitto_pub -m "message drom ..." -t "test" -q '+str(sys.argv[2])+' -d')





