#!/bin/bash
MY_IMG="blank_raw.img"


# sparse file
#dd if=/dev/zero of=${MY_IMG} bs=1K count=0 seek=8192K
#echo "sparse blank image is created."

# pre-allocated file
#dd if=/dev/zero of=${MY_IMG} bs=1K count=10240K
#dd if=/dev/zero of=${MY_IMG} bs=1K count=4096K
dd if=/dev/zero of=${MY_IMG} bs=1K count=8192K
echo "blank image is created."
