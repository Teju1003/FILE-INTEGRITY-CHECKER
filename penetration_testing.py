import requests
import socket
import whois
import nmap

def banner_grabbing(target):
    """Perform banner grabbing on the target."""
    try:
        s = socket.socket()
        s.connect((target, 80))
        s.send(b'HEAD / HTTP/1.1\r\nHost: ' + target.encode() + b'\r\n\r\n')
        response = s.recv(1024).decode()
        print("\n[+] Banner Grabbing Result:\n", response)
    except Exception as e:
        print("[-] Banner grabbing failed:", e)

def whois_lookup(domain):
    """Perform WHOIS lookup."""
    try:
        info = whois.whois(domain)
        print("\n[+] WHOIS Lookup Result:\n", info)
    except Exception as e:
        print("[-] WHOIS lookup failed:", e)

def port_scan(target):
    """Perform a basic port scan using Nmap."""
    scanner = nmap.PortScanner()
    print("\n[*] Scanning target:", target)
    scanner.scan(target, '1-1024')
    for host in scanner.all_hosts():
        print(f"[+] Host: {host} ({scanner[host].hostname()})")
        print(f"[+] State: {scanner[host].state()}")
        for proto in scanner[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = scanner[host][proto].keys()
            for port in ports:
                print(f"Port: {port}, State: {scanner[host][proto][port]['state']}")

def main():
    target = input("Enter the target domain/IP: ")
    banner_grabbing(target)
    whois_lookup(target)
    port_scan(target)
    print("\n[+] Penetration Testing Completed.")

if __name__ == "__main__":
    main()