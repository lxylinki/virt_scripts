#!/bin/bash
IMG_DIR="./imgs"
#IMG_DIR="./"
QEMU="/usr/bin/kvm"

#OS_SOURCE="${IMG_DIR}/centos/CentOS-6.6-i386-minimal.iso"
OS_SOURCE="${IMG_DIR}/ubuntu/ubuntu-14.04.1-desktop-i386.iso"
#OS_SOURCE="${IMG_DIR}/ubuntu/mini.iso"
#OS_SOURCE="${IMG_DIR}/gentoo/install-x86-minimal-20141111.iso"
#OS_SOURCE="${IMG_DIR}/en_windows_8_x64_dvd_915440.iso"

my_image_name="blank_raw.img"

MY_IMG="${IMG_DIR}/${my_image_name}"
${QEMU} -m 4096 -hda ${MY_IMG} -cdrom ${OS_SOURCE} -boot d -enable-kvm
