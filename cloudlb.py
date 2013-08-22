#!/usr/bin/env python

import pyrax
import sys
from prettytable import PrettyTable

pyrax.set_setting("identity_type", "rackspace")

if (len(sys.argv) == 3):
    pyrax.set_credentials(sys.argv[1], sys.argv[2])
else:
    print "Usage: list.exhaust <username> <api key>"
    sys.exit(0)

print "=" * 24
print "  Cloud Load Balancers  "
print "=" * 24

regions = ['dfw', 'iad', 'ord', 'syd']

x = PrettyTable(["Region", "Name", "ID", "Status",
                "Public IP", "ServiceNet IP", "Cluster"])
x.padding_width = 1
for n in regions:
    clb = pyrax.connect_to_cloud_loadbalancers(n.upper())
    lb = clb.list()
    for i in lb:
        x.add_row([n.upper(), i.name, i.id, i.status,
                  clb.get(i.id).sourceAddresses["ipv4Public"],
                  clb.get(i.id).sourceAddresses["ipv4Servicenet"],
                  clb.get(i.id).cluster])
print x
