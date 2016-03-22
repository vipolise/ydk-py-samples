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
# nc-create-config-bgp-10-ydk.py
# Create config for model openconfig-bgp. Additions to
# config data are contained in the config_bgp() function.
#

from argparse import ArgumentParser
from urlparse import urlparse

from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.bgp import bgp as oc_bgp
# import logging


# add config data to 'bgp' object
def config_bgp(bgp):
    pass


if __name__ == "__main__":
    """Main execution path.  Takes target device URL as single argument. URL
    must have format ssh://user:password@host:port"""
    parser = ArgumentParser()
    parser.add_argument("device",
                        help="NETCONF device (ssh://user:password@host:port)")
    device = urlparse(parser.parse_args().device)

    # YDK logger
    # logger = logging.getLogger("ydk")
    # logger.setLevel(logging.DEBUG)
    # handler = logging.FileHandler("nc-create-config-bgp-10-ydk.log")
    # formatter = logging.Formatter(("%(asctime)s - %(name)s - "
    #                                "%(levelname)s - %(message)s"))
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)

    # create NETCONF provider
    provider = NetconfServiceProvider(address=device.hostname,
                                      port=device.port,
                                      username=device.username,
                                      password=device.password,
                                      protocol=device.scheme)
    # create CRUD service
    crud = CRUDService()

    bgp = oc_bgp.Bgp()  # create config object
    config_bgp(bgp)  # add object configuration

    # crud.create(provider, bgp)  # create object on NETCONF device
    provider.close()
    exit()
# End of script
