"""Compute RTT for QoS 0 (PUBLISHER ---> BROKER)
SINGLE TRANSACTION 

Pre-requisites : 
tshark,tcpdump,mosquitto_pub need to be installed
create a directory ~/IoTresults in the home directory of your computer. Capture wireshark trace of QoS 2 transaction and save it as RTT_q0.pcapng
Program must be launched as SUDO"""

#import the module
import os
import sys
import subprocess
import numpy as np


#p1= subprocess.Popen(['tshark','-S -q -w capture_out -a duration:10'], stdout=subprocess.PIPE)
#output = subprocess.check_output(['tshark','-S -q -w capture_out -a duration:10'], timeout=10)
#output = subprocess.Popen(['tshark','-r "~/IoTresults/RTT_q0.pcapng" -j "mqtt" -P -T text -Y "mqtt.msgtype == 1 or mqtt.msgtype == 2"'], stdout=subprocess.PIPE)
output = subprocess.Popen("tshark -r ~/IoTresults/RTT_q0.pcapng -j 'mqtt' -P -T text -Y 'mqtt.msgtype == 1 or mqtt.msgtype == 2'| awk '{print $2}' > filtered_packets",stdout=subprocess.PIPE,shell=True)
#print (p1.communicate())
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
#os.system("rm result_tmp")
#os.system("rm results.pcap")
print('\n\nAVERAGE RTT for QoS 0 = '+str(np.average(differences)))


"""Handling Exception for timeout"""
#try:
#	output.wait(timeout=10)
#except subprocess.TimeoutExpired:
#	print("10 seconds of capture is over")
#	sys.exit(1) 

output.terminate()
