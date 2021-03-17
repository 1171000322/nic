import os
import commands

os.system('ovs-ofctl del-flows br1 ')
os.system('ovs-ofctl add-flow br1 "priority=1,in_port=1,actions=output:4"')
os.system('ovs-ofctl add-flow br1 "priority=1,in_port=4,actions=output:1"')

#os.system('ovs-ofctl add-flow vswitch0 "priority=1,in_port=1,actions=output:4"')
#os.system('ovs-ofctl add-flow vswitch0 "priority=2,in_port=4,actions=output:1"')
