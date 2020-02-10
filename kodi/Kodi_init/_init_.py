#How to control kodi through python
#Step 1. activate remote control in Kodi through settings>network>control>http
#Step 2. connect to a network
#Step 3. start sending inbuilt kodi commands!
#Note: the kodipydent library sends json lines as commands to kodi through kodi's inbuilt jsonrpc function
from kodipydent import Kodi
arcade = Kodi('localhost')
ael = "plugin.program.advanced.emulator.launcher"

def homemenu():
    print(arcade.Addons.ExecuteAddon(ael))

#def game1(): WIP
   #print(arcade.Input.ExecuteAction('ActivateWindow(Programs,"plugin://plugin.program.advanced.emulator.launcher/?catID=8fe77d3be88f23da046be1fca6828494&amp;com=SHOW_LAUNCHERS",return)'))

def getBuiltInFunc():
    print(arcade)





