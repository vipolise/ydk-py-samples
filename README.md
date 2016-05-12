# Sample Apps for YDK-Py
This repository provides a collection of sample applications that use [YDK-Py](https://github.com/CiscoDevNet/ydk-py) for network programmability.  YDK-Py is the Python package for the Cisco YANG development kit (YDK) which provides model-driven APIs generated from a variety of YANG models.  

## A "hello, world" App
The `hello-ydk.py` script illustrates a minimalistic app that prints the uptime of a device running Cisco IOS XR.  The script opens a NETCONF session to a device with address 10.0.0.1, reads the system time and prints the formatted uptime.

```python
# import providers, services and models
from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.shellutil import Cisco_IOS_XR_shellutil_oper \
    as xr_shellutil_oper
from datetime import timedelta


if __name__ == "__main__":
    """Main execution path"""

    # create NETCONF session
    provider = NetconfServiceProvider(address="10.0.0.1",
                                      port=830,
                                      username="admin",
                                      password="admin",
                                      protocol="ssh")
    # create CRUD service
    crud = CRUDService()

    # create system time object
    system_time = xr_shellutil_oper.SystemTime()

    # read system time from device
    system_time = crud.read(provider, system_time)

    # print system uptime
    print("System uptime is" +
          str(timedelta(seconds=system_time.uptime.uptime)))

    # close NETCONF session and exit
    provider.close()
    exit()
```

Sample output
```
$ ./hello-ydk.py
System uptime is 5 days, 3:52:08
$
```

## Sample App Library
This repository include a large number of basic sample apps. They focus on a single model and have no or minimal programming logic (conditionals, loops, etc).  They should be your starting point if you don't have strong experience with models or with programming.  They are grouped by model.

## Installation
The sample apps do not require any special installation, but they do require that YDK-Py is installed
```
$ pip list | grep ydk
ydk (0.4.0)
$
```

If it is not installed, verify first that you have Python 2.7 (or later) installed:
```
$ python --version
Python 2.7.6
$
```
[Download](https://github.com/CiscoDevNet/ydk-py/archive/master.zip) or clone the [YDK-Py repository](https://github.com/CiscoDevNet/ydk-py).  Then, follow the installation instructions for YDK-Py in its README file.

## Running an App
Instructions for using the basic apps can be found in their [README](https://github.com/CiscoDevNet/ydk-py-samples/tree/master/samples/basic) file.  For Cisco IOS XR models, you would need a device running version 6.0.0 or later as the target.

## Vagrant Sandbox
You can instantiate a YDK-PY sandbox on your computer using Vagrant.  The sandbox will provide an Ubuntu (14.04) VM with YDK-Py pre-installed.  Make sure you have these prerequisites installed on your computer:
* [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* An ssh client
* ssh keys generated on your system

To create a sandbox, issue the following command from the directory where the `Vagrantfile` resides:
```
$ vagrant up
```

To verify the status of your sandbox use:
```
$ vagrant status
```

Once your sandbox is running, you can connect to it using:
```
$ vagrant ssh
```

Note that the `samples` and `projects` directories are shared between your host and your Vagrant box.  Any changes to those directories are seen in both environments.  Any other data in your Vagrant box is isolated from your host and will be lost if you destroy your Vagrant box.

You can suspend and resume your sandbox using:
```
$ vagrant suspend
$ vagrant resume
```

To destroy your sandbox, issue the following command:
```
$ vagrant destroy
```
