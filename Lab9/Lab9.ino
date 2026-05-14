
int LED1 = 43;
int LED2 = 44;
int LED3 = 45;
int LED4 = 46;


int BTN1 = 30;
int BTN2 = 31;
int BTN3 = 32;
int BTN4 = 33;


bool ledState1 = false;
bool ledState2 = false;
bool ledState3 = false;
bool ledState4 = false;


bool lastButton1 = HIGH;
bool lastButton2 = HIGH;
bool lastButton3 = HIGH;
bool lastButton4 = HIGH;

void setup()
{
    
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
    pinMode(LED4, OUTPUT);

    
    pinMode(BTN1, INPUT_PULLUP);
    pinMode(BTN2, INPUT_PULLUP);
    pinMode(BTN3, INPUT_PULLUP);
    pinMode(BTN4, INPUT_PULLUP);
}

void loop()
{
    digitalWrite(LED1, HIGH);
    delay(1000);
    digitalWrite(LED1, LOW);

    digitalWrite(LED2, HIGH);
    delay(1000);
    digitalWrite(LED2, LOW);

    digitalWrite(LED3, HIGH);
    delay(1000);
    digitalWrite(LED3, LOW);

    digitalWrite(LED4, HIGH);
    delay(1000);
    digitalWrite(LED4, LOW);


    bool button1 = digitalRead(BTN1);
    bool button2 = digitalRead(BTN2);
    bool button3 = digitalRead(BTN3);
    bool button4 = digitalRead(BTN4);

    
    if (button1 == LOW && lastButton1 == HIGH)
    {
        ledState1 = !ledState1;
        digitalWrite(LED1, ledState1);
    }

    
    if (button2 == LOW && lastButton2 == HIGH)
    {
        ledState2 = !ledState2;
        digitalWrite(LED2, ledState2);
    }

    
    if (button3 == LOW && lastButton3 == HIGH)
    {
        ledState3 = !ledState3;
        digitalWrite(LED3, ledState3);
    }

    
    if (button4 == LOW && lastButton4 == HIGH)
    {
        ledState4 = !ledState4;
        digitalWrite(LED4, ledState4);
    }

    
    lastButton1 = button1;
    lastButton2 = button2;
    lastButton3 = button3;
    lastButton4 = button4;

    delay(50);
}
