"""Publish MQTT packets by specifying the number of transactions in the argument """

import os
import sys
import subprocess
import random, string
import numpy as np

def send(num,qos,ip,port, topic, message="message index...", fileName=None):
	#Create a subprocess to publish mqtt messages
	for i in range(int(num)):
		os.system('mosquitto_pub -h '+ip+' -p '+port+' -m "'+message+'" -t '+topic+' -q '+qos)

def get_random_string(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

def sender_function(num, qos, topic, iface, length, port="27000", ip="192.168.1.2", fileName="result.pcap"):

	####tcpdump########
    proc1 = subprocess.Popen("sudo tshark -i "+iface+" -w "+fileName+" -j 'mqtt' -P -T text -Y 'mqtt.msgtype == 1 or mqtt.msgtype == 2'", shell=True)		

	## start sending mqtt_pub##
    send(num, qos, ip, port, topic, get_random_string(length))

	##terminate tcpdump ##
    proc1.terminate()

    if len(sys.argv)==9:
        output = subprocess.Popen("tshark -r "+sys.argv[8]+" -j 'mqtt' -P -T text -Y 'mqtt.msgtype == 1 or mqtt.msgtype == 2 or mqtt.msgtype == 3 or mqtt.msgtype==4 or mqtt.msgtype==5 or mqtt.msgtype==6 or mqtt.msgtype==7'| awk '{print $2}' > filtered_packets",stdout=subprocess.PIPE,shell=True)
    elif len(sys.argv) == 8:
        output = subprocess.Popen("tshark -r result.pcap -j 'mqtt' -P -T text -Y 'mqtt.msgtype == 1 or mqtt.msgtype == 2 or mqtt.msgtype == 3 or mqtt.msgtype==4 or mqtt.msgtype==5 or mqtt.msgtype==6 or mqtt.msgtype==7'| awk '{print $2}' > filtered_packets",stdout=subprocess.PIPE,shell=True)

    #print (output.communicate()) #prints mqtt messages on the output terminal
    file_tmp = open('filtered_packets', "r+")
    i=0
    differences = []
    for item in file_tmp:
        if i%2==1:
            differences.append(float(item)-previous)
        else:
            previous = float(item)
        i += 1
        output.terminate()
    return {"rtt": np.average(differences), "std": np.std(differences)} 

#print('\n\nAVERAGE RTT for QoS '+sys.argv[2]+' = '+str(np.average(differences)))


#os.system('sudo rm result.pcap')


#python3 all_mqtt_pub.py [loop count] [qos] [ip] [port] [topic] [interface] [output_file]


	