#!/usr/bin/python
from string import Template

class kvm_template_generator:
    def __init__(self):
        # xml template 
        self.vm_xml=Template('''\
<domain type='kvm'>
    <name>${ip_prefix}.${node_Id}_vt${type_Id}_i${instance_Id}</name>
    <title>${OS_version} ${arch}</title>
    <uuid></uuid>
    <memory unit='GiB'>${mem}</memory>
    <currentMemory unit='GiB'>${mem}</currentMemory>
    <vcpu placement='static'>${vcpus}</vcpu>
    <os>
        <type arch='${arch}'>hvm</type>
        <boot dev='hd'/>
    </os>
    <features>
        <acpi/>
        <apic/>
        <pae/>
    </features>
    <clock offset='localtime'/>
    <on_poweroff>destroy</on_poweroff>
    <on_reboot>restart</on_reboot>
    <on_crash>destroy</on_crash>
    <devices>
        <emulator>${emulator}</emulator>
        <disk type='file' device='disk'>
            <driver name='qemu' type='${image_format}'/>
            <source file='${image_file}'/>
            <target dev='hda' bus='ide'/>
        </disk>
        <interface type='bridge'>
            <source bridge='br0'/>
            <mac address='52:54:${type_Id}:${instance_Id}:${OS_Id}:${version_Id}'/>
        </interface>
        <input type='mouse' bus='ps2'/>
        <graphics type='vnc' port='5900' autoport='no' keymap='en-us'/>
    </devices>
</domain>
        ''')

        # append to dhcp file
        self.vnode_line = Template('''
host node${node_Id} {
    hardware ethernet	52:54:${type_Id}:${instance_Id}:${OS_Id}:${version_Id};
    fixed-address 		${ip_prefix}.${node_Id};
}
        ''')

    # present int in two digits
    def twodigit(self,int_digit):
        if int_digit >= 10:
            return str(int_digit)
        else:
            str_digit = str(int_digit)
            return ('0' + str_digit)

    def centos_type_gen(self, type_Id, instance_Id, node_Ip):
        type_id = self.twodigit(type_Id)
        instance_id = self.twodigit(instance_Id)
        templatedir = './WRFV3_vmtypes/'
        dhcpfile = './vnodes.conf.eth0'

        #imagedir = '/var/lib/libvirt/images/'
        image_dir = '/home/img_repo/'
        image_filename = Template('vnode_10G_centos_7_x86_64_${type_Id}.qcow2').substitute(type_Id=type_id)
        values = dict(
                OS_version='centos_7', 
                OS_Id='00',
                ip_prefix='10.1.1',
                version_Id=self.twodigit(7),
                #image_file=imagedir+'vnode_10G_centos_7_x86_64.img', 
                image_file=image_dir+image_filename, 
                #image_format='raw',
                image_format='qcow2',
                
                type_Id=type_id, 
                arch='x86_64', 
                mem='8',
                vcpus=type_id,
                emulator='/usr/libexec/qemu-kvm', 
                instance_Id=instance_id,
                node_Id=node_Ip,
                )
        template = self.vm_xml.substitute(values)

        # set filename the same with name in xml definition
        filename = templatedir + Template('${ip_prefix}.${node_Id}_${OS_version}_vt${type_Id}_i${instance_Id}.xml').substitute(values)
        dhcpline = self.vnode_line.substitute(values)
        
        with open(filename, 'w') as tempfile:
            for line in template:
                tempfile.write(line)

        with open(dhcpfile, 'a') as dhcpfile:
            for line in dhcpline:
                dhcpfile.write(line)
        

    def ubuntu_type_gen(self, type_Id, instance_Id, node_Ip):
        type_id = self.twodigit(type_Id)
        instance_id = self.twodigit(instance_Id)
        templatedir = './WRFV3_vmtypes/'
        dhcpfile = './vnodes.conf.eth0'

        #imagedir = '/var/lib/libvirt/images/'
        image_dir = '/home/img_repo/'
        image_filename = Template('vnode_18G_ubuntu_14_x86_64_${type_Id}.qcow2').substitute(type_Id=type_id)
        values = dict(
                OS_version='ubuntu_14', 
                OS_Id='01',
                ip_prefix='10.1.1',
                version_Id=self.twodigit(14),
                image_file=image_dir+image_filename, 
                #image_format='raw',
                image_format='qcow2',
                
                type_Id=type_id, 
                arch='x86_64', 
                mem='8',
                vcpus=type_id,
                emulator='/usr/libexec/qemu-kvm', 
                instance_Id=instance_id,
                node_Id=node_Ip,
                )
        template = self.vm_xml.substitute(values)

        # set filename the same with name in xml definition
        filename = templatedir + Template('${ip_prefix}.${node_Id}_${OS_version}_vt${type_Id}_i${instance_Id}.xml').substitute(values)
        dhcpline = self.vnode_line.substitute(values)
        
        with open(filename, 'w') as tempfile:
            for line in template:
                tempfile.write(line)

        with open(dhcpfile, 'a') as dhcpfile:
            for line in dhcpline:
                dhcpfile.write(line)

    # number of types, instances per type, specific os func 
    def type_group_gen(self, numOfTypes, instancesPerType, start_Ip, type_gen):
        count = start_Ip
        for i in range (1, instancesPerType + 1):
            for vt in range (1, numOfTypes + 1):
                count += 1
                print (vt, i, count)
                type_gen(vt, i, count)

if __name__=='__main__':
    mygenerator = kvm_template_generator()
    dhcpfile = './vnodes.conf.eth0'

    # flush old contents with a header
    with open(dhcpfile, 'w') as dhcpfile:
        dhcpfile.write('# -------------------------------\n')
        dhcpfile.write('# VIRTUAL HOST for interface eth0\n')
        dhcpfile.write('# -------------------------------\n')
    
    # generate 1 instance for each type
    #mygenerator.type_group_gen(10, 1, 16, mygenerator.centos_type_gen)
    mygenerator.type_group_gen(10, 1, 26, mygenerator.ubuntu_type_gen)

