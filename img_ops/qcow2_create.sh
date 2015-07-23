#!/bin/bash
IMG_DIR=/home/img_repo/
#IMG_INFO=vnode_10G_centos_7_x86_64
IMG_INFO=vnode_18G_ubuntu_14_x86_64

BASE=${IMG_DIR}${IMG_INFO}_base.img
N=10

for i in {1..10}
do
    if [ $i -lt 10 ]; then
        qemu-img create -f qcow2 -b ${BASE} ${IMG_DIR}${IMG_INFO}_0${i}.qcow2
        chmod +x ${IMG_DIR}${IMG_INFO}_0${i}.qcow2
    else
        qemu-img create -f qcow2 -b ${BASE} ${IMG_DIR}${IMG_INFO}_${i}.qcow2
        chmod +x ${IMG_DIR}${IMG_INFO}_${i}.qcow2
    fi
done

