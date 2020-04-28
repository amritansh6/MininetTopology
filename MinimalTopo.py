from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSSwitch
class MinimalTopo( Topo ):  
    "Simple topology example."
    def __init__( self ):
        "Create custom topo."
        # Initialize topology
        Topo.__init__( self )
        
        
        h11 = self.addHost( 'h1r1' ,ip='10.0.1.1', mac='00:00:00:00:00:11')
        h21 = self.addHost( 'h2r1',ip='10.0.2.1', mac='00:00:00:00:00:21' )
        h31 = self.addHost( 'h3r1' ,ip='10.0.3.1', mac='00:00:00:00:00:31')
        h41 = self.addHost( 'h4r1' ,ip='10.0.4.1', mac='00:00:00:00:00:41')

        h12 = self.addHost( 'h1r2',ip='10.0.1.2', mac='00:00:00:00:00:12' )
        h22 = self.addHost( 'h2r2',ip='10.0.2.2', mac='00:00:00:00:00:22' )
        h32 = self.addHost( 'h3r2' ,ip='10.0.3.2', mac='00:00:00:00:00:32')
        h42 = self.addHost( 'h4r2' ,ip='10.0.4.2', mac='00:00:00:00:00:42')

        h13 = self.addHost( 'h1r3' ,ip='10.0.1.3', mac='00:00:00:00:00:13')
        h23 = self.addHost( 'h2r3' ,ip='10.0.2.3', mac='00:00:00:00:00:23')
        h33 = self.addHost( 'h3r3' ,ip='10.0.3.3', mac='00:00:00:00:00:33')
        h43 = self.addHost( 'h4r3' ,ip='10.0.4.3', mac='00:00:00:00:00:43')

        h14 = self.addHost( 'h1r4',ip='10.0.1.4', mac='00:00:00:00:00:14' )
        h24 = self.addHost( 'h2r4',ip='10.0.2.4', mac='00:00:00:00:00:24' )
        h34 = self.addHost( 'h3r4' ,ip='10.0.3.4', mac='00:00:00:00:00:34')
        h44 = self.addHost( 'h4r4',ip='10.0.4.4', mac='00:00:00:00:00:44' )


        s0 = self.addSwitch('s0')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 =self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        # Add links
        # Add links
        self.addLink( h11, s1 )
        self.addLink( h21, s1 )
        self.addLink( h31, s1 )
        self.addLink( h41, s1 )

        self.addLink( h12, s2 )
        self.addLink( h22, s2 )
        self.addLink( h32, s2 )
        self.addLink( h42, s2 )

        self.addLink( h13, s3 )
        self.addLink( h23, s3 )
        self.addLink( h33, s3 )
        self.addLink( h43, s3 )

        self.addLink( h14, s4 )
        self.addLink( h24, s4 )
        self.addLink( h34, s4 )
        self.addLink( h44, s4 )

        self.addLink( s0, s1)
        self.addLink( s0, s2)
        self.addLink( s0, s3)
        self.addLink( s0, s4)
def runMinimalTopo():
    
    
    net = Mininet(
        controller=lambda name: RemoteController( name, ip='127.0.0.1' ),
        switch=OVSSwitch,
        autoSetMacs=True )
    net.addController('c0')

    h11 = net.addHost( 'h1r1' ,ip='10.0.1.1', mac='00:00:00:00:00:11')
    h21 = net.addHost( 'h2r1',ip='10.0.2.1', mac='00:00:00:00:00:21' )
    h31 = net.addHost( 'h3r1' ,ip='10.0.3.1', mac='00:00:00:00:00:31')
    h41 = net.addHost( 'h4r1' ,ip='10.0.4.1', mac='00:00:00:00:00:41')

    h12 = net.addHost( 'h1r2',ip='10.0.1.2', mac='00:00:00:00:00:12' )
    h22 = net.addHost( 'h2r2',ip='10.0.2.2', mac='00:00:00:00:00:22' )
    h32 = net.addHost( 'h3r2' ,ip='10.0.3.2', mac='00:00:00:00:00:32')
    h42 = net.addHost( 'h4r2' ,ip='10.0.4.2', mac='00:00:00:00:00:42')

    h13 = net.addHost( 'h1r3' ,ip='10.0.1.3', mac='00:00:00:00:00:13')
    h23 = net.addHost( 'h2r3' ,ip='10.0.2.3', mac='00:00:00:00:00:23')
    h33 = net.addHost( 'h3r3' ,ip='10.0.3.3', mac='00:00:00:00:00:33')
    h43 = net.addHost( 'h4r3' ,ip='10.0.4.3', mac='00:00:00:00:00:43')

    h14 = net.addHost( 'h1r4',ip='10.0.1.4', mac='00:00:00:00:00:14' )
    h24 = net.addHost( 'h2r4',ip='10.0.2.4', mac='00:00:00:00:00:24' )
    h34 = net.addHost( 'h3r4' ,ip='10.0.3.4', mac='00:00:00:00:00:34')
    h44 = net.addHost( 'h4r4',ip='10.0.4.4', mac='00:00:00:00:00:44' )

    s0 = net.addSwitch('s0')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    # Add links
    net.addLink( h11, s1 )
    net.addLink( h21, s1 )
    net.addLink( h31, s1 )
    net.addLink( h41, s1 )

    net.addLink( h12, s2 )
    net.addLink( h22, s2 )
    net.addLink( h32, s2 )
    net.addLink( h42, s2 )

    net.addLink( h13, s3 )
    net.addLink( h23, s3 )
    net.addLink( h33, s3 )
    net.addLink( h43, s3 )

    net.addLink( h14, s4 )
    net.addLink( h24, s4 )
    net.addLink( h34, s4 )
    net.addLink( h44, s4 )

    net.addLink( s0, s1)
    net.addLink( s0, s2)
    net.addLink( s0, s3)
    net.addLink( s0, s4)

    
    net.start()

    
    CLI( net )

    
    net.stop()

if __name__ == '__main__':
    
    setLogLevel( 'info' )
    runMinimalTopo()

