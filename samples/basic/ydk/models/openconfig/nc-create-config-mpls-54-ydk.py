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
Create config for model openconfig-mpls.

usage: nc-create-config-mpls-54-ydk.py [-h] [-v] device

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
from ydk.models.openconfig import openconfig_mpls as oc_mpls
import logging


def config_mpls(mpls):
    """Add config data to mpls object."""
    # tunnel
    tunnel = mpls.lsps.constrained_path.Tunnel()
    tunnel.name = "LER1-LER2-t30"
    tunnel.config.name = "LER1-LER2-t30"
    # tunnel.config.type =  ## identity
    # tunnel.config.protection_style_requested =  ## identity
    # tunnel.type =  ## identity
    p2p_primary_paths = tunnel.p2p_tunnel_attributes.P2PPrimaryPaths()
    p2p_primary_paths.name = "DYNAMIC"
    p2p_primary_paths.config.name = "DYNAMIC"
    p2p_primary_paths.config.preference = 10
    # p2p_primary_paths.config.path_computation_method =   ## identity
    tunnel.p2p_tunnel_attributes.p2p_primary_paths.append(p2p_primary_paths)
    tunnel.p2p_tunnel_attributes.config.destination = "172.16.255.2"
    tunnel.bandwidth.config.set_bandwidth = 100000

    mpls.lsps.constrained_path.tunnel.append(tunnel)


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

    mpls = oc_mpls.Mpls()  # create config object
    config_mpls(mpls)  # add object configuration

    crud.create(provider, mpls)  # create object on NETCONF device
    provider.close()
    exit()
# End of script
