import requests
from bs4 import BeautifulSoup

def check_sql_injection(url):
    """Check for SQL Injection vulnerability."""
    payload = "' OR '1'='1"
    test_url = url + payload
    response = requests.get(test_url)
    
    if "error in your SQL syntax" in response.text.lower():
        print(f"[!] SQL Injection vulnerability detected at {url}")
    else:
        print(f"[-] No SQL Injection vulnerability found at {url}")

def check_xss(url):
    """Check for XSS vulnerability."""
    payload = "<script>alert('XSS')</script>"
    test_url = url + payload
    response = requests.get(test_url)
    
    if payload in response.text:
        print(f"[!] XSS vulnerability detected at {url}")
    else:
        print(f"[-] No XSS vulnerability found at {url}")

def enumerate_directories(url, wordlist):
    """Check for accessible directories."""
    print("[*] Checking for common directories...")
    
    for directory in wordlist:
        full_url = f"{url}/{directory}/"
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"[!] Found accessible directory: {full_url}")

def main():
    url = input("Enter the target URL (e.g., http://example.com): ")
    
    print("\nStarting vulnerability scan...")
    check_sql_injection(url)
    check_xss(url)
    
    common_dirs = ["admin", "login", "uploads", "backup", "config"]
    enumerate_directories(url, common_dirs)
    
    print("\nScan completed.")

if __name__ == "__main__":
    main()
