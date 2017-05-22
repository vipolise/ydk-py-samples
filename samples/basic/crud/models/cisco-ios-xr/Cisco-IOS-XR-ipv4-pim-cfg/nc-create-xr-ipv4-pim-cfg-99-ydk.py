#!/usr/bin/env python
#
# Copyright 2016 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Create configuration for model Cisco-IOS-XR-ipv4-pim-cfg.

usage: nc-create-xr-ipv4-pim-cfg-10-ydk.py [-h] [-v] device

positional arguments:
  device         NETCONF device (ssh://user:password@host:port)

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print debugging messages
"""

from argparse import ArgumentParser
from urlparse import urlparse

from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ipv4_pim_cfg \
    as xr_ipv4_pim_cfg
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_policy_repository_cfg \
    as xr_rpl_cfg
import logging
from ydk.types import Empty


def config_rpl(rpl):
    """Add config data to rpl object."""
    rpl.route_policies = rpl.RoutePolicies()
    route_policy = rpl.route_policies.RoutePolicy()
    route_policy.route_policy_name = "rpf-for-one"
    route_policy.rpl_route_policy = """route-policy rpf-for-one
  set core-tree pim-default
end-policy""" 
    rpl.route_policies.route_policy.append(route_policy)

def config_pim(pim):
    """Add config data to pim object."""
    pim.default_context = pim.DefaultContext()
    pim.default_context.ipv4 = pim.default_context.Ipv4()
    pim.default_context.ipv4.interfaces = pim.default_context.ipv4.Interfaces()
    intf = pim.default_context.ipv4.interfaces.Interface()
    intf.interface_name = "Loopback0"
    intf.interface_enable = True
    pim.default_context.ipv4.interfaces.interface.append(intf)
    pim.default_context.ipv4.bsr = pim.default_context.ipv4.Bsr()
    pim.default_context.ipv4.bsr.candidate_bsr = pim.default_context.ipv4.bsr.CandidateBsr()
    pim.default_context.ipv4.bsr.candidate_bsr.address = "10.1.1.1"
    pim.default_context.ipv4.bsr.candidate_bsr.prefix_length = 24

    pim.vrfs = pim.Vrfs()
    vrf = pim.vrfs.Vrf()
    vrf.vrf_name = "one"
    vrf.ipv4 = vrf.Ipv4()
    vrf.ipv4.rpf = vrf.ipv4.Rpf()
    vrf.ipv4.rpf.route_policy = "rpf-for-one"
    vrf.ipv4.interfaces = vrf.ipv4.Interfaces()
    intf = vrf.ipv4.interfaces.Interface()
    intf.interface_name = "GigabitEthernet0/0/0/0"
    intf.interface_enable = True
    vrf.ipv4.interfaces.interface.append(intf)
    pim.vrfs.vrf.append(vrf)
       


if __name__ == "__main__":
    """Execute main program."""
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="print debugging messages",
                        action="store_true")
    parser.add_argument("device",
                        help="NETCONF device (ssh://user:password@host:port)")
    args = parser.parse_args()
    device = urlparse(args.device)

    # log debug messages if verbose argument specified
    if args.verbose:
        logger = logging.getLogger("ydk")
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(("%(asctime)s - %(name)s - "
                                      "%(levelname)s - %(message)s"))
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # create NETCONF provider
    provider = NetconfServiceProvider(address=device.hostname,
                                      port=device.port,
                                      username=device.username,
                                      password=device.password,
                                      protocol=device.scheme)
    # create CRUD service
    crud = CRUDService()

    rpl = xr_rpl_cfg.RoutingPolicy()
    config_rpl(rpl)

    pim = xr_ipv4_pim_cfg.Pim()  # create object
    config_pim(pim)  # add object configuration

    # create configuration on NETCONF device
    crud.create(provider, rpl)
    crud.create(provider, pim)
    #crud.read(provider, rpl)

    provider.close()
    exit()
# End of script
