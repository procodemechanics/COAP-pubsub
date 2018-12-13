#! bin/bash


# Filter: mqtt.topic == "iot-2/cmd/leds/fmt/json"

### Read the time from trace #####

tshark -r $1 -t a -Y 'mqtt.topic == "iot-2/cmd/leds/fmt/json"' > $2.time

awk {'print $2'} $2.time > $2.result
