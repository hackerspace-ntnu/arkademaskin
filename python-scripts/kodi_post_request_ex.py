import requests
import json

API_ENDPOINT = "http://127.0.0.1:8080/jsonrpc"

headers = {
"Content-Type": "application/json"
}


# Pop up message
data_new_controller = {"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"New Controller","message":"A new Controller was plugged in"},"id":1}
data_json_new_controller = json.dumps(data_new_controller)

r = requests.post(url = API_ENDPOINT, headers=headers, data = data_json_new_controller)
print(r.json())


#quit application
#data_close_kodi = {"jsonrpc":"2.0","method":"Application.Quit","id":1}
#data_json_close_kodi = json.dumps(data_close_kodi)
#r = requests.post(url = API_ENDPOINT, headers=headers, data = data_json_close_kodi)
#print(r.json())

#reboots system that runs kodi
#data_reboot = {"jsonrpc":"2.0","method":"System.Reboot","id":1}
#data_json_reboot = json.dumps(data_reboot)
#r = requests.post(url = API_ENDPOINT, headers=headers, data = data_json_reboot)
#print(r.json())
