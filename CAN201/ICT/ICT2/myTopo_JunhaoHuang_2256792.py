#usr/bin/python
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import Host, OVSKernelSwitch
from mininet.log import setLogLevel, info

def myTopo():
    net = Mininet(topo=None, autoSetMacs=True, build=False, ipBase='192.168.45.0/24')
    h1 = net.addHost("h1", cls=Host, defaultRoute=None)
    h2 = net.addHost("h2", cls=Host, defaultRoute=None)
    s1 = net.addSwitch("s1", cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch("s2", cls=OVSKernelSwitch, failMode='standalone')
    s3 = net.addSwitch("s3", cls=OVSKernelSwitch, failMode='standalone')

    # add h1 links
    net.addLink(h1, s1, intfName1='h1-eth0')
    net.addLink(h1, s2, intfName1='h1-eth1')
    net.addLink(h1, s3, intfName1='h1-eth2')

    # add h2 links
    net.addLink(h2, s1, intfName1='h2-eth0')
    net.addLink(h2, s2, intfName1='h2-eth1')
    net.addLink(h2, s3, intfName1='h2-eth2')

    # build
    net.build()

    # assign IP address to interface
    # h1
    h1.setIP(intf='h1-eth0', ip='192.168.45.2/24')
    h1.setIP(intf='h1-eth1', ip='192.168.45.3/24')
    h1.setIP(intf='h1-eth2', ip='192.168.45.4/24')

    # h2
    h2.setIP(intf='h2-eth0', ip='192.168.45.100/24')
    h2.setIP(intf='h2-eth1', ip='192.168.45.101/24')
    h2.setIP(intf='h2-eth2', ip='192.168.45.102/24')


    net.start()
    CLI(net)
    net.stop()

# start
if __name__ == '__main__':
    setLogLevel('info')
    myTopo()

