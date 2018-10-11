"""Publish MQTT packets by specifying the number of transactions in the argument """

import os
import sys
import subprocess

#Snif on port 1883 corresponding to mqtt port
#process = subprocess.Popen(["tcpdump -i lo -w ~/IoTresults/result.pcap 'port 1883'"], shell=True)

#Create a subprocess to publish mqtt messages
mqtt_load= subprocess.Popen('mosquitto_sub -t test', shell=True)
for i in range(int(sys.argv[1])):
	os.system('mosquitto_pub -m "message index ..."'+ str(i) +' -t test -q 1 -d')
mqtt_load.terminate()
pid_mqtt_pub = mqtt_load.pid
os.system('sudo kill -9 '+str(pid_mqtt_pub))

#Snif on port 1883 corresponding to mqtt port
process = subprocess.Popen(["tcpdump -i wlo1 -w ~/IoTresults/result.pcap"], shell=True)

process.terminate()



