# Basic YDK-Py Apps
These apps illustrate simple examples of using YDK-Py to program a network. They do not require significant model or programming experience.  Each app uses a **single** model and they reside in a directory corresponding to the Python module path they use.  For instance, applications using the OpenConfig BGP model need to import the `ydk.models.bgp` Python model.  Therefore, you will find all the basic sample apps for that model under the `ydk/modules/bgp` directory.  

# Naming Convention
The application file names follow the following general structure:
```
<prefix>-<model>-<index>-ydk.py
```
Where
* `<prefix>` - Transport, main CRUD operation and type of data (config or oper)
* `<model>` - YANG model suffix
* `<index>` - Complexity level of the application. A higher number indicates higher complexity.

For instance, an application with file name `nc-read-config-ip-domain-10-ydk.py` represents a sample app using NETCONF transport to read IP domain configuration using the `Cisco-IOS-XR-ip-domain-cfg` model.  Apps may have one or more accompanying files with the same app base name, but different extensions.  These files capture the data (configuration or operational) that the app handles.  Data may be in log, CLI or in some cases, XML format.  All apps take a single command line argument in URL format.  This argument describes the connection details to the networking device (ssh://user:password@device:port).

# Boilerplate Apps
All apps with an index of 10 represent a boilerplate that can be used to create new apps.  The CRUD operation and logging is commented out.  In addition, a placeholder function to act on the top class is defined whenever relevant.  These boilerplate apps can be run, but will have no effect on the networking device.  If a model specifies configuration data, there will be four separate boilerplate apps to create, read, update and delete the data.  If a model specifies only configuration data, there will be a single boilerplate app to read the operational data.

# Running a Sample App
Unless specified by the app, all basic apps take a single argument specifying transport, credentials, target network device and port in URL notation:
```
$ ./nc-read-config-ip-domain-10-ydk.py ssh://admin:admin@10.0.0.1:830
```
