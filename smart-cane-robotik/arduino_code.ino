#include <Servo.h>
#include <avr/wdt.h>  // Watchdog timer for auto reset

// Define ultrasonic sensor pins
#define TRIG 4
#define ECHO 5

// Define motor driver pins (L298N)
#define MOTOR_R_F 6  // Right motor forward
#define MOTOR_R_B 7  // Right motor backward
#define MOTOR_L_F 8  // Left motor forward
#define MOTOR_L_B 9  // Left motor backward

// Define enable pins for PWM speed control
#define ENA 11  // Left motor speed control
#define ENB 12  // Right motor speed control

// Define servo pin
#define SERVO_PIN 10

// Create Servo object
Servo myServo;

// Function to measure distance using ultrasonic sensor
long getDistance() {
    digitalWrite(TRIG, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG, LOW);

    long duration = pulseIn(ECHO, HIGH);
    long distance = duration * 0.034 / 2;  // Convert to cm
    return (distance > 200) ? 200 : distance;  // Limit to 200 cm max
}

// Move Forward Correctly
void moveForward(int speed = 255) {
    analogWrite(ENA, speed);  
    analogWrite(ENB, speed);
    digitalWrite(MOTOR_R_F, HIGH);  // Right motor forward
    digitalWrite(MOTOR_R_B, LOW);   // Right motor not moving backward
    digitalWrite(MOTOR_L_F, LOW);   // Left motor forward (Due to wiring)
    digitalWrite(MOTOR_L_B, HIGH);  // Left motor NOT moving backward
}

// Move Backward
void moveBackward(int speed = 255) {
    analogWrite(ENA, speed);
    analogWrite(ENB, speed);
    digitalWrite(MOTOR_R_F, LOW);  // Right motor backward
    digitalWrite(MOTOR_R_B, HIGH);
    digitalWrite(MOTOR_L_F, HIGH);  // Left motor backward (Due to wiring)
    digitalWrite(MOTOR_L_B, LOW);
}

// Stop Robot
void stopRobot() {
    analogWrite(ENA, 0);
    analogWrite(ENB, 0);
    digitalWrite(MOTOR_R_F, LOW);
    digitalWrite(MOTOR_R_B, LOW);
    digitalWrite(MOTOR_L_F, LOW);
    digitalWrite(MOTOR_L_B, LOW);
}

// Left Turn
void turnLeft(int speed = 180) {
    analogWrite(ENA, speed);  // Left motor slower
    analogWrite(ENB, 255);    // Right motor full speed
    digitalWrite(MOTOR_R_F, HIGH);
    digitalWrite(MOTOR_R_B, LOW);
    digitalWrite(MOTOR_L_F, HIGH);  // Left motor moves backward (Due to wiring)
    digitalWrite(MOTOR_L_B, LOW);
}

// Right Turn
void turnRight(int speed = 180) {
    analogWrite(ENA, 255);    // Left motor full speed
    analogWrite(ENB, speed);  // Right motor slower
    digitalWrite(MOTOR_R_F, LOW);  // Right motor moves backward
    digitalWrite(MOTOR_R_B, HIGH);
    digitalWrite(MOTOR_L_F, LOW);  // Left motor forward
    digitalWrite(MOTOR_L_B, HIGH);
}

void setup() {
    Serial.begin(9600);
    wdt_enable(WDTO_8S);  // Enable auto-reset if frozen for 8 seconds

    // Initialize motor pins
    pinMode(MOTOR_R_F, OUTPUT);
    pinMode(MOTOR_R_B, OUTPUT);
    pinMode(MOTOR_L_F, OUTPUT);
    pinMode(MOTOR_L_B, OUTPUT);
    pinMode(ENA, OUTPUT);
    pinMode(ENB, OUTPUT);

    // Initialize ultrasonic sensor pins
    pinMode(TRIG, OUTPUT);
    pinMode(ECHO, INPUT);

    // Attach servo motor
    myServo.attach(SERVO_PIN);
    myServo.write(90);  // Center position
    delay(1000);
}

void loop() {
    wdt_reset();  // Prevent watchdog timer reset

    long frontDistance = getDistance();
    Serial.print("Front Distance: ");
    Serial.print(frontDistance);
    Serial.println(" cm");

    if (frontDistance > 25) {  
        moveForward(200);  // Move forward at reduced speed for smoother movement
    } else {  
        stopRobot();
        Serial.println("Obstacle detected! Scanning...");
        delay(500);

        // Scan left
        myServo.write(150);
        delay(500);
        long leftDistance = getDistance();
        Serial.print("Left Distance: ");
        Serial.print(leftDistance);
        Serial.println(" cm");

        // Scan right
        myServo.write(30);
        delay(500);
        long rightDistance = getDistance();
        Serial.print("Right Distance: ");
        Serial.print(rightDistance);
        Serial.println(" cm");

        // Reset servo to center
        myServo.write(90);
        delay(500);

        // Decide turning direction
        if (leftDistance > rightDistance && leftDistance > 20) {
            Serial.println("Turning LEFT...");
            turnLeft(180);  // Make a proper left turn
            delay(1000);
        } 
        else if (rightDistance > leftDistance && rightDistance > 20) {
            Serial.println("Turning RIGHT...");
            turnRight(180);  // Make a proper right turn
            delay(1000);
        } 
        else {
            Serial.println("Backing up and re-evaluating...");
            moveBackward(200);
            delay(1000);
            stopRobot();
        }

        delay(500);
        moveForward(200);  // Continue forward movement
    }

    delay(200);
}