"""Publish MQTT packets by specifying the number of transactions in the argument """

import os
import sys
import subprocess
import random, string

def send(num,qos,ip,port, topic, message="message index..."):
#Create a subprocess to publish mqtt messages
	for i in range(int(num)):
		os.system('mosquitto_pub -h '+ip+' -p '+port+' -m "'+message+'" -t '+topic+' -q '+qos+' -d')

def get_random_string(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))
	
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
length = sys.argv[7]
###################
####tcpdump########
if len(sys.argv) == 8:
    process = subprocess.Popen("sudo tcpdump -i "+iface+" -w "+sys.argv[8]+" 'port "+port+"'", shell=True)
elif len(sys.argv) == 7:
	process = subprocess.Popen("sudo tcpdump -i "+iface+" -w result.pcap 'port "+port+"'", shell=True)
else:
	print("Num_Message QoS broker_ip port topic iface")
## start sending mqtt_pub##
send(num, qos, ip, port, topic, get_random_string(length))

##terminate tcpdump ##
process.terminate()


#python3 all_mqtt_pub.py [loop count] [qos] [ip] [port] [topic] [interface] [output_file]


