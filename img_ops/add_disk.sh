#!/bin/bash
# add blank raw disk to original image
BLANK_RAW=blank_raw.img
echo "Usage: add_disk.sh -i image_name"
while getopts "i:" origimg
do
    # convert original image to raw format
    echo "Converting to raw first ...\n"
    qemu-img convert -O raw ${OPTARG} ${OPTARG}.img
    echo "${OPTARG} has been converted to raw format, adding disk...\n"

    # add blank img
    cat ${BLANK_RAW} >> ${OPTARG}.img
    echo "Added disk to ${OPTARG}.img\n"
done 
