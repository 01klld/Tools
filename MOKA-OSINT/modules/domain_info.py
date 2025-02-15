import requests

def lookup(domain):
    # Implement domain information lookup logic here
    info = {}
    response = requests.get(f"https://api.domaintools.com/v1/{domain}/whois")
    if response.status_code == 200:
        info = response.json()
    return info
