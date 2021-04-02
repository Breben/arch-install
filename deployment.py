import nmap3, re, paramiko, scp

# Modify these variables to suit you
NETWORK = "192.168.1.0/24"
PASSWORD = "root"

# Retrieve IP addresses connected to the network
nmap = nmap3.NmapHostDiscovery()
results = nmap.nmap_no_portscan(NETWORK)

# Retain only IPv4 results
for ip in results.keys():
    if re.match(r'([0-9]{1,3}\.){3}[0-9]{1,3}', ip):
        
        # SSH connection to remote machines
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = ip, username = 'root', password = PASSWORD)

        # Copy scripts from server to remote machines
        with scp.SCPClient(client.get_transport()) as copy:
            copy.put(['arch-install_1.py', 'arch-install_2.py'])

        # Run the newly first transferred script
        stdin, stdout, stderr = client.exec_command('python arch-install_1.py')

        # Display the output in real time
        while True:
            line = stdout.readline()
            if not line:
                break
            print(line, end="")
        
        client.exec_command('reboot')

        client.close()