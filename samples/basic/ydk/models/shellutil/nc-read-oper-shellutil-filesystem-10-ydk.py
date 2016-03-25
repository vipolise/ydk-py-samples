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
# nc-read-oper-shellutil-filesystem-10-ydk.py
# Read all data for model Cisco-IOS-XR-shellutil-filesystem-oper.  Actions performed on
# the data are contained in the process_file_system() function.
#

from argparse import ArgumentParser
from urlparse import urlparse

from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.shellutil import Cisco_IOS_XR_shellutil_filesystem_oper as xr_shellutil_filesystem_oper
import logging


# process data in 'file_system' object
def process_file_system(file_system):
    pass


if __name__ == "__main__":
    """Main execution path.  Takes target device URL as single argument. URL
    must have format ssh://user:password@host:port"""
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

    file_system = xr_shellutil_filesystem_oper.FileSystem()  # create oper object
    # file_system = crud.read(provider, file_system)  # read object from NETCONF device
    process_file_system(file_system)  # process object data

    provider.close()
    exit()
# End of script
