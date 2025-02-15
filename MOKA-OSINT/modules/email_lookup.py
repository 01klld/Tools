import requests

def lookup(email):
    # Implement email address lookup logic here
    info = {}
    response = requests.get(f"https://api.emailhunter.co/v2/email-verifier?email={email}")
    if response.status_code == 200:
        info = response.json()
    return info
