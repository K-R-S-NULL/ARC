void GCodeReaction(String msg){
  float x;
  float y;
  int g_command = parseGCode_G(msg);
  switch (g_command) {
    case 0:
      // Rapid move
      x = parseGCode_X(msg);
      y = parseGCode_Y(msg);
      move_straight(x,y);
      Serial.print("00 -RapidMove");
      Serial.print("X:");
      Serial.print(x);
      Serial.print(";Y:");
      Serial.print(y);
      Serial.println(";");
      break;
    case 1:
      // Move with speed
      x = parseGCode_X(msg);
      y = parseGCode_Y(msg);
      Serial.print("01 - ");
      Serial.print("X:");
      Serial.print(x);
      Serial.print(";Y:");
      Serial.print(y);
      Serial.println(";");
      break;
    default:
      //
      Serial.println(";");
    break;
  }
}

int parseGCode_G(String msg){
  int from = msg.indexOf('G');
  int too = msg.indexOf(';',from+1);
  String code = msg.substring(from+1,too);
 return code.toInt(); 
}
float parseGCode_X(String msg){
  int from = msg.indexOf('X');
  int too = msg.indexOf(';',from+1);
  String code = msg.substring(from+1,too);
 return code.toFloat(); 
}
float parseGCode_Y(String msg){
  int from = msg.indexOf('Y');
  int too = msg.indexOf(';',from+1);
  String code = msg.substring(from+1,too);
 return code.toFloat();
}