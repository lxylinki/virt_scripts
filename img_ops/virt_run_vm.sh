#!/bin/bash
IMG_DIR="./imgs/"
my_image_name="minicent.img"
MY_IMG="${IMG_DIR}/${my_image_name}"

virt-install \
 --connect qemu:///system \
 --ram 4096 -n minicent\
 --disk path=${MY_IMG} \
 --vcpus=4 \
 --graphics vnc \
 --import
