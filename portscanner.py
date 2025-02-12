import socket
import termcolor


#checks how many targets and ports needs to be scanned
def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1, ports):
		scan_port(target, port)

#scanning the targets and prints their open ports with their banners
def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		try:
			banner = sock.recv(1024).decode()
			print("[+] Port {} is open with banner {}".format(port, banner))
			sock.close()
		except:
			print("[+] Port Opened " + str(port))
			sock.close()
	except:
		pass


targets = input("[*] Enter Targets to Scan(split them by ,): ")
ports = int(input("[*] Enter how many Ports do You want to Scan: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets, ports)

