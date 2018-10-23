touch result_loss
touch result_delay
sudo tc qdisc add dev $5 root netem loss 0.001%
sudo tc qdisc add dev $5 root netem delay 0.0ms

if [ "$1" == "loss" ]
then
	for loss_value in  1.0 2.5 5.0 7.5 10 12.5 15 17.5 20 22.5 25 27.5 30 
	do
		sudo tc qdisc change dev $5 root netem loss $loss_value%
		sudo python launcher.py send-and-print $2 $3 $4 $5 $6 $7 $8 $loss_value 0 result_loss
	done
	sleep 1
	gnuplot printing_delay.gp
fi
if [ "$1" == "delay" ]
then
	for delay_value in 1.0 10.0 50.0 100.0 500.0 1000.0 5000.0 10000.0
	do
		sudo tc qdisc change dev $5 root netem delay $delay_valuems
		sudo python launcher.py send-and-print $2 $3 $4 $5 $6 $7 $8 0.0 $delay_value result_delay
	done
	sleep 1
	gnuplot printing_loss.gp
fi 
