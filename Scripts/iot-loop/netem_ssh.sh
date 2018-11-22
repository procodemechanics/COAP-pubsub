sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp2s0 root netem loss $1%"
sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp3s0 root netem loss $1%"
sshpass -p "IK2200ajpy"  ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp2s0 root netem delay $2ms"
sshpass -p "IK2200ajpy"  ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp3s0 root netem delay $2ms"
sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc -s qdisc show dev enp2s0"
sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc -s qdisc show dev enp3s0"
if [ $(($3)) != 0 ] ; then 
sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp2s0 root netem loss $1% $3%"
sshpass -p "IK2200ajpy" ssh -t student@192.168.1.4 " sudo tc qdisc change dev enp3s0 root netem loss $1% $3%"

fi
