touch result_loss
touch result_delay
sudo tc qdisc add dev $5 netem loss 0.001%
sudo tc qdisc add dev $5 netem delay 0.0ms

if [ "$1" == "loss" ]
then
	for loss_value in  0.1 0.5 1 1.5 2.0 5.0 7.5 10.0 15.0 25.0 35.0 45.0 
	do
		sudo tc qdisc change dev $5 netem loss $loss_value%
		sudo python launcher.py send-and-print $2 $3 $4 $5 $6 $7 $8 $loss_value 0 result_loss
	done
	gnuplot printing_delay.gp
fi
if [ "$1" == "loss" ]
then
	for delay_value in  1.0 2.0 5.0 10.0  20.0 30.0 40.0 50.0 60.0 70.0 80.0 90.0 100.0
	do
		sudo tc qdisc change dev $5 netem delay $delay_value ms
		sudo python launcher.py send-and-print $2 $3 $4 $5 $6 $7 $8 0.0 $delay_value result_delay
	done
	gnuplot printing_loss.gp
fi 

sudo rm result_loss
sudo rm result_delay