# wifimangement_linux

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 

![](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-360/)   
its only and only for **Linux and Unix** ,work with [Nmcli](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-network_bridging_using_the_networkmanager_command_line_tool_nmcli0) .
basic wifi or network tool controlling with python

**Note => its not work with any _Windows_ os**
## what is wifimangement_linux ?
its an **_python module_** .
Its use for **_network or wifi controlling tool_** for  Linux/unix .
That prove  _many function_ such as enable, disable and connect ..etc .
Its give **_full acces_** in python to **_handle system wifi_**.

## Installation
Open **terminal**
``` bash
sudo pip3 install wifimangement_linux
```

# Function
**Note:-**   Before use import moduls like below way :
``` python3
import wifimangement_linux as wifi 
```
### Disable Wifi
to Disable(off) the wifi
``` python3
wifi.off()
```
### Enable Wifi
to enable(on) the wifi
``` python3
wifi.on()
```
## Connect

Connect the wifi to network(name as wifi-name or your wifi name ) if the password
```python3
wifi.connect("wifi-name")
```
connect the wifi to network(name as wifi-name with password) 
```python
wifi.connect("wifi-name","wifi-password")
```
## Scan
scan local wi-fi network
```python3
 wifi.scan()
```
## list
get list of scan network
```python3
wifi.list()
```
# share
share a connect wifi (information  and password)
```python
wifi.share()
```
share a connect wifi (information  and password) with qr code 
```python
wifi.share("qr")
```
it return connect wifi password (pass=wifi.share("psk")) it store password in pass)
```python3
wifi.share("psk")
```
## Hospot
it create hostop (with name as hostop-name and password as password ) =>note:- to off hostop and turn on wifi use (wifi.on())
```python3
wifi.hostop("hostop-name","password")
```
## Interface List
it return list out all  interface in pc 
```python3
wifi.interface_list()
```
## Interface Status
it return   interfac stutus  in pc 
``` python
wifi.interface_status()
```
## Interface Config
it return   interfac configration in pc 
```python3
wifi.interface_config()
```
it return   interfac configration at certain interface in pc 
```python
wifi.interface_config("interface")
```
## Gateway
return gateway of router (its an ip address of router)
```python3
wifi.gateway()
```
## Ip Address
return ip addres of pc
```python
wifi.ip()
```
## Store
its return wifi and they password in dictory type
```python3
wifi.store()
```
## print table 
its print all saved wifi and password in nice table format
```python
wifi.printpsk()
```
## License
[![](https://img.shields.io/github/license/prajwalkedari/wifi-password?style=plastic)](https://github.com/prajwalkedari/wifimangement_linux/blob/main/LICENSE)
## Requirement

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
Install python3 on pc:-

![](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

  
## 🔗 Links
[![linkedin](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/prajwalkedari/wifimangement_linux)
