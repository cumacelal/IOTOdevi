# Cuma Celal KORKMAZ
# IOT Ödevi

from __future__ import print_function
import smtplib
import boto3
import json
from decimal import *

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
    elif  TEMP[1:-1] > "27.0" :
         print("KIRMIZI LED")
    
    elif  HUMI[1:-1] < "50.0" :
         print("YEŞİL LED")
    
     elif  HUMI[1:-1] > "60.0" :
         print("KIRMIZI LED")

    else:
        print("Status normal. /n" + TEXT)
    
    return dName, Moment
