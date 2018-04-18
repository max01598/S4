#define GREEN_LED 5
un num_ms 

void setup(void)
{
  pinMode(GREEN_LED, OUTPUT);
}

void loop(void)
{
  static uint8_t state = LOW;
  static uint32_t timeout = 0;

  if ( millis() >= timeout )
  {
    timeout = millis() + 500;
    state = !state;
    digitalWrite(GREEN_LED, state);
    Serial.println(millis());
  }
}

void my_millis()
{
  
}
}

