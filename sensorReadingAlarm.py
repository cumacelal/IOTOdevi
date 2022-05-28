# Cuma Celal KORKMAZ
# IOT Ödevi

from __future__ import print_function
import smtplib
import boto3
import json
import RPi.GPIO as GPIO // GPIO Pinlerini kontrol edebilmek için gerekli kütüphaneyi dahil ettik
import time // Zaman kutuphanesini dahil ettik
GPIO.cleanup() // Giriş çıkış pinlerinin verilerini sıfırladık
GPIO.setmode(GPIO.BCM) // BCM pin dizilimini seçtik
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
from decimal import *
 GPIO.setup(12, GPIO.OUT)
print('Loading function')

def lambda_handler(event, context):
    #get data from dynamoDB
    for record in event['Records']:
        AA = record['dynamodb']
        dName = json.dumps(AA['NewImage']['DeviceName']['S'])
        ID = json.dumps(AA['NewImage']['UUID']['S'])
        IP = json.dumps(AA['NewImage']['IP']['S'])
        TEMP = json.dumps(AA['NewImage']['Temperature']['N'])
        HUMI = json.dumps(AA['NewImage']['Humidity']['N'])
        Moment = json.dumps(AA['NewImage']['Moment']['S'])
        #set message
        text1 = dName+"\n Temperature : " +TEMP +"\n Humidity : " +HUMI
        text2 = "\n Time : " +Moment +"\n IP : " +IP    
        TEXT = text1 + text2
    
    #HUMI[1:-1]
    if TEMP[1:-1] < "23.0" :
        print("YEŞİL LED")
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)
    elif  TEMP[1:-1] > "27.0" :
         print("KIRMIZI LED")
         GPIO.output(17, GPIO.LOW)
         GPIO.output(18, GPIO.HIGH)
         time.sleep(1)
    
    elif  HUMI[1:-1] < "50.0" :
         print("YEŞİL LED")
         GPIO.output(19, GPIO.LOW)
         GPIO.output(20, GPIO.HIGH)
         time.sleep(1)
    
     elif  HUMI[1:-1] > "60.0" :
         print("KIRMIZI LED")
         GPIO.output(19, GPIO.HIGH)
         GPIO.output(20, GPIO.LOW)
         time.sleep(1)

    else:
        print("Status normal. /n" + TEXT)
         GPIO.output(17, GPIO.LOW)
         GPIO.output(18, GPIO.LOW)
         GPIO.output(19, GPIO.LOW)
         GPIO.output(20, GPIO.LOW)

    return dName, Moment
