import os
import subprocess
import numpy as np
process = subprocess.Popen(["tcpdump -i lo -w results.pcap 'port 1883'"], shell=True)
process_mosquitto_sub = subprocess.Popen(['mosquitto_sub -t "test"'], shell=True)
for i in range(50):
	os.system('mosquitto_pub -m "message drom ..." -t "test" -q 2 -d')
process.terminate()
process_mosquitto_sub.terminate()
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
print('\n\n ////////: AVERAGE = '+str(np.average(differences)))





