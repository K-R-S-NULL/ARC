#include <AccelStepper.h>

int pinout_x_driver_pul = 9;
int pinout_x_driver_dir = 8;

AccelStepper stepper_x(AccelStepper::DRIVER, pinout_x_driver_pul, pinout_x_driver_dir);

void setup()
{  
   stepper_x.setMaxSpeed(1000);
   stepper_x.setSpeed(50);	
}

void loop()
{  
   stepper_x.runSpeed();
}
