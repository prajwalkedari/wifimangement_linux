import os 

def off():
	os.system("nmcli radio wifi off")

def on():
        os.system("nmcli radio wifi on")
        
def connect(ssid,password=""):
	if password=="":
		print(f"nmcli dev wifi connect {ssid}")
		os.system(f"nmcli dev wifi connect {ssid}")
	else:
		os.system(f"nmcli dev wifi connect {ssid} password {password}")
		
	
def scan():
	os.system("nmcli dev wifi rescan")

def list():
	ls=os.popen("nmcli dev wifi list").read()
	return ls

def share(opt=""):
	if opt == "qr":
		os.system("nmcli dev wifi show-password")
		sh=0
	elif opt =="psk" or opt =="password" or  opt =="paskey":
		l = os.popen("nmcli dev wifi show-password").read()
		sh=l.split("\n")[2].split(":")[1]
	else:
		sh=os.popen("nmcli dev wifi show-password").read()
	return sh
	
def hospot(ssid,password):
	os.system("nmcli dev wifi hotspot ssid {ssid} password {password}")
	
def interface_list():
	i=os.listdir("/sys/class/net/")
	return i
def interface_status():
	in_s=os.popen("nmcli dev status").read()
	in_s.replace(r"\n", " \n ")
	return in_s
def interface_config(i=""):
	if i!="":
		in_s=os.popen(f"iwconfig {i}").read()
	else:
		in_s=os.popen("ifconfig").read()
	return in_s
	

def getinfo():
	name=[]
	psk=[]
	path = "/etc/NetworkManager/system-connections"
	os.chdir(path)
	wifiname = os.listdir()
	for wifi in wifiname:
		try:
			files=open(wifi,"r")
			files=files.read()
			files=files.split('\n')
			wifiname=[b.split("=")[1] for b in files if "id=" in b][0]
			password=[b.split("=")[1] for b in files if "psk=" in b][0]
			name.append(wifiname)
			psk.append(password)
		except IndexError:
			name.append(wifiname)
			psk.append(" ")
		except PermissionError:
			print("this need an root Permission to read accces \n give sudo permission(Enter sudo before files")
			break
	return name, psk

def gateway():
	ip_i=os.popen("ip r | grep -i default").read()
	ip_i=ip_i.split("via ")[1]
	ip_i=ip_i.split(" dev")[0]					
	return ip_i	
def ip():
	ip_i=os.popen("ip r | grep -i src").read()
	ip_i=ip_i.split("src ")[1]
	ip_i=ip_i.split(" metric")[0]					
	return ip_i	


def store():
	name,psk=getinfo()
	dic={}
	for wifi in name:
		for p in psk :
			dic[wifi]=p
			psk.remove(p)
			break
	return dic

def print_psk():
	name,psk=getinfo()
	print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
	print("----------------------------------------------")
	for i in name:
		for j in psk:
			print("{:<30}| {:<}".format(i , j))
			psk.remove(j)
			break
			

a=store()
print(a)
a=print_psk()
print(a)			    
			    

 
