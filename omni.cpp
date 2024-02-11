#include <math.h>
//motors 1 and 3 are x
//motors 2 and 4 are y

#define x_motor 3 //enable pins
#define y_motor 6

//motor 1
#define m1_in1 5 // input for the l293d from the arduino
#define m1_in2 7

//motor 2
#define m2_in1 11
#define m2_in2 8

//motor 3
#define m3_in1 4
#define m3_in2 2

//motor 4
#define m4_in1 9
#define m4_in2 10

//joystick
#define x_joy A7
#define y_joy A6
#define sw_joy 13

double threshold = 15;
int x_val;
int y_val;
int sw_pin;
int x, y;
double x_comp, y_comp;
int vel = 10;
float pwm_x, pwm_y;

void setup()
{
  pinMode(x_joy, INPUT);
  pinMode(y_joy, INPUT);
  pinMode(sw_joy, INPUT);
  Serial.begin(9600);
  for (int i=2; i<11; i++)
  {
    pinMode(i, OUTPUT);
    digitalWrite(i, LOW);
  }
  pinMode(11, OUTPUT);
  digitalWrite(11, LOW);
}

void loop()
{
  x_val = analogRead(x_joy); //taking input from joystick
  y_val = analogRead(y_joy);
  sw_pin = digitalRead(sw_joy);

  x = x_val - 499; // shifting origin
  y = y_val - 504;

  if (sqrt(pow(x,2) + pow(y,2)) > threshold)
  {
    x_comp = vel * abs((x/sqrt(pow(x,2) + pow(y,2)))); //finding the x comp and y comp of vel
    y_comp = vel * abs((y/sqrt(pow(x,2) + pow(y,2)))); //finding the x comp and y comp of vel
    Serial.print("X com:");
    Serial.println(x);
    Serial.println(x*x);
    Serial.print("Y com:");
    Serial.println(y);
    Serial.println(x_comp);
    pwm_x = map(x_comp, 0, vel, 250, 1023);
    pwm_y = map(y_comp, 0, vel, 250, 1023);

    analogWrite(x_motor, pwm_x);
    analogWrite(y_motor, pwm_y);

    if (x>15)
    {
      digitalWrite(m4_in1, HIGH);
      digitalWrite(m4_in2, LOW);

      digitalWrite(m2_in2, LOW);
      digitalWrite(m2_in1, HIGH);
    }

    else if (x<-15)
    {
      digitalWrite(m4_in1, LOW);
      digitalWrite(m4_in2, HIGH);

      digitalWrite(m2_in2, HIGH);
      digitalWrite(m2_in1, LOW);
    }

    if (y<-15)
    {
      digitalWrite(m1_in2, HIGH);
      digitalWrite(m1_in1, LOW);

      digitalWrite(m3_in1, LOW);
      digitalWrite(m3_in2, HIGH);
    }

    else if (y>15)
    {
      digitalWrite(m1_in1, HIGH);
      digitalWrite(m1_in2, LOW);

      digitalWrite(m3_in2, LOW);
      digitalWrite(m3_in1, HIGH);
    }
  }
  else
  {
    digitalWrite(m1_in1, LOW);
    digitalWrite(m1_in2, LOW);

    digitalWrite(m3_in2, LOW);
    digitalWrite(m3_in1, LOW);

    digitalWrite(m1_in2, LOW);
    digitalWrite(m1_in1, LOW);

    digitalWrite(m3_in1, LOW);
    digitalWrite(m3_in2, LOW);
    
    digitalWrite(m4_in1, LOW);
    digitalWrite(m4_in2, LOW);

    digitalWrite(m2_in2, LOW);
    analogWrite(m2_in1, LOW);

    digitalWrite(m4_in1, LOW);
    digitalWrite(m4_in2, LOW);

    digitalWrite(m2_in2, LOW);
    digitalWrite(m2_in1, LOW);
  }
  delay(200);
}