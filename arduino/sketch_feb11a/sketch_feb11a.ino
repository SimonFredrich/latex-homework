int LED = 13; // Use the onboard Uno LED
int fire_pin = 2;  // This is our input pin
int is_fire = HIGH;  // HIGH MEANS FIRE
int motor_pin = 4;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(fire_pin, INPUT);
  pinMode(motor_pin, INPUT);
  Serial.begin(9600);  
}

void loop() {
  digitalWrite(motor_pin, HIGH);
  /*
  is_fire = HIGH;//digitalRead(fire_pin);
  if (is_fire == LOW)
  {
    Serial.println("Kein Feuer.");
    digitalWrite(motor_pin, LOW);
  }
  else
  {
    Serial.println("FEUER!!!");
    digitalWrite(motor_pin, HIGH);
  }
  delay(200);
  */
}
