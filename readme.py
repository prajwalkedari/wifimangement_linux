import wifimangement-linux as wifi

# to disable(off) the wifi
# wifi.off()

# to enable(on) the wifi
# wifi.on()

# connect the wifi to network(name as wifi-name or your wifi name ) if the password
# wifi.connect("wifi-name")

# connect the wifi to network(name as wifi-name with password) 
# wifi.connect("wifi-name","wifi-password")

# to scan local wi-fi network
# wifi.scan()

# get list of scan network
# wifi.list()

# share a connect wifi (information  and password)
# wifi.share()

# share a connect wifi (information  and password) with qr code 
# wifi.share("qr")

# it return connect wifi password (pass=wifi.share("psk")) it store password in pass)
# wifi.share("psk")

# it create hostop (with name as hostop-name and password as password ) =>note:- to off hostop and turn on wifi use (wifi.on())
# wifi.hostop("hostop-name","password")

# it return list out all  interface in pc (inter_list=wifi.interface_list()) its store list of interface in inter_list
# wifi.interface_list()

# it return   interfac stutus  in pc (inter_stutas=wifi.interface_status()) its store  interface status  in inter_status
# wifi.interface_status()

# it return   interfac configration in pc (inter_conf=wifi.interface_status()) its store  interface config in inter_conf
# wifi.interface_config()

# it return   interfac configration at certain interface in pc (inter_conf_wlan0=wifi.interface_status("wlan0")) its store  interface config of wlan0 in inter_conf_wlan
# wifi.interface_config("interface")

# return gateway of router (its an ip address of router)
# wifi.gateway()

# return ip addres of pc
# wifi.ip()

# its return wifi they password in dictory (dic=wifi.store()) its store all saved wifi and password in dictory name as div
# wifi.store()


# its print all saved wifi and password in nice table format
# wifi.printpsk()