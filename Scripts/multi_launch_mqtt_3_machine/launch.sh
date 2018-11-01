touch result_loss
touch result_delay
sudo tc qdisc add dev $5 root netem loss 0.001%
sudo tc qdisc add dev $5 root netem delay 0.0ms

if [ "$1" == "loss" ]
then
	for loss_value in  2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0 11.0 12.0 13.0 14.0 15.0 16.0 17.0 18.0 19.0 20.0 21.0 22.0 23.0 24.0 25.0 26.0 27.0 28.0 29.0 30.0 
	do
		sudo tc qdisc change dev $5 root netem loss $loss_value%
		sudo python launcher.py send-and-print $2 $3 $4 $5 $6 $7 $8 $loss_value 0 result_loss
	done
fi
if [ "$1" == "delay" ]
then
	for delay_value in 1.0 10.0 50.0 100.0 500.0 1000.0 5000.0 10000.0
	do
		sudo tc qdisc change dev $5 root netem delay $delay_valuems
		sudo python launcher.py send-and-print $2 $3 $4 $5 $6 $7 $8 0.0 $delay_value result_delay
	done
fi 
