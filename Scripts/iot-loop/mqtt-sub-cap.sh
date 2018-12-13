#! bin/bash
case $1 in
	stop )
		ddd=$(ps -e | pgrep tcpdump)
		kill -2 $ddd
		sleep 2
	;;
	* )
		#sudo tcpdump -i $1 -w $2.pcap 'port '$3'' &
		mosquitto_sub  -h $4 -p $3 -q $2 -t m2m-mqtt 
		;;
esac
