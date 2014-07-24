#!/usr/bin/env python
# -*- coding: utf-8 -*-

DNS = {
    # Cogeco Cable (Trois-rivieres) 
    'cogeco.ca': ['205.151.69.200','205.151.68.200'],
    
    # Videotron.CA 
    'videotron.ca': ['205.151.222.250', '205.151.222.251'],
    
    # Colbanet
    'colba.net': ['69.28.239.8', '69.28.239.9'],
    }

prefix = (
"""
""")

template_host = (
"""
define host {
       use                      generic-host
       host_name                %(host)s
       address                  %(host)s
       alias                    %(host)s
       check_command            check_dummy!0!OK
}
""")

template_service = (
"""
define service {
       use                      generic-service
       host_name                %(host)s
       check_command            check_dig_service!%(ip)s!www.gouv.qc.ca
       display_name             %(host)s (%(ip)s)
       service_description      %(ip)s
       servicegroups            group-dns
       labels                   order_%(order)d
}
""")

postfix = (
"""
define host {
       use                            generic-host
       host_name                      DNS
       alias                          DNS
       check_command                  check_dummy!0!OK
}
define service {
       use                              generic-service
       host_name                        DNS
       service_description              DNS
       hostgroups                       group-dns
       check_command                    bp_rule!%(all_dns)s
       business_rule_output_template    $(x)$
       servicegroups                    group-dns
       labels                           order_0
       icon_image                       fa-gears
       notes                            Vérifie les principaux serveurs DNS.
}
""")


def main():
    print prefix
    all_dns = []
    order = 1
    for host, ips in DNS.iteritems():
        print template_host % {'host': host}
        for ip in ips:
            print template_service % {'host': host, 'ip': ip, 'order': order}
            all_dns.append('%(host)s,%(ip)s' % {'host': host, 'ip': ip})
            order += 1
    print postfix % {'all_dns': '&'.join(all_dns)}
        

if __name__ == '__main__':
    main()