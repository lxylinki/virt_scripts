#!/bin/bash
QEMU_KVM=/usr/bin/qemu-system-x86_64

#IMG=./imgs/ubt14_8G.img
#IMG=./imgs/minibuntu.img
#IMG=./imgs/minicent.img
IMG=./imgs/cent7_8G_x64.qcow2

# MAC address 52:54:00:xx:xx:xx
${QEMU_KVM} -enable-kvm -hda ${IMG} -device e1000,netdev=net0,mac=52:54:00:12:34:56 -netdev tap,id=net0,script=./qemu-ifup -m 2048 -smp $1

