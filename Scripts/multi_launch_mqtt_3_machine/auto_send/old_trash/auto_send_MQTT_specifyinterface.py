"""Publish MQTT packets by specifying the number of transactions in the argument """

import os
import sys
import subprocess
import random
import string
import time

def send(num,qos,ip,port, topic, message="message index..."):
#Create a subprocess to publish mqtt messages
	for i in range(int(num)):
		os.system('mosquitto_pub -h '+ip+' -p '+port+' -m "'+message+'" -t '+topic+' -q '+qos)

def get_random_string(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))


#output = subprocess.Popen("sudo tcpdump -i enx00133b000009 -w capture.pcap", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#command=
#output = subprocess.Popen("sudo tcpdump -i enx00133b000009 -w capture.pcap", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#output = subprocess.Popen(['sudo','tcpdump','-i','enx00133b000009','-w','capture.pcap','-l'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#for row in iter(output.stdout.readline,b''):
	#print (row.rstrip())

#s=output.std

#time.sleep(2)

#####input#######
num = sys.argv[1]
qos = sys.argv[2]
if int(qos) not in [0, 1, 2]:
	print ("Error: QoS [0 1 2]")
	exit()
ip = sys.argv[3]
port = sys.argv[4]
topic = sys.argv[5]
iface = sys.argv[6]
length = int(sys.argv[7])
###################


#Snif on port 1883 corresponding to mqtt port
#process = subprocess.Popen(["tcpdump -i lo -w ~/IoTresults/result.pcap 'port 1883'"], shell=True)
#os.system("sudo tcpdump -i wlo1 -w ~/IoTresults/result.pcap")


## start sending mqtt_pub##
send(num, qos, ip, port, topic, get_random_string(length))

#print(output.communicate())
#for i in range(int(sys.argv[1])):
#	os.system('mosquitto_pub -h 192.168.1.2 -p 27000 -t test -m "message index : "'+ str(i) +' -q 0')
#mqtt_load.terminate()
#pid_mqtt_pub = mqtt_load.pid
#os.system('sudo kill -9 '+str(pid_mqtt_pub))

#Sniff corresponding to interface
#os.system("sudo tcpdump -i wlo1 -w result.pcap")
#output.send_signal(subprocess.signal.SIGTERM)
#output.terminate()



