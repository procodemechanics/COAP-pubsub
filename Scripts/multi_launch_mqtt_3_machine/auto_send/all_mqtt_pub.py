"""Publish MQTT packets by specifying the number of transactions in the argument """

import os
import sys
import subprocess

def send(num,qos,ip,port, topic):
#Create a subprocess to publish mqtt messages
	for i in range(int(num)):
		os.system('mosquitto_pub -h '+ip+' -p '+port+' -m "message index ..." -t '+topic+' -q '+qos+' -d')
#####input#######
num = sys.argv[1]
qos = sys.argv[2]
if int(qos) > 2:
	print ("Error: QoS [0 1 2]")
	exit()
ip = sys.argv[3]
port = sys.argv[4]
topic = sys.argv[5]
iface = sys.argv[6]
###################
####tcpdump########
if len(sys.argv) > 7:
	process = subprocess.Popen("sudo tcpdump -i "+iface+" -w "+sys.argv[7]+" 'port "+port+"'", shell=True)
else:
	process = subprocess.Popen("sudo tcpdump -i "+iface+" -w result.pcap 'port "+port+"'", shell=True)
## start sending mqtt_pub##
send(num,qos,ip,port,topic)

##terminate tcpdump ##
process.terminate()


#python3 all_mqtt_pub.py [loop count] [qos] [ip] [port] [topic] [interface] [output_file]


