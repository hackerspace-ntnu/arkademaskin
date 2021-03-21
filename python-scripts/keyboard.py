from pynput import keyboard
import time
code = ""
current_code = ""
import kodi_handler as kodi

def on_press(key):
    global code
    global current_code
    if(key == keyboard.Key.f12):
        code = code + "1"
    if(key == keyboard.Key.f11):
        code = code +  "0"
    if len(code) == 8:
        current_code = code
        code = ""
        print(current_code)
        print(kodi.notification('Hello','World'))
        #call method for kodi
    

def on_release(key):
    return False

def initiatelistener():
    try:
        while(True):
            with keyboard.Listener(
                    on_press=on_press,
                    on_release=on_release) as listener:
                listener.join()

    except KeyboardInterrupt:
        print("Finished")
        


def main():
    initiatelistener()


if __name__ == "__main__":
    main()
    on_press(keyboard.Key.f12)
