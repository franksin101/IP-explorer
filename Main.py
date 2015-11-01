import os


ipv4 = [192, 168, 1, 128]
submask = [255, 255, 255, 0]
gateway = [192, 168, 1, 1]

dns1 = [8, 8, 8, 8]
dns2 = [8, 8, 4, 4]

def run() :
	for way in range(1, 256):
		ipv4[2] = way
		gateway[2] = way
		#print("IPv4 : " + '.'.join([str(e) for e in ipv4]))
		#print("Gateway : " + '.'.join([str(e) for e in gateway]))
		#os.system("netsh interface ipv4 set address name=\"Wi-Fi\" source=static address="+'.'.join([str(e) for e in ipv4]) + "mask=255.255.255.0" + " gateway=" + '.'.join([str(e) for e in gateway]))
		#print("netsh interface ipv4 set address name=\"Wi-Fi\" source=static address="+ '.'.join([str(e) for e in ipv4]) + " mask=255.255.255.0 " + " gateway=" + '.'.join([str(e) for e in gateway]))
		#print("netsh interface ipv4 add dnsserver name=\"Wi-Fi\" address=8.8.8.8 index=1")
		#print("netsh interface ipv4 add dnsserver name=\"Wi-Fi\" address=8.8.4.4 index=2")
		#cmd0 = "netsh interface ipv4 set address name=\"Wi-Fi\" source=static address="+ '.'.join([str(e) for e in ipv4]) + " mask=255.255.255.0 " + " gateway=" + '.'.join([str(e) for e in gateway])
		#cmd1 = "netsh interface ipv4 add dnsserver name=\"Wi-Fi\" address=8.8.8.8 index=1"
		#cmd2 = "netsh interface ipv4 add dnsserver name=\"Wi-Fi\" address=8.8.4.4 index=2"
		#os.system(cmd0)
		#os.system(cmd1)
		#os.system(cmd2)
		#ping = os.popen("ping " + '.'.join([str(e) for e in gateway])).read()
		
		# tmp = os.popen("echo %cd%").read()
		# print(tmp)
		
		#os.system("Pause")

if __name__=="__main__":
	run()