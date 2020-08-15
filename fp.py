#!/usr/bin/python3

import os

with open ("football-players.txt","r") as file:
	
	ftext = file.read()
	file.seek(0)
	satır = ftext.count("\n")
	sk = list(ftext.split("\n"))[:-1]
	

with open("realmadrid.txt","w") as file1:
	file1.write("\nREAL MADRID PLAYERS\n\n")
	with open("manchesterunited.txt","w") as file2:
		file2.write("\nMANCHESTER UNITED PLAYERS\n\n")
		with open("barcelona.txt","w") as file3:
			file3.write("BARCELONA PLAYERS\n\n")
			for i in range(satır):
				
				sk[i] = [sk[i]]
				sk[i] = sk[i][0].split(",")
				
				
			for j in range(satır):
				
				if sk[j][1] == "Real Madrid":
					file1.write(sk[j][0])
					file1.write("\n")	
				elif sk[j][1] == "Manchester":
					file2.write(sk[j][0])
					file2.write("\n")
				elif sk[j][1] == "Barcelona":
					file3.write(sk[j][0])
					file3.write("\n")

os.system("cat barcelona.txt")
os.system("cat manchesterunited.txt")
os.system("cat realmadrid.txt")
