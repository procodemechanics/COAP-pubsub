import os
import sys
import subprocess
import numpy as np
"""Compute the average rtt over the n mqtt messages sent n being the first parameter when launching;
!!! Must be launched as sudo !!!
tshark, tcpdump, mosquitto_pub need to be installed"""

for i in range(int(sys.argv[1])):
	os.system('mosquitto_pub -m "message drom ..." -t "test" -q 2 -d')





