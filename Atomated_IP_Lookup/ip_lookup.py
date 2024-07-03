import sys
import requests

# Define the URL endpoint for fetching IP information
URL_TEMPLATE = "https://ipinfo.io/{}"

def fetch_ip_info(ip):
    # Fetch information for the IP address using requests
    response = requests.get(URL_TEMPLATE.format(ip))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching information for {ip}: {response.status_code}")
        return None

def main():
    # Check if the file containing IP addresses is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <ip_list_file>")
        return

    ip_list_file = sys.argv[1]

    # Read IP addresses from the provided file
    with open(ip_list_file, "r") as file:
        ip_addresses = file.read().splitlines()

    # Iterate through each IP address and fetch information
    for ip in ip_addresses:
        ip_info = fetch_ip_info(ip)
        if ip_info:
            print(ip_info)

if __name__ == "__main__":
    main()
