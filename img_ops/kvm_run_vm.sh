#!/bin/bash
KVM=/usr/bin/kvm

IMG=./imgs/cent7_8G_x64.qcow2

# MAC address 52:54:00:xx:xx:xx
#${KVM} -m 2048 -smp $1 ${IMG} -net nic,vlan=0,model=virtio,macaddr=52:54:00:12:34:56 -net tap,vlan=0,ifname=tap0,script=./qemu-ifup
${KVM} -m 2048 -smp $1 ${IMG} -net nic,model=virtio,macaddr=52:54:00:12:34:56 -net tap,ifname=tap0,script=./qemu-ifup

