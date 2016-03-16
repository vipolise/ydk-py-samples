# Sample Apps for YDK-Py
This repository provides a collection of sample applications that use [YDK-Py](https://github.com/CiscoDevNet/ydk-py) for network programmability.  YDK-Py is the Python package for the Cisco YANG development kit (YDK) which provides model-driven APIs generated from a variety of YANG models.  

# A "hello, world" App
The `hello-ydk.py` script illustrates a minimalistic app that prints the uptime of a device running Cisco IOS XR.  The script opens a NETCONF session to a device with address 10.0.0.1, reads the system time and prints the formatted uptime.

```python
from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.shellutil import Cisco_IOS_XR_shellutil_oper as xr_shellutil_oper
from datetime import timedelta


if __name__ == "__main__":
    """Main execution path"""

    # create NETCONF session
    session = NetconfServiceProvider(address="10.0.0.1",
                                     port=830,
                                     username="admin",
                                     password="admin",
                                     protocol="ssh")
    # create CRUD service
    crud = CRUDService()

    system_time = xr_shellutil_oper.SystemTime()  # create oper object
    system_time = crud.read(session, system_time)  # read object from device
    print "System uptime is", str(timedelta(seconds=system_time.uptime.uptime))

    session.close()
    exit()
```

Sample output
```
$ ./hello-ydk.py
System uptime is 5 days, 3:52:08
$
```

# Sample App Library
Sample apps in this repository are classified as either basic or intermediate.  They have the following characteristics:

* Basic apps: focus on a single model and have no or minimal programming logic (conditionals, loops, etc).  They should be your starting point if you don't have strong experience with models or with programming.  They are grouped by model.

* Intermediate: may have some programming logic and combine more than one model.  They are classified separately by use case.

## Installation
The sample apps do not require any special installation, but they do require that YDK-Py is  installed.  First, verify that you have Python 2.7 (or later) installed:
```
$ python --version
Python 2.7.6
$
```
[Download](https://github.com/CiscoDevNet/ydk-py/archive/master.zip) or clone the [YDK-Py repository](https://github.com/CiscoDevNet/ydk-py).  Then, follow the installation instructions for YDK-Py in its README file.

## Running an App
Instructions for using the basic apps can be found in their [README](https://github.com/CiscoDevNet/ydk-py-samples/tree/master/samples/basic) file.
