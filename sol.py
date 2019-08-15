import os
import time
import ipaddress
from subprocess import Popen,PIPE

ipa=str()
def System_ip_add():
	stdout=Popen("hostname -I",shell=True,stdout=PIPE).stdout
	ip=stdout.read()
#	print(ip)
	ip=list(map(str,ip.split()))	
	ip4 = str(ip[0][2:len(ip[0])-1])
	#print(ip4)
	return ip4
	#print (str(ipaddress.IPv4Address(ip[0])))

def work():
	
	os.system("ettercap -T -s ' s(5)cq' -L /tmp/dump > log.txt")
	#os.system("netstat -t -u -n > net.txt")
	f = open('log.txt','r')
	lines = f.readlines()
	i=0
	for line in lines:
		i+=1
		if line == 'Connections list:\n':
			break
	i+=1
	f.close()
	f = open('parsed.csv','w')
	while lines[i]!='\n':
		cells = lines[i].split()
		if len(cells)==9:
			if  '255' in cells[2] or '::' in cells[0]:
				i+=1
				continue
			row = cells[0]+','+cells[2]+','+cells[3]+','+cells[4]+','+cells[6]+','+cells[8]+'\n'
			f.write(row)


		i+=1
	f.close()
	
def service():
	f = open('parsed.csv','r')
	g=open('ser.txt','r')
	r=f.readlines()
	s=g.readlines()
	#print(ipa)
	ipa = System_ip_add()
	for line in r:	
		i=0
		out=str()
		cells = line.split(',') 
		#print(cells)
		if ipa in cells[1]:
			serv=cells[0].split(':')
		else:
			serv = cells[1].split(':')
		#print(serv)
		if(serv[0] in '255.255.255.255') or ('::' in cells[0]):
			continue
		if (serv[1]!=''):				
			print(serv[1])

			for y in s:
				if serv[1] in y:
					sp=y.split(',')
					# if(sp[0]==None):
					# 	pass
					# else:
					print(sp[0])
					return sp[0]



	f.close()
	g.close()

work()
# service()