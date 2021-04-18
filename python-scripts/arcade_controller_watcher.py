import signal
import re
import threading
import time
import struct
import kodi_handler as kodi

class ArcadeControllerWatcher(object):
    
  KEYCODE_KEY_F13 = 183
  KEYCODE_KEY_F14 = 184  

  def __init__(self):
    self.inputcode = ""
    self.current_inputcode = ""
    self.done = False
    signal.signal(signal.SIGINT, self.cleanup)

    with open('/proc/bus/input/devices') as f:
      devices_file_contents = f.read()

    for handlers in re.findall(r"""H: Handlers=([^\n]+)""", devices_file_contents, re.DOTALL):
      dev_event_file = '/dev/input/event' + re.search(r'event(\d+)', handlers).group(1)
      if 'kbd' in handlers:
        t = threading.Thread(target=self.read_events, kwargs={'dev_event_file': dev_event_file})
        t.daemon = True
        t.start()
    

    while not self.done: #  Wait for Ctrl+C
      time.sleep(1)

  def createInputEventListener(dev_event_file):
    print("test")
    #Maybe implement watchdog?

  def cleanup(self, signum, frame):
    self.done = True

  def on_press(self,key):
    if(key == ArcadeControllerWatcher.KEYCODE_KEY_F13):
        self.inputcode += "0"
    if(key == ArcadeControllerWatcher.KEYCODE_KEY_F14):
        self.inputcode += "1"
    if len(self.inputcode) == 8:
        self.current_inputcode = self.inputcode
        self.inputcode = ""
        print(self.current_inputcode)
        #print(kodi.notification('Hello','World'))
        #call method for kodi

  def read_events(self, dev_event_file):
    print("Listening for kbd events on dev_event_file=" + str(dev_event_file))
    try:
      of = open(dev_event_file, 'rb')
    except IOError as e:
      if e.strerror == 'Permission denied':
        print("You don't have read permission on ({}). Are you root?".format(dev_event_file))
        return
    while True:
      event_bin_format = 'llHHI'  #  See kernel documentation for 'struct input_event'
      #  For details, read section 5 of this document:
      #  https://www.kernel.org/doc/Documentation/input/input.txt
      data = of.read(struct.calcsize(event_bin_format))
      seconds, microseconds, e_type, code, value = struct.unpack(event_bin_format, data)
      full_time = seconds + microseconds / 1000000
      if e_type == 0x1:  #  0x1 == EV_KEY means key press or release.
        if(value == 1):
          self.on_press(code)

arcadeControllerWatcher = ArcadeControllerWatcher()
