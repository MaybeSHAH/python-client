#!usr/bin/python3



from pymysql import connect
from pymysql.cursors import DictCursor
import os, time
import sys
from _datetime import datetime as dt
import paho.mqtt.client as mqttClient
import time
import json
import mysql.connector
from threading import Thread, Lock
from pyModbusTCP.client import ModbusClient
from datetime import datetime

        
class globalBS():
    # set global
    
    manProcessStop1 = manProcessStart1 = manProcessStop2 = manProcessStart2 = False
    oldTagBit = processStop = processHalf = processStart = False
    braidOldTagBit1 = braidProcessStop1 = braidProcessHalf1 = braidProcessStart1 = False
    braidOldTagBit2 = braidProcessStop2 = braidProcessHalf2 = braidProcessStart2 = False
    braidOldTagBit3 = braidProcessStop3 = braidProcessHalf3 = braidProcessStart3 = False
    braidOldTagBit4 = braidProcessStop4 = braidProcessHalf4 = braidProcessStart4 = False
    braidOldTagBit5 = braidProcessStop5 = braidProcessHalf5 = braidProcessStart5 = False
    braidOldTagBit6 = braidProcessStop6 = braidProcessHalf6 = braidProcessStart6 = False
    braidOldTagBit7 = braidProcessStop7 = braidProcessHalf7 = braidProcessStart7 = False
    braidOldTagBit8 = braidProcessStop8 = braidProcessHalf8 = braidProcessStart8 = False
    covexOldTagBit = covexProcessStop = covexProcessHalf = covexProcessStart = False
    vulOldTagBit = vulProcessStop = vulProcessHalf = vulProcessStart = False
    testOldTagBit1 = testProcessStop1 = testProcessHalf1 = testProcessStart1 = False
    testOldTagBit2 = testProcessStop2 = testProcessHalf2 = testProcessStart2 = False
    testOldTagBit3 = testProcessStop3 = testProcessHalf3 = testProcessStart3 = False



dic = {}


#count2 = 0


# create the connection
connection = connect(host='localhost', port=3306, user='root', 
                     password='', db='pims', 
                     cursorclass=DictCursor, autocommit=True)

# get the cursor
mycursor = connection.cursor()
  


SERVER_HOST = '192.168.1.29'
SERVER_PORT = '502'





#publishing
def data(topic, q):
    client = mqttClient.Client("MQTT")
    client.username_pw_set("", "")
    client.connect('localhost', 1883)
    client.publish(topic, q)
    client.disconnect()

def fixedInt(val):
    if(val == ''):
        return '0'
    else:
        return val
                
def findFloat(val):
    return "{:.2f}".format(val)


def is_valid_json(data):
    try:
        json_obj = json.loads(data)
    except ValueError as e:
        connection.ping(reconnect=True)
        return False
    return True

#subscribing
def sub(topic):
    client = mqttClient.Client("MQTT")
    client.username_pw_set(username, pwd)
    client.connect(broker_add, port_no)
    client.subscribe(topic)
    client.disconnect()

def findBool(val):
    return val.lower() in ['1', 'true', 't']



def on_connect2(client, userdata, flags, rc):
    client.subscribe('polyhose1/')
    client.subscribe('polyhose2/')
    print("Thread4: subscribed")


def on_message2(client, userdata, message):
    try:    
        #global count2
        connection.ping(reconnect=True)

        if(message.topic == 'polyhose1/'):
            json_data = str(message.payload.decode("utf-8","ignore"))
            if(is_valid_json(json_data)):
                json_obj = json.loads(json_data)
                if(findBool(json_obj['connected'])):
                    dic['BraidTagBit_1'] = fixedInt(json_obj['M-B_H_1-2']) #Search bit
                    dic['BraidOkPir_1'] = fixedInt(json_obj['M-B_H_1-0']) #ok PIR
                    dic['BraidProStart_1'] = fixedInt(json_obj['M-B_H_1-5']) #Process Start
                    dic['BraidProHalf_1'] = fixedInt(json_obj['M-B_H_1-60']) #Process Half
                    dic['BraidProStop_1'] = fixedInt(json_obj['M-B_H_1-6']) #Process Stop
                    dic['BraidSearchBit_1'] = fixedInt(json_obj['M-B_H_1-1']) #Search pir
                    dic['BraidDrumOut_1'] = fixedInt(json_obj['M-B_P_1-1']) #Drum Out
                    
                    #braider---2
                    dic['BraidTagBit_2'] = fixedInt(json_obj['M-B_H_2-2']) #Search Bit
                    dic['BraidOkPir_2'] = fixedInt(json_obj['M-B_H_2-0']) #ok PIR
                    dic['BraidProStart_2'] = fixedInt(json_obj['M-B_H_2-5']) #Process Start
                    dic['BraidProHalf_2'] = fixedInt(json_obj['M-B_H_2-60']) #Process Half
                    dic['BraidProStop_2'] = fixedInt(json_obj['M-B_H_2-6']) #Process Stop
                    dic['BraidSearchBit_2'] = fixedInt(json_obj['M-B_H_2-1']) #search Pir
                    dic['BraidDrumOut_2'] = fixedInt(json_obj['M-B_P_2-1']) #Drum Out
                    
                    #braider---3
                    dic['BraidTagBit_3'] = fixedInt(json_obj['M-B_H_3-2']) #Search Bit
                    dic['BraidOkPir_3'] = fixedInt(json_obj['M-B_H_3-0']) #ok PIR
                    dic['BraidProStart_3'] = fixedInt(json_obj['M-B_H_3-5']) #Process Start
                    dic['BraidProHalf_3'] = fixedInt(json_obj['M-B_H_3-60']) #Process Half
                    dic['BraidProStop_3'] = fixedInt(json_obj['M-B_H_3-6']) #Process Stop
                    dic['BraidSearchBit_3'] = fixedInt(json_obj['M-B_H_3-1']) #search Pir
                    dic['BraidDrumOut_3'] = fixedInt(json_obj['M-B_P_3-1']) #Drum Out
                    
                    #braider---4
                    dic['BraidTagBit_4'] = fixedInt(json_obj['M-B_H_4-2']) #Search Bit
                    dic['BraidOkPir_4'] = fixedInt(json_obj['M-B_H_4-0']) #ok PIR
                    dic['BraidProStart_4'] = fixedInt(json_obj['M-B_H_4-5']) #Process Start
                    dic['BraidProHalf_4'] = fixedInt(json_obj['M-B_H_4-60']) #Process Half
                    dic['BraidProStop_4'] = fixedInt(json_obj['M-B_H_4-6']) #Process Stop
                    dic['BraidSearchBit_4'] = fixedInt(json_obj['M-B_H_4-1']) #search Pir
                    dic['BraidDrumOut_4'] = fixedInt(json_obj['M-B_P_4-1']) #Drum Out
                    
                    #braider---5
                    dic['BraidTagBit_5'] = fixedInt(json_obj['M-B_H_5-2']) #Search Bit
                    dic['BraidOkPir_5'] = fixedInt(json_obj['M-B_H_5-0']) #ok PIR
                    dic['BraidProStart_5'] = fixedInt(json_obj['M-B_H_5-5']) #Process Start
                    dic['BraidProHalf_5'] = fixedInt(json_obj['M-B_H_5-60']) #Process Half
                    dic['BraidProStop_5'] = fixedInt(json_obj['M-B_H_5-6']) #Process Stop
                    dic['BraidSearchBit_5'] = fixedInt(json_obj['M-B_H_5-1']) #search Pir
                    dic['BraidDrumOut_5'] = fixedInt(json_obj['M-B_P_5-1']) #Drum Out
                    
                    #braider---6
                    dic['BraidTagBit_6'] = fixedInt(json_obj['M-B_H_6-2']) #Search Bit
                    dic['BraidOkPir_6'] = fixedInt(json_obj['M-B_H_6-0']) #ok PIR
                    dic['BraidProStart_6'] = fixedInt(json_obj['M-B_H_6-5']) #Process Start
                    dic['BraidProHalf_6'] = fixedInt(json_obj['M-B_H_6-60']) #Process Half
                    dic['BraidProStop_6'] = fixedInt(json_obj['M-B_H_6-6']) #Process Stop
                    dic['BraidSearchBit_6'] = fixedInt(json_obj['M-B_H_6-1']) #search Pir
                    dic['BraidDrumOut_6'] = fixedInt(json_obj['M-B_P_6-1']) #Drum Out
                    
                    #braider---7
                    dic['BraidTagBit_7'] = fixedInt(json_obj['M-B_H_7-2']) #Search Bit
                    dic['BraidOkPir_7'] = fixedInt(json_obj['M-B_H_7-0']) #ok PIR
                    dic['BraidProStart_7'] = fixedInt(json_obj['M-B_H_7-5']) #Process Start
                    dic['BraidProHalf_7'] = fixedInt(json_obj['M-B_H_7-60']) #Process Half
                    dic['BraidProStop_7'] = fixedInt(json_obj['M-B_H_7-6']) #Process Stop
                    dic['BraidSearchBit_7'] = fixedInt(json_obj['M-B_H_7-1']) #search Pir
                    dic['BraidDrumOut_7'] = fixedInt(json_obj['M-B_P_7-1']) #Drum Out
                    
                    #braider---8
                    dic['BraidTagBit_8'] = fixedInt(json_obj['M-B_H_8-2']) #Search Bit
                    dic['BraidOkPir_8'] = fixedInt(json_obj['M-B_H_8-0']) #ok PIR
                    dic['BraidProStart_8'] = fixedInt(json_obj['M-B_H_8-5']) #Process Start
                    dic['BraidProHalf_8'] = fixedInt(json_obj['M-B_H_8-60']) #Process Half
                    dic['BraidProStop_8'] = fixedInt(json_obj['M-B_H_8-6']) #Process Stop
                    dic['BraidSearchBit_8'] = fixedInt(json_obj['M-B_H_8-1']) #search Pir
                    dic['BraidDrumOut_8'] = fixedInt(json_obj['M-B_P_8-1']) #Drum Out

                    #print(":::::::::::::::::::::INFO::::::::::::::::::::::::::::")
                    #print("BraidSearchBit ::", dic['BraidSearchBit_1'])
                    #print("BraidTagBit_1 ::", dic['BraidTagBit_1'])
                    if(findBool(dic['BraidTagBit_1'])):
                        dataCheck(str(dic['BraidSearchBit_1']), "Braider 1", "M-B_H_1-0", "Linear Extruder 1", "M-B_H_1-61", "M-B_H_1-62", "M-B_P_1-0", str(dic['BraidDrumOut_1']))
                    #print("BraidProStart_1 ::", dic['BraidProStart_1'])
                    if(findBool(dic['BraidProStart_1']) and not globalBS.braidProcessStart1):
                        #
                        
                        if(int(dic['BraidOkPir_1']) != 0 and int(dic['BraidOkPir_1']) != 1 ):
                            if(dataCheck1(str(dic['BraidOkPir_1']), str(dic['BraidProStart_1']), "pro_start", "Braider 1", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_1']))):
                                globalBS.braidProcessStart1 = True
                                globalBS.braidProcessStop1 = False
                    #print("BraidProHalf_1 ::", dic['BraidProHalf_1'])
                    if(dic['BraidProHalf_1'] == "1" and not globalBS.braidProcessHalf1):
                        globalBS.braidProcessHalf1 = True
                        if(findBool(dic['BraidOkPir_1'])):
                            dataCheck1(str(dic['BraidOkPir_1']), str(dic['BraidProHalf_1']), "pro_half", "Braider 1", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_1']))
                    #print("BraidProStop_1 ::", dic['BraidProStop_1'])
                    if(findBool(dic['BraidProStop_1']) and not globalBS.braidProcessStop1):
                        if(dic['BraidOkPir_1'] != 0):
                            if(dataCheck1(str(dic['BraidOkPir_1']), str(dic['BraidProStop_1']), "pro_stop", "Braider 1", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_1']))):
                                globalBS.braidProcessStop1 = True
                                globalBS.braidProcessHalf1 = False
                                globalBS.braidProcessStart1 = False
                                globalBS.braidOldTagBit1 = False
                    #print("BraidSearchBit_2 ::", dic['BraidSearchBit_2'])
                    if(findBool(dic['BraidTagBit_2'])):
                        dataCheck(str(dic['BraidSearchBit_2']), "Braider 2", "M-B_H_2-0", "Linear Extruder 1", "M-B_H_2-61", "M-B_H_2-62", "M-B_P_2-0", str(dic['BraidDrumOut_2']))
                    #print("BraidProStart_2 ::", dic['BraidProStart_2'])
                    if(findBool(dic['BraidProStart_2']) and not globalBS.braidProcessStart2):
                        #
                        if(int(dic['BraidOkPir_2']) != 0 and int(dic['BraidOkPir_2']) != 1):
                            if(dataCheck1(str(dic['BraidOkPir_2']), str(dic['BraidProStart_2']), "pro_start", "Braider 2", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_2']))):
                                globalBS.braidProcessStart2 = True
                                globalBS.braidProcessStop2 = False
                    
                    if(dic['BraidProHalf_2'] == "1" and not globalBS.braidProcessHalf2):
                        globalBS.braidProcessHalf2 = true;
                        if(findBool(dic['BraidOkPir_2'])):
                            dataCheck1(str(dic['BraidOkPir_2']), str(dic['BraidProHalf_2']), "pro_half", "Braider 2", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_2']))
                    #print("BraidProStop_2 ::", dic['BraidProStop_2'])
                    if(findBool(dic['BraidProStop_2']) and not globalBS.braidProcessStop2):
                        if(dic['BraidOkPir_2'] != 0):
                            if(dataCheck1(str(dic['BraidOkPir_2']), str(dic['BraidProStop_2']), "pro_stop", "Braider 2", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_2']))):
                                globalBS.braidProcessStop2 = True
                                globalBS.braidProcessHalf2 = False
                                globalBS.braidProcessStart2 = False
                                globalBS.braidOldTagBit2 = False
                    #print("BraidTagBit_3 ::", dic['BraidTagBit_3'])
                    if(findBool(dic['BraidTagBit_3'])):
                        dataCheck(str(dic['BraidSearchBit_3']), "Braider 3", "M-B_H_3-0", "Linear Extruder 1", "M-B_H_3-61", "M-B_H_3-62", "M-B_P_3-0", str(dic['BraidDrumOut_3']))
                    #print("BraidProStart_3 ::", dic['BraidProStart_3'])
                    if(findBool(dic['BraidProStart_3']) and not globalBS.braidProcessStart3):
                        #
                        if(int(dic['BraidOkPir_3']) != 0 and int(dic['BraidOkPir_3']) != 1):
                            if(dataCheck1(str(dic['BraidOkPir_3']), str(dic['BraidProStart_3']), "pro_start", "Braider 3", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_3']))):
                                globalBS.braidProcessStart3 = True
                                globalBS.braidProcessStop3 = False
                    if(dic['BraidProHalf_3'] == "1" and not globalBS.braidProcessHalf3):
                        globalBS.braidProcessHalf3 = True
                        if(findBool(dic['BraidOkPir_3'])):
                            dataCheck1(str(dic['BraidOkPir_3']), str(dic['BraidProHalf_3']), "pro_half", "Braider 3", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_3']))
                    #print("BraidProStop_3 ::", dic['BraidProStop_3'])
                    if(findBool(dic['BraidProStop_3']) and not globalBS.braidProcessStop3):
                        if(dic['BraidOkPir_3'] != 0):
                            if(dataCheck1(str(dic['BraidOkPir_3']), str(dic['BraidProStop_3']), "pro_stop", "Braider 3", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_3']))):
                                globalBS.braidProcessStop3 = True
                                globalBS.braidProcessHalf3 = False
                                globalBS.braidProcessStart3 = False
                                globalBS.braidOldTagBit3 = False
                    #print("BraidTagBit_4 ::", dic['BraidTagBit_4'])
                    if(findBool(dic['BraidTagBit_4'])):
                        dataCheck(str(dic['BraidSearchBit_4']), "Braider 4", "M-B_H_4-0", "Linear Extruder 1", "M-B_H_4-61", "M-B_H_4-62", "M-B_P_4-0", str(dic['BraidDrumOut_4']))
                    #print("BraidProStart_4 ::", dic['BraidProStart_4'])
                    if(findBool(dic['BraidProStart_4']) and not globalBS.braidProcessStart4):
                        #
                        if(int(dic['BraidOkPir_4']) != 0 and int(dic['BraidOkPir_4']) != 1 ):
                            if(dataCheck1(str(dic['BraidOkPir_4']), str(dic['BraidProStart_4']), "pro_start", "Braider 4", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_4']))):
                                globalBS.braidProcessStart4 = True
                                globalBS.braidProcessStop4 = False
                    if(dic['BraidProHalf_4'] == "1" and not globalBS.braidProcessHalf4):
                        globalBS.braidProcessHalf4 = True
                        if(findBool(dic['BraidOkPir_4'])):
                            dataCheck1(str(dic['BraidOkPir_4']), str(dic['BraidProHalf_4']), "pro_half", "Braider 4", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_4']))
                    #print("BraidProStop_4 ::", dic['BraidProStop_4'])
                    if(findBool(dic['BraidProStop_4']) and not globalBS.braidProcessStop4):
                        if(dic['BraidOkPir_4'] != 0):
                            if(dataCheck1(str(dic['BraidOkPir_4']), str(dic['BraidProStop_4']), "pro_stop", "Braider 4", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_4']))):
                                globalBS.braidProcessStop4 = True
                                globalBS.braidProcessHalf4 = False
                                globalBS.braidProcessStart4 = False
                                globalBS.braidOldTagBit4 = False
                    #print("BraidTagBit_5 ::", dic['BraidTagBit_5'])
                    if(findBool(dic['BraidTagBit_5'])):
                        dataCheck(str(dic['BraidSearchBit_5']), "Braider 5", "M-B_H_5-0", "Linear Extruder 1", "M-B_H_5-61", "M-B_H_5-62", "M-B_P_5-0", str(dic['BraidDrumOut_5']))
                    #print("BraidProStart_5 ::", dic['BraidProStart_5'])
                    if(findBool(dic['BraidProStart_5']) and not globalBS.braidProcessStart5):
                        
                        if(int(dic['BraidOkPir_5']) != 0 and int(dic['BraidOkPir_5']) != 1):
                            if(dataCheck1(str(dic['BraidOkPir_5']), str(dic['BraidProStart_5']), "pro_start", "Braider 5", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_5']))):
                                globalBS.braidProcessStart5 = True
                                globalBS.braidProcessStop5 = False
                    if(dic['BraidProHalf_5'] == "1" and not globalBS.braidProcessHalf5):
                        globalBS.braidProcessHalf5 = True
                        if(findBool(dic['BraidOkPir_5'])):
                            dataCheck1(str(dic['BraidOkPir_5']), str(dic['BraidProHalf_5']), "pro_half", "Braider 5", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_5']))
                    #print("BraidProStop_5 ::", dic['BraidProStop_5'])
                    if(findBool(dic['BraidProStop_5']) and not globalBS.braidProcessStop5):
                        if(dic['BraidOkPir_5'] != 0):
                            if(dataCheck1(str(dic['BraidOkPir_5']), str(dic['BraidProStop_5']), "pro_stop", "Braider 5", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_5']))):
                                globalBS.braidProcessStop5 = True
                                globalBS.braidProcessHalf5 = False
                                globalBS.braidProcessStart5 = False
                                globalBS.braidOldTagBit5 = False

                    #print("BraidTagBit_6 ::", dic['BraidTagBit_6'])
                    if(findBool(dic['BraidTagBit_6'])):
                        dataCheck(str(dic['BraidSearchBit_6']), "Braider 6", "M-B_H_6-0", "Linear Extruder 1", "M-B_H_6-61", "M-B_H_6-62", "M-B_P_6-0", str(dic['BraidDrumOut_6']))
                    #print("BraidProStart_6 ::", dic['BraidProStart_6'])
                    if(findBool(dic['BraidProStart_6']) and not globalBS.braidProcessStart6):
                        
                        if(int(dic['BraidOkPir_6']) != 0 and int(dic['BraidOkPir_6']) != 1):
                            if(dataCheck1(str(dic['BraidOkPir_6']), str(dic['BraidProStart_6']), "pro_start", "Braider 6", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_6']))):
                                globalBS.braidProcessStart6 = True
                                globalBS.braidProcessStop6 = False
                    if(dic['BraidProHalf_6'] == "1" and not globalBS.braidProcessHalf6):
                        globalBS.braidProcessHalf6 = True
                        if(findBool(dic['BraidOkPir_6'])):
                            dataCheck1(str(dic['BraidOkPir_6']), str(dic['BraidProHalf_6']), "pro_half", "Braider 6", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_6']))
                    #print("BraidProStop_6 ::", dic['BraidProStop_6'])
                    if(findBool(dic['BraidProStop_6']) and not globalBS.braidProcessStop6):
                        if(dic['BraidOkPir_6']):
                            if(dataCheck1(str(dic['BraidOkPir_6']), str(dic['BraidProStop_6']), "pro_stop", "Braider 6", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_6']))):
                                globalBS.braidProcessStop6 = True
                                globalBS.braidProcessHalf6 = False
                                globalBS.braidProcessStart6 = False
                                globalBS.braidOldTagBit6 = False
                    #print("BraidTagBit_7 ::", dic['BraidTagBit_7'])
                    if(findBool(dic['BraidTagBit_7'])):
                        dataCheck(str(dic['BraidSearchBit_7']), "Braider 7", "M-B_H_7-0", "Linear Extruder 1", "M-B_H_7-61", "M-B_H_7-62", "M-B_P_7-0", str(dic['BraidDrumOut_7']))
                    #print("BraidProStart_7 ::", dic['BraidProStart_7'])
                    if(findBool(dic['BraidProStart_7']) and not globalBS.braidProcessStart7):
                        #
                        if(int(dic['BraidOkPir_7']) != 0 and int(dic['BraidOkPir_7']) != 1 ):
                            if(dataCheck1(str(dic['BraidOkPir_7']), str(dic['BraidProStart_7']), "pro_start", "Braider 7", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_7']))):
                                globalBS.braidProcessStart7 = True
                                globalBS.braidProcessStop7 = False
                    if(dic['BraidProHalf_7'] == "1" and not globalBS.braidProcessHalf7):
                        globalBS.braidProcessHalf7 = True
                        if(findBool(dic['BraidOkPir_7'])):
                            dataCheck1(str(dic['BraidOkPir_7']), str(dic['BraidProHalf_7']), "pro_half", "Braider 7", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_7']))
                    #print("BraidProStop_7 ::", dic['BraidProStop_7'])
                    if(findBool(dic['BraidProStop_7']) and not globalBS.braidProcessStop7):
                        if(dic['BraidOkPir_7'] != 0):
                            if(dataCheck1(str(dic['BraidOkPir_7']), str(dic['BraidProStop_7']), "pro_stop", "Braider 7", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_7']))):
                                globalBS.braidProcessStop7 = True
                                globalBS.braidProcessHalf7 = False
                                globalBS.braidProcessStart7 = False
                                globalBS.braidOldTagBit7 = False
                    #print("BraidTagBit_8 ::", dic['BraidTagBit_8'])
                    if(findBool(dic['BraidTagBit_8'])):
                        dataCheck(str(dic['BraidSearchBit_8']), "Braider 8", "M-B_H_8-0", "Linear Extruder 1", "M-B_H_8-61", "M-B_H_8-62", "M-B_P_8-0", str(dic['BraidDrumOut_8']))
                    #print("BraidProStart_8 ::", dic['BraidProStart_8'])
                    if(findBool(dic['BraidProStart_8']) and not globalBS.braidProcessStart8):
                        #
                        if(int(dic['BraidOkPir_8']) != 0 and int(dic['BraidOkPir_8']) != 1):
                            if(dataCheck1(str(dic['BraidOkPir_8']), str(dic['BraidProStart_8']), "pro_start", "Braider 8", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_8']))):
                                globalBS.braidProcessStart8 = True
                                globalBS.braidProcessStop8 = False
                    if(dic['BraidProHalf_8'] == "1" and not globalBS.braidProcessHalf8):
                        globalBS.braidProcessHalf8 = True
                        if(findBool(dic['BraidOkPir_8'])):
                            dataCheck1(str(dic['BraidOkPir_8']), str(dic['BraidProHalf_8']), "pro_half", "Braider 8", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_8']))
                    #print("BraidProStop_8 ::", dic['BraidProStop_8'])
                    if(findBool(dic['BraidProStop_8']) and not globalBS.braidProcessStop8):
                        if(dic['BraidOkPir_8'] != 0):
                            if(dataCheck1(str(dic['BraidOkPir_8']), str(dic['BraidProStop_8']), "pro_stop", "Braider 8", "Linear Extruder 1", "", "", str(dic['BraidDrumOut_8']))):
                                globalBS.braidProcessStop8 = True
                                globalBS.braidProcessHalf8 = False
                                globalBS.braidProcessStart8 = False
                                globalBS.braidOldTagBit8 = False
                    
                    
                
        if message.topic == 'polyhose2/':
            #count2 += 1
            json_data = str(message.payload.decode("utf-8","ignore"))
            if(is_valid_json(json_data)):
                json_obj = json.loads(json_data)
                if(findBool(json_obj['connected'])):
                    dic['CovexTagBit'] = fixedInt(json_obj['M-E_H_3-1']) #search bit
                    dic['CovexOkPir'] = fixedInt(json_obj['M-E_H_3-0']) #ok PIR
                    dic['CovexProStart'] = fixedInt(json_obj['M-E_H_3-44']) #Process Start
                    dic['CovexProHalf'] = fixedInt(json_obj['M-E_H_3-53']) #Process Half
                    dic['CovexProStop'] =  fixedInt(json_obj['M-E_H_3-45']) #Process Stop
                    dic['CovexSearchBit'] = fixedInt(json_obj['M-E_H_3-2']) #Search pir
                    dic['CovexDrumOut'] = fixedInt(json_obj['M-E_P_3-1']) #Drum Out
                    #Vulcaniser
                    dic['VulTagBit'] = fixedInt(json_obj['M-V_H_1-11']) #search bit
                    dic['VulOkPir'] = fixedInt(json_obj['M-V_H_1-12']) #ok PIR
                    dic['VulOkPir1'] = fixedInt(json_obj['M-V_H_1-3']) #ok PIR
                    dic['VulOkPir2'] = fixedInt(json_obj['M-V_H_1-4']) #ok PIR
                    dic['VulOkPir3'] = fixedInt(json_obj['M-V_H_1-5']) #ok PIR
                    dic['VulOkPir4'] = fixedInt(json_obj['M-V_H_1-6']) #ok PIR
                    dic['VulOkPir5'] = fixedInt(json_obj['M-V_H_1-7']) #ok PIR
                    dic['VulOkPir6'] = fixedInt(json_obj['M-V_H_1-16']) #ok PIR
                    dic['VulProStart'] = fixedInt(json_obj['M-V_H_1-8']) #Process Start
                    dic['VulProHalf']  = fixedInt(json_obj['M-V_H_1-13']) #Process Half
                    dic['VulProStop'] = fixedInt(json_obj['M-V_H_1-9']) #Process Stop
                    dic['VulSearchBit'] = fixedInt(json_obj['M-V_H_1-10']) #Search pir
                    dic['VulDrumOut'] = fixedInt(json_obj['M-V_P_1-11']) #Drum Out
                    dic['VulDrumOut1'] = fixedInt(json_obj['M-V_H_1-17']) #Drum Out
                    dic['VulDrumOut2'] = fixedInt(json_obj['M-V_H_1-18']) #Drum Out
                    dic['VulDrumOut3'] = fixedInt(json_obj['M-V_H_1-19']) #Drum Out
                    dic['VulDrumOut4'] = fixedInt(json_obj['M-V_H_1-20']) #Drum Out
                    dic['VulDrumOut5'] = fixedInt(json_obj['M-V_H_1-21']) #Drum Out
                    dic['VulDrumOut6'] = fixedInt(json_obj['M-V_H_1-22']) #Drum Out
                    #Testing 1
                    dic['TestTagBit_1'] = fixedInt(json_obj['M-T_H_1-6']) #search bit
                    dic['TestOkPir_1'] = fixedInt(json_obj['M-T_R_1-0']) #ok PIR
                    dic['TestProStart_1'] = fixedInt(json_obj['M-T_H_1-0']) #Process Start
                    dic['TestProHalf_1'] = fixedInt(json_obj['M-T_H_1-8']) #Process Half
                    dic['TestProStop_1'] = fixedInt(json_obj['M-T_H_1-1']) #Process Stop
                    dic['TestSearchBit_1'] = fixedInt(json_obj['M-T_H_1-5']) #Search pir
                    dic['TestDrumOut_1'] = fixedInt(json_obj['M-T_P_1-1']) #Drum Out
                    #Testing 2
                    dic['TestTagBit_2'] = fixedInt(json_obj['M-T_H_2-6']) #search bit
                    dic['TestOkPir_2'] = fixedInt(json_obj['M-T_R_2-0']) #ok PIR
                    dic['TestProStart_2'] = fixedInt(json_obj['M-T_H_2-0']) #Process Start
                    dic['TestProHalf_2'] = fixedInt(json_obj['M-T_H_2-8']) #Process Half
                    dic['TestProStop_2'] = fixedInt(json_obj['M-T_H_2-1']) #Process Stop
                    dic['TestSearchBit_2'] = fixedInt(json_obj['M-T_H_2-5']) #Search pir
                    dic['TestDrumOut_2'] = fixedInt(json_obj['M-T_P_2-1']) #Drum Out
                    #Testing 3
                    dic['TestTagBit_3'] = fixedInt(json_obj['M-T_H_3-6']) #search bit
                    dic['TestOkPir_3'] = fixedInt(json_obj['M-T_R_3-0']) #ok PIR
                    dic['TestProStart_3'] = fixedInt(json_obj['M-T_H_3-0']) #Process Start
                    dic['TestProHalf_3'] =  fixedInt(json_obj['M-T_H_3-8']) #Process Half
                    dic['TestProStop_3'] = fixedInt(json_obj['M-T_H_3-1']) #Process Stop
                    dic['TestSearchBit_3'] = fixedInt(json_obj['M-T_H_3-5']) #Search pir
                    dic['TestDrumOut_3'] = fixedInt(json_obj['M-T_P_3-1']) #Drum Out 
                    #Mandrel---1
                    dic['ManProStart_1'] = fixedInt(json_obj['M-M_H_1-4']) #Process Start
                    dic['ManProStop_1'] = fixedInt(json_obj['M-M_H_1-5']) #Process Stop
                    dic['ManOldPir1_1'] = fixedInt(json_obj['M-M_H_1-1']) #Old PIR 1
                    dic['ManOldPir2_1'] = fixedInt(json_obj['M-M_H_1-2']) #Old PIR 2
                    dic['ManOldPir3_1'] = fixedInt(json_obj['M-M_H_1-3']) #Old PIR 3
                    dic['ManMpir_1'] = fixedInt(json_obj['M-M_H_1-0']) #MPIR
                    dic['ManDrumIn_1'] = fixedInt(json_obj['M-M_P_1-0']) #Drum In
                    dic['ManDrumOut_1'] = fixedInt(json_obj['M-M_P_1-1']) #Drum Out
                    #Mandrel---2
                    dic['ManProStart_2'] = fixedInt(json_obj['M-M_H_2-4']) #Process Start
                    dic['ManProStop_2'] =  fixedInt(json_obj['M-M_H_2-5']) #Process Stop
                    dic['ManOldPir1_2'] = fixedInt(json_obj['M-M_H_2-1']) #Old PIR 1
                    dic['ManOldPir2_2'] = fixedInt(json_obj['M-M_H_2-2']) #Old PIR 2
                    dic['ManOldPir3_2'] = fixedInt(json_obj['M-M_H_2-3']) #Old PIR 3
                    dic['ManMpir_2'] = fixedInt(json_obj['M-M_H_2-0']) #MPIR
                    dic['ManDrumIn_2'] = fixedInt(json_obj['M-M_P_2-0']) #Drum In
                    dic['ManDrumOut_2'] = fixedInt(json_obj['M-M_P_2-1']) #Drum Out
                    #Linear Extruder---1
                    dic['TagBit'] = fixedInt(json_obj['M-E_H_1-1']) #search bit #should find 1
                    dic['OkPir'] = fixedInt(json_obj['M-E_H_1-0']) #ok PIR
                    dic['Mpir'] = fixedInt(json_obj['M-E_H_1-56']) #MPIR
                    dic['ProStart'] = fixedInt(json_obj['M-E_H_1-44']) #Process Start
                    dic['ProHalf'] = fixedInt(json_obj['M-E_H_1-53']) #Process Half
                    dic['ProStop'] = fixedInt(json_obj['M-E_H_1-45']) #Process Stop
                    dic['SearchBit'] = fixedInt(json_obj['M-E_H_1-2']) #Search pir
                    dic['DrumIn'] = fixedInt(json_obj['M-E_P_1-0']) #Drum In
                    dic['DrumOut'] = fixedInt(json_obj['M-E_P_1-1']) #Drum Out
                    #
                    #print("ManProStart_1 ::", dic['ManProStart_1'])
                    if(findBool(dic['ManProStart_1']) and not globalBS.manProcessStart1):
                        globalBS.manProcessStart1 = True
                        globalBS.manProcessStop1 = False
                        insertManProData("Mandrel 1", str(dic['ManOldPir1_1']), str(dic['ManOldPir2_1']), str(dic['ManOldPir3_1']), str(dic['ManMpir_1']), str(dic['ManDrumIn_1']), str(dic['ManDrumOut_1']), str(dic['ManProStart_1']), "0")
                    #
                    #print("ManProStop_1 ::", dic['ManProStop_1'])
                    if(findBool(dic['ManProStop_1']) and not globalBS.manProcessStop1):
                        globalBS.manProcessStop1 = True
                        globalBS.manProcessStart1 = False
                        insertManProData("Mandrel 1", str(dic['ManOldPir1_1']), str(dic['ManOldPir2_1']), str(dic['ManOldPir3_1']), str(dic['ManMpir_1']), str(dic['ManDrumIn_1']), str(dic['ManDrumOut_1']), "0", str(dic['ManProStop_1']))
                    #
                    #print("ManProStart_2 ::", dic['ManProStart_2'])
                    if(findBool(dic['ManProStart_2']) and not globalBS.manProcessStart2):
                        globalBS.manProcessStart2 = True
                        globalBS.manProcessStop2 = False
                        insertManProData("Mandrel 2", str(dic['ManOldPir1_2']), str(dic['ManOldPir2_2']), str(dic['ManOldPir3_2']), str(dic['ManMpir_2']), str(dic['ManDrumIn_2']), str(dic['ManDrumOut_2']), str(dic['ManProStart_2']), "0")
                    #
                    #print("ManProStop_2 ::", dic['ManProStop_2'])
                    if(findBool(dic['ManProStop_2']) and not globalBS.manProcessStop2):
                        globalBS.manProcessStop2 = True
                        globalBS.manProcessStart2 = False
                        insertManProData("Mandrel 2", str(dic['ManOldPir1_2']), str(dic['ManOldPir2_2']), str(dic['ManOldPir3_2']), str(dic['ManMpir_2']), str(dic['ManDrumIn_2']), str(dic['ManDrumOut_2']), "0", str(dic['ManProStop_2']))
                    #::::::::::::::::::::::::::::::::::::::::::::LINEAR::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    #print("TagBit ::", dic['TagBit'])
                    if(findBool(dic['TagBit'])):
                        dataCheck(str(dic['SearchBit']), "Linear Extruder 1", "M-E_H_1-0", "", "M-E_H_1-54", "M-E_H_1-55", "M-E_P_1-0", str(dic['DrumOut']))
                    #
                    #print("ProStart ::", dic['ProStart'])
                    #print("processStart (Bool) ::", globalBS.processStart)
                    if(findBool(dic['ProStart']) and not globalBS.processStart):
                        #globalBS.processStart = True
                        #print("OkPir ::", dic['ProStart'])
                        if(int(dic['OkPir']) != 0 and int(dic['OkPir']) != 1 ):
                            if(dataCheck1(str(dic['OkPir']), str(dic['ProStart']), "pro_start", "Linear Extruder 1", "Linear Extruder 1", str(dic['Mpir']), str(dic['DrumIn']), str(dic['DrumOut']))):
                                globalBS.processStart = True
                                globalBS.processStop = False
                    #
                    #print("ProHalf ::", dic['ProHalf'])
                    if(findBool(dic['ProHalf']) and not globalBS.processHalf):
                        globalBS.processHalf = True
                        if(int(dic['OkPir']) != 0):
                            dataCheck1(str(dic['OkPir']), str(dic['ProHalf']), "pro_half", "Linear Extruder 1", "Linear Extruder 1", str(dic['Mpir']), str(dic['DrumIn']), str(dic['DrumOut']))
                    #
                    #print("ProStop ::", dic['ProStop'])
                    #print("processStop (Bool) ::", globalBS.processStop)
                    if(findBool(dic['ProStop']) and not globalBS.processStop):
                        if(dic['OkPir'] != 0):
                            if(dataCheck1(str(dic['OkPir']), str(dic['ProStop']), "pro_stop", "Linear Extruder 1", "Linear Extruder 1", str(dic['Mpir']), str(dic['DrumIn']), str(dic['DrumOut']))):
                                globalBS.processStop = True
                                globalBS.processHalf = False
                                globalBS.processStart = False
                        
                    #
                    #print("CovexTagBit::", dic['CovexTagBit'])
                    if(findBool(dic['CovexTagBit'])):
                        dataCheck(str(dic['CovexSearchBit']), "Cover Extruder", "M-E_H_3-0", "Braider ", "M-E_H_3-54", "M-E_H_3-55", "M-E_P_3-0", str(dic['CovexDrumOut']))
                    #
                    #print("CovexProStart::", dic['CovexProStart'])
                    if(findBool(dic['CovexProStart']) and not globalBS.covexProcessStart):
                        #globalBS.covexProcessStart = True
                        if(int(dic['CovexOkPir']) != 0 and int(dic['CovexOkPir']) != 1):
                            if(dataCheck1(str(dic['CovexOkPir']), str(dic['CovexProStart']), "pro_start", "Cover Extruder", "Braider ", "", "", str(dic['CovexDrumOut']))):
                                globalBS.covexProcessStart = True
                                globalBS.covexProcessStop = False
                    #
                    if(findBool(dic['CovexProHalf']) and not globalBS.covexProcessHalf):
                        globalBS.covexProcessHalf = True
                        if(dic['CovexOkPir'] != 0):
                            dataCheck1(str(dic['CovexOkPir']), str(dic['CovexProHalf']), "pro_half", "Cover Extruder", "Braider ", "", "", str(dic['CovexDrumOut']))

                    # 
                    #print("CovexProStop::", dic['CovexProStop'])
                    if(findBool(dic['CovexProStop']) and not globalBS.covexProcessStop):
                        if(dic['CovexOkPir'] != 0):
                            if(dataCheck1(str(dic['CovexOkPir']), str(dic['CovexProStop']), "pro_stop", "Cover Extruder", "Braider ", "", "", str(dic['CovexDrumOut']))):
                                globalBS.covexProcessStop = True
                                globalBS.covexProcessHalf = False
                                globalBS.covexProcessStart = False
                                globalBS.covexOldTagBit = False
                        
                    #::::::::::::::::::::::::::::::::::::::::::::::::::Vulcanizer::::::::::::::::::::::::::::::::::::::::::::::::
                    #print("VulTagBit::", dic['VulTagBit'])
                    if(findBool(dic['VulTagBit'])):
                        dataCheck(str(dic['VulSearchBit']), "Vulcaniser 1", "M-V_H_1-12", "Cover Extruder", "M-V_H_1-14", "M-V_H_1-15", "M-V_P_1-0", str(dic['VulDrumOut']))
                    #
                    #print("VulProStart::", dic['VulProStart'])
                    if(findBool(dic['VulProStart']) and not globalBS.vulProcessStart):
                        
                        if(int(dic['VulOkPir1']) != 0 and int(dic['VulOkPir1']) != 1):
                            if(dataCheck1(str(dic['VulOkPir1']), str(dic['VulProStart']), "pro_start", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut1']), str(dic['VulDrumOut1']))):
                                globalBS.vulProcessStart = True
                                globalBS.vulProcessStop = False

                        if(int(dic['VulOkPir2']) != 0 and int(dic['VulOkPir2']) != 1):
                            if(dataCheck1(str(dic['VulOkPir2']), str(dic['VulProStart']), "pro_start", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut2']), str(dic['VulDrumOut2']))):
                                globalBS.vulProcessStart = True
                                globalBS.vulProcessStop = False

                        if(int(dic['VulOkPir3']) != 0 and int(dic['VulOkPir3']) != 1):
                            if(dataCheck1(str(dic['VulOkPir3']), str(dic['VulProStart']), "pro_start", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut3']), str(dic['VulDrumOut3']))):
                                globalBS.vulProcessStart = True
                                globalBS.vulProcessStop = False
                        
                        if(int(dic['VulOkPir4']) != 0 and int(dic['VulOkPir4']) != 1):
                            if(dataCheck1(str(dic['VulOkPir4']), str(dic['VulProStart']), "pro_start", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut4']), str(dic['VulDrumOut4']))):
                                globalBS.vulProcessStart = True
                                globalBS.vulProcessStop = False
                              
                        if(int(dic['VulOkPir5']) != 0 and int(dic['VulOkPir5']) != 1):
                            if(dataCheck1(str(dic['VulOkPir5']), str(dic['VulProStart']), "pro_start", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut5']), str(dic['VulDrumOut5']))):
                                globalBS.vulProcessStart = True
                                globalBS.vulProcessStop = False

                        if(int(dic['VulOkPir6']) != 0 and int(dic['VulOkPir6']) != 1):
                            if(dataCheck1(str(dic['VulOkPir6']), str(dic['VulProStart']), "pro_start", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut6']), str(dic['VulDrumOut6']))):
                                globalBS.vulProcessStart = True
                                globalBS.vulProcessStop = False                
                    #
                    if(findBool(dic['VulProHalf']) and not globalBS.vulProcessHalf):
                        globalBS.vulProcessHalf = True
                        if(dic['VulOkPir1'] != 0):
                            dataCheck1(str(dic['VulOkPir1']), str(dic['VulProHalf']), "pro_half", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut1']), str(dic['VulDrumOut1']))
                   
                    #print("VulProStop::", dic['VulProStop'])
                    if(findBool(dic['VulProStop']) and not globalBS.vulProcessStop):
                        if(dic['VulOkPir1'] != 0):
                            if(dataCheck1(str(dic['VulOkPir1']), str(dic['VulProStop']), "pro_stop", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut1']), str(dic['VulDrumOut1']))):
                                globalBS.vulProcessStop = True
                                globalBS.vulProcessHalf = False
                                globalBS.vulProcessStart = False
                                globalBS.vulOldTagBit = False
                        if(dic['VulOkPir2'] != 0):
                            if(dataCheck1(str(dic['VulOkPir2']), str(dic['VulProStop']), "pro_stop", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut2']), str(dic['VulDrumOut2']))):
                                globalBS.vulProcessStop = True
                                globalBS.vulProcessHalf = False
                                globalBS.vulProcessStart = False
                                globalBS.vulOldTagBit = False 
                        if(dic['VulOkPir3'] != 0):
                            if(dataCheck1(str(dic['VulOkPir3']), str(dic['VulProStop']), "pro_stop", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut3']), str(dic['VulDrumOut3']))):
                                globalBS.vulProcessStop = True
                                globalBS.vulProcessHalf = False
                                globalBS.vulProcessStart = False
                                globalBS.vulOldTagBit = False  
                        if(dic['VulOkPir4'] != 0):
                            if(dataCheck1(str(dic['VulOkPir4']), str(dic['VulProStop']), "pro_stop", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut4']), str(dic['VulDrumOut4']))):
                                globalBS.vulProcessStop = True
                                globalBS.vulProcessHalf = False
                                globalBS.vulProcessStart = False
                                globalBS.vulOldTagBit = False  
                        if(dic['VulOkPir5'] != 0):
                            if(dataCheck1(str(dic['VulOkPir5']), str(dic['VulProStop']), "pro_stop", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut5']), str(dic['VulDrumOut5']))):
                                globalBS.vulProcessStop = True
                                globalBS.vulProcessHalf = False
                                globalBS.vulProcessStart = False
                                globalBS.vulOldTagBit = False  
                        if(dic['VulOkPir6'] != 0):
                            if(dataCheck1(str(dic['VulOkPir6']), str(dic['VulProStop']), "pro_stop", "Vulcaniser 1", "Cover Extruder", "", str(dic['VulDrumOut6']), str(dic['VulDrumOut6']))):
                                globalBS.vulProcessStop = True
                                globalBS.vulProcessHalf = False
                                globalBS.vulProcessStart = False
                                globalBS.vulOldTagBit = False                  

                    #print("TestTagBit_1 ::", dic['TestTagBit_1'])
                    if(findBool(dic['TestTagBit_1'])):
                        dataCheck(str(dic['TestSearchBit_1']), "Testing 1", "M-T_R_1-0", "Vulcaniser 1", "M-T_H_1-9", "M-T_H_1-10", "M-T_P_1-0", str(dic['TestDrumOut_1']))
                    #print("TestProStart_1 ::", dic['TestProStart_1'])
                    if(findBool(dic['TestProStart_1']) and not globalBS.testProcessStart1):
                        #
                        if(int(dic['TestOkPir_1']) != 0 and int(dic['TestOkPir_1']) != 1):
                            if(dataCheck1(str(dic['TestOkPir_1']), str(dic['TestProStart_1']), "pro_start", "Testing 1", "Vulcaniser 1", "", "", str(dic['TestDrumOut_1']))):
                                globalBS.testProcessStart1 = True
                                globalBS.testProcessStop1 = False
                    if(findBool(dic['TestProHalf_1']) and not globalBS.testProcessHalf1):
                        globalBS.testProcessHalf1 = True
                        if(dic['TestOkPir_1'] != 0):
                            dataCheck1(str(dic['TestOkPir_1']), str(dic['TestProHalf_1']), "pro_half", "Testing 1", "Vulcaniser 1", "", "", str(dic['TestDrumOut_1']))
                    #print("TestProStop_1 ::", dic['TestProStop_1'])
                    if(findBool(dic['TestProStop_1']) and not globalBS.testProcessStop1):
                        if(dic['TestOkPir_1'] != 0):
                            if(dataCheck1(str(dic['TestOkPir_1']), str(dic['TestProStop_1']), "pro_stop", "Testing 1", "Vulcaniser 1", "", "", str(dic['TestDrumOut_1']))):
                                globalBS.testProcessStop1 = True
                                globalBS.testProcessHalf1 = False
                                globalBS.testProcessStart1 = False
                                globalBS.testOldTagBit1 = False
                    #
                    #print("TestTagBit_2 ::", dic['TestTagBit_2'])
                    if(findBool(dic['TestTagBit_2'])):
                        dataCheck(str(dic['TestSearchBit_2']), "Testing 2", "M-T_R_2-0", "Vulcaniser 1", "M-T_H_2-9", "M-T_H_2-10", "M-T_P_2-0", str(dic['TestDrumOut_2']))
                    #
                    #print("TestProStart_2 ::", dic['TestProStart_2'])
                    if(findBool(dic['TestProStart_2']) and not globalBS.testProcessStart2):
                        
                        if(int(dic['TestOkPir_2']) != 0 and int(dic['TestOkPir_2']) != 1):
                            if(dataCheck1(str(dic['TestOkPir_2']), str(dic['TestProStart_2']), "pro_start", "Testing 2", "Vulcaniser 1", "", "", str(dic['TestDrumOut_2']))):
                                globalBS.testProcessStart2 = True
                                globalBS.testProcessStop2 = False
                    #
                    if(dic['TestProHalf_2'] == "1" and not globalBS.testProcessHalf2):
                        globalBS.testProcessHalf2 = True
                        if(findBool(dic['TestOkPir_2'])):
                            dataCheck1(str(dic['TestOkPir_2']), str(dic['TestProHalf_2']), "pro_half", "Testing 2", "Vulcaniser 1", "", "", str(dic['TestDrumOut_2']))
                    #
                    #print("TestProStop_2 ::", dic['TestProStop_2'])
                    if(findBool(dic['TestProStop_2']) and not globalBS.testProcessStop2):
                        if(dic['TestOkPir_2'] != 0):
                            if(dataCheck1(str(dic['TestOkPir_2']), str(dic['TestProStop_2']), "pro_stop", "Testing 2", "Vulcaniser 1", "", "", str(dic['TestDrumOut_2']))):
                                globalBS.testProcessStop2 = True
                                globalBS.testProcessHalf2 = False
                                globalBS.testProcessStart2 = False
                                globalBS.testOldTagBit2 = False
                    #print("TestTagBit_3 ::", dic['TestTagBit_3'])
                    if(findBool(dic['TestTagBit_3'])):
                        dataCheck(str(dic['TestSearchBit_3']), "Testing 3", "M-T_R_3-0", "Vulcaniser 1", "M-T_H_3-9", "M-T_H_3-10", "M-T_P_3-0", str(dic['TestDrumOut_3']))
                    #
                    #print("TestProStart_3 ::", dic['TestProStart_3'])
                    if(findBool(dic['TestProStart_3']) and not globalBS.testProcessStart3):
                        #
                        if(int(dic['TestOkPir_3']) != 0 and int(dic['TestOkPir_3']) != 1):
                            if(dataCheck1(str(dic['TestOkPir_3']), str(dic['TestProStart_3']), "pro_start", "Testing 3", "Vulcaniser 1", "", "", str(dic['TestDrumOut_3']))):
                                globalBS.testProcessStart3 = True
                                globalBS.testProcessStop3 = False
                    #
                    if(dic['TestProHalf_3'] == "1" and not globalBS.testProcessHalf3):
                        globalBS.testProcessHalf3 = True
                        if(findBool(dic['TestOkPir_3'])):
                            dataCheck1(str(dic['TestOkPir_3']), str(dic['TestProHalf_3']), "pro_half", "Testing 3", "Vulcaniser 1", "", "", str(dic['TestDrumOut_3']))
                    #
                    #print("TestProStop_3 ::", dic['TestProStop_3'])
                    if(findBool(dic['TestProStop_3']) and not globalBS.testProcessStop3):
                        if(dic['TestOkPir_3'] != 0):
                            if(dataCheck1(str(dic['TestOkPir_3']), str(dic['TestProStop_3']), "pro_stop", "Testing 3", "Vulcaniser 1", "", "", str(dic['TestDrumOut_3']))):
                                globalBS.testProcessStop3 = True
                                globalBS.testProcessHalf3 = False
                                globalBS.testProcessStart3 = False
                                globalBS.testOldTagBit3 = False
        
                                    
    except(error):
        print("Error ::", error)




def on_disconnect(client, userdata, rc=0):
    print("disconnect")
    client.loop_stop()


def insertManProData(machineName, pir1, pir2, pir3, mpir, drumin, drumout, start, stop):
    try:
        sql = "INSERT INTO pirtracking_man (machine_name, old_pir_1, old_pir_2, old_pir_3, mpir, drum_in, drum_out, process_start, process_half, process_stop) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        val = (machineName, pir1, pir2, pir3, mpir, drumin, drumout, start, "0", stop)
        mycursor.execute(sql, val)
        print("Inserted Man Pro Data")
    except(error):
        print("Error: ", error)

def dataCheck(searchBit, machineName, publishTag, searchMachine, hoseType, hoseSize, drumOutTag, drumOut):
    temp1 = {}
    temp1['no'] = 0
    query = "SELECT pir_no, type, size FROM `planningcsvmaster` WHERE pir_no = "+ searchBit
    query1 = "SELECT * FROM `pirtracking` WHERE pir_no = '" + searchBit + "' AND machine_name like '" + searchMachine +"%' order by date_time desc limit 1"
    query2 = "SELECT * FROM `pirtracking` WHERE pir_no = '" + searchBit + "' AND machine_name like '" + machineName.split()[0] + "%' AND process_stop = '1' order by date_time desc limit 1"

    mycursor.execute(query2)
    if (mycursor.rowcount > 0):
        temp1['no'] = 1
    else:
        if( machineName == "Linear Extruder 1"):
            try:
                mycursor.execute(query)
                result = mycursor.fetchall()
                if result is None:
                    temp1['no'] = 0
                for x in result:
                    temp1['no'] = x['pir_no']
                    temp1['pir_no'] = x['pir_no']
                    temp1['type1'] = x['type']
                    temp1['size'] = x['size']
                    temp1['dout'] = drumOut
            except(error):
                print("Error ::", error)


        else:
            try:
                mycursor.execute(query1)
                results = mycursor.fetchall()
                if results is None:
                    temp1['no'] = 0
                for x in results:
                    temp1['no'] = x['pir_no']
                    temp1['pir_no'] = x['pir_no']
                    temp1['type1'] = x['hose_type']
                    temp1['size'] = x['hose_size']
                    temp1['dout'] = x['drum_out']

            except(error):
                print("Error ::", error)


    payload = ''
    if( temp1['no'] != 0 and temp1['no'] != 1):
        payload =  { 
            publishTag : temp1['no'],
            hoseType : temp1['type1'], 
            hoseSize : temp1['size'], 
            drumOutTag : temp1['dout'] 
            }
    else:
        payload =  { 
            publishTag : temp1['no'], 
            hoseType : 0, 
            hoseSize : 0, 
            drumOutTag : 0
            }

    payload = json.dumps(payload)
    print(payload)
    data('poly', payload)



def dataCheck1(searchBit, proHalf, valfor, machineName, searchMachine, mpir, drumIn, drumOut):
    temp1 = {}
    temp1['no'] = 0
    query = "SELECT * FROM `planningcsvmaster` WHERE pir_no = "+ searchBit
    query1 = "SELECT * FROM `pirtracking` WHERE pir_no = '"+ searchBit +"' AND machine_name like '" + searchMachine + "%' order by date_time desc limit 1"
    #os.environ['TZ'] = 'Asia/Kolkata'
    if hasattr(time, 'tzset'):
        os.environ['TZ'] = self.TIME_ZONE
        time.tzset()
    timestamp = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    if(machineName == "Linear Extruder 1"):
        try:
            mycursor.execute(query)
            results = mycursor.fetchall()
            if results is None:
                temp1['no'] = 0
            for x in results:
                temp1['no'] = x['pir_no']
                temp1['pir_no'] = x['pir_no']
                temp1['type1'] = x['type']
                temp1['size'] = x['size']
                temp1['din'] = drumIn
                temp1['dout'] = drumOut
                temp1['mpir_no'] = mpir
        except(error):
            print("Error ::", error)
    
    else:
        try:
            mycursor.execute(query1)
            results = mycursor.fetchall()
            if results is None:
                   temp1['no'] = 0
            for x in results:
                temp1['no'] = x['pir_no']
                temp1['pir_no'] = x['pir_no']
                temp1['type1'] = x['hose_type']
                temp1['size'] = x['hose_size']
                temp1['din'] = x['drum_in']
                temp1['dout'] = drumOut
                temp1['mpir_no'] = x['mpir_no']
        except(error):
            print("Error ::", error)
    
    if(machineName == "Vulcaniser 1"):
        temp1['din'] = drumIn
        
    print("temp1['no'] ::", temp1['no'])
    if(temp1['no'] != 0):
        try:
            if(valfor == "pro_start"):
                #print("Trying ", searchBit)
                sql = "SELECT * FROM `pirtracking` WHERE pir_no = '" + searchBit + "' AND machine_name like '" + machineName.split()[0] + "%' order by date_time desc limit 1"
                mycursor.execute(sql)
                if (mycursor.rowcount == 0):
                    #print("INSERTING ", mycursor.rowcount)
                    sql = "INSERT INTO pirtracking (start_date, stop_date, half_date, mpir_no, pir_no, machine_name, process_start, process_half, process_stop, hose_type, hose_size, drum_in, drum_out) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (timestamp, "", "", str(temp1['mpir_no']), str(temp1['pir_no']), machineName, proHalf, "0", "0", str(temp1['type1']), str(temp1['size']), str(temp1['din']), str(temp1['dout']))
                    mycursor.execute(sql, val)
                    print("pro start data inserted")
                    return True
            if(valfor == "pro_half"):
                sql = "UPDATE `pirtracking` SET `half_date`= %s, `mpir_no` = %s , `process_half` = %s WHERE  `pir_no` = %s AND `machine_name` = %s"
                val = (timestamp, str(temp1['mpir_no']), proHalf, str(temp1['pir_no']), machineName)
                mycursor.execute(sql, val)
                print("pro half data inserted")
                return True
            if(valfor == "pro_stop"): 
                sql = "UPDATE `pirtracking` SET `stop_date`= %s, `mpir_no` = %s, `process_stop` = %s WHERE  `pir_no` = %s AND `machine_name` = %s"
                val = (timestamp, str(temp1['mpir_no']), proHalf, str(temp1['pir_no']), machineName)
                mycursor.execute(sql, val)
                print("pro stop data inserted")
                if(valfor == "pro_stop" and "Testing " in machineName):
                    sql = "UPDATE  planningcsvmaster SET pir_status = 'Completed', close_date = %s where pir_no = %s"
                    val = (timestamp, searchBit)
                    mycursor.execute(sql, val)
                    print("pro stop data updated")
                return True
            print("Failed")
            return False
        except(error):
            print("Error ::", error)
            return False
    else:
        return False





# display loop (in main thread)
if __name__ == "__main__":
    try:
        print("Thread4:PushedClient Initialized")
        client = mqttClient.Client("MQTT3898737345")
        client.username_pw_set("", "")
        client.on_message=on_message2
        client.on_connect=on_connect2
        #client.on_log=on_log
        client.on_disconnect=on_disconnect
        client.connect('localhost', 1883) #192.168.1.102
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()
