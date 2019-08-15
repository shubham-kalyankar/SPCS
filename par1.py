import os
from subprocess import Popen,PIPE
def parser():
	count=0
	count1=list()
	success=0
	success1=list()
	guest=0
	guest1=list()
	urgent=0
	urgent1=list()
	ou1=list()
	total=list()
	failure=0
	failure1=list()
	f = open('parsed.csv','r')
	r=f.readlines()

	newFile = open('/var/log/auth.log','r')
	auth_lines=newFile.readlines()

	
	tmp_c=0
	count_test=0
	for line in r:	
		cells = line.split(',') 
		if ('T' in cells[2]):
			os.system("sudo etterlog -F tcp:"+cells[0]+":"+cells[1]+" /tmp/dump.ecp > /home/it/TY12/packets.txt")
		if ('U' in cells[2]):
			os.system("sudo etterlog -F udp:"+cells[0]+":"+cells[1]+" /tmp/dump.ecp > /home/it/TY12/packets.txt")
		# os.system(str1)
		newfile2=open('/home/it/TY12/packets.txt','r')
		for line in newfile2.readlines():
			urgent=0
			if ('TCP' in line) or ('UDP' in line):
				l_split=line.split()
				if 'U' in l_split[5]:
					urgent=urgent+1
		urgent1.append(urgent)
		count_test+=1



	
		newfile1=open('mylog.txt','w')
		for line in auth_lines:
			success=0
			failure=0
			if ('authentication failure' in line):
			    newfile1.write(line)
			if ('Successful su' in line):
			    # print (line)
			    
			    newfile1.write(line)
			if('changed user' in line) and ('guest' in line):
				newfile1.write(line)
			
		newfile1.close()
	# print("User Change count")
	# print (count);
	# print("success login")
	# print (success);
	# print("guest login")
	# print (guest);	
		newfile1=open('mylog.txt','r')
		my_log=newfile1.readlines()

		
		for line in my_log:
			tmp_c+=1
			count=0
			guest=0
			if('rhost=  'in line):
				count=count
			else:
				count=count+1;
			if('changed user' in line) and ('guest' in line):
				guest=guest+1
			# elif('user' not in line):
			# 	count=count;
			
			if ('authentication failure' in line):
			    failure+=1
			if ('Successful su' in line):
			    # print (line)
			    success=success+1
		count1.append(count)
		guest1.append(guest)
		success1.append(success)
		failure1.append(failure)
		
	# print("Total attempts")
	# print(total)
	#os.system("ps a | awk '{print $2}' | grep -vi 'tty*' | uniq | wc -l")
		stdout=Popen("ps a | awk '{print $2}' | grep -vi 'tty*' | uniq | wc -l",shell=True,stdout=PIPE).stdout
		output = stdout.read()
		
		ou=int(output)
		ou=ou-1
		ou1.append(ou)

		# print(ou)

		f.close()
		total.append(count+success+guest)

	print("urgent")
	print(urgent1)
	print("User Change count")
	print (count1);
	print("success login")
	print (success1);
	print("guest login")
	print (guest1);
	print("Total attempts")
	print(total)
	print("Number of shells")
	print(ou1)
	print(count_test)
	print(tmp_c)
	# os.system("sudo etterlog -F tcp:216.58.197.46:443:10.10.13.173:51832 /tmp/dump.ecp >/home/it/TY12/packets.txt")





