#! /bin/bash

### Run experiment X time ######
mkdir test-mqtt-sensor
cd test-mqtt-sensor
for ((c=0;c<=$1;c++));
do
	#sudo minicom -C test-$c.min  &
#sleep 2
	
	### Run loop 10 time ###
	bash ../loop.sh 10 mss-$c
	sleep 5
	#sudo killall minicom
#sleep 2
done


