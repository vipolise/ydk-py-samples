# Basic YDK-Py Apps
These apps illustrate simple examples of using YDK-Py to program the network. They do not require significant model or programming experience.  Each app uses a **single** model and they reside in a directory corresponding to the Python module path they use.  For instance, applications using the OpenConfig BGP model need to import the `ydk.models.bgp` Python model.  Therefore, you will find all the basic sample apps for that model under the `ydk/modules/bgp` directory.  

The application file names follow the following general structure:
```
<prefix>-<model>-<index>-ydk.py
```
Where
* `<prefix>` - Transport, main CRUD operation and type of data
* `<model>` - YANG model suffix
* `<index>` - Complexity level of the application. An index of 00 indicates the simplest app available for the model.

For instance, an application with file name `nc-read-config-ip-domain-10-ydk.py` represents a simple YDK-Py sample app using NETCONF transport to read IP domain configuration using the `Cisco-IOS-XR-ip-domain-cfg` model.

Apps may have one or more accompanying files with the same app base name, but different extensions.  These files capture the data (configuration or operational) that the app handles.  Data may be in XML or CLI format. XML files include NETCONF RPC details.  CLI files only include configuration data and have a `.txt` extension.
