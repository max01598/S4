#include <SPI.h>
#include <RH_RF22.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_TSL2561_U.h>

typedef union {
    float f;
    char b[4];
} float_union;

uint8_t data[] = {
        0x5A,           /* entête */
        0x01,           /* numéro de protocole */
        0x00,           /* numéro de séquence */
        0x00, 0xAF,     /* adresse source */
        0x00, 0x02,     /* numéro d'application */
        0b00011100, 0x00, 0x00, 0x00, 0x00,
    };
   
// Singleton instance of the radio driver
RH_RF22 rf22(SS,9);
Adafruit_TSL2561_Unified tsl = Adafruit_TSL2561_Unified(TSL2561_ADDR_LOW, 12345);


void setup() 
{
  SPI.setSCK(14);
  Serial.begin(9600);
  if (!rf22.init())
    Serial.println("init failed");
  // Defaults after init are 434.0MHz, 0.05MHz AFC pull-in, modulation FSK_Rb2_4Fd36
  rf22.setTxPower(8);
  if(!tsl.begin())
  {
    Serial.print("Ooops, no TSL2561 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
}


void loop()
{
  sensors_event_t event;
  tsl.getEvent(&event);
  if (event.light)
  {
    Serial.print(event.light); Serial.println(" lux");
    float_union lumi; 
    lumi.f= event.light;
    Serial.println("Sending to rf22_server");
    // Send a message to rf22_server
    
    data[8] = lumi.b[0];
    data[9] = lumi.b[1];
    data[10] = lumi.b[2];
    data[11] = lumi.b[3];
    rf22.send(data, sizeof(data));
    rf22.waitPacketSent();
    data[2]= data[2]+1;
  }
  else
  {
    /* If event.light = 0 lux the sensor is probably saturated
       and no reliable data could be generated! */
    Serial.println("Sensor overload");
  }
  delay(5000);
}
