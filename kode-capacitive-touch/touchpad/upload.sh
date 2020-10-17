#!/bin/bash
# A simple script to upload hex files to Arduino with avrdude, by Per Emil Skjold.
# Full tutorial here:
# https://skjoldtech.wordpress.com/2019/05/10/flashing-arduino-hex-file-in-linux-with-avrdude/

avrdude -p m168 -P usb -c avrispmkII -Uflash:w:touchpad.ino.standard.hex:i -B 1.0
