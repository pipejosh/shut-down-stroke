#include <LiquidCrystal.h>

const int rs = 12, e = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, e, d4, d5, d6, d7);

const int buzzer = 9;  // Buzzer pin
const int correctLights = 6;
int lives = 3;  // Starting lives

void setup() {
    lcd.begin(16, 2);
    lcd.setCursor(0, 0);
    lcd.print("Lives left: ");
    lcd.setCursor(0, 1);
    lcd.print(lives);

    pinMode(buzzer, OUTPUT);
    pinMode(correctLights, OUTPUT);
    Serial.begin(9600);
}

void loop() {
  
  // tone(buzzer, 1000, 500);

    if (Serial.available() > 0) {
        char command = Serial.read();
        
        Serial.print("RECIVIDO PAPU");

        if (command == 'L') {  // 'L' means lose a life
            if (lives > 0) {
                lives--;
                lcd.clear();
                lcd.setCursor(0, 0);
                lcd.print("Lives left: ");
                lcd.setCursor(0, 1);
                lcd.print(lives);

                for (int i = 0; i < 50; i++)
                {
                  digitalWrite(buzzer, HIGH);
                  delay(1);
                  digitalWrite(buzzer, LOW);
                  delay(2);
                }
                
                if (lives == 0) {
                    lcd.clear();
                    lcd.setCursor(0, 0);
                    lcd.print("GAME OVER!");

                    lcd.setCursor(0,1);
                    lcd.print("SHUTTING DOWN!");
                }
            }
        }
    }
}
