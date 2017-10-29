from nanpy import (ArduinoApi, SerialManager)
from time import sleep

Motor1A = 2
Motor1B = 3
 
Motor2A = 4
Motor2B = 5

# Connecting to the Arduino

try:
    connection = SerialManager()
    arduino = ArduinoApi(connection = connection)
except:
    print "Failed to connect to the arduino" 
 
arduino.pinMode(Motor1A,arduino.OUTPUT)
arduino.pinMode(Motor1B,arduino.OUTPUT)
 
arduino.pinMode(Motor2A,arduino.OUTPUT)
arduino.pinMode(Motor2B,arduino.OUTPUT)
 
print "Going forwards" 
arduino.digitalWrite(Motor1A,arduino.HIGH)
arduino.digitalWrite(Motor1B,arduino.LOW)
 
arduino.digitalWrite(Motor2A,arduino.HIGH)
arduino.digitalWrite(Motor2B,arduino.LOW)
 
sleep(2)

# Stop the motors from moving (kill all power)
arduino.digitalWrite(Motor1A,arduino.LOW)
arduino.digitalWrite(Motor2A,arduino.LOW)
arduino.digitalWrite(Motor1B,arduino.LOW)
arduino.digitalWrite(Motor2B,arduino.LOW)
 
print "end"