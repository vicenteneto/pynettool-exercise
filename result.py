import pynettool

with pynettool.NetworkElement('171.0.2.45') as ne:
    for route in ne.routing_table:
        print '{:>15} -> {}'.format(route.name, route.ip_addr)
