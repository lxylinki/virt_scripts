#!/bin/bash
format=qcow2
name=vnode
#size=8G
size=20
qemu-img create -f ${format} ${name}.${format} ${size}G  
