#!/bin/bash

case $1 in
	get)
	if [ $(($3)) != 0 ]; then
		for ((c=1; c<=$(($3)); c++))
		do			
			coap-client -m get  coap://$2:/ddd/dd
		done
	fi
	;;
	put)
	if [ $(($3)) != 0 ]; then
                for ((c=1; c<=$(($3)); c++))
                do
			coap-client -m put -t 0 coap://$2:/ddd/dd -e "$4"
		done
	fi
	;;
	-h)
	echo "############################ Help #############################"
	echo "This script is for running multiple CoAP client to the server"
	echo " "
	echo "bash m2m-coap.sh [get/put] [host] [number of loop] [data for put]"
	echo " "
	echo "Example: bash m2m-coap.sh get 127.0.0.1 4 "
	echo "Example: bash m2m-coap.sh put 127.0.0.1 1 data"
	echo "################################################################"

	;;
esac
