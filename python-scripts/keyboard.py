from pynput import keyboard
import time
code = ""
current_code = ""

def on_press(key):
    global code
    global current_code
    if(key == keyboard.Key.f13):
        code = code + "1"
        print(code)
        print(current_code)
    if(key == keyboard.Key.f14):
        code = code +  "0"
        print(code)
        print(current_code)
    if len(code) == 8:
        current_code = code
        code = ""
        print(code)
        print(current_code)
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
    on_press(keyboard.Key.f13)
