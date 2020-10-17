# Code for the arcade navigation touchpad
The arcade navigation touchpad is the main interface for navigating the arcade menu system. It's a custom touchpad that utilizes capasitive touch sensing for it's buttons and communicates over i2c.

# Compiling and uploading
The program for the touchpad is an Arduino sketch, but since the touch controller PCB doesn't feature any usb interface the program needs to be flashed to the MCU using an ISP programmer.  
For these instructiins we are using avrdude and an AVRISPmkII programmer for burning the programm to the MCU.
- The touch controller uses an atmega168 MCU, in the arduino IDE, select "Arduino Duamilanove or Dicilima" as the board and "ATmega168" as the processor.
- Verify the program.
- Under the "Sketch" menu use the "Export compiled Binary" option.
- Run the "upload.sh" script to upload the non-bootloader binary hex to the MCU.
- If it now works; get a sense of pride and accomplishment for successfully programming your touchpad.
