import os
import sys
import subprocess
import numpy as np
"""Compute the average rtt over the n mqtt messages sent n being the first parameter when launching;
!!! Must be launched as sudo !!!
tshark, tcpdump, mosquitto_pub need to be installed"""

#Snif on port 1883 corresponding to mqtt port
process = subprocess.Popen(["tcpdump -i wlp2s0 -w results.pcap 'port 1883'"], shell=False)
process.terminate()
#pid_mosquitto_sub = process_mosquitto_sub.pid
#Analyse the trace to get only the time of the TCP connection openning and closing put them in a text file: result_tmp
os.system('tshark -r results.pcap -Y "(tcp.flags.syn == 1 and tcp.flags.ack == 0) or (tcp.flags.fin == 1 and tcp.srcport == 1883) " -T fields -e frame.time_epoch > result_tmp')
file_tmp = open('result_tmp', "r+")
i=0
differences = []
for item in file_tmp:
	if i%2==1:
		differences.append(float(item)-previous)
	else:
		previous = float(item)
	i += 1
os.system("rm result_tmp")
os.system("rm results.pcap")
print('\n\n ////////: AVERAGE = '+str(np.average(differences)))





