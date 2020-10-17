#include <Wire.h>

void setup() {
  Wire.begin();        // join i2c bus (address optional for master)
  Serial.begin(9600);  // start serial for output
}

void loop() {
  Wire.requestFrom(8, 6 + 5*4);    // request 6 bytes from slave device #8

  byte i = 0;
  while (Wire.available()) { // slave may send less than requested
    if(i < 6) {
      char c = Wire.read(); // receive a byte as character
      Serial.print(c);         // print the character
    }
    else {
      long l = wireReadLong();
      Serial.print(l);
      Serial.print(" - ");
    }
    
    i++;
    if(i == 6) {
      Serial.print("\n");
    }
  }
  Serial.print("\n");

  delay(500);
}

long wireReadLong() {
  long l = 0;
  for(int i = 0; i < 4; i++) {
    long rl = Wire.read();
    l += rl << 8*i;
  }
  return l;
}
