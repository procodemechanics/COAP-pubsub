#!/bin/bash

case $1 in
	mqtt_pub)
	if [ $(($4)) != 0 ]; then
                for ((c=1; c<=$(($4)); c++))
                do
			mosquitto_pub -h $2 -p $3 -q $5 -t m2m-mqtt -m 'Test msg = '$(($c))''
		done
	fi
	;;
	-h)
	echo "############################ Help #############################"
	echo "This script is for sending multiple MQTT publish messages using 3 arguments"
	echo "1. MSG TYPE(mqtt_sub or mqtt_pub) "
	echo "2. BROKER IP ADDRESS "
	echo "3. BROKER PORT "
	echo "4. Number of messages to be published "
	echo "bash m2m-mqtt.sh [mqtt_pub] [broker_ip] [port] [number of msg] "
	echo "bash m2m-mqtt.sh [mqtt_sub] [broker_ip] [port]"
	echo " "
	echo "Example: bash m2m-mqtt.sh mqtt_sub 127.0.0.1"
	echo "Example: bash m2m-mqtt.sh mqtt_pub 127.0.0.1 1"
	echo "################################################################"
	;;
esac