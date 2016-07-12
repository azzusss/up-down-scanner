import os
import sys

start = ""
range1 = 0
range2 = 0

for carg in sys.argv:
	if carg == "-s":
		argnum = sys.argv.index(carg)
		argnum += 1
		start = sys.argv[argnum]
	elif carg == "-r1":
		argnum= sys.argv.index(carg)
		argnum += 1
		range1r = sys.argv[argnum]
		range1 = int(range1r)
	elif carg == "-r2":
		argnum = sys.argv.index(carg)
		argnum += 1
		range2r = sys.argv[argnum]
		range2 = int(range2r)
		
print ("[*] Up/Down Scanner Launched Successfully!")

if start == "":
	print ("[!] No Host Provided...")
elif range1 == 0:
	print ("[!] No range1 Provided...")
elif range2 == 0:
	print ("[!] No range2 Provided...")
else:
	if range1 > range2:
		count = range1 - range2
	elif range1 < range2:
		count = range2 - range1
	for ccount in range(range1, range2):
		target = start + "." + str(ccount)
		response = os.system("ping " + target + " 2>&1 >/dev/null")
		if response == 0:
			err = 0
		else:
			err = 1
		if err == 0:
			print ("[*] " + target + " looks up from here!") 
