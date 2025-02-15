import requests

def lookup(phone_number):
    # Implement phone number lookup logic here
    info = {}
    response = requests.get(f"https://api.numlookupapi.com/v1/validate?number={phone_number}")
    if response.status_code == 200:
        info = response.json()
    return info
