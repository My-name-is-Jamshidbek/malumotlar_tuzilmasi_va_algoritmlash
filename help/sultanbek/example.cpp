#include "Arduino.h"
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <Wire.h>
#include <Servo.h>
// #include <WebServer.h>
// #include <WiFiManager.h>
const char* ssid = "espTEST";
const char* password = "123456789";

ESP8266WebServer server(80);
// WebServer server(80);
Servo esc1;
Servo servo_front;
Servo servo_right;
Servo servo_left;
Servo servo_back;
bool active = false;
//Функция чтобы менять скорость у двигателя
void setPower() {
  if (server.arg("power") != NULL && active) {  //Проверяем http аргумент
    int power = server.arg("power").toInt();
    esc1.writeMicroseconds(map(power, 0, 100, 1000, 2000));  //Из диапазона 0.100 переводим в 1400..2300(для обычных двигателей 1000.2000, у нашего немного отличается)
    Serial.print("Test :");
    Serial.println(power);
  }
  server.send(200, "text/json", "");
}
void activate() {
  Serial.println(server.arg("active"));
  if (server.arg("active") != NULL) {  //Проверяем http аргумент
    if (server.arg("active") == "true") {
      active = true;
    } else {
      active = false;
    }
  }
  server.send(200, "text/json", "");
}
void joystickState() {
  if (server.arg("xPos") != NULL && server.arg("yPos") != NULL && active) {  //Проверяем http аргумент
    int xPos = server.arg("xPos").toInt();
    int yPos = server.arg("yPos").toInt();
    servo_front.write(map(xPos, -100, 100, 0, 180));
    servo_right.write(map(xPos, -100, 100, 0, 180));
    servo_left.write(map(yPos, -100, 100, 0, 180));
    servo_back.write(map(yPos, -100, 100, 0, 180));
    Serial.print("x:");
    Serial.print(String(xPos));
    Serial.print("   ");
    Serial.print("y:");
    Serial.println(String(yPos));
  }
  server.send(200, "text/json", "");
}
void getConnection() {
  String response = "{";
  response += "\"xAc\": 0.0";
  response += ",\"yAc\": 0.0";
  response += ",\"zAc\": 0.0";
  response += "}";
  server.send(200, "text/json", response);
}
// Назначаем get функции
void restServerRouting() {
  server.on("/", HTTP_GET, []() {
    Serial.print("Test :");
    server.send(200, F("text/html"),
                F("Welcome to the REST Web Server"));
  });
  server.on(F("/motor"), HTTP_GET, setPower);
  server.on(F("/mpu"), HTTP_GET, getConnection);
  server.on(F("/start"), HTTP_GET, activate);
  server.on(F("/joystick"), HTTP_GET, joystickState);
}

// Если обратились по несуществуещему адресу
void handleNotFound() {
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
}
void setup(void) {
  Serial.begin(115200);
  if(!WiFi.softAP("EspDrone", "c1tr0nR&D")){
    Serial.println("Soft AP creation failed.");
    while(1);
  }
  Serial.println("");
  Serial.println("");
  Serial.print("IP address: ");
  Serial.println(WiFi.softAPIP());  //Отправляем IP адрес хоста

  restServerRouting();                //Вызываем настройки get запросов
  server.onNotFound(handleNotFound);  //Для ошибки 404

  server.begin();
  esc1.attach(D4, 1000, 2000);
  servo_front.attach(D5);
  servo_right.attach(D6);
  servo_left.attach(D7);
  servo_back.attach(D8);
  esc1.writeMicroseconds(1000);
  Serial.println("HTTP server started");
}

uint32_t tmr;
void loop(void) {
  server.handleClient();
}