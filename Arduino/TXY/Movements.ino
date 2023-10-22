void move_straight(long x_go, long y_go){
  long x_go_p = x_go;
  long y_go_p = y_go;
  int x_factor = 1;
  int y_factor = 1;
  if(x_go_p < 0){
    x_go_p = x_go_p *-1;
    x_factor = -1;
  }
  if(y_go_p < 0){
    y_go_p = y_go_p *-1;
    y_factor = -1;
  }
  float max_distance = max(x_go_p,y_go_p);
  float x_speed = ((x_go_p/max_distance) * stepper_maxSpeed) * x_factor;
  float y_speed = ((y_go_p/max_distance) * stepper_maxSpeed) * y_factor;
  stepper_x.move(x_go);
  stepper_y.move(y_go);
  stepper_x.setSpeed(x_speed);
  stepper_x.setMaxSpeed(x_speed);
  stepper_y.setSpeed(y_speed);
  stepper_y.setMaxSpeed(y_speed);
  bool x_not_done = true;
  bool y_not_done = true;
  while(x_not_done || y_not_done){
    x_not_done = stepper_x.run();
    y_not_done = stepper_y.run();
  }
}