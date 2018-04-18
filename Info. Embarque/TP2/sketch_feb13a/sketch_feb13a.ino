#define GREEN_LED 5
#define BLUE_LED 6
#define RED_LED 23

void setup() {
  // put your setup code here, to run once:
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  static uint8_t state = LOW;
  static uint32_t timeout = 0;
 
    state = !state;
    digitalWrite(GREEN_LED, state);
    delay(1000);
    digitalWrite(RED_LED, state);
    delay(1000);
    digitalWrite(BLUE_LED, state);

}
