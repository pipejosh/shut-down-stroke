#include <LiquidCrystal.h>

const int rs = 12, e = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, e, d4, d5, d6, d7);

const int buzzer = 9;  
const int correctLights = 8;
const int incorrectLights = 6;
int lives = 3;  

boolean inGame = true;

void setup() 
{
    lcd.begin(16, 2);
    lcd.setCursor(0, 0);
    lcd.setCursor(0, 1);
    lcd.print(lives);

    pinMode(buzzer, OUTPUT);
    pinMode(correctLights, OUTPUT);
    pinMode(incorrectLights, OUTPUT); 
    Serial.begin(9600);
}

void loop() {
    if (lives == 0) return;  // Ignore further input if game is over
    
    // Update screen with lives left
    lcd.setCursor(0, 0);
    lcd.print("Lives left: ");
    lcd.setCursor(0, 1);
    lcd.print(lives);   

    if (Serial.available() > 0) {
        char command = Serial.read();
        
        if (command == 'L') {  // Lose a life
            if (lives > 0) {
                lives--;
                lcd.clear(); 
                lcd.setCursor(0, 0);
                lcd.print("Lives left: ");
                lcd.setCursor(0, 1);
                lcd.print(lives);

                // Buzzer sound
                for (int i = 0; i < 100; i++) {
                    digitalWrite(buzzer, HIGH);
                    delay(1);
                    digitalWrite(buzzer, LOW);
                    delay(2);
                }

                // Incorrect lights flash
                digitalWrite(incorrectLights, HIGH);
                delay(300);  
                digitalWrite(incorrectLights, LOW);

                if (lives == 0) {
                    lcd.clear();
                    lcd.setCursor(0, 0);
                    lcd.print("GAME OVER!");
                    lcd.setCursor(0, 1);
                    lcd.print("SHUTTING DOWN!");
                    while (true);  // Stops execution once the game is over
                }
            }
        }

        else if (command == 'C') {  // Correct answer
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("CORRECT");
            lcd.setCursor(0, 1);
            lcd.print(":)");

            // Buzzer sound
            for (int i = 0; i < 100; i++) {
                digitalWrite(buzzer, HIGH);
                delay(4);
                digitalWrite(buzzer, LOW);
                delay(4);
            }

            // Correct lights blink
            digitalWrite(correctLights, HIGH);
            delay(300);
            digitalWrite(correctLights, LOW);
        }

        else if (command == 'W') {  // You won
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("YOU WON!!!!");
            lcd.setCursor(0, 1);
            lcd.print("GOOD JOB!!!!");

            // Buzzer sound
            for (int i = 0; i < 100; i++) {
                digitalWrite(buzzer, HIGH);
                delay(4);
                digitalWrite(buzzer, LOW);
                delay(1);
            }

            // Correct lights and incorrect lights blink alternately
            for (int j = 0; j < 6; j++) {
                digitalWrite(correctLights, HIGH);
                delay(300);
                digitalWrite(correctLights, LOW);

                digitalWrite(incorrectLights, HIGH);
                delay(300);
                digitalWrite(incorrectLights, LOW);
            }
        }
    }
}
