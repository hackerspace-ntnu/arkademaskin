#include <Wire.h>
#include "Keyboard.h"

#define TRESHOLD 200
#define MSG_LENGTH 6

void setup() {
  Wire.begin();        // join i2c bus (address optional for master)
  Serial.begin(9600);  // start serial for output
  Keyboard.begin();
}

void loop() {

  long buttonArray[5];
  wireReadTouchpad(buttonArray);

  for(int i = 0; i < 5; i++) {
    Serial.print(buttonArray[i]);
    Serial.print(' ');
  }
  Serial.println();
  if(buttonArray[0] >= 200) Keyboard.press(KEY_LEFT_ARROW);
  if(buttonArray[1] >= 200) Keyboard.press(KEY_RIGHT_ARROW);
  if(buttonArray[2] >= 200) Keyboard.press(KEY_UP_ARROW);
  if(buttonArray[3] >= 200) Keyboard.press(KEY_DOWN_ARROW);
  //if(buttonArray[4] >= 200) Keyboard.println();
  delay(100);
  Keyboard.releaseAll();
}

void wireReadTouchpad(long buttonArray[]) {
  Wire.requestFrom(8, MSG_LENGTH + 5*4);    // request 6 + 5x4 bytes from slave device #8

  char msgArray[MSG_LENGTH];
  wireReadMessage(msgArray);
  
  wireReadButtons(buttonArray);
  //for(int i = 0; i < 6; i++) Serial.print(msgArray[i]);
  //Serial.print('\n');
}

void wireReadMessage(char msgArray[]) {
  for(int i = 0; i < MSG_LENGTH; i++) {
    while (!Wire.available());
    msgArray[i] = Wire.read();
  }
}

void wireReadButtons(long buttonArray[]) {
  for(int i = 0; i < 5; i++) {
    buttonArray[i] = wireReadLong();
  }
}

long wireReadLong() {
  long l = 0;
  for(int i = 0; i < 4; i++) {
    while (!Wire.available());
    long rl = Wire.read();
    l += rl << 8*i;
  }
  return l;
}
