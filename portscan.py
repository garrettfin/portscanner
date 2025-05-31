import socket

port_definitions = {21:"FTP", 22:"SSH", 23:"Telnet", 25:"SMTP", 53:"DNS", 80:"HTTP",
                 110:"POP3", 135:"RPC", 139:"NetBIOS", 143:"IMAP", 194:"IRC", 443:"HTTPS", 
                 445:"SMB", 1433:"MSSQL", 3306:"MySQL", 3389:"RDP", 5900:"VNC"}

def port_scan (target_ip, target_ports):
    print(f"\nScanning {target_ip} ports....")

    for port in target_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        #Try establishing connection to each port
        try:
            s.connect((target_ip, port))
            print(f"Port {port}: {port_definitions.get(port)} is OPEN [✔]")
        except:
            print(f"Port {port}: {port_definitions.get(port)} is closed")


def main():
    #Get target ip address
    continueFlag = 1
    while (continueFlag):
        target_ip = input("Please enter the Web Address or IP Address you would like to scan: ")
        if target_ip and target_ip[0].isalpha():
            try:
                target_ip = socket.gethostbyname(target_ip)
                continueFlag = 0
            except:
                print(f"Could not establish an IP address for: {target_ip}")

    target_ports = []

    #Display port selection menu
    print("\nWhat ports do you want to scan?")
    print("1. Most Popular Ports")
    print("2. Custom Ports")
    menu_option = input("Select a menu option: ")

    #Create an array of the specified ports to be scanned
    if menu_option == "1":
        target_ports = [21,22,23,25,53,80,110,135,139,143,194,443,445,1433,3306,3389,5900]
    elif menu_option == "2":
        port_range = input("Enter the port range you would like to scan (i.e. '20-1024'): ")
        start_port = int(port_range.split('-')[0])
        end_port = int(port_range.split('-')[1])
        for port in range(start_port, end_port):
            target_ports.append(port)

    #Call the port scanning function
    port_scan(target_ip, target_ports)

if __name__ == "__main__":
    main()
