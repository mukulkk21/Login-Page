import requests

Token = '7376682875:AAE4QuYnuZBYifaQ_j1zkj9cRQVsO9LII0w'
url = f"https://api.telegram.org/bot{Token}/getUpdates"

response = requests.get(url)
if response.status_code == 200:
    updates = response.json()
    print(updates)
    if 'result' in updates:
        for update in updates['result']:
            print(update['message']['chat']['id'])
    else:
        print("No updates found.")
else:
    print("Failed to fetch updates. Status code:", response.status_code)
