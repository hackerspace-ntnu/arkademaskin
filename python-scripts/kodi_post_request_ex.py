import requests
import json

API_ENDPOINT = "http://127.0.0.1:8080/jsonrpc"

headers = {
"Content-Type": "application/json"
}

data = {"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}

data_json = json.dumps(data)

r = requests.post(url = API_ENDPOINT, headers=headers, data = data_json)


print(r.json())
