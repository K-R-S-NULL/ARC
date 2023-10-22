

void setup() {
  Serial.begin(115200);
  while (!Serial) {}
}

void loop() {    
  if (Serial.available() > 0) {
    String msg = Serial.readStringUntil('\n');
    if (msg.startsWith("ERR")){
      msg.remove(0, 3);
      ErrorReaction(msg);
    }
    if (msg.startsWith("MIL")){
      msg.remove(0, 3);
      //
    }
  }
}