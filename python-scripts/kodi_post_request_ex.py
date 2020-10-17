import requests
import json

API_ENDPOINT = "http://localhost:8080/jsonrpc"

headers = {
"Content-Type": "application/json"
}
#Subfolder paths:
piano = "//plugin.program.advanced.emulator.launcher/?com=SHOW_LAUNCHERS&catID=5944f8d8e0a2e8554f845e0755b7136f"
flash = "//plugin.program.advanced.emulator.launcher/?com=SHOW_LAUNCHERS&catID=d45fb2e7ebe6d09d2cb03af60e24cbd8"

def rpcPost(jsonInput):
    r = requests.post(url = API_ENDPOINT, headers=headers, data = json.dumps(jsonInput))
    return r

def notification(title, message):
    # Pop up message
    data_notification = {
        "jsonrpc":"2.0",
        "id":"notification",
        "method":"GUI.ShowNotification",
        "params":{
            "title":title,
            "message":message
        }
    }
    r = rpcPost(data_notification)
    print(r.json())


#Get directories from advanced emulator launcher
def getDirectories():
    data_dir = {
        "jsonrpc": "2.0",
        "id": "get_ael_dir",
        "method": "Files.GetDirectory",
        "params": {
            "directory": "plugin://plugin.program.advanced.emulator.launcher"
        }
    }
    r = rpcPost(data_dir)
    print(r.json())

#Go to main menu
def mainmenu():
    data_mainmenu = {
        "jsonrpc": "2.0",
        "method": "Addons.ExecuteAddon",
        "id": "open_main_menu",
        "params": {
            "addonid": "plugin.program.advanced.emulator.launcher"
        }
    }
    r = rpcPost(data_mainmenu)
    print(r.json())


#Opens a subdirectory to the Advanced emulator launcher
def open(path):
    data_open_subdir = {
         "jsonrpc": "2.0",
         "method": "Addons.ExecuteAddon",
         "id": "open_subdir",
         "params": {
             "addonid": "plugin.program.advanced.emulator.launcher",
             "params": paths
         }
    }
    r = rpcPost(data_open_subdir)
    print(r.json())

    
#def open(folder):
    #open plugin and favorite shitt
    #data_open_plugin_fav = {
      #"jsonrpc": "2.0",
      #"method": "GUI.ActivateWindow",
      #"id": 3,
      #"params": {
      #  "window": "favourites", #you can change this with games videos etc.
      #  "parameters": [folder]   
      #  }
   # }
    #r = rpcPost(data_open_plugin_fav)
   # print(r.json())


#quit application
def exit():
    data_close_kodi = {"jsonrpc":"2.0","method":"Application.Quit","id":"exit"}
    r = rpcPost(data_close_kodi)
    print(r.json())


def reboot():
    #reboots system that runs kodi
    data_reboot = {"jsonrpc":"2.0","method":"System.Reboot","id":"reboot"}
    r = rpcPost(data_reboot)
    print(r.json())

while(True):
    val = input("Enter your value: ")   
    i = int(val)
    print(i)
    if(i==1):
        notification('Hello','World')
    elif(i==2):
        open(piano)
    elif(i==3):
        open(flash)
    elif(i==4):
        exit()
        break


