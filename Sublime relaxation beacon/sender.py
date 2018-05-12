from pyrebase import pyrebase
import nmap, time
ip='ip+/24'
nm = nmap.PortScanner() 
count={}
status=True

config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


while status ==True:
	nm.scan(hosts=ip, arguments='-sP')
	for h in nm.all_hosts():
		if 'mac' in nm[h]['addresses']:
			addr=nm[h]['addresses']['mac']
			print(addr)
			if not addr in count:
				count[addr]=1
			else :
				count[addr]+=1
			db.child("Send").child(addr).set(count[addr])


			
	#sleep(1000)
