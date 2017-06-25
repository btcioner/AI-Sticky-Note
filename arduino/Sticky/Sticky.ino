/*
 *    http://server_ip/gpio/0 will set the GPIO2 low,
 *    http://server_ip/gpio/1 will set the GPIO2 high
 *    http://server_ip/api/login/yourname  will login sign in
 *    http://server_ip/api/mail/txt   you have a new mail
 *    http://server_ip/api/ocr/txt  show ocr txt
 *    
 */

#include "SSD1306.h" // alias for `#include "SSD1306Wire.h"`
#include "images.h"
#include <ESP8266WiFi.h>

const char* ssid = "Lguest";
const char* password = "legendstar006";


SSD1306  display(0x3c, D5, D6);
//SSD1306  display(0x3c, 0, 2);

WiFiServer server(80);

int demoMode = 0;
int counter = 1;
String txt;
String ocr;
void setup() {
  Serial.begin(115200);
  delay(10);

  //prepare GPIO2 (1)
  pinMode(2, OUTPUT);
  digitalWrite(2, 0);
  
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  
  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.println(WiFi.localIP());


  // Initialising the UI will init the display too.
  display.init();

  display.flipScreenVertically();
  display.setFont(ArialMT_Plain_10);

  display.clear();
  drawsw(); 
  //display.setTextAlignment(TEXT_ALIGN_RIGHT);
  //display.drawString(10, 128, String(millis()));
  // write the buffer to the display
  display.display();
  delay(100);
  for (int i=1;i<450;i++) {
      drawProgressBarDemo();
      counter++;
      display.display();
      delay(10);
  }
  delay(100);
  display.clear();
  drawlogo();
  display.display(); 
}

void drawFontFaceDemo(String ocr) {
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.setFont(ArialMT_Plain_24);
    display.drawString(0, 10, ocr);
}

void drawTextFlowDemo( String txt) {
    display.setFont(ArialMT_Plain_10);
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.drawStringMaxWidth(0, 0, 128,txt);
}

void drawProgressBarDemo() {
  int progress = (counter / 5) % 100;
  // draw the progress bar
  display.drawProgressBar(0, 42, 120, 10, progress);

  // draw the percentage as String
  display.setTextAlignment(TEXT_ALIGN_CENTER);
  display.drawString(64, 25, String(progress) + "%");
}

void drawImageDemo() {
    display.drawXbm(34, 4, WiFi_Logo_width, WiFi_Logo_height, WiFi_Logo_bits);
}

void drawsw() {
    display.drawXbm(1, 1,128, 64, westworld);
}

void drawwx() {
    display.drawXbm(30, 1,64, 64, wx);
}

void drawlogo() {
    display.drawXbm(1, 1,128, 64, logo);
}

void drawGaoshine() {
    display.drawXbm(1, 1,128, 64, gaoshine);
}

void drawBiaoqing() {
    display.drawXbm(30, 1,64, 64, biaoqing);
}

void drawLiuke() {
    display.drawXbm(30, 1,64, 64, liuke);
}

void drawEmail() {
    display.drawXbm(30, 1,64, 64, email);
}
void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
  
  // Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }
  
  // Read the first line of the request
  String req = client.readStringUntil('\r');
  txt = req;
  ocr = req;
  Serial.println(req);
  client.flush();
  
  // Match the request
  int val;
  if (req.indexOf("/gpio/0") != -1){
    val = 0;
    display.clear();    
    drawwx();
    display.display();
  } else if (req.indexOf("/ocr/") != -1){
    val = 0;
    ocr = ocr.substring(req.indexOf("/ocr/")+5,req.length()-6 );
    display.clear();    
    drawFontFaceDemo(ocr);
    //drawTextFlowDemo(ocr);
    display.display();
  }
  else if (req.indexOf("/mail/") != -1){
    val = 1;
    txt = txt.substring(req.indexOf("/mail/")+6,req.length()-9);
    display.clear();    
    drawEmail();
    display.display();
    counter = 0;
    for (int i=1;i<450;i++) {
      drawProgressBarDemo();
      counter++;
      display.display();
      delay(10);
     }
    delay(10);
    display.clear();  
    drawTextFlowDemo(txt);
    display.display();
    
  }
    else if (req.indexOf("/login/gaoshine") != -1){
    val = 1;
    display.clear();    
    drawGaoshine();
    display.display();
  }     
    else if (req.indexOf("/login/biaoqing") != -1){
    val = 1;
    display.clear();    
    drawBiaoqing();
    display.display();
  }
  else {
    Serial.println("invalid request");
    client.stop();
    return;
  }

  // Set GPIO2 according to the request
  digitalWrite(2, val);
  
  client.flush();

  // Prepare the response
  String s = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE HTML>\r\n<html>\r\nGPIO is now ";
  s += (val)?"high":"low";
  s += "</html>\n";

  // Send the response to the client
  client.print(s);
  delay(1);
  Serial.println("Client disonnected");

  // The client will actually be disconnected 
  // when the function returns and 'client' object is detroyed
}

