# Smart Cane Prototype – Robotik Module

**Module:** Robotik  
**Technologies:** Arduino, Ultrasonic Sensor, 2WD Smart Car Kit

## Overview

This project explores assistive robotics by transforming a 2WD smart car into a prototype for a smart cane designed to help visually impaired individuals navigate independently. It uses ultrasonic sensors and Arduino code to detect obstacles and provide basic navigation feedback via the serial monitor.

The initial goal of autonomous parking was re-scoped due to time limitations, leading to this assistive application as a low-cost alternative to high-end smart canes like WeWalk.

## Features

- Real-time obstacle detection using ultrasonic sensors
- Arduino-based control and logic
- Modular smart car platform (2WD)
- Potential for future upgrades (Bluetooth, GPS, haptic feedback)

## Folder Structure

smart-cane-robotik/  
├── code/          # Arduino source code  
├── media/         # Images, wiring diagrams, and demonstration videos  
├── report/        # Full written report (PDF)  
└── README.md      # Project description and setup instructions  


## How It Works

1. The ultrasonic sensor continuously scans for obstacles.
2. When an object is detected within a defined range, the Arduino triggers predefined maneuvers.
3. The robot reacts by turning or reversing to avoid collisions.
4. Feedback is currently output via the Arduino Serial Monitor.

## Limitations

- Motors experienced wiring/power issues, causing the robot to move in circles.
- Navigation works, but path precision is limited.
- Future work includes Bluetooth feedback, GPS, and improved motion control.

## Media

Check the `media/` folder for:
- Assembly photos
- Demonstration videos


