# $1  Loss     $2  Delay   $3  Successive loss probablity 
# sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp2s0 root netem loss $(($1))%"
# sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp3s0 root netem loss $(($1))%"
# sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp2s0 root netem delay $2ms"
# sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp3s0 root netem delay $2ms"
# sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc -s qdisc show dev enp2s0"
# sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc -s qdisc show dev enp3s0"
case $1 in
	loss )
	sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp2s0 root netem loss $2%"
	sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp3s0 root netem loss $2%"
	;;

	burst )
	sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp2s0 root netem loss $2% $3%"
	sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp3s0 root netem loss $2% $3%"
	;;

	delay )
	sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp2s0 root netem delay $2ms"
	sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp3s0 root netem delay $2ms"
	;;
	
	add )
	sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc add dev enp2s0 root netem loss 0.001%"
	sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc add dev enp3s0 root netem loss 0.001%"
	;;

	del )
	sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc del dev enp2s0 root netem "
	sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc del dev enp3s0 root netem "
	;;

	show )
	sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc -s qdisc show dev enp2s0"
	sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc -s qdisc show dev enp3s0"
	;;
esac
