#! /bin/bash

### Start capture ####

sudo tcpdump -i enp2s0 -w $3.pcap 'port 1883' &

for ((c=1;c<=$1;c++));
do
#	Publish the data 
	mosquitto_pub -h 192.168.1.3 -m "1" -t iot-2/cmd/leds/fmt/json -q 0
	sleep 0.1
	
done
#	Publish invalid data to seperate debug code in minicom
mosquitto_pub -h 192.168.1.3 -m "" -t iot-2/cmd/leds/fmt/json -q 0
sleep 3
sudo killall tcpdump
echo "END"

