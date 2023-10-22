int inByte = '0';

void setup() {
  Serial.begin(115200);
  while(!Serial){}
  

  
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

  if (Serial.available() > 0) {
    String msg = Serial.readStringUntil('\n');
    Serial.print(msg);
    if(msg.startsWith("G")){
      Serial.println("LED-HIGH");
      digitalWrite(LED_BUILTIN, HIGH);
    }
    if (msg.startsWith("D")) {
      Serial.println("LED-LOW");
      digitalWrite(LED_BUILTIN, LOW);

    } 

  }

}