#!/bin/bash

case $1 in
	mqtt_sub)
	mosquitto_sub -h $2 -t m2m-mqtt &
	;;
	mqtt_pub)
	if [ $(($3)) != 0 ]; then
                for ((c=1; c<=$(($3)); c++))
                do
			mosquitto_pub -h $2 -t m2m-mqtt -m 'Test msg = '$(($c))''
		done
	fi
	;;
	-h)
	echo "############################ Help #############################"
	echo "This script is for sending multiple MQTT publish messages to the subscribers."
	echo "Run the command 'mosquitto' on the broker. Now run script using the following parameters :"
	echo "1. MSG TYPE(mqtt_sub or mqtt_pub) "
	echo "2. BROKER IP ADDRESS "
	echo "3. Number of messages to be published "
	echo "bash m2m-mqtt.sh [mqtt_sub] [broker_ip]"
	echo "bash m2m-mqtt.sh [mqtt_pub] [broker_ip] [number of msg] "
	echo " "
	echo "Example: bash m2m-mqtt.sh mqtt_sub 127.0.0.1"
	echo "Example: bash m2m-mqtt.sh mqtt_pub 127.0.0.1 1"
	echo "################################################################"

	;;
esac
