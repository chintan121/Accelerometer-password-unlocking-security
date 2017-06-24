#!/usr/bin/env python  

import RPi.GPIO as GPIO
import time
from RPLCD import CharLCD
from adxl345 import ADXL345
adxl345 = ADXL345()
servopin = 40
green=11
bzr=38


GPIO.setmode(GPIO.BOARD)
GPIO.setup(servopin, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green,1)
GPIO.setup(bzr, GPIO.OUT)
GPIO.output(bzr,0)
CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).clear()
p = GPIO.PWM(servopin,50)
p.start(2.5)
time.sleep(1)
p.ChangeDutyCycle(0)

try:

        while True:
        
                while True:
        
                        j=1
                        if adxl345.getAxes(True)['x']*10<7 and adxl345.getAxes(True)['y']*10<7 and adxl345.getAxes(True)['x']*10>-7 and adxl345.getAxes(True)['y']*10>-7:

                                
                                h=1
                                while j==1:
                                        
                                        if h==2:
                                                CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).clear()
                                                time.sleep(0.1)
                                                CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).write_string('2 Try\'s left')
                                                time.sleep(0.31)
                                        if h==3:
                                                CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).clear()
                                                time.sleep(0.1)
                                                CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).write_string('1 Try left')
                                                
                                                time.sleep(0.31)
                                        if h>3:
                                                CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).clear()
                                                time.sleep(0.1)
                                                CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).write_string('Alert!!!')
                                                                       
                                                GPIO.output(bzr,1)
                                                
                                        
                                                
                                       
                                  
                                
                                        x=adxl345.getAxes(True)['x']*10
                                        y=adxl345.getAxes(True)['y']*10
                                        z=adxl345.getAxes(True)['z']*10
                        
                                        a=1
                                        b=1
                                        m=1
                                        c=1
                                        d=1
                                        
                                                        
                                        if adxl345.getAxes(True)['x']*10>10:
                                                CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).clear()
                                                time.sleep(0.1)

                                                CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).write_string(' Enter  your     Patten')
                                                
                                                print 1
                                                time.sleep(1)
                                                while a==1:
                                                        if adxl345.getAxes(True)['x']*10<-9:
                                                                print 2
                                                                time.sleep(1)
                                                                while b==1:
                                                                        if adxl345.getAxes(True)['y']*10>9:
                                                                                print 3
                                                                                time.sleep(1)

                                                                                while c==1:
                                                                                        if adxl345.getAxes(True)['y']*10<-7 and  adxl345.getAxes(True)['x']*10<-7:
                                                                                                while m==1:
                                                                                                        
                                                                                                        p.ChangeDutyCycle(12.5)
                                                                                                        time.sleep(0.2)
                                                                                                        p.ChangeDutyCycle(0)
                                                                                                        GPIO.output(green,0)
                                                                                                        GPIO.output(bzr,0)
                                                                                                        CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).clear()
                                                                                                        time.sleep(0.1)


                                                                                                        CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).write_string('Door Opened')
                                                                                                        CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).write_string('Door Opened')
                                                                                                        h=1
                                                                                                        time.sleep(8)
                                                                                                        p.ChangeDutyCycle(2.5)
                                                                                                        time.sleep(0.25)
                                                                                                        p.ChangeDutyCycle(0)
                                                                                                        GPIO.output(green,1)
                                                                                                        CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).clear()
                                                                                                        time.sleep(0.1)
                                                                                                        CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36]).write_string('Door Closed')
                                                                                                        a+=1
                                                                                                        b+=1
                                                                                                        c+=1
                                                                                                        m+=1
                                                                                                        d+=1
                                                                                                        j+=1
                                                                                                        
                                                                        
                                                                                                        
                                                                                        elif adxl345.getAxes(True)['x']*10>9 or adxl345.getAxes(True)['y']*10>9:
                                                                                                while d==1:
                                                                                                        
                                                                                                        time.sleep(1)
                                                                                                        a+=1
                                                                                                        b+=1
                                                                                                        c+=1
                                                                                                        d+=1
                                                                                                        h+=1
                                                                                                                                
                                                                        elif adxl345.getAxes(True)['x']*10<-9 or adxl345.getAxes(True)['y']*10<-9 or adxl345.getAxes(True)['x']*10>9:
                                                                                while d==1:
                                                                                       
                                                                                        time.sleep(1)
                                                                                        a+=1
                                                                                        b+=1
                                                                                        c+=1
                                                                                        d+=1
                                                                                        h+=1
                                                                                                
                                                        elif adxl345.getAxes(True)['x']*10>9 or adxl345.getAxes(True)['y']*10<-9 or adxl345.getAxes(True)['y']*10>9:
                                                                while d==1:
                                                                
                                                                        time.sleep(1)
                                                                        a+=1
                                                                        b+=1
                                                                        c+=1
                                                                        d+=1
                                                                        h+=1
                                                                                      


                                                             
                                                                
                                                        
except KeyboardInterrupt:
        GPIO.cleanup()
        p.stop()
