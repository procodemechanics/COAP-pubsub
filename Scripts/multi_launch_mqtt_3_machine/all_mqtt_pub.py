"""Publish MQTT packets by specifying the number of transactions in the argument """

import os
import sys
import subprocess
import random, string
import time
import numpy as np

def send(num, qos, ip, port, topic, message="message index...", fileName=None):
	#Create a subprocess to publish mqtt messages
    process_array = []
    for i in range(int(num)):
        str_mqtt = 'mosquitto_pub -d -h '+ip+' -p '+port+' -m '+message+' -t '+topic+' -q '+qos
        print(str_mqtt)
        proc = subprocess.Popen(str_mqtt, shell=True)
        process_array.append(proc)

    for p in process_array:
        if p.poll == None:
            continue
        os.waitpid(p.pid, 0)

def get_random_string(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

def sender_function(num, qos, topic, iface, length, port="27000", ip="192.168.1.2"):      
    ## start sending mqtt_pub##
    os.system("sudo rm result.pcap")
    proc = subprocess.Popen("sudo stdbuf -oL tcpdump  -i "+iface+" -w result.pcap ", shell=True)
    #Wait for tcpdump to  start sensing
    time.sleep(1)
    send(num, qos, ip, port, topic, get_random_string(length))
    ##!terminate tcpdump ##
    proc.terminate()
    return 

def analyse_function(port="27000", fileName="result.pcap"):
    output = subprocess.Popen("tshark -r "+fileName+" -o mqtt.tcp.port:"+str(port)+"  -Y 'mqtt.msgtype == 1 or mqtt.msgtype == 2 or mqtt.msgtype == 3 or mqtt.msgtype==4 or mqtt.msgtype==5 or  mqtt.msgtype==6 or mqtt.msgtype==7'| awk '{print $2}' > filtered_packets", stdout=subprocess.PIPE, shell=True)
    pid_output = output.pid
    os.waitpid(pid_output, 0)
    file_tmp = open('filtered_packets', "r+")
    i=0
    differences = []
    for item in file_tmp:
        if i%2==1:
            differences.append(float(item)-previous)
        else:
            previous = float(item)
        i += 1
    
    os.system('sudo rm filtered_packets')
    return {"rtt": np.average(differences), "std": np.std(differences)} 

#print('\n\nAVERAGE RTT for QoS '+sys.argv[2]+' = '+str(np.average(differences)))


#os.system('sudo rm result.pcap')


#python3 all_mqtt_pub.py [loop count] [qos] [ip] [port] [topic] [interface] [output_file]


	
