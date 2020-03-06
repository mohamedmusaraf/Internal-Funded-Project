#include <NTPClient.h>
#include <WiFiUdp.h>
#include <Servo.h>
#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>

// Set these to run example.
#define FIREBASE_HOST "sensordb-eb5ba.firebaseio.com"
#define FIREBASE_AUTH "PVS6QuEZ5jDnJWivEfj4AmSP4pRJktpJrP0JLhrJ"
#define WIFI_SSID "Kapar"
#define WIFI_PASSWORD "kapar@1994"


//timestamp
#define NTP_OFFSET   60 * 60      // In seconds
#define NTP_INTERVAL 60 * 1000    // In miliseconds
#define NTP_ADDRESS  "europe.pool.ntp.org"

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, NTP_ADDRESS, NTP_OFFSET, NTP_INTERVAL);

Servo servo;

const int trigP = 2;  //D4 Or GPIO-2 of nodemcu
const int echoP = 0;  //D3 Or GPIO-0 of nodemcu

const int trigQ = 12;  //D6 Or GPIO-2 of nodemcu
const int echoQ = 14;  //D5 Or GPIO-0 of nodemcu

long duration,t;
int distance,d;

void setup() {

    timeClient.begin();

  
  // connect to wifi.
  Serial.begin(9600);      // Open serial channel at 9600 baud rate
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
pinMode(trigP, OUTPUT);  // Sets the trigPin as an Output
pinMode(echoP, INPUT);   // Sets the echoPin as an Input
pinMode(trigQ, OUTPUT);  // Sets the trigPin as an Output
pinMode(echoQ, INPUT);   // Sets the echoPin as an Input
servo.attach(D2);  //D2
  servo.write(0);
  delay(2000);
}

int n = 0;
void loop() {

digitalWrite(trigP, LOW);   // Makes trigPin low
delayMicroseconds(2);       // 2 micro second delay 

digitalWrite(trigP, HIGH);  // tigPin high
delayMicroseconds(10);      // trigPin high for 10 micro seconds
digitalWrite(trigP, LOW); 
// trigPin low

duration = pulseIn(echoP, HIGH);   //Read echo pin, time in microseconds
distance= duration*0.034/2;        //Calculating actual/real distance

//Serial.print("Distance = ");        //Output distance on arduino serial monitor 
//Serial.println(distance);


digitalWrite(trigQ, LOW);   // Makes trigPin low
delayMicroseconds(2);       // 2 micro second delay 

digitalWrite(trigQ, HIGH);  // tigPin high
delayMicroseconds(10);      // trigPin high for 10 micro seconds
digitalWrite(trigQ, LOW); 
// trigPin low

t = pulseIn(echoQ, HIGH);   //Read echo pin, time in microseconds
d= t*0.034/2;        //Calculating actual/real distance

Serial.print("Distance2 = ");        //Output distance on arduino serial monitor 
Serial.println(d);
  

if(distance<=20){
   servo.write(0);
  delay(3000);
  servo.write(180);
  delay(1000); 
}

StaticJsonBuffer<200> jsonBuffer;
  JsonObject& data = jsonBuffer.createObject();
  

if(d<=5){


    timeClient.update();
    String formattedTime = timeClient.getFormattedTime();
    
    data["Lat"]="40.0";
    data["Long"]="80.0";
     data["Type"]="0";
    data["Time"]=formattedTime;
    data["Serviced"]="0";
   
    


  String key=Firebase.push("sensors",data);
  // handle error
  if (Firebase.failed()) {
      Serial.print("setting /message failed:");
      Serial.println(Firebase.error());  
      return;
    }
   else{
   Serial.print(key);
   Serial.println("inserted");
   }
  
  }

}



//Pause for 3 seconds and start measuring distance again
