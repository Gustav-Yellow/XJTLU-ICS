from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import Host
from mininet.node import OVSKernelSwitch
from mininet.log import setLogLevel, info

def myTopo():
    net = Mininet( topo=None, autoSetMacs=True, build=False, ipBase='10.0.1.0/24')

    # add host and switch
    h1 = net.addHost( 'h1', cls=Host, defaultRoute=None)
    h2 = net.addHost( 'h2', cls=Host, defaultRoute=None)
    h3 = net.addHost( 'h3', cls=Host, defaultRoute=None)

    s1 = net.addSwitch( 's1', cls=OVSKernelSwitch, failMode='standalone')

    # add links
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)

    # Assign IP address to interface
    h1.setIP(intf="h1-eth0",ip='10.0.1.2/24')
    h2.setIP(intf="h2-eth0",ip='10.0.1.3/24')

    # Network build and start
    net.build()
    net.start()

    # CLI mode running
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myTopo()

