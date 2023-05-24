import requests

target_input = "google.com"

with open("subdomainlister.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()
        url = "http://" + word + "." + target_input
        try:
            response = requests.get(url)
            print(url)
        except requests.exceptions.ConnectionError:
            continue
