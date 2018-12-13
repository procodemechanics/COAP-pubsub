#! bin/bash

bash ../netem_ssh.sh del
# Add loss #
#bash ../netem_ssh.sh add
d=0
for ((c=0;c<=$1;c++));
do	
####### Case for loss #
# 	for ((c=0;c<=$1;c=c+5));
#	do
#		if [ $(($c)) == 0 ]; then
#			bash ../netem_ssh.sh loss 0.001
#		else
#			bash ../netem_ssh.sh loss $c
#		fi
#	echo "Start $c with $c % loss"
#	sleep 2
########### Loss #######
	d=round-$c

	bash ~/SensorL/sensor-mqtt.sh 100 enp2s0 $d
	sleep 1
done
