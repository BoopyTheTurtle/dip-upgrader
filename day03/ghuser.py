import requests 
import sys 

try: 
    response = requests.get('https://api.github.com/users/BoopyTheTurtle', timeout=10)
except requests.exceptions.RequestException as e: 
    print(e, file=sys.stderr)
    sys.exit(1)


if response.status_code != 200:
    print("Error code:", response.status_code, file=sys.stderr)
    sys.exit(1) 

json_data = response.json()
print("login:", json_data['login'])
print("public_repos:", json_data['public_repos'])


