# Basic YDK-Py Apps
These apps illustrate simple examples of using YDK-Py to program a network device. They do not require significant model or programming experience.  Apps are grouped in separate directories by service (e.g. CRUD, Codec, Netconf, Executor).  Within each service, each app uses a **single** model and they reside in a specific directory corresponding to the Python module path they use.  For instance, applications using the OpenConfig BGP model need to import the `ydk.models.openconfig` Python module.  You will find all the OpenConfig BGP sample apps that use the CRUD service under the `crud/models/openconfig/openconfig-bgp` directory.  Similarly, you will find all the OpenConfig BGP samples apps that use the Codec service under the `codec/models/openconfig/openconfig-bgp` directory.

# Naming Convention
The application file names follow the following general structure:
```
<prefix>-<model>-<index>-ydk.py
```
Where
* `<prefix>` - provider and service operation
* `<model>` - YANG model name (generally, abbreviated)
* `<index>` - relative complexity level of the application. A higher number indicates higher complexity.

For instance, an application with file name `nc-read-xr-ip-ntp-oper-10-ydk.py` represents a very basic app using NETCONF protocol to read NTP state based on the `Cisco-IOS-XR-ip-ntp-oper` model.  Apps may have one or more accompanying files with the same app base name, but different extensions.  These files capture the data (configuration or operational) that the app handles.  Data may be in CLI or XML format.  

# Boilerplate Apps for Model Specific Apps
Applications with an index of 10 are boilerplates that can be used to create custom apps.  Most boilerplate applications have a placeholder function to act on the top object.  When a model specifies configuration data, there will be four separate boilerplate apps for the CRUD service (create, read, update and delete) and one for the Codec service (encode).  If a model specifies only operational data, there will be a single boilerplate app for the CRUD service (read) and a single boilerplate for the Codec service (encode).  The boilerplate apps can be executed, but have no effect on the networking device.  The service operation is commented out.

# Running a Sample App
Unless specified by the app, all basic apps take two command line arguments.  An optional argument (-v | --verbose) to enable logging and a mandatory argument in URL format that describes the connection details to the networking device (ssh://user:password@device:port):
```
$ ./nc-read-xr-ip-ntp-oper-10-ydk.py ssh://admin:admin@10.0.0.1
```
