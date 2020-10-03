import requests
import json

API_ENDPOINT = "http://localhost:8080/jsonrpc"

headers = {
"Content-Type": "application/json"
}

def notification(title, message):
    # Pop up message
    data_notification = {"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":title,"message":message},"id":1}
    data_json_notification = json.dumps(data_notification)
    r = requests.post(url = API_ENDPOINT, headers=headers, data = data_json_notification)
    print(r.json())
    

def open():
    #open plugin and favorite shitt
    data_open_plugin_fav = {
      "jsonrpc": "2.0",
      "method": "GUI.ActivateWindow",
      "id": 1,
      "params": {
        "window": "favourites", #you can change this with games videos etc.
        "parameters": [
         "plugin://plugin.program.advanced.emulator.launcher/?catID=vcategory_collections&com=SHOW_COLLECTION_ROMS&launID=19f283de98723e813d15a268f4fa2441"
        ]   
        }
    }
    data_json_open_plugin_fav = json.dumps(data_open_plugin_fav)
    r = requests.post(url = API_ENDPOINT, headers=headers, data = data_json_open_plugin_fav)
    print(r.json())


def exit():
    #quit application
    data_close_kodi = {"jsonrpc":"2.0","method":"Application.Quit","id":1}
    data_json_close_kodi = json.dumps(data_close_kodi)
    r = requests.post(url = API_ENDPOINT, headers=headers, data = data_json_close_kodi)
    print(r.json())


#def reboot():
    #reboots system that runs kodi
    #data_reboot = {"jsonrpc":"2.0","method":"System.Reboot","id":1}
    #data_json_reboot = json.dumps(data_reboot)
    #r = requests.post(url = API_ENDPOINT, headers=headers, data = data_json_reboot)
    #print(r.json())

while(True):
    val = input("Enter your value: ")   
    i = int(val)
    print(i)
    if(i==1):
        notification('Hello','World')
    elif(i==2):
        open()
    elif(i==3):
        exit()
        break


