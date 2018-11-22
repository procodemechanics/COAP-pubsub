#! bin/bash

################# This one run on subscriber side for stop tcpdump and run mosquitto sub #######################
######################## Part of iot-loop.sh ###################################################################
case $1 in
	stop )
		ddd=$(ps -e | pgrep tcpdump)
		kill -2 $ddd
		sleep 2
	;;
	* )
		#sudo tcpdump -i $1 -w $2.pcap 'port '$3'' &
		mosquitto_sub  -h $4 -p $3 -q 2 -t m2m-mqtt &
		;;
esac
##################################### END #######################################################################