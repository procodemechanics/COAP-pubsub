#! bin/bash

## Get the time out of minicom file ##
## Copy range of data from minicom file into new text file
## Then run bash read-minicom.sh input output

cat $1 | awk {'print $2'} > result/$2
cat result/$2 | cut -f1 -d "]" > result/$2.res
rm result/$2
