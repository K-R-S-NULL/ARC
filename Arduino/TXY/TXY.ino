#include <AccelStepper.h>
int pinout_x_driver_pul = 10;
int pinout_x_driver_dir = 11;
int pinout_y_driver_pul = 9;
int pinout_y_driver_dir = 8;
//int config_x_steps = 4000;
//int config_x_clockwise_direction_multiplier = 1;
//double config_x_distance_per_rotation = 4.0;
AccelStepper stepper_x(AccelStepper::DRIVER, pinout_x_driver_pul, pinout_x_driver_dir);
// Define some steppers and the pins the will use

AccelStepper stepper_y(AccelStepper::DRIVER, pinout_y_driver_pul, pinout_y_driver_dir);

float stepper_maxSpeed = 1000.0;

int stepper_x_acceleration = 30000L;
int stepper_y_acceleration = 30000L;

void setup() {
  Serial.begin(115200);
  while (!Serial) {}
  stepper_x.setMaxSpeed(4000.0);
  stepper_x.setAcceleration(stepper_x_acceleration);
  stepper_y.setMaxSpeed(4000.0);
  stepper_y.setAcceleration(stepper_y_acceleration);
  delay(5000);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String msg = Serial.readStringUntil('\n');
    if (msg.startsWith("ERR")){
      msg.remove(0, 3);
      ErrorReaction(msg);
    }
    if (msg.startsWith("TXY")){
      msg.remove(0, 3);
      GCodeReaction(msg);
    }
  }
}