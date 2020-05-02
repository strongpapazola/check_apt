# source
# https://itsfoss.com/could-not-get-lock-error/

# author : strongpapazola

import subprocess
from os import system
import sys

def banner():
	print('usage: python3 '+sys.argv[0]+' [--id/--rmfile]')

try:
	if sys.argv[1] == "--id":
		print('Killing Process apt')
		getProcess = subprocess.Popen('ps aux | grep apt', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8').splitlines()
		getProcess2 = []
		for i in getProcess:
			if i:
				getProcess2.append(i)
		result = []
		for i in getProcess2:
			getProcess4 = []
			i = i.split(' ')
			for j in i:
				if j:
					getProcess4.append(j)
			result.append(getProcess4)

		pid = []
		for i in result:
			pid.append(i[1])

		for i in pid:
			system('kill -9 %s &>/dev/null&' % (i,))
	elif sys.argv[1] == "--rmfile":
		print('remove apt file')
		system('sudo rm /var/lib/apt/lists/lock')
		system('sudo rm /var/cache/apt/archives/lock')
		system('sudo rm /var/lib/dpkg/lock')
		system('sudo dpkg --configure -a')
	else:
		banner()
except:
	banner()

