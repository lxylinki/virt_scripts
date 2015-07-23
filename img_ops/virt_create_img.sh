#!/bin/bash
#TODO 
#xiangyu: permission issue on tap creating
#root: cannot find uid 107(qemu) 
IMG_DIR="/home/xiangyu/OS_Images"

my_image_name="test.qcow2"

MY_IMG="${IMG_DIR}/${my_image_name}"
OS_SOURCE="${IMG_DIR}/Fedora-20-x86_64-netinst.iso"

virt-install --network bridge:br0 --name vnode0 --ram=1024 --vcpus=4 --disk ${MY_IMG},size=8 --cdrom ${OS_SOURCE} #--extra-args="console=tty0 console=ttyS0,115200"
