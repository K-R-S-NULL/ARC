#include <AccelStepper.h>
// X
int pinout_x_driver_pul = 9;
int pinout_x_driver_dir = 8;
int pinout_x_min = 1;
int pinout_x_max = 2;
int config_x_steps = 25000;
float config_x_distance_per_rotation = 22.2;
AccelStepper x_stepper(AccelStepper::DRIVER, pinout_x_driver_pul, pinout_x_driver_dir);
int x_btn_min_state;
int x_btn_min_value;
int x_btn_max_state;
int x_btn_max_value;
/*
int pinout_x_driver_pul = 9;
int pinout_x_driver_dir = 8;
int pinout_x_min = 1;
int pinout_x_max = 2;
int config_x_steps = 200;
float config_x_distance_per_rotation = 22.2;
AccelStepper x_stepper(AccelStepper::DRIVER, pinout_x_driver_pul, pinout_x_driver_dir);
int x_btn_max_state;
int x_btn_max_value;
 */
void setup()
{  
  pinMode(pinout_x_min, INPUT_PULLUP);
  pinMode(pinout_x_max, INPUT_PULLUP);
  x_stepper.setMaxSpeed(-4000);
  x_stepper.setSpeed(-4000);

}

void loop()
{
  
  x_stepper.runSpeed();
}
