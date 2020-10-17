#include <Wire.h>
#include <CapacitiveSensor.h>

CapacitiveSensor   cs_l = CapacitiveSensor(1, 0);
CapacitiveSensor   cs_r= CapacitiveSensor(6, 5);
CapacitiveSensor   cs_u = CapacitiveSensor(4, 3);
CapacitiveSensor   cs_d = CapacitiveSensor(A2, A3);
CapacitiveSensor   cs_c = CapacitiveSensor(8, 7);

long l, r, u, d, c;

void setup() {
  Wire.begin(8);                // join i2c bus with address #8
  Wire.onRequest(requestEvent); // register event

  //pinMode(13, OUTPUT);
}

void loop() {
  //delay(100);
  //digitalWrite(13, HIGH);
  //delay(100);
  //digitalWrite(13, LOW);

  l =  cs_l.capacitiveSensor(30);
  r =  cs_r.capacitiveSensor(30);
  u =  cs_u.capacitiveSensor(30);
  d =  cs_d.capacitiveSensor(30);
  c =  cs_c.capacitiveSensor(30);
}

// function that executes whenever data is requested by master
// this function is registered as an event, see setup()
void requestEvent() {
  Wire.write("hello "); // respond with message of 6 bytes + 5 longs (4 bytes each)
  wireWriteLong(l);
  wireWriteLong(r);
  wireWriteLong(u);
  wireWriteLong(d);
  wireWriteLong(c);
  // as expected by master
}

void wireWriteLong(long l) {
  for(int i = 0; i < 4; i++) {
    Wire.write((l >> 8*i) & 0xFF);
  }
}
