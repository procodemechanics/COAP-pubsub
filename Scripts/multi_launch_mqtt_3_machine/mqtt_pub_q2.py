"""
Compute RTT for QoS 2 (PUBLISHER ---> BROKER)
SINGLE TRANSACTION 

Pre-requisites : 
tshark,tcpdump,mosquitto_pub need to be installed
create a directory ~/IoTresults in the home directory of your computer. Capture wireshark trace of QoS 2 transaction and save it as RTT_q2.pcapng
Program must be launched as SUDO"""

#import the module
import os
import sys
import subprocess
import numpy as np

output = subprocess.Popen("tshark -r ~/IoTresults/RTT_q2.pcapng -j 'mqtt' -P -T text -Y 'mqtt.msgtype == 1 or mqtt.msgtype == 2 or mqtt.msgtype == 3 or mqtt.msgtype==5 or mqtt.msgtype==6 or mqtt.msgtype==7'| awk '{print $2}' > filtered_packets",stdout=subprocess.PIPE,shell=True)
print (output.communicate())
file_tmp = open('filtered_packets', "r+")
i=0
differences = []
for item in file_tmp:
	if i%2==1:
		differences.append(float(item)-previous)
	else:
		previous = float(item)
	i += 1

print('\n\nAVERAGE RTT for QoS 2 = '+str(np.average(differences)))

output.terminate()
