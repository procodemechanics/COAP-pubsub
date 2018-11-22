#! bin/bash

####################################### Start iot-loop.sh ################################################################

### Run loop for X trial time and Y packets 
### Use NetEM to generate the loss 
### By remote to NetEM machine and increase the loss
### LOSS #####
### Loss will be from 0% - 15%
###



### CAPTURE ########
#Start#
case $8 in
	mqtt )
	sshpass -p "howislife" ssh -t student@192.168.1.2 "mkdir TEST && cd TEST"
;;
esac
case $1 in
	-h)

	############### HELP ####################################
	echo "bash iot-loop.sh [interface/put/-h] [coap/mqtt] [output] [ip] [no of trial loop][total packet]"
	echo ""	
	echo "Parameter list:"	
	echo ""	
	echo "1. interface or put option for coap or -h for help"	
	echo "8. CoAP or MQTT"
	echo "############ For CoAP put option###############################"	
	echo "2. IP address of the server"	
	echo "3. Data"	
	echo "############# For CoAP ##########################"	
	echo "2. Prefix name of the pcap file"	
	echo "3. Protocol Port number"	
	echo "4. IP address of the server"	
	echo "5. Number of trial loop"	
	echo "6. total of message sent"
	echo "7. Path for other script"		
	echo "############# For MQTT ##########################"	
	echo "9. QoS"
	echo "10 MQTT sub IP"
	echo "############### Example #########################"
	echo "bash iot-loop.sh enp2s0 test-coap 5683 192.168.1.2 2 100 ~/TEST-RUN/iot-loop coap"
	echo "bash iot-loop.sh enp2s0 test-mqtt 1883 192.168.1.2 2 100 ~/TEST-RUN/iot-loop mqtt 1"
	echo "#########################################################"	



	#########################################################
	;;



	put)

	########## This is just for putting the data into the server ###############
	coap-client -m put -t 0 coap://$2:/ddd/dd -e "$3"
	;;

	#################### Else ####################################
	*)

	### CAPTURE ########
	#Start#
	echo "Start"
	fol=$2
	mkdir $fol
	cd $fol
	#### Loss Loop #######
	for ((d=0;d<=15;d++))
	do
	
	############# ADD LOSS ##################
	echo "======== Loss $d % =============== "
	if [ $(($d)) == 0 ]; then
		bash "$7/netem_ssh.sh" 0.001 0.0
	
	else
	bash "$7/netem_ssh.sh" $(($d)) 0.0
	fi
	echo "=================================="
	sleep 3

	########### Optional for Burst loss ##########

	# echo "======== Loss $d % $d% =============== "
	# if [ $(($d)) == 0 ]; then
	# 	bash "$7/netem_ssh.sh" 0.001 0.0 0.001
 	
	# else
	# 	bash "$7/netem_ssh.sh" $(($d)) 0.0 $(($d)) 
	# fi
	# echo "=================================="
	# sleep 3

	##############################################
	case $8 in
		coap )
	
		####### Create CoAP loss X% folder #######

		fol2="$fol-CoAP-loss$d"
		mkdir $fol2
		cd $fol2

		for ((c=1; c<=$5;c++))
		do

		############## Start the process ##############
		echo " ############# Round $c ###########"
		############## Start Capture  #################
		sudo tcpdump -i $1 -w $2-$c.pcap 'port '$3'' &
		sleep 2
		
		#    ~/m2m-coap.sh -h
		bash "$7/m2m-coap.sh" get $4 $6
		sleep 5
		############################# Stop Capture ###################################
		pid=$(ps -e | pgrep tcpdump)  
		#echo $pid  
		#sleep 2
		sudo kill -2 $pid
		sleep 2
		
		echo " ################ End ##############"
		
		#################################### END ######################################
		done

		;;

		mqtt )
		
		fol2="$fol-MQTT-loss$d"
		mkdir $fol2
		############## Create directory for remote PC (Sub) ##############
		sshpass -p "howislife" ssh -t student@192.168.1.2 "cd TEST && mkdir $fol2-sub-$d"
		cd $fol2
		for ((c=1; c<=$5;c++))
		do
			############## Start the process ##############
			echo " ############# Round $c ###########"
			############## Start Capture  #################
			sudo tcpdump -i $1 -w $2-$c.pcap 'port '$3'' &
			sleep 2
			sname="~/TEST/$fol2-sub-$d/test-mqtt-$c"
			####### Remote to another PC (Sub) and capture the packets ###########
			
			sshpass -p 'howislife' ssh student@192.168.1.2 "sudo tcpdump -i enp2s0 -w $sname 'port $3' " &
			sleep 2

			######## To received TCP ack might need to remove PORT ########
			
			sshpass -p 'howislife' ssh student@192.168.1.2  "bash ~/mqtt-sub-cap.sh enp2s0 '~/TEST/test-mqtt-$c' $3 $4 "& 

			
			bash "$7/m2m-mqtt.sh" mqtt_pub $4 $3 $6 $9
			######## Wait for some left over packet ################
			sleep 5

			#echo $pid  
			#sleep 2
			############################# Stop Capture ###################################
			sshpass -p 'howislife' ssh student@192.168.1.2 'sudo bash ~/mqtt-sub-cap.sh stop'

			pid=$(ps -e | pgrep tcpdump) 
			sleep 2
			sudo kill -2 $pid

			echo " ################ End ##############"
		
			#################################### END ######################################

		done
		### Go out of the folder in remote PC (Sub) ###
		sshpass -p 'howislife' ssh -t student@192.168.1.2 'cd ..'
		;;
	
	esac
	### Go out of the folder ###
	cd ..
	done
	;;
esac


######################################################### DONE ###############################################