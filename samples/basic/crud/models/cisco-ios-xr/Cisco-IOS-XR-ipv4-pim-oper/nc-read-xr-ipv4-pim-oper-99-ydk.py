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
Read all data for model Cisco-IOS-XR-ipv4-pim-oper.

usage: nc-read-xr-ipv4-pim-oper-10-ydk.py [-h] [-v] device

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
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ipv4_pim_oper \
    as xr_ipv4_pim_oper
import logging
from ydk.types import READ


def setup_query(pim):
    """Set query data in pim object."""
    pim.active = pim.Active()
    pim.active.default_context = pim.active.DefaultContext()

def process_pim(pim):
    #summary = pim.active.default_context.summary
    summary = pim
    """Process the data in pim object."""
    print """\nPIM Summary for VRF:default\n
PIM State Counters\n
                            Current        Maximum        Warning-threshold"""
    print "Routes  ", summary.route_count, summary.route_limit, summary.route_limit
    print "Topology Interface States ", summary.topology_interface_state_count, summary.topology_interface_state_limit, summary.topology_interface_state_threshold
     

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

    pim = xr_ipv4_pim_oper.Pim()  # create object

    # read data from NETCONF device
    setup_query(pim)
    pim = crud.read(provider, pim.active.default_context.summary)
    process_pim(pim)  # process object data
    

    provider.close()
    exit()
# End of script
