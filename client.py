#!usr/bin/python3


from pymysql import connect
from pymysql.cursors import DictCursor


import sys
from _datetime import datetime as dt
import datetime
import paho.mqtt.client as mqttClient
import time
import json
import mysql.connector
import os
import time
from threading import Thread, Lock
from pyModbusTCP.client import ModbusClient

class globalBS():
        # set global
        tempBraid1_1 = tempBraid1_2 = tempBraid1_3 = tempBraid1_4 = tempBraid1_5 = tempBraid1_6 = tempBraid1_7 = tempBraid1_8 = tempBraid1_9 = tempBraid1_10 = tempBraid1_11 = tempBraid1_12 = tempBraid1_13 = tempBraid1_14 = tempBraid1_15 = tempBraid1_16 = tempBraid1_17 = tempBraid1_18 = tempBraid1_19 = tempBraid1_20 = tempBraid1_21 = tempBraid1_22 = tempBraid1_23 = False
        tempBraid2_1 = tempBraid2_2 = tempBraid2_3 = tempBraid2_4 = tempBraid2_5 = tempBraid2_6 = tempBraid2_7 = tempBraid2_8 = tempBraid2_9 = tempBraid2_10 = tempBraid2_11 = tempBraid2_12 = tempBraid2_13 = tempBraid2_14 = tempBraid2_15 = tempBraid2_16 = tempBraid2_17 = tempBraid2_18 = tempBraid2_19 = tempBraid2_20 = tempBraid2_21 = tempBraid2_22 = tempBraid2_23 = False 
        tempBraid3_1 = tempBraid3_2 = tempBraid3_3 = tempBraid3_4 = tempBraid3_5 = tempBraid3_6 = tempBraid3_7 = tempBraid3_8 = tempBraid3_9 = tempBraid3_10 = tempBraid3_11 = tempBraid3_12 = tempBraid3_13 = tempBraid3_14 = tempBraid3_15 = tempBraid3_16 = tempBraid3_17 = tempBraid3_18 = tempBraid3_19 = tempBraid3_20 = tempBraid3_21 = tempBraid3_22 = tempBraid3_23 = False 
        tempBraid4_1 = tempBraid4_2 = tempBraid4_3 = tempBraid4_4 = tempBraid4_5 = tempBraid4_6 = tempBraid4_7 = tempBraid4_8 = tempBraid4_9 = tempBraid4_10 = tempBraid4_11 = tempBraid4_12 = tempBraid4_13 = tempBraid4_14 = tempBraid4_15 = tempBraid4_16 = tempBraid4_17 = tempBraid4_18 = tempBraid4_19 = tempBraid4_20 = tempBraid4_21 = tempBraid4_22 = tempBraid4_23 = False 
        tempBraid5_1 = tempBraid5_2 = tempBraid5_3 = tempBraid5_4 = tempBraid5_5 = tempBraid5_6 = tempBraid5_7 = tempBraid5_8 = tempBraid5_9 = tempBraid5_10 = tempBraid5_11 = tempBraid5_12 = tempBraid5_13 = tempBraid5_14 = tempBraid5_15 = tempBraid5_16 = tempBraid5_17 = tempBraid5_18 = tempBraid5_19 = tempBraid5_20 = tempBraid5_21 = tempBraid5_22 = tempBraid5_23 = False 
        tempBraid6_1 = tempBraid6_2 = tempBraid6_3 = tempBraid6_4 = tempBraid6_5 = tempBraid6_6 = tempBraid6_7 = tempBraid6_8 = tempBraid6_9 = tempBraid6_10 = tempBraid6_11 = tempBraid6_12 = tempBraid6_13 = tempBraid6_14 = tempBraid6_15 = tempBraid6_16 = tempBraid6_17 = tempBraid6_18 = tempBraid6_19 = tempBraid6_20 = tempBraid6_21 = tempBraid6_22 = tempBraid6_23 = False 
        tempBraid7_1 = tempBraid7_2 = tempBraid7_3 = tempBraid7_4 = tempBraid7_5 = tempBraid7_6 = tempBraid7_7 = tempBraid7_8 = tempBraid7_9 = tempBraid7_10 = tempBraid7_11 = tempBraid7_12 = tempBraid7_13 = tempBraid7_14 = tempBraid7_15 = tempBraid7_16 = tempBraid7_17 = tempBraid7_18 = tempBraid7_19 = tempBraid7_20 = tempBraid7_21 = tempBraid7_22 = tempBraid7_23 = False 
        tempBraid8_1 = tempBraid8_2 = tempBraid8_3 = tempBraid8_4 = tempBraid8_5 = tempBraid8_6 = tempBraid8_7 = tempBraid8_8 = tempBraid8_9 = tempBraid8_10 = tempBraid8_11 = tempBraid8_12 = tempBraid8_13 = tempBraid8_14 = tempBraid8_15 = tempBraid8_16 = tempBraid8_17 = tempBraid8_18 = tempBraid8_19 = tempBraid8_20 = tempBraid8_21 = tempBraid8_22 = tempBraid8_23 = False 
        tempBraid9_1 = tempBraid9_2 = tempBraid9_3 = tempBraid9_4 = tempBraid9_5 = tempBraid9_6 = tempBraid9_7 = tempBraid9_8 = tempBraid9_9 = tempBraid9_10 = tempBraid9_11 = tempBraid9_12 = tempBraid9_13 = tempBraid9_14 = tempBraid9_15 = tempBraid9_16 = tempBraid9_17 = tempBraid9_18 = tempBraid9_19 = tempBraid9_20 = tempBraid9_21 = tempBraid9_22 = tempBraid9_23 = False 

        tempBraidStop1 = tempBraidStop2 = tempBraidStop3 = tempBraidStop4 = tempBraidStop5 = tempBraidStop6 = tempBraidStop7 = tempBraidStop8 = tempBraidStop9 = False
        tempBraidStopID1 = tempBraidStopID2 = tempBraidStopID3 = tempBraidStopID4 = tempBraidStopID5 = tempBraidStopID6 = tempBraidStopID7 = tempBraidStopID8 = tempBraidStopID9 = False
        tempBraidProd1 = tempBraidProd2 = tempBraidProd3 = tempBraidProd4 = tempBraidProd5 = tempBraidProd6 = tempBraidProd7 = tempBraidProd8 = tempBraidProd9 = False
        tempBraidStart1 = tempBraidStart2 = tempBraidStart3 = tempBraidStart4 = tempBraidStart5 = tempBraidStart6 = tempBraidStart7 = tempBraidStart8 = tempBraidStart9 = False
        tempBraidDT1 = tempBraidDT2 = tempBraidDT3 = tempBraidDT4 = tempBraidDT5 = tempBraidDT6 = tempBraidDT7 = tempBraidDT8 = tempBraidDT9 = ''
        tempBraidEnd1 = tempBraidEnd2 = tempBraidEnd3 = tempBraidEnd4 = tempBraidEnd5 = tempBraidEnd6 = tempBraidEnd7 = tempBraidEnd8 = tempBraidEnd9 = False
        tempBraidElapsed1 = tempBraidElapsed2 = tempBraidElapsed3 = tempBraidElapsed4 = tempBraidElapsed5 = tempBraidElapsed6 = tempBraidElapsed7 = tempBraidElapsed8 = tempBraidElapsed9 = False
        
        tempBraidSetup1 = tempBraidSetup2 = tempBraidSetup3 = tempBraidSetup4 = tempBraidSetup5 = tempBraidSetup6 = tempBraidSetup7 = tempBraidSetup8 = False
        
        tempMan1_1 = tempMan1_2 = tempMan1_3 = tempMan1_4 = tempMan1_5 = tempMan1_6 = tempMan1_7 = tempMan1_8 = tempMan1_9 = tempMan1_10 = tempMan1_11 = tempMan1_12 = tempMan1_13 = tempMan1_14 = tempMan1_15 = tempMan1_16 = tempMan1_17 = tempMan1_18 = False
        tempMan2_1 = tempMan2_2 = tempMan2_3 = tempMan2_4 = tempMan2_5 = tempMan2_6 = tempMan2_7 = tempMan2_8 = tempMan2_9 = tempMan2_10 = tempMan2_11 = tempMan2_12 = tempMan2_13 = tempMan2_14 = tempMan2_15 = tempMan2_16 = tempMan2_17 = tempMan2_18 = False 
        tempMan3_1 = tempMan3_2 = tempMan3_3 = tempMan3_4 = tempMan3_5 = tempMan3_6 = tempMan3_7 = tempMan3_8 = tempMan3_9 = tempMan3_10 = tempMan3_11 = tempMan3_12 = tempMan3_13 = tempMan3_14 = tempMan3_15 = tempMan3_16 = tempMan3_17 = tempMan3_18 = False 

        tempPlc_1 = tempPlc_2 = tempPlc_3 = tempPlc_4 = tempPlc_5 = tempPlc_6 = tempPlc_7 = tempPlc_8 = tempPlc_9 = False


        tempExt1_1 = tempExt1_2 = tempExt1_3 = tempExt1_4 = tempExt1_5 = tempExt1_6 = tempExt1_7 = tempExt1_8 = tempExt1_9 = tempExt1_10 = tempExt1_11 = tempExt1_12 = tempExt1_13 = tempExt1_14 = tempExt1_15 = tempExt1_16 = tempExt1_17 = tempExt1_18 = tempExt1_19 = tempExt1_20 = tempExt1_21 = tempExt1_22 = tempExt1_23 = tempExt1_24 = tempExt1_25 = tempExt1_26 = tempExt1_27 = tempExt1_28 = tempExt1_29 = tempExt1_30 = tempExt1_31 = tempExt1_32 =False
        tempExt2_1 = tempExt2_2 = tempExt2_3 = tempExt2_4 = tempExt2_5 = tempExt2_6 = tempExt2_7 = tempExt2_8 = tempExt2_9 = tempExt2_10 = tempExt2_11 = tempExt2_12 = tempExt2_13 = tempExt2_14 = tempExt2_15 = tempExt2_16 = tempExt2_17 = tempExt2_18 = tempExt2_19 = tempExt2_20 = tempExt2_21 = tempExt2_22 = tempExt2_23 = tempExt2_24 = tempExt2_25 = tempExt2_26 = tempExt2_27 = tempExt2_28 = tempExt2_29 = tempExt2_30 = tempExt2_31 = tempExt2_32 =False 
        tempExt3_1 = tempExt3_2 = tempExt3_3 = tempExt3_4 = tempExt3_5 = tempExt3_6 = tempExt3_7 = tempExt3_8 = tempExt3_9 = tempExt3_10 = tempExt3_11 = tempExt3_12 = tempExt3_13 = tempExt3_14 = tempExt3_15 = tempExt3_16 = tempExt3_17 = tempExt3_18 = tempExt3_19 = tempExt3_20 = tempExt3_21 = tempExt3_22 = tempExt3_23 = tempExt3_24 = tempExt3_25 = tempExt3_26 = tempExt3_27 = tempExt3_28 = tempExt3_29 = tempExt3_30 = tempExt3_31 = tempExt3_32 =False 
        tempExt4_1 = tempExt4_2 = tempExt4_3 = tempExt4_4 = tempExt4_5 = tempExt4_6 = tempExt4_7 = tempExt4_8 = tempExt4_9 = tempExt4_10 = tempExt4_11 = tempExt4_12 = tempExt4_13 = tempExt4_14 = tempExt4_15 = tempExt4_16 = tempExt4_17 = tempExt4_18 = tempExt4_19 = tempExt4_20 = tempExt4_21 = tempExt4_22 = tempExt4_23 = tempExt4_24 = tempExt4_25 = tempExt4_26 = tempExt4_27 = tempExt4_28 = tempExt4_29 = tempExt4_30 = tempExt4_31 = tempExt4_32 =False 

        tempVul1_1 = tempVul1_2 = tempVul1_3 = tempVul1_4 = tempVul1_5 = tempVul1_6 = tempVul1_7 = tempVul1_8 = tempVul1_9 = tempVul1_10 = tempVul1_11 = tempVul1_12 = tempVul1_13 = tempVul1_14 = tempVul1_15 = tempVul1_16 = tempVul1_17 = tempVul1_18 = tempVul1_19 = tempVul1_20 = tempVul1_21 = tempVul1_22 = tempVul1_23 = tempVul1_24 = tempVul1_25 = tempVul1_26 = tempVul1_27 = tempVul1_28 = tempVul1_29 = tempVul1_30 = tempVul1_31 = tempVul1_32 =False

        tempTest1_1 = tempTest1_2 = tempTest1_3 = tempTest1_4 = tempTest1_5 = tempTest1_6 = tempTest1_7 = tempTest1_8 = tempTest1_9 = tempTest1_10 = tempTest1_11 = tempTest1_12 = tempTest1_13 = tempTest1_14 = tempTest1_15 = tempTest1_16 = False
        tempTest2_1 = tempTest2_2 = tempTest2_3 = tempTest2_4 = tempTest2_5 = tempTest2_6 = tempTest2_7 = tempTest2_8 = tempTest2_9 = tempTest2_10 = tempTest2_11 = tempTest2_12 = tempTest2_13 = tempTest2_14 = tempTest2_15 = tempTest2_16 = False 
        tempTest3_1 = tempTest3_2 = tempTest3_3 = tempTest3_4 = tempTest3_5 = tempTest3_6 = tempTest3_7 = tempTest3_8 = tempTest3_9 = tempTest3_10 = tempTest3_11 = tempTest3_12 = tempTest3_13 = tempTest3_14 = tempTest3_15 = tempTest3_16 = False 

 
regs = []
dic = {}
count1 = 0
count2 = 0





'''
mydb = mysql.connector.connect(
    host="localhost",
    port ="3307",
    user="root",
    password="",
    database='pims'
)
mycursor = mydb.cursor()
'''



# create the connection
connection = connect(host='localhost', port=3306, user='root', 
                     password='', db='pims', 
                     cursorclass=DictCursor, autocommit=True)

# get the cursor
mycursor = connection.cursor()
  

onlydate = datetime.datetime.now().date()
onlytime = str(datetime.datetime.now().time()).split('.')
tim = onlytime[0]


SERVER_HOST = '192.168.1.29'
SERVER_PORT = '502'


# init a thread lock
regs_lock = Lock()


#publishing
def data(topic, q):
    client = mqttClient.Client("MQTT")
    client.username_pw_set("", "")
    client.connect('localhost', 8883)
    client.publish(topic, q)
    client.disconnect()

def fixedInt(val):
        if(val == ''):
                return '0'
        else:
                return val
                
def findFloat(val):
    return "{:.2f}".format(val)

#subscribing
def sub(topic):
    client = mqttClient.Client("MQTT")
    client.username_pw_set(username, pwd)
    client.connect(broker_add, port_no)
    client.subscribe(topic)
    client.disconnect()

def on_connect(client, userdata, flags, rc):
    client.subscribe('polyhose1/')
    print("Thread1: subscribed")

def is_valid_json(data):
        try:
                json_obj = json.loads(data)
        except ValueError as e:
                connection.ping(reconnect=True)
                if(globalBS.tempPlc_9 != True):
                        globalBS.tempPlc_9 = True
                        sql = "INSERT INTO plcstatus ( col_id, client1 ) VALUES (%s,%s)"
                        val = (17, True)
                        mycursor.execute(sql, val)
                print("Invalid data found")
                return False
        return True

#on message arrived
def on_message(client, userdata, message):
    try:
        global count1
        connection.ping(reconnect=True)
        #print("message received " ,str(message.payload.decode("utf-8")))
        #print(message.payload.decode("utf-8"))
        if message.topic == 'polyhose1/':
            count1 += 1
            json_data = str(message.payload.decode("utf-8","ignore"))
            if(is_valid_json(json_data)):
                json_obj = json.loads(json_data)
                if(findBool(json_obj['connected'])):
                        if(globalBS.tempPlc_9 != False):
                                globalBS.tempPlc_9 = False
                                sql = "INSERT INTO plcstatus ( col_id, client1 ) VALUES (%s,%s)"
                                val = (17, False)
                                mycursor.execute(sql, val)
                        dic['BraidProd1_1'] = fixedInt(json_obj['M-B_H_1-0']) #PIR
                        dic['BraidProd1_2'] = fixedInt(json_obj['M-B_R_1-1']) #operator name
                        dic['BraidProd1_3'] = fixedInt(json_obj['M-B_H_1-58']) #Actual Line Speed
                        dic['BraidProd1_4'] = not findBool(json_obj['M-B_S_1-1']) #sys Run Boolean Bit
                        dic['BraidProd1_5'] = fixedInt(json_obj['M-B_H_1-57']) #Prod Time coming from prod tag
                        dic['BraidProd1_6'] = fixedInt(json_obj['M-B_P_1-0']) #DRUM IN
                        dic['BraidProd1_7'] = fixedInt(json_obj['M-B_P_1-1']) #DRUM OUT
                        dic['BraidProd1_8'] = fixedInt(json_obj['M-B_H_1-5']) #Process Start Bit
                        dic['BraidProd1_9'] = fixedInt(json_obj['M-B_H_1-59']) #run bit
                        dic['BraidProd2_1'] = fixedInt(json_obj['M-B_H_2-0']) #PIR
                        dic['BraidProd2_2'] = fixedInt(json_obj['M-B_R_2-1']) #operator name
                        dic['BraidProd2_3'] = fixedInt(json_obj['M-B_H_2-58']) #Actual Line Speed
                        dic['BraidProd2_4'] = not findBool(json_obj['M-B_S_2-1']) #sys Run Boolean Bit
                        dic['BraidProd2_5'] = fixedInt(json_obj['M-B_H_2-57']) #Prod Time coming from prod tag
                        dic['BraidProd2_6'] = fixedInt(json_obj['M-B_P_2-0']) #DRUM IN
                        dic['BraidProd2_7'] = fixedInt(json_obj['M-B_P_2-1']) #DRUM OUT
                        dic['BraidProd2_8'] = fixedInt(json_obj['M-B_H_2-5']) #Process Start Bit
                        dic['BraidProd2_9'] = fixedInt(json_obj['M-B_H_2-59']) #run bit
                        dic['BraidProd3_1'] = fixedInt(json_obj['M-B_H_3-0']) #PIR
                        dic['BraidProd3_2'] = fixedInt(json_obj['M-B_R_3-1']) #operator name
                        dic['BraidProd3_3'] = fixedInt(json_obj['M-B_H_3-58']) #Actual Line Speed
                        dic['BraidProd3_4'] = not findBool(json_obj['M-B_S_3-1']) #sys Run Boolean Bit
                        dic['BraidProd3_5'] = fixedInt(json_obj['M-B_H_3-57']) #Prod Time coming from prod tag
                        dic['BraidProd3_6'] = fixedInt(json_obj['M-B_P_3-0']) #DRUM IN
                        dic['BraidProd3_7'] = fixedInt(json_obj['M-B_P_3-1']) #DRUM OUT
                        dic['BraidProd3_8'] = fixedInt(json_obj['M-B_H_3-5']) #Process Start Bit
                        dic['BraidProd3_9'] = fixedInt(json_obj['M-B_H_3-59']) #run bit
                        dic['BraidProd4_1'] = fixedInt(json_obj['M-B_H_4-0']) #PIR
                        dic['BraidProd4_2'] = fixedInt(json_obj['M-B_R_4-1']) #operator name
                        dic['BraidProd4_3'] = fixedInt(json_obj['M-B_H_4-58']) #Actual Line Speed
                        dic['BraidProd4_4'] = not findBool(json_obj['M-B_S_4-1']) #sys Run Boolean Bit
                        dic['BraidProd4_5'] = fixedInt(json_obj['M-B_H_4-57']) #Prod Time coming from prod tag
                        dic['BraidProd4_6'] = fixedInt(json_obj['M-B_P_4-0']) #DRUM IN
                        dic['BraidProd4_7'] = fixedInt(json_obj['M-B_P_4-1']) #DRUM OUT
                        dic['BraidProd4_8'] = fixedInt(json_obj['M-B_H_4-5']) #Process Start Bit
                        dic['BraidProd4_9'] = fixedInt(json_obj['M-B_H_4-59']) #run bit
                        dic['BraidProd5_1'] = fixedInt(json_obj['M-B_H_5-0']) #PIR
                        dic['BraidProd5_2'] = fixedInt(json_obj['M-B_R_5-1']) #operator name
                        dic['BraidProd5_3'] = fixedInt(json_obj['M-B_H_5-58']) #Actual Line Speed
                        dic['BraidProd5_4'] = not findBool(json_obj['M-B_S_5-1']) #sys Run Boolean Bit
                        dic['BraidProd5_5'] = fixedInt(json_obj['M-B_H_5-57']) #Prod Time coming from prod tag
                        dic['BraidProd5_6'] = fixedInt(json_obj['M-B_P_5-0']) #DRUM IN
                        dic['BraidProd5_7'] = fixedInt(json_obj['M-B_P_5-1']) #DRUM OUT
                        dic['BraidProd5_8'] = fixedInt(json_obj['M-B_H_5-5']) #Process Start Bit
                        dic['BraidProd5_9'] = fixedInt(json_obj['M-B_H_5-59']) #run bit
                        dic['BraidProd6_1'] = fixedInt(json_obj['M-B_H_6-0']) #PIR
                        dic['BraidProd6_2'] = fixedInt(json_obj['M-B_R_6-1']) #operator name
                        dic['BraidProd6_3'] = fixedInt(json_obj['M-B_H_6-58']) #Actual Line Speed
                        dic['BraidProd6_4'] = not findBool(json_obj['M-B_S_6-1']) #sys Run Boolean Bit
                        dic['BraidProd6_5'] = fixedInt(json_obj['M-B_H_6-57']) #Prod Time coming from prod tag
                        dic['BraidProd6_6'] = fixedInt(json_obj['M-B_P_6-0']) #DRUM IN
                        dic['BraidProd6_7'] = fixedInt(json_obj['M-B_P_6-1']) #DRUM OUT
                        dic['BraidProd6_8'] = fixedInt(json_obj['M-B_H_6-5']) #Process Start Bit
                        dic['BraidProd6_9'] = fixedInt(json_obj['M-B_H_6-59']) #run bit
                        dic['BraidProd7_1'] = fixedInt(json_obj['M-B_H_7-0']) #PIR
                        dic['BraidProd7_2'] = fixedInt(json_obj['M-B_R_7-1']) #operator name
                        dic['BraidProd7_3'] = fixedInt(json_obj['M-B_H_7-58']) #Actual Line Speed
                        dic['BraidProd7_4'] = not findBool(json_obj['M-B_S_7-1']) #sys Run Boolean Bit
                        dic['BraidProd7_5'] = fixedInt(json_obj['M-B_H_7-57']) #Prod Time coming from prod tag
                        dic['BraidProd7_6'] = fixedInt(json_obj['M-B_P_7-0']) #DRUM IN
                        dic['BraidProd7_7'] = fixedInt(json_obj['M-B_P_7-1']) #DRUM OUT
                        dic['BraidProd7_8'] = fixedInt(json_obj['M-B_H_7-5']) #Process Start Bit
                        dic['BraidProd7_9'] = fixedInt(json_obj['M-B_H_7-59']) #run bit
                        dic['BraidProd8_1'] = fixedInt(json_obj['M-B_H_8-0']) #PIR
                        dic['BraidProd8_2'] = fixedInt(json_obj['M-B_R_8-1']) #operator name
                        dic['BraidProd8_3'] = fixedInt(json_obj['M-B_H_8-58']) #Actual Line Speed
                        dic['BraidProd8_4'] = not findBool(json_obj['M-B_S_8-1']) #sys Run Boolean Bit
                        dic['BraidProd8_5'] = fixedInt(json_obj['M-B_H_8-57']) #Prod Time coming from prod tag
                        dic['BraidProd8_6'] = fixedInt(json_obj['M-B_P_8-0']) #DRUM IN
                        dic['BraidProd8_7'] = fixedInt(json_obj['M-B_P_8-1']) #DRUM OUT
                        dic['BraidProd8_8'] = fixedInt(json_obj['M-B_H_8-5']) #Process Start Bit
                        dic['BraidProd8_9'] = fixedInt(json_obj['M-B_H_8-59']) #run bit

                        dic['Braid1_1'] = fixedInt(json_obj['M-B_R_1-0']) #PIR
                        dic['Braid1_2'] = fixedInt(json_obj['M-B_R_1-1']) #operator name

                        dic['Braid2_1'] = fixedInt(json_obj['M-B_R_2-0']) #PIR
                        dic['Braid2_2'] = fixedInt(json_obj['M-B_R_2-1']) #operator name

                        dic['Braid3_1'] = fixedInt(json_obj['M-B_R_3-0']) #PIR
                        dic['Braid3_2'] = fixedInt(json_obj['M-B_R_3-1']) #operator name
                            

                        dic['Braid4_1'] = fixedInt(json_obj['M-B_R_4-0']) #PIR
                        dic['Braid4_2'] = fixedInt(json_obj['M-B_R_4-1']) #operator name
                            

                        dic['Braid5_1'] = fixedInt(json_obj['M-B_R_5-0']) #PIR
                        dic['Braid5_2'] = fixedInt(json_obj['M-B_R_5-1']) #operator name
                           

                        dic['Braid6_1'] = fixedInt(json_obj['M-B_R_6-0']) #PIR
                        dic['Braid6_2'] = fixedInt(json_obj['M-B_R_6-1']) #operator name
                            

                        dic['Braid7_1'] = fixedInt(json_obj['M-B_R_7-0']) #PIR
                        dic['Braid7_2'] = fixedInt(json_obj['M-B_R_7-1']) #operator name
                            
                        dic['Braid8_1'] = fixedInt(json_obj['M-B_R_8-0']) #PIR
                        dic['Braid8_2'] = fixedInt(json_obj['M-B_R_8-1']) #operator name


                        dic['Plc_1'] = fixedInt(json_obj['M-B_A_1-23']) #Braider 1
                        dic['Plc_2'] = fixedInt(json_obj['M-B_A_2-23']) #Braider 2
                        dic['Plc_3'] = fixedInt(json_obj['M-B_A_3-23']) #Braider 3
                        dic['Plc_4'] = fixedInt(json_obj['M-B_A_4-23']) #Braider 4
                        dic['Plc_5'] = fixedInt(json_obj['M-B_A_5-23']) #Braider 5
                        dic['Plc_6'] = fixedInt(json_obj['M-B_A_6-23']) #Braider 6
                        dic['Plc_7'] = fixedInt(json_obj['M-B_A_7-23']) #Braider 7
                        dic['Plc_8'] = fixedInt(json_obj['M-B_A_8-23']) #Braider 8







                        dic['Alarm1_1'] = fixedInt(json_obj['M-B_A_1-0']) #MACHINE EMERGENCY PRESSED
                        dic['Alarm1_2'] = fixedInt(json_obj['M-B_A_1-1']) #DOOR NOT CLOSED
                        dic['Alarm1_3'] = fixedInt(json_obj['M-B_A_1-2']) #CLOSE FRONT RIGHT DOOR AND PRESS RESET
                        dic['Alarm1_4'] = fixedInt(json_obj['M-B_A_1-3']) #CLOSE FRONT LEFT DOOR AND PRESS RESET
                        dic['Alarm1_5'] = fixedInt(json_obj['M-B_A_1-4']) #CLOSE BACK RIGHT DOOR AND PRESS RESET
                        dic['Alarm1_6'] = fixedInt(json_obj['M-B_A_1-5']) #CLOSE BACK LEFT DOOR AND PRESS RESET
                        dic['Alarm1_7'] = fixedInt(json_obj['M-B_A_1-6']) #BOBBIN EMPTY D1 INNER ACTIVATED
                        dic['Alarm1_8'] = fixedInt(json_obj['M-B_A_1-7']) #BOBBIN EMPTY D1 OUTER ACTIVATED
                        dic['Alarm1_9'] = fixedInt(json_obj['M-B_A_1-8']) #BOBBIN EMPTY D2 INNER ACTIVATED
                        dic['Alarm1_10'] = fixedInt(json_obj['M-B_A_1-9']) #BOBBIN EMPTY D2 OUTER ACTIVATED
                        dic['Alarm1_11'] = fixedInt(json_obj['M-B_A_1-10']) #WIRE BREAK D1 BACK ACTIVATED
                        dic['Alarm1_12'] = fixedInt(json_obj['M-B_A_1-11']) #WIRE BREAK D1 FRONT ACTIVATED
                        dic['Alarm1_13'] = fixedInt(json_obj['M-B_A_1-12']) #WIRE BREAK D2 BACK ACTIVATED
                        dic['Alarm1_14'] = fixedInt(json_obj['M-B_A_1-13']) #WIRE BREAK D2 OUTER ACTIVATED
                        dic['Alarm1_15'] = fixedInt(json_obj['M-B_A_1-14']) #OIL LEVEL D2 SENSOR ACTIVATED
                        dic['Alarm1_16'] = fixedInt(json_obj['M-B_A_1-15']) #MPCB TRIP ACTIVATED
                        dic['Alarm1_17'] = fixedInt(json_obj['M-B_A_1-16']) #RUNNING PLY SENSOR ACTIVATED
                        dic['Alarm1_18'] = fixedInt(json_obj['M-B_A_1-17']) #OIL LEVEL D1 SENSOR ACTIVATED
                        dic['Alarm1_19'] = fixedInt(json_obj['M-B_A_1-18']) #TAKE UP EMERGENGY ACTIVATED
                        dic['Alarm1_20'] = fixedInt(json_obj['M-B_A_1-19']) #WIRE BREAK D1 TOP ACTIVATED
                        dic['Alarm1_21'] = fixedInt(json_obj['M-B_A_1-20']) #WIRE BREAK D2 TOP ACTIVATED
                        dic['Alarm1_22'] = fixedInt(json_obj['M-B_A_1-21']) #METAL SENSOR DETECHED PUT RED TAPE
                        dic['Alarm1_23'] = fixedInt(json_obj['M-B_A_1-22']) #ALUMINIUM SENSOR DETECHED PUT RED TAPE

                        dic['Alarm2_1'] = fixedInt(json_obj['M-B_A_2-0']) #MACHINE EMERGENCY PRESSED
                        dic['Alarm2_2'] = fixedInt(json_obj['M-B_A_2-1']) #DOOR NOT CLOSED
                        dic['Alarm2_3'] = fixedInt(json_obj['M-B_A_2-2']) #CLOSE FRONT RIGHT DOOR AND PRESS RESET
                        dic['Alarm2_4'] = fixedInt(json_obj['M-B_A_2-3']) #CLOSE FRONT LEFT DOOR AND PRESS RESET
                        dic['Alarm2_5'] = fixedInt(json_obj['M-B_A_2-4']) #CLOSE BACK RIGHT DOOR AND PRESS RESET
                        dic['Alarm2_6'] = fixedInt(json_obj['M-B_A_2-5']) #CLOSE BACK LEFT DOOR AND PRESS RESET
                        dic['Alarm2_7'] = fixedInt(json_obj['M-B_A_2-6']) #BOBBIN EMPTY D1 INNER ACTIVATED
                        dic['Alarm2_8'] = fixedInt(json_obj['M-B_A_2-7']) #BOBBIN EMPTY D1 OUTER ACTIVATED
                        dic['Alarm2_9'] = fixedInt(json_obj['M-B_A_2-8']) #BOBBIN EMPTY D2 INNER ACTIVATED
                        dic['Alarm2_10'] = fixedInt(json_obj['M-B_A_2-9'] )#BOBBIN EMPTY D2 OUTER ACTIVATED
                        dic['Alarm2_11'] = fixedInt(json_obj['M-B_A_2-10']) #WIRE BREAK D1 BACK ACTIVATED
                        dic['Alarm2_12'] = fixedInt(json_obj['M-B_A_2-11']) #WIRE BREAK D1 FRONT ACTIVATED
                        dic['Alarm2_13'] = fixedInt(json_obj['M-B_A_2-12']) #WIRE BREAK D2 BACK ACTIVATED
                        dic['Alarm2_14'] = fixedInt(json_obj['M-B_A_2-13']) #WIRE BREAK D2 OUTER ACTIVATED
                        dic['Alarm2_15'] = fixedInt(json_obj['M-B_A_2-14']) #OIL LEVEL D2 SENSOR ACTIVATED
                        dic['Alarm2_16'] = fixedInt(json_obj['M-B_A_2-15']) #MPCB TRIP ACTIVATED
                        dic['Alarm2_17'] = fixedInt(json_obj['M-B_A_2-16']) #RUNNING PLY SENSOR ACTIVATED
                        dic['Alarm2_18'] = fixedInt(json_obj['M-B_A_2-17']) #OIL LEVEL D1 SENSOR ACTIVATED
                        dic['Alarm2_19'] = fixedInt(json_obj['M-B_A_2-18']) #TAKE UP EMERGENGY ACTIVATED
                        dic['Alarm2_20'] = fixedInt(json_obj['M-B_A_2-19']) #WIRE BREAK D1 TOP ACTIVATED
                        dic['Alarm2_21'] = fixedInt(json_obj['M-B_A_2-20']) #WIRE BREAK D2 TOP ACTIVATED
                        dic['Alarm2_22'] = fixedInt(json_obj['M-B_A_2-21']) #METAL SENSOR DETECHED PUT RED TAPE
                        dic['Alarm2_23'] = fixedInt(json_obj['M-B_A_2-22']) #ALUMINIUM SENSOR DETECHED PUT RED TAPE

                        dic['Alarm3_1'] = fixedInt(json_obj['M-B_A_3-0']) #MACHINE EMERGENCY PRESSED
                        dic['Alarm3_2'] = fixedInt(json_obj['M-B_A_3-1']) #DOOR NOT CLOSED
                        dic['Alarm3_3'] = fixedInt(json_obj['M-B_A_3-2']) #CLOSE FRONT RIGHT DOOR AND PRESS RESET
                        dic['Alarm3_4'] = fixedInt(json_obj['M-B_A_3-3']) #CLOSE FRONT LEFT DOOR AND PRESS RESET
                        dic['Alarm3_5'] = fixedInt(json_obj['M-B_A_3-4']) #CLOSE BACK RIGHT DOOR AND PRESS RESET
                        dic['Alarm3_6'] = fixedInt(json_obj['M-B_A_3-5']) #CLOSE BACK LEFT DOOR AND PRESS RESET
                        dic['Alarm3_7'] = fixedInt(json_obj['M-B_A_3-6']) #BOBBIN EMPTY D1 INNER ACTIVATED
                        dic['Alarm3_8'] = fixedInt(json_obj['M-B_A_3-7']) #BOBBIN EMPTY D1 OUTER ACTIVATED
                        dic['Alarm3_9'] = fixedInt(json_obj['M-B_A_3-8']) #BOBBIN EMPTY D2 INNER ACTIVATED
                        dic['Alarm3_10'] = fixedInt(json_obj['M-B_A_3-9'] )#BOBBIN EMPTY D2 OUTER ACTIVATED
                        dic['Alarm3_11'] = fixedInt(json_obj['M-B_A_3-10']) #WIRE BREAK D1 BACK ACTIVATED
                        dic['Alarm3_12'] = fixedInt(json_obj['M-B_A_3-11']) #WIRE BREAK D1 FRONT ACTIVATED
                        dic['Alarm3_13'] = fixedInt(json_obj['M-B_A_3-12']) #WIRE BREAK D2 BACK ACTIVATED
                        dic['Alarm3_14'] = fixedInt(json_obj['M-B_A_3-13']) #WIRE BREAK D2 OUTER ACTIVATED
                        dic['Alarm3_15'] = fixedInt(json_obj['M-B_A_3-14']) #OIL LEVEL D2 SENSOR ACTIVATED
                        dic['Alarm3_16'] = fixedInt(json_obj['M-B_A_3-15']) #MPCB TRIP ACTIVATED
                        dic['Alarm3_17'] = fixedInt(json_obj['M-B_A_3-16']) #RUNNING PLY SENSOR ACTIVATED
                        dic['Alarm3_18'] = fixedInt(json_obj['M-B_A_3-17']) #OIL LEVEL D1 SENSOR ACTIVATED
                        dic['Alarm3_19'] = fixedInt(json_obj['M-B_A_3-18']) #TAKE UP EMERGENGY ACTIVATED
                        dic['Alarm3_20'] = fixedInt(json_obj['M-B_A_3-19']) #WIRE BREAK D1 TOP ACTIVATED
                        dic['Alarm3_21'] = fixedInt(json_obj['M-B_A_3-20']) #WIRE BREAK D2 TOP ACTIVATED
                        dic['Alarm3_22'] = fixedInt(json_obj['M-B_A_3-21']) #METAL SENSOR DETECHED PUT RED TAPE
                        dic['Alarm3_23'] = fixedInt(json_obj['M-B_A_3-22']) #ALUMINIUM SENSOR DETECHED PUT RED TAPE

                        dic['Alarm4_1'] = fixedInt(json_obj['M-B_A_4-0']) #MACHINE EMERGENCY PRESSED
                        dic['Alarm4_2'] = fixedInt(json_obj['M-B_A_4-1']) #DOOR NOT CLOSED
                        dic['Alarm4_3'] = fixedInt(json_obj['M-B_A_4-2']) #CLOSE FRONT RIGHT DOOR AND PRESS RESET
                        dic['Alarm4_4'] = fixedInt(json_obj['M-B_A_4-3']) #CLOSE FRONT LEFT DOOR AND PRESS RESET
                        dic['Alarm4_5'] = fixedInt(json_obj['M-B_A_4-4']) #CLOSE BACK RIGHT DOOR AND PRESS RESET
                        dic['Alarm4_6'] = fixedInt(json_obj['M-B_A_4-5']) #CLOSE BACK LEFT DOOR AND PRESS RESET
                        dic['Alarm4_7'] = fixedInt(json_obj['M-B_A_4-6']) #BOBBIN EMPTY D1 INNER ACTIVATED
                        dic['Alarm4_8'] = fixedInt(json_obj['M-B_A_4-7']) #BOBBIN EMPTY D1 OUTER ACTIVATED
                        dic['Alarm4_9'] = fixedInt(json_obj['M-B_A_4-8']) #BOBBIN EMPTY D2 INNER ACTIVATED
                        dic['Alarm4_10'] = fixedInt(json_obj['M-B_A_4-9']) #BOBBIN EMPTY D2 OUTER ACTIVATED
                        dic['Alarm4_11'] = fixedInt(json_obj['M-B_A_4-10']) #WIRE BREAK D1 BACK ACTIVATED
                        dic['Alarm4_12'] = fixedInt(json_obj['M-B_A_4-11']) #WIRE BREAK D1 FRONT ACTIVATED
                        dic['Alarm4_13'] = fixedInt(json_obj['M-B_A_4-12']) #WIRE BREAK D2 BACK ACTIVATED
                        dic['Alarm4_14'] = fixedInt(json_obj['M-B_A_4-13']) #WIRE BREAK D2 OUTER ACTIVATED
                        dic['Alarm4_15'] = fixedInt(json_obj['M-B_A_4-14']) #OIL LEVEL D2 SENSOR ACTIVATED
                        dic['Alarm4_16'] = fixedInt(json_obj['M-B_A_4-15']) #MPCB TRIP ACTIVATED
                        dic['Alarm4_17'] = fixedInt(json_obj['M-B_A_4-16']) #RUNNING PLY SENSOR ACTIVATED
                        dic['Alarm4_18'] = fixedInt(json_obj['M-B_A_4-17']) #OIL LEVEL D1 SENSOR ACTIVATED
                        dic['Alarm4_19'] = fixedInt(json_obj['M-B_A_4-18']) #TAKE UP EMERGENGY ACTIVATED
                        dic['Alarm4_20'] = fixedInt(json_obj['M-B_A_4-19']) #WIRE BREAK D1 TOP ACTIVATED
                        dic['Alarm4_21'] = fixedInt(json_obj['M-B_A_4-20']) #WIRE BREAK D2 TOP ACTIVATED
                        dic['Alarm4_22'] = fixedInt(json_obj['M-B_A_4-21']) #METAL SENSOR DETECHED PUT RED TAPE
                        dic['Alarm4_23'] = fixedInt(json_obj['M-B_A_4-22']) #ALUMINIUM SENSOR DETECHED PUT RED TAPE

                        dic['Alarm5_1'] = fixedInt(json_obj['M-B_A_5-0']) #MACHINE EMERGENCY PRESSED
                        dic['Alarm5_2'] = fixedInt(json_obj['M-B_A_5-1']) #DOOR NOT CLOSED
                        dic['Alarm5_3'] = fixedInt(json_obj['M-B_A_5-2']) #CLOSE FRONT RIGHT DOOR AND PRESS RESET
                        dic['Alarm5_4'] = fixedInt(json_obj['M-B_A_5-3']) #CLOSE FRONT LEFT DOOR AND PRESS RESET
                        dic['Alarm5_5'] = fixedInt(json_obj['M-B_A_5-4']) #CLOSE BACK RIGHT DOOR AND PRESS RESET
                        dic['Alarm5_6'] = fixedInt(json_obj['M-B_A_5-5']) #CLOSE BACK LEFT DOOR AND PRESS RESET
                        dic['Alarm5_7'] = fixedInt(json_obj['M-B_A_5-6']) #BOBBIN EMPTY D1 INNER ACTIVATED
                        dic['Alarm5_8'] = fixedInt(json_obj['M-B_A_5-7']) #BOBBIN EMPTY D1 OUTER ACTIVATED
                        dic['Alarm5_9'] = fixedInt(json_obj['M-B_A_5-8']) #BOBBIN EMPTY D2 INNER ACTIVATED
                        dic['Alarm5_10'] = fixedInt(json_obj['M-B_A_5-9']) #BOBBIN EMPTY D2 OUTER ACTIVATED
                        dic['Alarm5_11'] = fixedInt(json_obj['M-B_A_5-10']) #WIRE BREAK D1 BACK ACTIVATED
                        dic['Alarm5_12'] = fixedInt(json_obj['M-B_A_5-11']) #WIRE BREAK D1 FRONT ACTIVATED
                        dic['Alarm5_13'] = fixedInt(json_obj['M-B_A_5-12']) #WIRE BREAK D2 BACK ACTIVATED
                        dic['Alarm5_14'] = fixedInt(json_obj['M-B_A_5-13']) #WIRE BREAK D2 OUTER ACTIVATED
                        dic['Alarm5_15'] = fixedInt(json_obj['M-B_A_5-14']) #OIL LEVEL D2 SENSOR ACTIVATED
                        dic['Alarm5_16'] = fixedInt(json_obj['M-B_A_5-15']) #MPCB TRIP ACTIVATED
                        dic['Alarm5_17'] = fixedInt(json_obj['M-B_A_5-16']) #RUNNING PLY SENSOR ACTIVATED
                        dic['Alarm5_18'] = fixedInt(json_obj['M-B_A_5-17']) #OIL LEVEL D1 SENSOR ACTIVATED
                        dic['Alarm5_19'] = fixedInt(json_obj['M-B_A_5-18']) #TAKE UP EMERGENGY ACTIVATED
                        dic['Alarm5_20'] = fixedInt(json_obj['M-B_A_5-19']) #WIRE BREAK D1 TOP ACTIVATED
                        dic['Alarm5_21'] = fixedInt(json_obj['M-B_A_5-20']) #WIRE BREAK D2 TOP ACTIVATED
                        dic['Alarm5_22'] = fixedInt(json_obj['M-B_A_5-21']) #METAL SENSOR DETECHED PUT RED TAPE
                        dic['Alarm5_23'] = fixedInt(json_obj['M-B_A_5-22']) #ALUMINIUM SENSOR DETECHED PUT RED TAPE

                        dic['Alarm6_1'] = fixedInt(json_obj['M-B_A_6-0']) #MACHINE EMERGENCY PRESSED
                        dic['Alarm6_2'] = fixedInt(json_obj['M-B_A_6-1']) #DOOR NOT CLOSED
                        dic['Alarm6_3'] = fixedInt(json_obj['M-B_A_6-2']) #CLOSE FRONT RIGHT DOOR AND PRESS RESET
                        dic['Alarm6_4'] = fixedInt(json_obj['M-B_A_6-3']) #CLOSE FRONT LEFT DOOR AND PRESS RESET
                        dic['Alarm6_5'] = fixedInt(json_obj['M-B_A_6-4']) #CLOSE BACK RIGHT DOOR AND PRESS RESET
                        dic['Alarm6_6'] = fixedInt(json_obj['M-B_A_6-5']) #CLOSE BACK LEFT DOOR AND PRESS RESET
                        dic['Alarm6_7'] = fixedInt(json_obj['M-B_A_6-6']) #BOBBIN EMPTY D1 INNER ACTIVATED
                        dic['Alarm6_8'] = fixedInt(json_obj['M-B_A_6-7']) #BOBBIN EMPTY D1 OUTER ACTIVATED
                        dic['Alarm6_9'] = fixedInt(json_obj['M-B_A_6-8']) #BOBBIN EMPTY D2 INNER ACTIVATED
                        dic['Alarm6_10'] = fixedInt(json_obj['M-B_A_6-9']) #BOBBIN EMPTY D2 OUTER ACTIVATED
                        dic['Alarm6_11'] = fixedInt(json_obj['M-B_A_6-10']) #WIRE BREAK D1 BACK ACTIVATED
                        dic['Alarm6_12'] = fixedInt(json_obj['M-B_A_6-11']) #WIRE BREAK D1 FRONT ACTIVATED
                        dic['Alarm6_13'] = fixedInt(json_obj['M-B_A_6-12']) #WIRE BREAK D2 BACK ACTIVATED
                        dic['Alarm6_14'] = fixedInt(json_obj['M-B_A_6-13']) #WIRE BREAK D2 OUTER ACTIVATED
                        dic['Alarm6_15'] = fixedInt(json_obj['M-B_A_6-14']) #OIL LEVEL D2 SENSOR ACTIVATED
                        dic['Alarm6_16'] = fixedInt(json_obj['M-B_A_6-15']) #MPCB TRIP ACTIVATED
                        dic['Alarm6_17'] = fixedInt(json_obj['M-B_A_6-16']) #RUNNING PLY SENSOR ACTIVATED
                        dic['Alarm6_18'] = fixedInt(json_obj['M-B_A_6-17']) #OIL LEVEL D1 SENSOR ACTIVATED
                        dic['Alarm6_19'] = fixedInt(json_obj['M-B_A_6-18']) #TAKE UP EMERGENGY ACTIVATED
                        dic['Alarm6_20'] = fixedInt(json_obj['M-B_A_6-19']) #WIRE BREAK D1 TOP ACTIVATED
                        dic['Alarm6_21'] = fixedInt(json_obj['M-B_A_6-20']) #WIRE BREAK D2 TOP ACTIVATED
                        dic['Alarm6_22'] = fixedInt(json_obj['M-B_A_6-21']) #METAL SENSOR DETECHED PUT RED TAPE
                        dic['Alarm6_23'] = fixedInt(json_obj['M-B_A_6-22']) #ALUMINIUM SENSOR DETECHED PUT RED TAPE

                        dic['Alarm7_1'] = fixedInt(json_obj['M-B_A_7-0']) #MACHINE EMERGENCY PRESSED
                        dic['Alarm7_2'] = fixedInt(json_obj['M-B_A_7-1']) #DOOR NOT CLOSED
                        dic['Alarm7_3'] = fixedInt(json_obj['M-B_A_7-2']) #CLOSE FRONT RIGHT DOOR AND PRESS RESET
                        dic['Alarm7_4'] = fixedInt(json_obj['M-B_A_7-3']) #CLOSE FRONT LEFT DOOR AND PRESS RESET
                        dic['Alarm7_5'] = fixedInt(json_obj['M-B_A_7-4']) #CLOSE BACK RIGHT DOOR AND PRESS RESET
                        dic['Alarm7_6'] = fixedInt(json_obj['M-B_A_7-5']) #CLOSE BACK LEFT DOOR AND PRESS RESET
                        dic['Alarm7_7'] = fixedInt(json_obj['M-B_A_7-6']) #BOBBIN EMPTY D1 INNER ACTIVATED
                        dic['Alarm7_8'] = fixedInt(json_obj['M-B_A_7-7']) #BOBBIN EMPTY D1 OUTER ACTIVATED
                        dic['Alarm7_9'] = fixedInt(json_obj['M-B_A_7-8']) #BOBBIN EMPTY D2 INNER ACTIVATED
                        dic['Alarm7_10'] = fixedInt(json_obj['M-B_A_7-9']) #BOBBIN EMPTY D2 OUTER ACTIVATED
                        dic['Alarm7_11'] = fixedInt(json_obj['M-B_A_7-10']) #WIRE BREAK D1 BACK ACTIVATED
                        dic['Alarm7_12'] = fixedInt(json_obj['M-B_A_7-11']) #WIRE BREAK D1 FRONT ACTIVATED
                        dic['Alarm7_13'] = fixedInt(json_obj['M-B_A_7-12']) #WIRE BREAK D2 BACK ACTIVATED
                        dic['Alarm7_14'] = fixedInt(json_obj['M-B_A_7-13']) #WIRE BREAK D2 OUTER ACTIVATED
                        dic['Alarm7_15'] = fixedInt(json_obj['M-B_A_7-14']) #OIL LEVEL D2 SENSOR ACTIVATED
                        dic['Alarm7_16'] = fixedInt(json_obj['M-B_A_7-15']) #MPCB TRIP ACTIVATED
                        dic['Alarm7_17'] = fixedInt(json_obj['M-B_A_7-16']) #RUNNING PLY SENSOR ACTIVATED
                        dic['Alarm7_18'] = fixedInt(json_obj['M-B_A_7-17']) #OIL LEVEL D1 SENSOR ACTIVATED
                        dic['Alarm7_19'] = fixedInt(json_obj['M-B_A_7-18']) #TAKE UP EMERGENGY ACTIVATED
                        dic['Alarm7_20'] = fixedInt(json_obj['M-B_A_7-19']) #WIRE BREAK D1 TOP ACTIVATED
                        dic['Alarm7_21'] = fixedInt(json_obj['M-B_A_7-20']) #WIRE BREAK D2 TOP ACTIVATED
                        dic['Alarm7_22'] = fixedInt(json_obj['M-B_A_7-21']) #METAL SENSOR DETECHED PUT RED TAPE
                        dic['Alarm7_23'] = fixedInt(json_obj['M-B_A_7-22']) #ALUMINIUM SENSOR DETECHED PUT RED TAPE

                        dic['Alarm8_1'] = fixedInt(json_obj['M-B_A_8-0']) #MACHINE EMERGENCY PRESSED
                        dic['Alarm8_2'] = fixedInt(json_obj['M-B_A_8-1']) #DOOR NOT CLOSED
                        dic['Alarm8_3'] = fixedInt(json_obj['M-B_A_8-2']) #CLOSE FRONT RIGHT DOOR AND PRESS RESET
                        dic['Alarm8_4'] = fixedInt(json_obj['M-B_A_8-3']) #CLOSE FRONT LEFT DOOR AND PRESS RESET
                        dic['Alarm8_5'] = fixedInt(json_obj['M-B_A_8-4']) #CLOSE BACK RIGHT DOOR AND PRESS RESET
                        dic['Alarm8_6'] = fixedInt(json_obj['M-B_A_8-5']) #CLOSE BACK LEFT DOOR AND PRESS RESET
                        dic['Alarm8_7'] = fixedInt(json_obj['M-B_A_8-6']) #BOBBIN EMPTY D1 INNER ACTIVATED
                        dic['Alarm8_8'] = fixedInt(json_obj['M-B_A_8-7']) #BOBBIN EMPTY D1 OUTER ACTIVATED
                        dic['Alarm8_9'] = fixedInt(json_obj['M-B_A_8-8']) #BOBBIN EMPTY D2 INNER ACTIVATED
                        dic['Alarm8_10'] = fixedInt(json_obj['M-B_A_8-9']) #BOBBIN EMPTY D2 OUTER ACTIVATED
                        dic['Alarm8_11'] = fixedInt(json_obj['M-B_A_8-10']) #WIRE BREAK D1 BACK ACTIVATED
                        dic['Alarm8_12'] = fixedInt(json_obj['M-B_A_8-11']) #WIRE BREAK D1 FRONT ACTIVATED
                        dic['Alarm8_13'] = fixedInt(json_obj['M-B_A_8-12']) #WIRE BREAK D2 BACK ACTIVATED
                        dic['Alarm8_14'] = fixedInt(json_obj['M-B_A_8-13']) #WIRE BREAK D2 OUTER ACTIVATED
                        dic['Alarm8_15'] = fixedInt(json_obj['M-B_A_8-14']) #OIL LEVEL D2 SENSOR ACTIVATED
                        dic['Alarm8_16'] = fixedInt(json_obj['M-B_A_8-15']) #MPCB TRIP ACTIVATED
                        dic['Alarm8_17'] = fixedInt(json_obj['M-B_A_8-16']) #RUNNING PLY SENSOR ACTIVATED
                        dic['Alarm8_18'] = fixedInt(json_obj['M-B_A_8-17']) #OIL LEVEL D1 SENSOR ACTIVATED
                        dic['Alarm8_19'] = fixedInt(json_obj['M-B_A_8-18']) #TAKE UP EMERGENGY ACTIVATED
                        dic['Alarm8_20'] = fixedInt(json_obj['M-B_A_8-19']) #WIRE BREAK D1 TOP ACTIVATED
                        dic['Alarm8_21'] = fixedInt(json_obj['M-B_A_8-20']) #WIRE BREAK D2 TOP ACTIVATED
                        dic['Alarm8_22'] = fixedInt(json_obj['M-B_A_8-21']) #METAL SENSOR DETECHED PUT RED TAPE
                        dic['Alarm8_23'] = fixedInt(json_obj['M-B_A_8-22']) #ALUMINIUM SENSOR DETECHED PUT RED TAPE
                            
                        dic['BraidStop1_1'] = fixedInt(json_obj['M-B_S_1-0']) #Int value containing 1-20 value's
                        dic['BraidStop1_2'] = json_obj['M-B_S_1-1'] #Boolean value containing on off status
                        dic['BraidStopMessage1'] = ""
                        dic['BraidStop2_1'] = fixedInt(json_obj['M-B_S_2-0']) #Int value containing 1-20 value's
                        dic['BraidStop2_2'] = json_obj['M-B_S_2-1'] #Boolean value containing on off status
                        dic['BraidStopMessage2'] = ""
                        dic['BraidStop3_1'] = fixedInt(json_obj['M-B_S_3-0']) #Int value containing 1-20 value's
                        dic['BraidStop3_2'] = json_obj['M-B_S_3-1'] #Boolean value containing on off status
                        dic['BraidStopMessage3'] = ""
                        dic['BraidStop4_1'] = fixedInt(json_obj['M-B_S_4-0']) #Int value containing 1-20 value's
                        dic['BraidStop4_2'] = json_obj['M-B_S_4-1'] #Boolean value containing on off status
                        dic['BraidStopMessage4'] = ""
                        dic['BraidStop5_1'] = fixedInt(json_obj['M-B_S_5-0']) #Int value containing 1-20 value's
                        dic['BraidStop5_2'] = json_obj['M-B_S_5-1'] #Boolean value containing on off status
                        dic['BraidStopMessage5'] = ""
                        dic['BraidStop6_1'] = fixedInt(json_obj['M-B_S_6-0']) #Int value containing 1-20 value's
                        dic['BraidStop6_2'] = json_obj['M-B_S_6-1'] #Boolean value containing on off status
                        dic['BraidStopMessage6'] = ""
                        dic['BraidStop7_1'] = fixedInt(json_obj['M-B_S_7-0']) #Int value containing 1-20 value's
                        dic['BraidStop7_2'] = json_obj['M-B_S_7-1'] #Boolean value containing on off status
                        dic['BraidStopMessage7'] = ""
                        dic['BraidStop8_1'] = fixedInt(json_obj['M-B_S_8-0']) #Int value containing 1-20 value's
                        dic['BraidStop8_2'] = json_obj['M-B_S_8-1'] #Boolean value containing on off status
                        dic['BraidStopMessage8'] = ""
                        
                        if(globalBS.tempBraidProd1 != findBool(dic['BraidProd1_8'])):
                                globalBS.tempBraidProd1 = findBool(dic['BraidProd1_8'])
                                if(findBool(dic['BraidProd1_8']) == True):
                                        globalBS.tempBraidStart1 = time.time()
                                        globalBS.tempBraidDT1 = datetime.datetime.now()
                                        #if(findBool(dic['BraidProd1_8']) == True):
                                        #globalBS.tempBraidDown1 = 1
                                if(findBool(dic['BraidProd1_8']) == False):
                                        globalBS.tempBraidEnd1 = time.time()
                                        globalBS.tempBraidElapsed1 = (globalBS.tempBraidEnd1 - globalBS.tempBraidStart1) / 60
                                        sql = "INSERT INTO braidproduction1 ( pir, operator_name, ontime, actual_line_speed, prod_time, drum_in, drum_out ) VALUES (%s, %s, %s,%s,%s,%s,%s)"
                                        val = (str(dic['BraidProd1_1']), str(dic['BraidProd1_2']), globalBS.tempBraidDT1, findFloat(float(dic['BraidProd1_3'])),  int(globalBS.tempBraidElapsed1) , str(dic['BraidProd1_6']), str(dic['BraidProd1_7']))
                                        mycursor.execute(sql, val)
                                        
        
                        if(globalBS.tempBraidProd2 != findBool(dic['BraidProd2_8'])):
                                globalBS.tempBraidProd2 = findBool(dic['BraidProd2_8'])
                                if(findBool(dic['BraidProd2_8']) == True):
                                        globalBS.tempBraidStart2 = time.time()
                                        globalBS.tempBraidDT2 = datetime.datetime.now()
                                if(findBool(dic['BraidProd2_8']) == False):
                                        globalBS.tempBraidEnd2 = time.time()
                                        globalBS.tempBraidElapsed2 = (globalBS.tempBraidEnd2 - globalBS.tempBraidStart2) / 60
                                        sql = "INSERT INTO braidproduction2 ( pir, operator_name, ontime, actual_line_speed, prod_time, drum_in, drum_out ) VALUES (%s, %s, %s,%s,%s,%s,%s)"
                                        val = (str(dic['BraidProd2_1']), str(dic['BraidProd2_2']), globalBS.tempBraidDT2, findFloat(float(dic['BraidProd2_3'])),  int(globalBS.tempBraidElapsed2) , str(dic['BraidProd2_6']), str(dic['BraidProd2_7']))
                                        mycursor.execute(sql, val)
                                        
                        
                        if(globalBS.tempBraidProd3 != findBool(dic['BraidProd3_8'])):
                                globalBS.tempBraidProd3 = findBool(dic['BraidProd3_8'])
                                if(findBool(dic['BraidProd3_8']) == True):
                                        globalBS.tempBraidStart3 = time.time()
                                        globalBS.tempBraidDT3 = datetime.datetime.now()
                                if(findBool(dic['BraidProd3_8']) == False):
                                        globalBS.tempBraidEnd3 = time.time()
                                        globalBS.tempBraidElapsed3 = (globalBS.tempBraidEnd3 - globalBS.tempBraidStart3) / 60
                                        sql = "INSERT INTO braidproduction3 ( pir, operator_name, ontime, actual_line_speed, prod_time, drum_in, drum_out ) VALUES (%s, %s, %s,%s,%s,%s,%s)"
                                        val = (str(dic['BraidProd3_1']), str(dic['BraidProd3_2']), globalBS.tempBraidDT3, findFloat(float(dic['BraidProd3_3'])),  int(globalBS.tempBraidElapsed3) , str(dic['BraidProd3_6']), str(dic['BraidProd3_7']))
                                        mycursor.execute(sql, val)
                                        
                        
                        if(globalBS.tempBraidProd4 != findBool(dic['BraidProd4_8'])):
                                globalBS.tempBraidProd4 = findBool(dic['BraidProd4_8'])
                                if(findBool(dic['BraidProd4_8']) == True):
                                        globalBS.tempBraidStart4 = time.time()
                                        globalBS.tempBraidDT4 = datetime.datetime.now()
                                if(findBool(dic['BraidProd4_8']) == False):
                                        globalBS.tempBraidEnd4 = time.time()
                                        globalBS.tempBraidElapsed4 = (globalBS.tempBraidEnd4 - globalBS.tempBraidStart4) / 60
                                        sql = "INSERT INTO braidproduction4 ( pir, operator_name, ontime, actual_line_speed, prod_time, drum_in, drum_out ) VALUES (%s, %s, %s,%s,%s,%s,%s)"
                                        val = (str(dic['BraidProd4_1']), str(dic['BraidProd4_2']), globalBS.tempBraidDT4, findFloat(float(dic['BraidProd4_3'])),  int(globalBS.tempBraidElapsed4) , str(dic['BraidProd4_6']), str(dic['BraidProd4_7']))
                                        mycursor.execute(sql, val)
                                        
                        
                        if(globalBS.tempBraidProd5 != findBool(dic['BraidProd5_8'])):
                                globalBS.tempBraidProd5 = findBool(dic['BraidProd5_8'])
                                if(findBool(dic['BraidProd5_8']) == True):
                                        globalBS.tempBraidStart5 = time.time()
                                        globalBS.tempBraidDT5 = datetime.datetime.now()
                                if(findBool(dic['BraidProd5_8']) == False):
                                        globalBS.tempBraidEnd5 = time.time()
                                        globalBS.tempBraidElapsed5 = (globalBS.tempBraidEnd5 - globalBS.tempBraidStart5) / 60
                                        sql = "INSERT INTO braidproduction5 ( pir, operator_name, ontime, actual_line_speed, prod_time, drum_in, drum_out ) VALUES (%s, %s, %s,%s,%s,%s,%s)"
                                        val = (str(dic['BraidProd5_1']), str(dic['BraidProd5_2']), globalBS.tempBraidDT5, findFloat(float(dic['BraidProd5_3'])),  int(globalBS.tempBraidElapsed5) , str(dic['BraidProd5_6']), str(dic['BraidProd5_7']))
                                        mycursor.execute(sql, val)
                                        
                
                        if(globalBS.tempBraidProd6 != findBool(dic['BraidProd6_8'])):
                                globalBS.tempBraidProd6 = findBool(dic['BraidProd6_8'])
                                if(findBool(dic['BraidProd6_8']) == True):
                                        globalBS.tempBraidStart6 = time.time()
                                        globalBS.tempBraidDT6 = datetime.datetime.now()
                                if(findBool(dic['BraidProd6_8']) == False):
                                        globalBS.tempBraidEnd6 = time.time()
                                        globalBS.tempBraidElapsed6 = (globalBS.tempBraidEnd6 - globalBS.tempBraidStart6) / 60
                                        sql = "INSERT INTO braidproduction6 ( pir, operator_name, ontime, actual_line_speed, prod_time, drum_in, drum_out ) VALUES (%s, %s, %s,%s,%s,%s,%s)"
                                        val = (str(dic['BraidProd6_1']), str(dic['BraidProd6_2']), globalBS.tempBraidDT6, findFloat(float(dic['BraidProd6_3'])),  int(globalBS.tempBraidElapsed6) , str(dic['BraidProd6_6']), str(dic['BraidProd6_7']))
                                        mycursor.execute(sql, val)
                                        
                        
                        if(globalBS.tempBraidProd7 != findBool(dic['BraidProd7_8'])):
                                globalBS.tempBraidProd7 = findBool(dic['BraidProd7_8'])
                                if(findBool(dic['BraidProd7_8']) == True):
                                        globalBS.tempBraidStart7 = time.time()
                                        globalBS.tempBraidDT7 = datetime.datetime.now()
                                if(findBool(dic['BraidProd7_8']) == False):
                                        globalBS.tempBraidEnd7 = time.time()
                                        globalBS.tempBraidElapsed7 = (globalBS.tempBraidEnd7 - globalBS.tempBraidStart7) / 60
                                        sql = "INSERT INTO braidproduction7 ( pir, operator_name, ontime, actual_line_speed, prod_time, drum_in, drum_out ) VALUES (%s, %s, %s,%s,%s,%s,%s)"
                                        val = (str(dic['BraidProd7_1']), str(dic['BraidProd7_2']), globalBS.tempBraidDT7, findFloat(float(dic['BraidProd7_3'])),  int(globalBS.tempBraidElapsed7) , str(dic['BraidProd7_6']), str(dic['BraidProd7_7']))
                                        mycursor.execute(sql, val)
                                        
                
                        if(globalBS.tempBraidProd8 != findBool(dic['BraidProd8_8'])):
                                globalBS.tempBraidProd8 = findBool(dic['BraidProd8_8'])
                                if(findBool(dic['BraidProd8_8']) == True):
                                        globalBS.tempBraidStart8 = time.time()
                                        globalBS.tempBraidDT8 = datetime.datetime.now()
                                if(findBool(dic['BraidProd8_8']) == False):
                                        globalBS.tempBraidEnd8 = time.time()
                                        globalBS.tempBraidElapsed8 = (globalBS.tempBraidEnd8 - globalBS.tempBraidStart8) / 60
                                        sql = "INSERT INTO braidproduction8 ( pir, operator_name, ontime, actual_line_speed, prod_time, drum_in, drum_out ) VALUES (%s, %s, %s,%s,%s,%s,%s)"
                                        val = (str(dic['BraidProd8_1']), str(dic['BraidProd8_2']), globalBS.tempBraidDT8, findFloat(float(dic['BraidProd8_3'])),  int(globalBS.tempBraidElapsed8) , str(dic['BraidProd8_6']), str(dic['BraidProd8_7']))
                                        mycursor.execute(sql, val)



                        #Braider alarm Processing should come here
                        if(globalBS.tempBraid1_1 != findBool(dic['Alarm1_1'])):
                                globalBS.tempBraid1_1 = findBool(dic['Alarm1_1'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 1, 'MACHINE EMERGENCY PRESSED', findBool(dic['Alarm1_1']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_2 != findBool(dic['Alarm1_2'])):
                                globalBS.tempBraid1_2 = findBool(dic['Alarm1_2'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 2, 'DOOR NOT CLOSED', findBool(dic['Alarm1_2']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_3 != findBool(dic['Alarm1_3'])):
                                globalBS.tempBraid1_3 = findBool(dic['Alarm1_3'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 3, 'CLOSE FRONT RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm1_3']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_4 != findBool(dic['Alarm1_4'])):
                                globalBS.tempBraid1_4 = findBool(dic['Alarm1_4'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 4, 'CLOSE FRONT LEFT DOOR AND PRESS RESET', findBool(dic['Alarm1_4']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_5 != findBool(dic['Alarm1_5'])):
                                globalBS.tempBraid1_5 = findBool(dic['Alarm1_5'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 5, 'CLOSE BACK RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm1_5']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_6 != findBool(dic['Alarm1_6'])):
                                globalBS.tempBraid1_6 = findBool(dic['Alarm1_6'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 6, 'CLOSE BACK LEFT DOOR AND PRESS RESET', findBool(dic['Alarm1_6']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_7 != findBool(dic['Alarm1_7'])):
                                globalBS.tempBraid1_7 = findBool(dic['Alarm1_7'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 7, 'BOBBIN EMPTY D1 INNER ACTIVATED', findBool(dic['Alarm1_7']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_8 != findBool(dic['Alarm1_8'])):
                                globalBS.tempBraid1_8 = findBool(dic['Alarm1_8'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 8, 'BOBBIN EMPTY D1 OUTER ACTIVATED', findBool(dic['Alarm1_8']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_9 != findBool(dic['Alarm1_9'])):
                                globalBS.tempBraid1_9 = findBool(dic['Alarm1_9'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 9, 'BOBBIN EMPTY D2 INNER ACTIVATED', findBool(dic['Alarm1_9']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_10 != findBool(dic['Alarm1_10'])):
                                globalBS.tempBraid1_10 = findBool(dic['Alarm1_10'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 10, 'BOBBIN EMPTY D2 OUTER ACTIVATED', findBool(dic['Alarm1_10']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_11 != findBool(dic['Alarm1_11'])):
                                globalBS.tempBraid1_11 = findBool(dic['Alarm1_11'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 11, 'WIRE BREAK D1 BACK ACTIVATED', findBool(dic['Alarm1_11']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_12 != findBool(dic['Alarm1_12'])):
                                globalBS.tempBraid1_12 = findBool(dic['Alarm1_12'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 12, 'WIRE BREAK D1 FRONT ACTIVATED', findBool(dic['Alarm1_12']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_13 != findBool(dic['Alarm1_13'])):
                                globalBS.tempBraid1_13 = findBool(dic['Alarm1_13'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 13, 'WIRE BREAK D2 BACK ACTIVATED', findBool(dic['Alarm1_13']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_14 != findBool(dic['Alarm1_14'])):
                                globalBS.tempBraid1_14 = findBool(dic['Alarm1_14'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 14, 'WIRE BREAK D2 OUTER ACTIVATED', findBool(dic['Alarm1_14']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_15 != findBool(dic['Alarm1_15'])):
                                globalBS.tempBraid1_15 = findBool(dic['Alarm1_15'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 15, 'OIL LEVEL D2 SENSOR ACTIVATED', findBool(dic['Alarm1_15']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_16 != findBool(dic['Alarm1_16'])):
                                globalBS.tempBraid1_16 = findBool(dic['Alarm1_16'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 16, 'MPCB TRIP ACTIVATED', findBool(dic['Alarm1_16']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_17 != findBool(dic['Alarm1_17'])):
                                globalBS.tempBraid1_17 = findBool(dic['Alarm1_17'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 17, 'RUNNING PLY SENSOR ACTIVATED', findBool(dic['Alarm1_17']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_18 != findBool(dic['Alarm1_18'])):
                                globalBS.tempBraid1_18 = findBool(dic['Alarm1_18'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 18, 'OIL LEVEL D1 SENSOR ACTIVATED', findBool(dic['Alarm1_18']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_19 != findBool(dic['Alarm1_19'])):
                                globalBS.tempBraid1_19 = findBool(dic['Alarm1_19'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 19, 'TAKE UP EMERGENGY ACTIVATED', findBool(dic['Alarm1_19']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_20 != findBool(dic['Alarm1_20'])):
                                globalBS.tempBraid1_20 = findBool(dic['Alarm1_20'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 20, 'WIRE BREAK D1 TOP ACTIVATED', findBool(dic['Alarm1_20']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_21 != findBool(dic['Alarm1_21'])):
                                globalBS.tempBraid1_21 = findBool(dic['Alarm1_21'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 21, 'WIRE BREAK D2 TOP ACTIVATED', findBool(dic['Alarm1_21']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_22 != findBool(dic['Alarm1_22'])):
                                globalBS.tempBraid1_22 = findBool(dic['Alarm1_22'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 22, 'METAL SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm1_22']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid1_23 != findBool(dic['Alarm1_23'])):
                                globalBS.tempBraid1_23 = findBool(dic['Alarm1_23'])
                                sql = "INSERT INTO braidalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid1_1'], dic['Braid1_2'], 23, 'ALUMINIUM SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm1_23']))
                                mycursor.execute(sql, val)


                        if(globalBS.tempBraid2_1 != findBool(dic['Alarm2_1'])):
                                globalBS.tempBraid2_1 = findBool(dic['Alarm2_1'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 1, 'MACHINE EMERGENCY PRESSED', findBool(dic['Alarm2_1']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_2 != findBool(dic['Alarm2_2'])):
                                globalBS.tempBraid2_2 = findBool(dic['Alarm2_2'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 2, 'DOOR NOT CLOSED', findBool(dic['Alarm2_2']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_3 != findBool(dic['Alarm2_3'])):
                                globalBS.tempBraid2_3 = findBool(dic['Alarm2_3'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 3, 'CLOSE FRONT RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm2_3']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_4 != findBool(dic['Alarm2_4'])):
                                globalBS.tempBraid2_4 = findBool(dic['Alarm2_4'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 4, 'CLOSE FRONT LEFT DOOR AND PRESS RESET', findBool(dic['Alarm2_4']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_5 != findBool(dic['Alarm2_5'])):
                                globalBS.tempBraid2_5 = findBool(dic['Alarm2_5'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 5, 'CLOSE BACK RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm2_5']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_6 != findBool(dic['Alarm2_6'])):
                                globalBS.tempBraid2_6 = findBool(dic['Alarm2_6'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 6, 'CLOSE BACK LEFT DOOR AND PRESS RESET', findBool(dic['Alarm2_6']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_7 != findBool(dic['Alarm2_7'])):
                                globalBS.tempBraid2_7 = findBool(dic['Alarm2_7'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 7, 'BOBBIN EMPTY D1 INNER ACTIVATED', findBool(dic['Alarm2_7']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_8 != findBool(dic['Alarm2_8'])):
                                globalBS.tempBraid2_8 = findBool(dic['Alarm2_8'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 8, 'BOBBIN EMPTY D1 OUTER ACTIVATED', findBool(dic['Alarm2_8']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_9 != findBool(dic['Alarm2_9'])):
                                globalBS.tempBraid2_9 = findBool(dic['Alarm2_9'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 9, 'BOBBIN EMPTY D2 INNER ACTIVATED', findBool(dic['Alarm2_9']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_10 != findBool(dic['Alarm2_10'])):
                                globalBS.tempBraid2_10 = findBool(dic['Alarm2_10'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 10, 'BOBBIN EMPTY D2 OUTER ACTIVATED', findBool(dic['Alarm2_10']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_11 != findBool(dic['Alarm2_11'])):
                                globalBS.tempBraid2_11 = findBool(dic['Alarm2_11'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 11, 'WIRE BREAK D1 BACK ACTIVATED', findBool(dic['Alarm2_11']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_12 != findBool(dic['Alarm2_12'])):
                                globalBS.tempBraid2_12 = findBool(dic['Alarm2_12'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 12, 'WIRE BREAK D1 FRONT ACTIVATED', findBool(dic['Alarm2_12']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_13 != findBool(dic['Alarm2_13'])):
                                globalBS.tempBraid2_13 = findBool(dic['Alarm2_13'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 13, 'WIRE BREAK D2 BACK ACTIVATED', findBool(dic['Alarm2_13']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_14 != findBool(dic['Alarm2_14'])):
                                globalBS.tempBraid2_14 = findBool(dic['Alarm2_14'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 14, 'WIRE BREAK D2 OUTER ACTIVATED', findBool(dic['Alarm2_14']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_15 != findBool(dic['Alarm2_15'])):
                                globalBS.tempBraid2_15 = findBool(dic['Alarm2_15'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 15, 'OIL LEVEL D2 SENSOR ACTIVATED', findBool(dic['Alarm2_15']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_16 != findBool(dic['Alarm2_16'])):
                                globalBS.tempBraid2_16 = findBool(dic['Alarm2_16'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 16, 'MPCB TRIP ACTIVATED', findBool(dic['Alarm2_16']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_17 != findBool(dic['Alarm2_17'])):
                                globalBS.tempBraid2_17 = findBool(dic['Alarm2_17'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 17, 'RUNNING PLY SENSOR ACTIVATED', findBool(dic['Alarm2_17']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_18 != findBool(dic['Alarm2_18'])):
                                globalBS.tempBraid2_18 = findBool(dic['Alarm2_18'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 18, 'OIL LEVEL D1 SENSOR ACTIVATED', findBool(dic['Alarm2_18']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_19 != findBool(dic['Alarm2_19'])):
                                globalBS.tempBraid2_19 = findBool(dic['Alarm2_19'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 19, 'TAKE UP EMERGENGY ACTIVATED', findBool(dic['Alarm2_19']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_20 != findBool(dic['Alarm2_20'])):
                                globalBS.tempBraid2_20 = findBool(dic['Alarm2_20'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 20, 'WIRE BREAK D1 TOP ACTIVATED', findBool(dic['Alarm2_20']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_21 != findBool(dic['Alarm2_21'])):
                                globalBS.tempBraid2_21 = findBool(dic['Alarm2_21'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 21, 'WIRE BREAK D2 TOP ACTIVATED', findBool(dic['Alarm2_21']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_22 != findBool(dic['Alarm2_22'])):
                                globalBS.tempBraid2_22 = findBool(dic['Alarm2_22'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 22, 'METAL SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm2_22']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid2_23 != findBool(dic['Alarm2_23'])):
                                globalBS.tempBraid2_23 = findBool(dic['Alarm2_23'])
                                sql = "INSERT INTO braidalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid2_1'], dic['Braid2_2'], 23, 'ALUMINIUM SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm2_23']))
                                mycursor.execute(sql, val)



                        if(globalBS.tempBraid3_1 != findBool(dic['Alarm3_1'])):
                                globalBS.tempBraid3_1 = findBool(dic['Alarm3_1'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 1, 'MACHINE EMERGENCY PRESSED', findBool(dic['Alarm3_1']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_2 != findBool(dic['Alarm3_2'])):
                                globalBS.tempBraid3_2 = findBool(dic['Alarm3_2'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 2, 'DOOR NOT CLOSED', findBool(dic['Alarm3_2']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_3 != findBool(dic['Alarm3_3'])):
                                globalBS.tempBraid3_3 = findBool(dic['Alarm3_3'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 3, 'CLOSE FRONT RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm3_3']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_4 != findBool(dic['Alarm3_4'])):
                                globalBS.tempBraid3_4 = findBool(dic['Alarm3_4'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 4, 'CLOSE FRONT LEFT DOOR AND PRESS RESET', findBool(dic['Alarm3_4']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_5 != findBool(dic['Alarm3_5'])):
                                globalBS.tempBraid3_5 = findBool(dic['Alarm3_5'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 5, 'CLOSE BACK RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm3_5']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_6 != findBool(dic['Alarm3_6'])):
                                globalBS.tempBraid3_6 = findBool(dic['Alarm3_6'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 6, 'CLOSE BACK LEFT DOOR AND PRESS RESET', findBool(dic['Alarm3_6']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_7 != findBool(dic['Alarm3_7'])):
                                globalBS.tempBraid3_7 = findBool(dic['Alarm3_7'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 7, 'BOBBIN EMPTY D1 INNER ACTIVATED', findBool(dic['Alarm3_7']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_8 != findBool(dic['Alarm3_8'])):
                                globalBS.tempBraid3_8 = findBool(dic['Alarm3_8'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 8, 'BOBBIN EMPTY D1 OUTER ACTIVATED', findBool(dic['Alarm3_8']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_9 != findBool(dic['Alarm3_9'])):
                                globalBS.tempBraid3_9 = findBool(dic['Alarm3_9'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 9, 'BOBBIN EMPTY D2 INNER ACTIVATED', findBool(dic['Alarm3_9']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_10 != findBool(dic['Alarm3_10'])):
                                globalBS.tempBraid3_10 = findBool(dic['Alarm3_10'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 10, 'BOBBIN EMPTY D2 OUTER ACTIVATED', findBool(dic['Alarm3_10']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_11 != findBool(dic['Alarm3_11'])):
                                globalBS.tempBraid3_11 = findBool(dic['Alarm3_11'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 11, 'WIRE BREAK D1 BACK ACTIVATED', findBool(dic['Alarm3_11']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_12 != findBool(dic['Alarm3_12'])):
                                globalBS.tempBraid3_12 = findBool(dic['Alarm3_12'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 12, 'WIRE BREAK D1 FRONT ACTIVATED', findBool(dic['Alarm3_12']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_13 != findBool(dic['Alarm3_13'])):
                                globalBS.tempBraid3_13 = findBool(dic['Alarm3_13'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 13, 'WIRE BREAK D2 BACK ACTIVATED', findBool(dic['Alarm3_13']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_14 != findBool(dic['Alarm3_14'])):
                                globalBS.tempBraid3_14 = findBool(dic['Alarm3_14'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 14, 'WIRE BREAK D2 OUTER ACTIVATED', findBool(dic['Alarm3_14']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_15 != findBool(dic['Alarm3_15'])):
                                globalBS.tempBraid3_15 = findBool(dic['Alarm3_15'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 15, 'OIL LEVEL D2 SENSOR ACTIVATED', findBool(dic['Alarm3_15']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_16 != findBool(dic['Alarm3_16'])):
                                globalBS.tempBraid3_16 = findBool(dic['Alarm3_16'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 16, 'MPCB TRIP ACTIVATED', findBool(dic['Alarm3_16']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_17 != findBool(dic['Alarm3_17'])):
                                globalBS.tempBraid3_17 = findBool(dic['Alarm3_17'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 17, 'RUNNING PLY SENSOR ACTIVATED', findBool(dic['Alarm3_17']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_18 != findBool(dic['Alarm3_18'])):
                                globalBS.tempBraid3_18 = findBool(dic['Alarm3_18'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 18, 'OIL LEVEL D1 SENSOR ACTIVATED', findBool(dic['Alarm3_18']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_19 != findBool(dic['Alarm3_19'])):
                                globalBS.tempBraid3_19 = findBool(dic['Alarm3_19'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 19, 'TAKE UP EMERGENGY ACTIVATED', findBool(dic['Alarm3_19']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_20 != findBool(dic['Alarm3_20'])):
                                globalBS.tempBraid3_20 = findBool(dic['Alarm3_20'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 20, 'WIRE BREAK D1 TOP ACTIVATED', findBool(dic['Alarm3_20']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_21 != findBool(dic['Alarm3_21'])):
                                globalBS.tempBraid3_21 = findBool(dic['Alarm3_21'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 21, 'WIRE BREAK D2 TOP ACTIVATED', findBool(dic['Alarm3_21']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_22 != findBool(dic['Alarm3_22'])):
                                globalBS.tempBraid3_22 = findBool(dic['Alarm3_22'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 22, 'METAL SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm3_22']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid3_23 != findBool(dic['Alarm3_23'])):
                                globalBS.tempBraid3_23 = findBool(dic['Alarm3_23'])
                                sql = "INSERT INTO braidalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid3_1'], dic['Braid3_2'], 23, 'ALUMINIUM SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm3_23']))
                                mycursor.execute(sql, val)



                        if(globalBS.tempBraid4_1 != findBool(dic['Alarm4_1'])):
                                globalBS.tempBraid4_1 = findBool(dic['Alarm4_1'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 1, 'MACHINE EMERGENCY PRESSED', findBool(dic['Alarm4_1']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_2 != findBool(dic['Alarm4_2'])):
                                globalBS.tempBraid4_2 = findBool(dic['Alarm4_2'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 2, 'DOOR NOT CLOSED', findBool(dic['Alarm4_2']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_3 != findBool(dic['Alarm4_3'])):
                                globalBS.tempBraid4_3 = findBool(dic['Alarm4_3'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 3, 'CLOSE FRONT RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm4_3']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_4 != findBool(dic['Alarm4_4'])):
                                globalBS.tempBraid4_4 = findBool(dic['Alarm4_4'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 4, 'CLOSE FRONT LEFT DOOR AND PRESS RESET', findBool(dic['Alarm4_4']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_5 != findBool(dic['Alarm4_5'])):
                                globalBS.tempBraid4_5 = findBool(dic['Alarm4_5'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 5, 'CLOSE BACK RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm4_5']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_6 != findBool(dic['Alarm4_6'])):
                                globalBS.tempBraid4_6 = findBool(dic['Alarm4_6'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 6, 'CLOSE BACK LEFT DOOR AND PRESS RESET', findBool(dic['Alarm4_6']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_7 != findBool(dic['Alarm4_7'])):
                                globalBS.tempBraid4_7 = findBool(dic['Alarm4_7'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 7, 'BOBBIN EMPTY D1 INNER ACTIVATED', findBool(dic['Alarm4_7']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_8 != findBool(dic['Alarm4_8'])):
                                globalBS.tempBraid4_8 = findBool(dic['Alarm4_8'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 8, 'BOBBIN EMPTY D1 OUTER ACTIVATED', findBool(dic['Alarm4_8']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_9 != findBool(dic['Alarm4_9'])):
                                globalBS.tempBraid4_9 = findBool(dic['Alarm4_9'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 9, 'BOBBIN EMPTY D2 INNER ACTIVATED', findBool(dic['Alarm4_9']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_10 != findBool(dic['Alarm4_10'])):
                                globalBS.tempBraid4_10 = findBool(dic['Alarm4_10'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 10, 'BOBBIN EMPTY D2 OUTER ACTIVATED', findBool(dic['Alarm4_10']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_11 != findBool(dic['Alarm4_11'])):
                                globalBS.tempBraid4_11 = findBool(dic['Alarm4_11'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 11, 'WIRE BREAK D1 BACK ACTIVATED', findBool(dic['Alarm4_11']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_12 != findBool(dic['Alarm4_12'])):
                                globalBS.tempBraid4_12 = findBool(dic['Alarm4_12'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 12, 'WIRE BREAK D1 FRONT ACTIVATED', findBool(dic['Alarm4_12']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_13 != findBool(dic['Alarm4_13'])):
                                globalBS.tempBraid4_13 = findBool(dic['Alarm4_13'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 13, 'WIRE BREAK D2 BACK ACTIVATED', findBool(dic['Alarm4_13']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_14 != findBool(dic['Alarm4_14'])):
                                globalBS.tempBraid4_14 = findBool(dic['Alarm4_14'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 14, 'WIRE BREAK D2 OUTER ACTIVATED', findBool(dic['Alarm4_14']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_15 != findBool(dic['Alarm4_15'])):
                                globalBS.tempBraid4_15 = findBool(dic['Alarm4_15'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 15, 'OIL LEVEL D2 SENSOR ACTIVATED', findBool(dic['Alarm4_15']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_16 != findBool(dic['Alarm4_16'])):
                                globalBS.tempBraid4_16 = findBool(dic['Alarm4_16'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 16, 'MPCB TRIP ACTIVATED', findBool(dic['Alarm4_16']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_17 != findBool(dic['Alarm4_17'])):
                                globalBS.tempBraid4_17 = findBool(dic['Alarm4_17'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 17, 'RUNNING PLY SENSOR ACTIVATED', findBool(dic['Alarm4_17']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_18 != findBool(dic['Alarm4_18'])):
                                globalBS.tempBraid4_18 = findBool(dic['Alarm4_18'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 18, 'OIL LEVEL D1 SENSOR ACTIVATED', findBool(dic['Alarm4_18']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_19 != findBool(dic['Alarm4_19'])):
                                globalBS.tempBraid4_19 = findBool(dic['Alarm4_19'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 19, 'TAKE UP EMERGENGY ACTIVATED', findBool(dic['Alarm4_19']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_20 != findBool(dic['Alarm4_20'])):
                                globalBS.tempBraid4_20 = findBool(dic['Alarm4_20'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 20, 'WIRE BREAK D1 TOP ACTIVATED', findBool(dic['Alarm4_20']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_21 != findBool(dic['Alarm4_21'])):
                                globalBS.tempBraid4_21 = findBool(dic['Alarm4_21'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 21, 'WIRE BREAK D2 TOP ACTIVATED', findBool(dic['Alarm4_21']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_22 != findBool(dic['Alarm4_22'])):
                                globalBS.tempBraid4_22 = findBool(dic['Alarm4_22'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 22, 'METAL SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm4_22']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid4_23 != findBool(dic['Alarm4_23'])):
                                globalBS.tempBraid4_23 = findBool(dic['Alarm4_23'])
                                sql = "INSERT INTO braidalarm4 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid4_1'], dic['Braid4_2'], 23, 'ALUMINIUM SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm4_23']))
                                mycursor.execute(sql, val)



                        if(globalBS.tempBraid5_1 != findBool(dic['Alarm5_1'])):
                                globalBS.tempBraid5_1 = findBool(dic['Alarm5_1'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 1, 'MACHINE EMERGENCY PRESSED', findBool(dic['Alarm5_1']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_2 != findBool(dic['Alarm5_2'])):
                                globalBS.tempBraid5_2 = findBool(dic['Alarm5_2'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 2, 'DOOR NOT CLOSED', findBool(dic['Alarm5_2']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_3 != findBool(dic['Alarm5_3'])):
                                globalBS.tempBraid5_3 = findBool(dic['Alarm5_3'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 3, 'CLOSE FRONT RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm5_3']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_4 != findBool(dic['Alarm5_4'])):
                                globalBS.tempBraid5_4 = findBool(dic['Alarm5_4'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 4, 'CLOSE FRONT LEFT DOOR AND PRESS RESET', findBool(dic['Alarm5_4']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_5 != findBool(dic['Alarm5_5'])):
                                globalBS.tempBraid5_5 = findBool(dic['Alarm5_5'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 5, 'CLOSE BACK RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm5_5']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_6 != findBool(dic['Alarm5_6'])):
                                globalBS.tempBraid5_6 = findBool(dic['Alarm5_6'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 6, 'CLOSE BACK LEFT DOOR AND PRESS RESET', findBool(dic['Alarm5_6']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_7 != findBool(dic['Alarm5_7'])):
                                globalBS.tempBraid5_7 = findBool(dic['Alarm5_7'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 7, 'BOBBIN EMPTY D1 INNER ACTIVATED', findBool(dic['Alarm5_7']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_8 != findBool(dic['Alarm5_8'])):
                                globalBS.tempBraid5_8 = findBool(dic['Alarm5_8'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 8, 'BOBBIN EMPTY D1 OUTER ACTIVATED', findBool(dic['Alarm5_8']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_9 != findBool(dic['Alarm5_9'])):
                                globalBS.tempBraid5_9 = findBool(dic['Alarm5_9'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 9, 'BOBBIN EMPTY D2 INNER ACTIVATED', findBool(dic['Alarm5_9']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_10 != findBool(dic['Alarm5_10'])):
                                globalBS.tempBraid5_10 = findBool(dic['Alarm5_10'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 10, 'BOBBIN EMPTY D2 OUTER ACTIVATED', findBool(dic['Alarm5_10']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_11 != findBool(dic['Alarm5_11'])):
                                globalBS.tempBraid5_11 = findBool(dic['Alarm5_11'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 11, 'WIRE BREAK D1 BACK ACTIVATED', findBool(dic['Alarm5_11']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_12 != findBool(dic['Alarm5_12'])):
                                globalBS.tempBraid5_12 = findBool(dic['Alarm5_12'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 12, 'WIRE BREAK D1 FRONT ACTIVATED', findBool(dic['Alarm5_12']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_13 != findBool(dic['Alarm5_13'])):
                                globalBS.tempBraid5_13 = findBool(dic['Alarm5_13'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 13, 'WIRE BREAK D2 BACK ACTIVATED', findBool(dic['Alarm5_13']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_14 != findBool(dic['Alarm5_14'])):
                                globalBS.tempBraid5_14 = findBool(dic['Alarm5_14'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 14, 'WIRE BREAK D2 OUTER ACTIVATED', findBool(dic['Alarm5_14']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_15 != findBool(dic['Alarm5_15'])):
                                globalBS.tempBraid5_15 = findBool(dic['Alarm5_15'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 15, 'OIL LEVEL D2 SENSOR ACTIVATED', findBool(dic['Alarm5_15']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_16 != findBool(dic['Alarm5_16'])):
                                globalBS.tempBraid5_16 = findBool(dic['Alarm5_16'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 16, 'MPCB TRIP ACTIVATED', findBool(dic['Alarm5_16']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_17 != findBool(dic['Alarm5_17'])):
                                globalBS.tempBraid5_17 = findBool(dic['Alarm5_17'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 17, 'RUNNING PLY SENSOR ACTIVATED', findBool(dic['Alarm5_17']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_18 != findBool(dic['Alarm5_18'])):
                                globalBS.tempBraid5_18 = findBool(dic['Alarm5_18'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 18, 'OIL LEVEL D1 SENSOR ACTIVATED', findBool(dic['Alarm5_18']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_19 != findBool(dic['Alarm5_19'])):
                                globalBS.tempBraid5_19 = findBool(dic['Alarm5_19'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 19, 'TAKE UP EMERGENGY ACTIVATED', findBool(dic['Alarm5_19']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_20 != findBool(dic['Alarm5_20'])):
                                globalBS.tempBraid5_20 = findBool(dic['Alarm5_20'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 20, 'WIRE BREAK D1 TOP ACTIVATED', findBool(dic['Alarm5_20']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_21 != findBool(dic['Alarm5_21'])):
                                globalBS.tempBraid5_21 = findBool(dic['Alarm5_21'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 21, 'WIRE BREAK D2 TOP ACTIVATED', findBool(dic['Alarm5_21']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_22 != findBool(dic['Alarm5_22'])):
                                globalBS.tempBraid5_22 = findBool(dic['Alarm5_22'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 22, 'METAL SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm5_22']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid5_23 != findBool(dic['Alarm5_23'])):
                                globalBS.tempBraid5_23 = findBool(dic['Alarm5_23'])
                                sql = "INSERT INTO braidalarm5 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid5_1'], dic['Braid5_2'], 23, 'ALUMINIUM SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm5_23']))
                                mycursor.execute(sql, val)


                        if(globalBS.tempBraid6_1 != findBool(dic['Alarm6_1'])):
                                globalBS.tempBraid6_1 = findBool(dic['Alarm6_1'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 1, 'MACHINE EMERGENCY PRESSED', findBool(dic['Alarm6_1']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_2 != findBool(dic['Alarm6_2'])):
                                globalBS.tempBraid6_2 = findBool(dic['Alarm6_2'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 2, 'DOOR NOT CLOSED', findBool(dic['Alarm6_2']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_3 != findBool(dic['Alarm6_3'])):
                                globalBS.tempBraid6_3 = findBool(dic['Alarm6_3'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 3, 'CLOSE FRONT RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm6_3']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_4 != findBool(dic['Alarm6_4'])):
                                globalBS.tempBraid6_4 = findBool(dic['Alarm6_4'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 4, 'CLOSE FRONT LEFT DOOR AND PRESS RESET', findBool(dic['Alarm6_4']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_5 != findBool(dic['Alarm6_5'])):
                                globalBS.tempBraid6_5 = findBool(dic['Alarm6_5'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 5, 'CLOSE BACK RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm6_5']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_6 != findBool(dic['Alarm6_6'])):
                                globalBS.tempBraid6_6 = findBool(dic['Alarm6_6'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 6, 'CLOSE BACK LEFT DOOR AND PRESS RESET', findBool(dic['Alarm6_6']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_7 != findBool(dic['Alarm6_7'])):
                                globalBS.tempBraid6_7 = findBool(dic['Alarm6_7'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 7, 'BOBBIN EMPTY D1 INNER ACTIVATED', findBool(dic['Alarm6_7']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_8 != findBool(dic['Alarm6_8'])):
                                globalBS.tempBraid6_8 = findBool(dic['Alarm6_8'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 8, 'BOBBIN EMPTY D1 OUTER ACTIVATED', findBool(dic['Alarm6_8']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_9 != findBool(dic['Alarm6_9'])):
                                globalBS.tempBraid6_9 = findBool(dic['Alarm6_9'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 9, 'BOBBIN EMPTY D2 INNER ACTIVATED', findBool(dic['Alarm6_9']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_10 != findBool(dic['Alarm6_10'])):
                                globalBS.tempBraid6_10 = findBool(dic['Alarm6_10'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 10, 'BOBBIN EMPTY D2 OUTER ACTIVATED', findBool(dic['Alarm6_10']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_11 != findBool(dic['Alarm6_11'])):
                                globalBS.tempBraid6_11 = findBool(dic['Alarm6_11'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 11, 'WIRE BREAK D1 BACK ACTIVATED', findBool(dic['Alarm6_11']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_12 != findBool(dic['Alarm6_12'])):
                                globalBS.tempBraid6_12 = findBool(dic['Alarm6_12'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 12, 'WIRE BREAK D1 FRONT ACTIVATED', findBool(dic['Alarm6_12']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_13 != findBool(dic['Alarm6_13'])):
                                globalBS.tempBraid6_13 = findBool(dic['Alarm6_13'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 13, 'WIRE BREAK D2 BACK ACTIVATED', findBool(dic['Alarm6_13']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_14 != findBool(dic['Alarm6_14'])):
                                globalBS.tempBraid6_14 = findBool(dic['Alarm6_14'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 14, 'WIRE BREAK D2 OUTER ACTIVATED', findBool(dic['Alarm6_14']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_15 != findBool(dic['Alarm6_15'])):
                                globalBS.tempBraid6_15 = findBool(dic['Alarm6_15'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 15, 'OIL LEVEL D2 SENSOR ACTIVATED', findBool(dic['Alarm6_15']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_16 != findBool(dic['Alarm6_16'])):
                                globalBS.tempBraid6_16 = findBool(dic['Alarm6_16'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 16, 'MPCB TRIP ACTIVATED', findBool(dic['Alarm6_16']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_17 != findBool(dic['Alarm6_17'])):
                                globalBS.tempBraid6_17 = findBool(dic['Alarm6_17'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 17, 'RUNNING PLY SENSOR ACTIVATED', findBool(dic['Alarm6_17']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_18 != findBool(dic['Alarm6_18'])):
                                globalBS.tempBraid6_18 = findBool(dic['Alarm6_18'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 18, 'OIL LEVEL D1 SENSOR ACTIVATED', findBool(dic['Alarm6_18']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_19 != findBool(dic['Alarm6_19'])):
                                globalBS.tempBraid6_19 = findBool(dic['Alarm6_19'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 19, 'TAKE UP EMERGENGY ACTIVATED', findBool(dic['Alarm6_19']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_20 != findBool(dic['Alarm6_20'])):
                                globalBS.tempBraid6_20 = findBool(dic['Alarm6_20'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 20, 'WIRE BREAK D1 TOP ACTIVATED', findBool(dic['Alarm6_20']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_21 != findBool(dic['Alarm6_21'])):
                                globalBS.tempBraid6_21 = findBool(dic['Alarm6_21'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 21, 'WIRE BREAK D2 TOP ACTIVATED', findBool(dic['Alarm6_21']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_22 != findBool(dic['Alarm6_22'])):
                                globalBS.tempBraid6_22 = findBool(dic['Alarm6_22'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 22, 'METAL SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm6_22']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid6_23 != findBool(dic['Alarm6_23'])):
                                globalBS.tempBraid6_23 = findBool(dic['Alarm6_23'])
                                sql = "INSERT INTO braidalarm6 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid6_1'], dic['Braid6_2'], 23, 'ALUMINIUM SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm6_23']))
                                mycursor.execute(sql, val)



                        if(globalBS.tempBraid7_1 != findBool(dic['Alarm7_1'])):
                                globalBS.tempBraid7_1 = findBool(dic['Alarm7_1'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 1, 'MACHINE EMERGENCY PRESSED', findBool(dic['Alarm7_1']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_2 != findBool(dic['Alarm7_2'])):
                                globalBS.tempBraid7_2 = findBool(dic['Alarm7_2'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 2, 'DOOR NOT CLOSED', findBool(dic['Alarm7_2']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_3 != findBool(dic['Alarm7_3'])):
                                globalBS.tempBraid7_3 = findBool(dic['Alarm7_3'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 3, 'CLOSE FRONT RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm7_3']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_4 != findBool(dic['Alarm7_4'])):
                                globalBS.tempBraid7_4 = findBool(dic['Alarm7_4'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 4, 'CLOSE FRONT LEFT DOOR AND PRESS RESET', findBool(dic['Alarm7_4']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_5 != findBool(dic['Alarm7_5'])):
                                globalBS.tempBraid7_5 = findBool(dic['Alarm7_5'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 5, 'CLOSE BACK RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm7_5']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_6 != findBool(dic['Alarm7_6'])):
                                globalBS.tempBraid7_6 = findBool(dic['Alarm7_6'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 6, 'CLOSE BACK LEFT DOOR AND PRESS RESET', findBool(dic['Alarm7_6']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_7 != findBool(dic['Alarm7_7'])):
                                globalBS.tempBraid7_7 = findBool(dic['Alarm7_7'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 7, 'BOBBIN EMPTY D1 INNER ACTIVATED', findBool(dic['Alarm7_7']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_8 != findBool(dic['Alarm7_8'])):
                                globalBS.tempBraid7_8 = findBool(dic['Alarm7_8'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 8, 'BOBBIN EMPTY D1 OUTER ACTIVATED', findBool(dic['Alarm7_8']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_9 != findBool(dic['Alarm7_9'])):
                                globalBS.tempBraid7_9 = findBool(dic['Alarm7_9'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 9, 'BOBBIN EMPTY D2 INNER ACTIVATED', findBool(dic['Alarm7_9']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_10 != findBool(dic['Alarm7_10'])):
                                globalBS.tempBraid7_10 = findBool(dic['Alarm7_10'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 10, 'BOBBIN EMPTY D2 OUTER ACTIVATED', findBool(dic['Alarm7_10']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_11 != findBool(dic['Alarm7_11'])):
                                globalBS.tempBraid7_11 = findBool(dic['Alarm7_11'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 11, 'WIRE BREAK D1 BACK ACTIVATED', findBool(dic['Alarm7_11']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_12 != findBool(dic['Alarm7_12'])):
                                globalBS.tempBraid7_12 = findBool(dic['Alarm7_12'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 12, 'WIRE BREAK D1 FRONT ACTIVATED', findBool(dic['Alarm7_12']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_13 != findBool(dic['Alarm7_13'])):
                                globalBS.tempBraid7_13 = findBool(dic['Alarm7_13'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 13, 'WIRE BREAK D2 BACK ACTIVATED', findBool(dic['Alarm7_13']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_14 != findBool(dic['Alarm7_14'])):
                                globalBS.tempBraid7_14 = findBool(dic['Alarm7_14'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 14, 'WIRE BREAK D2 OUTER ACTIVATED', findBool(dic['Alarm7_14']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_15 != findBool(dic['Alarm7_15'])):
                                globalBS.tempBraid7_15 = findBool(dic['Alarm7_15'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 15, 'OIL LEVEL D2 SENSOR ACTIVATED', findBool(dic['Alarm7_15']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_16 != findBool(dic['Alarm7_16'])):
                                globalBS.tempBraid7_16 = findBool(dic['Alarm7_16'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 16, 'MPCB TRIP ACTIVATED', findBool(dic['Alarm7_16']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_17 != findBool(dic['Alarm7_17'])):
                                globalBS.tempBraid7_17 = findBool(dic['Alarm7_17'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 17, 'RUNNING PLY SENSOR ACTIVATED', findBool(dic['Alarm7_17']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_18 != findBool(dic['Alarm7_18'])):
                                globalBS.tempBraid7_18 = findBool(dic['Alarm7_18'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 18, 'OIL LEVEL D1 SENSOR ACTIVATED', findBool(dic['Alarm7_18']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_19 != findBool(dic['Alarm7_19'])):
                                globalBS.tempBraid7_19 = findBool(dic['Alarm7_19'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 19, 'TAKE UP EMERGENGY ACTIVATED', findBool(dic['Alarm7_19']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_20 != findBool(dic['Alarm7_20'])):
                                globalBS.tempBraid7_20 = findBool(dic['Alarm7_20'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 20, 'WIRE BREAK D1 TOP ACTIVATED', findBool(dic['Alarm7_20']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_21 != findBool(dic['Alarm7_21'])):
                                globalBS.tempBraid7_21 = findBool(dic['Alarm7_21'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 21, 'WIRE BREAK D2 TOP ACTIVATED', findBool(dic['Alarm7_21']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_22 != findBool(dic['Alarm7_22'])):
                                globalBS.tempBraid7_22 = findBool(dic['Alarm7_22'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 22, 'METAL SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm7_22']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid7_23 != findBool(dic['Alarm7_23'])):
                                globalBS.tempBraid7_23 = findBool(dic['Alarm7_23'])
                                sql = "INSERT INTO braidalarm7 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid7_1'], dic['Braid7_2'], 23, 'ALUMINIUM SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm7_23']))
                                mycursor.execute(sql, val)




                        if(globalBS.tempBraid8_1 != findBool(dic['Alarm8_1'])):
                                globalBS.tempBraid8_1 = findBool(dic['Alarm8_1'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 1, 'MACHINE EMERGENCY PRESSED', findBool(dic['Alarm8_1']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_2 != findBool(dic['Alarm8_2'])):
                                globalBS.tempBraid8_2 = findBool(dic['Alarm8_2'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 2, 'DOOR NOT CLOSED', findBool(dic['Alarm8_2']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_3 != findBool(dic['Alarm8_3'])):
                                globalBS.tempBraid8_3 = findBool(dic['Alarm8_3'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 3, 'CLOSE FRONT RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm8_3']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_4 != findBool(dic['Alarm8_4'])):
                                globalBS.tempBraid8_4 = findBool(dic['Alarm8_4'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 4, 'CLOSE FRONT LEFT DOOR AND PRESS RESET', findBool(dic['Alarm8_4']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_5 != findBool(dic['Alarm8_5'])):
                                globalBS.tempBraid8_5 = findBool(dic['Alarm8_5'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 5, 'CLOSE BACK RIGHT DOOR AND PRESS RESET', findBool(dic['Alarm8_5']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_6 != findBool(dic['Alarm8_6'])):
                                globalBS.tempBraid8_6 = findBool(dic['Alarm8_6'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 6, 'CLOSE BACK LEFT DOOR AND PRESS RESET', findBool(dic['Alarm8_6']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_7 != findBool(dic['Alarm8_7'])):
                                globalBS.tempBraid8_7 = findBool(dic['Alarm8_7'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 7, 'BOBBIN EMPTY D1 INNER ACTIVATED', findBool(dic['Alarm8_7']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_8 != findBool(dic['Alarm8_8'])):
                                globalBS.tempBraid8_8 = findBool(dic['Alarm8_8'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 8, 'BOBBIN EMPTY D1 OUTER ACTIVATED', findBool(dic['Alarm8_8']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_9 != findBool(dic['Alarm8_9'])):
                                globalBS.tempBraid8_9 = findBool(dic['Alarm8_9'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 9, 'BOBBIN EMPTY D2 INNER ACTIVATED', findBool(dic['Alarm8_9']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_10 != findBool(dic['Alarm8_10'])):
                                globalBS.tempBraid8_10 = findBool(dic['Alarm8_10'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 10, 'BOBBIN EMPTY D2 OUTER ACTIVATED', findBool(dic['Alarm8_10']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_11 != findBool(dic['Alarm8_11'])):
                                globalBS.tempBraid8_11 = findBool(dic['Alarm8_11'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 11, 'WIRE BREAK D1 BACK ACTIVATED', findBool(dic['Alarm8_11']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_12 != findBool(dic['Alarm8_12'])):
                                globalBS.tempBraid8_12 = findBool(dic['Alarm8_12'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 12, 'WIRE BREAK D1 FRONT ACTIVATED', findBool(dic['Alarm8_12']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_13 != findBool(dic['Alarm8_13'])):
                                globalBS.tempBraid8_13 = findBool(dic['Alarm8_13'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 13, 'WIRE BREAK D2 BACK ACTIVATED', findBool(dic['Alarm8_13']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_14 != findBool(dic['Alarm8_14'])):
                                globalBS.tempBraid8_14 = findBool(dic['Alarm8_14'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 14, 'WIRE BREAK D2 OUTER ACTIVATED', findBool(dic['Alarm8_14']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_15 != findBool(dic['Alarm8_15'])):
                                globalBS.tempBraid8_15 = findBool(dic['Alarm8_15'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 15, 'OIL LEVEL D2 SENSOR ACTIVATED', findBool(dic['Alarm8_15']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_16 != findBool(dic['Alarm8_16'])):
                                globalBS.tempBraid8_16 = findBool(dic['Alarm8_16'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 16, 'MPCB TRIP ACTIVATED', findBool(dic['Alarm8_16']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_17 != findBool(dic['Alarm8_17'])):
                                globalBS.tempBraid8_17 = findBool(dic['Alarm8_17'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 17, 'RUNNING PLY SENSOR ACTIVATED', findBool(dic['Alarm8_17']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_18 != findBool(dic['Alarm8_18'])):
                                globalBS.tempBraid8_18 = findBool(dic['Alarm8_18'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 18, 'OIL LEVEL D1 SENSOR ACTIVATED', findBool(dic['Alarm8_18']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_19 != findBool(dic['Alarm8_19'])):
                                globalBS.tempBraid8_19 = findBool(dic['Alarm8_19'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 19, 'TAKE UP EMERGENGY ACTIVATED', findBool(dic['Alarm8_19']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_20 != findBool(dic['Alarm8_20'])):
                                globalBS.tempBraid8_20 = findBool(dic['Alarm8_20'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 20, 'WIRE BREAK D1 TOP ACTIVATED', findBool(dic['Alarm8_20']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_21 != findBool(dic['Alarm8_21'])):
                                globalBS.tempBraid8_21 = findBool(dic['Alarm8_21'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 21, 'WIRE BREAK D2 TOP ACTIVATED', findBool(dic['Alarm8_21']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_22 != findBool(dic['Alarm8_22'])):
                                globalBS.tempBraid8_22 = findBool(dic['Alarm8_22'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 22, 'METAL SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm8_22']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempBraid8_23 != findBool(dic['Alarm8_23'])):
                                globalBS.tempBraid8_23 = findBool(dic['Alarm8_23'])
                                sql = "INSERT INTO braidalarm8 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                val = (dic['Braid8_1'], dic['Braid8_2'], 23, 'ALUMINIUM SENSOR DETECHED PUT RED TAPE', findBool(dic['Alarm8_23']))
                                mycursor.execute(sql, val)

                        #PLC Status
                        if(globalBS.tempPlc_1 != findBool(dic['Plc_1'])):
                                globalBS.tempPlc_1 = findBool(dic['Plc_1'])
                                sql = "INSERT INTO plcstatus ( col_id, braider1 ) VALUES (%s,%s)"
                                val = (1, findBool(dic['Plc_1']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempPlc_2 != findBool(dic['Plc_2'])):
                                globalBS.tempPlc_2 = findBool(dic['Plc_2'])
                                sql = "INSERT INTO plcstatus ( col_id, braider2 ) VALUES (%s,%s)"
                                val = (2, findBool(dic['Plc_2']))
                                mycursor.execute(sql, val)
                        
                        if(globalBS.tempPlc_3 != findBool(dic['Plc_3'])):
                                globalBS.tempPlc_3 = findBool(dic['Plc_3'])
                                sql = "INSERT INTO plcstatus ( col_id, braider3 ) VALUES (%s,%s)"
                                val = (3, findBool(dic['Plc_3']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempPlc_4 != findBool(dic['Plc_4'])):
                                globalBS.tempPlc_4 = findBool(dic['Plc_4'])
                                sql = "INSERT INTO plcstatus ( col_id, braider4 ) VALUES (%s,%s)"
                                val = (4, findBool(dic['Plc_4']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempPlc_5 != findBool(dic['Plc_5'])):
                                globalBS.tempPlc_5 = findBool(dic['Plc_5'])
                                sql = "INSERT INTO plcstatus ( col_id, braider5 ) VALUES (%s,%s)"
                                val = (5, findBool(dic['Plc_5']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempPlc_6 != findBool(dic['Plc_6'])):
                                globalBS.tempPlc_6 = findBool(dic['Plc_6'])
                                sql = "INSERT INTO plcstatus ( col_id, braider6 ) VALUES (%s,%s)"
                                val = (6, findBool(dic['Plc_6']))
                                mycursor.execute(sql, val)
                        
                        if(globalBS.tempPlc_7 != findBool(dic['Plc_7'])):
                                globalBS.tempPlc_7 = findBool(dic['Plc_7'])
                                sql = "INSERT INTO plcstatus ( col_id, braider7 ) VALUES (%s,%s)"
                                val = (7, findBool(dic['Plc_7']))
                                mycursor.execute(sql, val)

                        if(globalBS.tempPlc_8 != findBool(dic['Plc_8'])):
                                globalBS.tempPlc_8 = findBool(dic['Plc_8'])
                                sql = "INSERT INTO plcstatus ( col_id, braider8 ) VALUES (%s,%s)"
                                val = (8, findBool(dic['Plc_8']))
                                mycursor.execute(sql, val)


                        
                        if(globalBS.tempBraidStop1 != findBool(dic['BraidStop1_2'])):
                                globalBS.tempBraidStop1 = findBool(dic['BraidStop1_2'])
                                if(findBool(dic['BraidStop1_2']) == True):
                                        globalBS.tempBraidStopID1 = int(dic['BraidStop1_1'])
                                if(dic['BraidStop1_1'] == '1'):
                                        dic['BraidStopMessage1'] = "Carrier Problem"
                                elif(dic['BraidStop1_1'] == '2'):
                                        dic['BraidStopMessage1'] = "Joint Bobbin"
                                elif(dic['BraidStop1_1'] == '3'):
                                        dic['BraidStopMessage1'] = "Liner Cut"
                                elif(dic['BraidStop1_1'] == '4'):
                                        dic['BraidStopMessage1'] = "Mandrel Broken"
                                elif(dic['BraidStop1_1'] == '5'):
                                        dic['BraidStopMessage1'] = "Pitch Problem"
                                elif(dic['BraidStop1_1'] == '6'):
                                        dic['BraidStopMessage1'] = "Ply Cut Joint"
                                elif(dic['BraidStop1_1'] == '7'):
                                        dic['BraidStopMessage1'] = "Power Cut"
                                elif(dic['BraidStop1_1'] == '8'):
                                        dic['BraidStopMessage1'] = "Push Back"
                                elif(dic['BraidStop1_1'] == '9'):
                                        dic['BraidStopMessage1'] = "Setting Joint"
                                elif(dic['BraidStop1_1'] == '10'):
                                        dic['BraidStopMessage1'] = "Tube Joint"
                                elif(dic['BraidStop1_1'] == '11'):
                                        dic['BraidStopMessage1'] = "Wire Break"
                                elif(dic['BraidStop1_1'] == '12'):
                                        dic['BraidStopMessage1'] = "Wire Loose"
                                elif(dic['BraidStop1_1'] == '13'):
                                        dic['BraidStopMessage1'] = "Over Heating"
                                elif(dic['BraidStop1_1'] == '14'):
                                        dic['BraidStopMessage1'] = "M/C Stop"
                                elif(dic['BraidStop1_1'] == '15'):
                                        dic['BraidStopMessage1'] = "No Tube"
                                elif(dic['BraidStop1_1'] == '16'):
                                        dic['BraidStopMessage1'] = "No Braider Wire"
                                elif(dic['BraidStop1_1'] == '17'):
                                        dic['BraidStopMessage1'] = "Break Down"
                                elif(dic['BraidStop1_1'] == '18'):
                                        dic['BraidStopMessage1'] = "PM"
                                elif(dic['BraidStop1_1'] == '19'):
                                        dic['BraidStopMessage1'] = "No Plan"
                                elif(dic['BraidStop1_1'] == '20'):
                                        dic['BraidStopMessage1'] = "Setting Time"

                                if(findBool(dic['BraidStop1_2']) == True):
                                        sql = "INSERT INTO braidstoppage1 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid1_1'], dic['Braid1_2'], int(dic['BraidStop1_1']), dic['BraidStopMessage1'], findBool(dic['BraidStop1_2']))
                                        mycursor.execute(sql, val)

                                else:
                                        sql = "INSERT INTO braidstoppage1 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid1_1'], dic['Braid1_2'], globalBS.tempBraidStopID1, dic['BraidStopMessage1'], findBool(dic['BraidStop1_2']))
                                        mycursor.execute(sql, val)


                        if(globalBS.tempBraidStop2 != findBool(dic['BraidStop2_2'])):
                                globalBS.tempBraidStop2 = findBool(dic['BraidStop2_2'])
                                if(findBool(dic['BraidStop2_2']) == True):
                                        globalBS.tempBraidStopID2 = int(dic['BraidStop2_1'])
                                if(dic['BraidStop2_1'] == '1'):
                                        dic['BraidStopMessage2'] = "Carrier Problem"
                                elif(dic['BraidStop2_1'] == '2'):
                                        dic['BraidStopMessage2'] = "Joint Bobbin"
                                elif(dic['BraidStop2_1'] == '3'):
                                        dic['BraidStopMessage2'] = "Liner Cut"
                                elif(dic['BraidStop2_1'] == '4'):
                                        dic['BraidStopMessage2'] = "Mandrel Broken"
                                elif(dic['BraidStop2_1'] == '5'):
                                        dic['BraidStopMessage2'] = "Pitch Problem"
                                elif(dic['BraidStop2_1'] == '6'):
                                        dic['BraidStopMessage2'] = "Ply Cut Joint"
                                elif(dic['BraidStop2_1'] == '7'):
                                        dic['BraidStopMessage2'] = "Power Cut"
                                elif(dic['BraidStop2_1'] == '8'):
                                        dic['BraidStopMessage2'] = "Push Back"
                                elif(dic['BraidStop2_1'] == '9'):
                                        dic['BraidStopMessage2'] = "Setting Joint"
                                elif(dic['BraidStop2_1'] == '10'):
                                        dic['BraidStopMessage2'] = "Tube Joint"
                                elif(dic['BraidStop2_1'] == '11'):
                                        dic['BraidStopMessage2'] = "Wire Break"
                                elif(dic['BraidStop2_1'] == '12'):
                                        dic['BraidStopMessage2'] = "Wire Loose"
                                elif(dic['BraidStop2_1'] == '13'):
                                        dic['BraidStopMessage2'] = "Over Heating"
                                elif(dic['BraidStop2_1'] == '14'):
                                        dic['BraidStopMessage2'] = "M/C Stop"
                                elif(dic['BraidStop2_1'] == '15'):
                                        dic['BraidStopMessage2'] = "No Tube"
                                elif(dic['BraidStop2_1'] == '16'):
                                        dic['BraidStopMessage2'] = "No Braider Wire"
                                elif(dic['BraidStop2_1'] == '17'):
                                        dic['BraidStopMessage2'] = "Break Down"
                                elif(dic['BraidStop2_1'] == '18'):
                                        dic['BraidStopMessage2'] = "PM"
                                elif(dic['BraidStop2_1'] == '19'):
                                        dic['BraidStopMessage2'] = "No Plan"
                                elif(dic['BraidStop2_1'] == '20'):
                                        dic['BraidStopMessage2'] = "Setting Time"

                                if(findBool(dic['BraidStop2_2']) == True):
                                        sql = "INSERT INTO braidstoppage2 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid2_1'], dic['Braid2_2'], int(dic['BraidStop2_1']), dic['BraidStopMessage2'], findBool(dic['BraidStop2_2']))
                                        mycursor.execute(sql, val)

                                else:
                                        sql = "INSERT INTO braidstoppage2 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid2_1'], dic['Braid2_2'], globalBS.tempBraidStopID2, dic['BraidStopMessage2'], findBool(dic['BraidStop2_2']))
                                        mycursor.execute(sql, val)



                        if(globalBS.tempBraidStop3 != findBool(dic['BraidStop3_2'])):
                                globalBS.tempBraidStop3 = findBool(dic['BraidStop3_2'])
                                if(findBool(dic['BraidStop3_2']) == True):
                                        globalBS.tempBraidStopID3 = int(dic['BraidStop3_1'])
                                if(dic['BraidStop3_1'] == '1'):
                                        dic['BraidStopMessage3'] = "Carrier Problem"
                                elif(dic['BraidStop3_1'] == '2'):
                                        dic['BraidStopMessage3'] = "Joint Bobbin"
                                elif(dic['BraidStop3_1'] == '3'):
                                        dic['BraidStopMessage3'] = "Liner Cut"
                                elif(dic['BraidStop3_1'] == '4'):
                                        dic['BraidStopMessage3'] = "Mandrel Broken"
                                elif(dic['BraidStop3_1'] == '5'):
                                        dic['BraidStopMessage3'] = "Pitch Problem"
                                elif(dic['BraidStop3_1'] == '6'):
                                        dic['BraidStopMessage3'] = "Ply Cut Joint"
                                elif(dic['BraidStop3_1'] == '7'):
                                        dic['BraidStopMessage3'] = "Power Cut"
                                elif(dic['BraidStop3_1'] == '8'):
                                        dic['BraidStopMessage3'] = "Push Back"
                                elif(dic['BraidStop3_1'] == '9'):
                                        dic['BraidStopMessage3'] = "Setting Joint"
                                elif(dic['BraidStop3_1'] == '10'):
                                        dic['BraidStopMessage3'] = "Tube Joint"
                                elif(dic['BraidStop3_1'] == '11'):
                                        dic['BraidStopMessage3'] = "Wire Break"
                                elif(dic['BraidStop3_1'] == '12'):
                                        dic['BraidStopMessage3'] = "Wire Loose"
                                elif(dic['BraidStop3_1'] == '13'):
                                        dic['BraidStopMessage3'] = "Over Heating"
                                elif(dic['BraidStop3_1'] == '14'):
                                        dic['BraidStopMessage3'] = "M/C Stop"
                                elif(dic['BraidStop3_1'] == '15'):
                                        dic['BraidStopMessage3'] = "No Tube"
                                elif(dic['BraidStop3_1'] == '16'):
                                        dic['BraidStopMessage3'] = "No Braider Wire"
                                elif(dic['BraidStop3_1'] == '17'):
                                        dic['BraidStopMessage3'] = "Break Down"
                                elif(dic['BraidStop3_1'] == '18'):
                                        dic['BraidStopMessage3'] = "PM"
                                elif(dic['BraidStop3_1'] == '19'):
                                        dic['BraidStopMessage3'] = "No Plan"
                                elif(dic['BraidStop3_1'] == '20'):
                                        dic['BraidStopMessage3'] = "Setting Time"

                                if(findBool(dic['BraidStop3_2']) == True):
                                        sql = "INSERT INTO braidstoppage3 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid3_1'], dic['Braid3_2'], int(dic['BraidStop3_1']), dic['BraidStopMessage3'], findBool(dic['BraidStop3_2']))
                                        mycursor.execute(sql, val)

                                else:
                                        sql = "INSERT INTO braidstoppage3 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid3_1'], dic['Braid3_2'], globalBS.tempBraidStopID3, dic['BraidStopMessage3'], findBool(dic['BraidStop3_2']))
                                        mycursor.execute(sql, val)


                        if(globalBS.tempBraidStop4 != findBool(dic['BraidStop4_2'])):
                                globalBS.tempBraidStop4 = findBool(dic['BraidStop4_2'])
                                if(findBool(dic['BraidStop4_2']) == True):
                                        globalBS.tempBraidStopID4 = int(dic['BraidStop4_1'])
                                if(dic['BraidStop4_1'] == '1'):
                                        dic['BraidStopMessage4'] = "Carrier Problem"
                                elif(dic['BraidStop4_1'] == '2'):
                                        dic['BraidStopMessage4'] = "Joint Bobbin"
                                elif(dic['BraidStop4_1'] == '3'):
                                        dic['BraidStopMessage4'] = "Liner Cut"
                                elif(dic['BraidStop4_1'] == '4'):
                                        dic['BraidStopMessage4'] = "Mandrel Broken"
                                elif(dic['BraidStop4_1'] == '5'):
                                        dic['BraidStopMessage4'] = "Pitch Problem"
                                elif(dic['BraidStop4_1'] == '6'):
                                        dic['BraidStopMessage4'] = "Ply Cut Joint"
                                elif(dic['BraidStop4_1'] == '7'):
                                        dic['BraidStopMessage4'] = "Power Cut"
                                elif(dic['BraidStop4_1'] == '8'):
                                        dic['BraidStopMessage4'] = "Push Back"
                                elif(dic['BraidStop4_1'] == '9'):
                                        dic['BraidStopMessage4'] = "Setting Joint"
                                elif(dic['BraidStop4_1'] == '10'):
                                        dic['BraidStopMessage4'] = "Tube Joint"
                                elif(dic['BraidStop4_1'] == '11'):
                                        dic['BraidStopMessage4'] = "Wire Break"
                                elif(dic['BraidStop4_1'] == '12'):
                                        dic['BraidStopMessage4'] = "Wire Loose"
                                elif(dic['BraidStop4_1'] == '13'):
                                        dic['BraidStopMessage4'] = "Over Heating"
                                elif(dic['BraidStop4_1'] == '14'):
                                        dic['BraidStopMessage4'] = "M/C Stop"
                                elif(dic['BraidStop4_1'] == '15'):
                                        dic['BraidStopMessage4'] = "No Tube"
                                elif(dic['BraidStop4_1'] == '16'):
                                        dic['BraidStopMessage4'] = "No Braider Wire"
                                elif(dic['BraidStop4_1'] == '17'):
                                        dic['BraidStopMessage4'] = "Break Down"
                                elif(dic['BraidStop4_1'] == '18'):
                                        dic['BraidStopMessage4'] = "PM"
                                elif(dic['BraidStop4_1'] == '19'):
                                        dic['BraidStopMessage4'] = "No Plan"
                                elif(dic['BraidStop4_1'] == '20'):
                                        dic['BraidStopMessage4'] = "Setting Time"

                                if(findBool(dic['BraidStop4_2']) == True):
                                        sql = "INSERT INTO braidstoppage4 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid4_1'], dic['Braid4_2'], int(dic['BraidStop4_1']), dic['BraidStopMessage4'], findBool(dic['BraidStop4_2']))
                                        mycursor.execute(sql, val)

                                else:
                                        sql = "INSERT INTO braidstoppage4 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid4_1'], dic['Braid4_2'], globalBS.tempBraidStopID4, dic['BraidStopMessage4'], findBool(dic['BraidStop4_2']))
                                        mycursor.execute(sql, val)


                        if(globalBS.tempBraidStop5 != findBool(dic['BraidStop5_2'])):
                                globalBS.tempBraidStop5 = findBool(dic['BraidStop5_2'])
                                if(findBool(dic['BraidStop5_2']) == True):
                                        globalBS.tempBraidStopID5 = int(dic['BraidStop5_1'])
                                if(dic['BraidStop5_1'] == '1'):
                                        dic['BraidStopMessage5'] = "Carrier Problem"
                                elif(dic['BraidStop5_1'] == '2'):
                                        dic['BraidStopMessage5'] = "Joint Bobbin"
                                elif(dic['BraidStop5_1'] == '3'):
                                        dic['BraidStopMessage5'] = "Liner Cut"
                                elif(dic['BraidStop5_1'] == '4'):
                                        dic['BraidStopMessage5'] = "Mandrel Broken"
                                elif(dic['BraidStop5_1'] == '5'):
                                        dic['BraidStopMessage5'] = "Pitch Problem"
                                elif(dic['BraidStop5_1'] == '6'):
                                        dic['BraidStopMessage5'] = "Ply Cut Joint"
                                elif(dic['BraidStop5_1'] == '7'):
                                        dic['BraidStopMessage5'] = "Power Cut"
                                elif(dic['BraidStop5_1'] == '8'):
                                        dic['BraidStopMessage5'] = "Push Back"
                                elif(dic['BraidStop5_1'] == '9'):
                                        dic['BraidStopMessage5'] = "Setting Joint"
                                elif(dic['BraidStop5_1'] == '10'):
                                        dic['BraidStopMessage5'] = "Tube Joint"
                                elif(dic['BraidStop5_1'] == '11'):
                                        dic['BraidStopMessage5'] = "Wire Break"
                                elif(dic['BraidStop5_1'] == '12'):
                                        dic['BraidStopMessage5'] = "Wire Loose"
                                elif(dic['BraidStop5_1'] == '13'):
                                        dic['BraidStopMessage5'] = "Over Heating"
                                elif(dic['BraidStop5_1'] == '14'):
                                        dic['BraidStopMessage5'] = "M/C Stop"
                                elif(dic['BraidStop5_1'] == '15'):
                                        dic['BraidStopMessage5'] = "No Tube"
                                elif(dic['BraidStop5_1'] == '16'):
                                        dic['BraidStopMessage5'] = "No Braider Wire"
                                elif(dic['BraidStop5_1'] == '17'):
                                        dic['BraidStopMessage5'] = "Break Down"
                                elif(dic['BraidStop5_1'] == '18'):
                                        dic['BraidStopMessage5'] = "PM"
                                elif(dic['BraidStop5_1'] == '19'):
                                        dic['BraidStopMessage5'] = "No Plan"
                                elif(dic['BraidStop5_1'] == '20'):
                                        dic['BraidStopMessage5'] = "Setting Time"

                                if(findBool(dic['BraidStop5_2']) == True):
                                        sql = "INSERT INTO braidstoppage5 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid5_1'], dic['Braid5_2'], int(dic['BraidStop5_1']), dic['BraidStopMessage5'], findBool(dic['BraidStop5_2']))
                                        mycursor.execute(sql, val)

                                else:
                                        sql = "INSERT INTO braidstoppage5 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid5_1'], dic['Braid5_2'], globalBS.tempBraidStopID5, dic['BraidStopMessage5'], findBool(dic['BraidStop5_2']))
                                        mycursor.execute(sql, val)



                        if(globalBS.tempBraidStop6 != findBool(dic['BraidStop6_2'])):
                                globalBS.tempBraidStop6 = findBool(dic['BraidStop6_2'])
                                if(findBool(dic['BraidStop6_2']) == True):
                                        globalBS.tempBraidStopID6 = int(dic['BraidStop6_1'])
                                if(dic['BraidStop6_1'] == '1'):
                                        dic['BraidStopMessage6'] = "Carrier Problem"
                                elif(dic['BraidStop6_1'] == '2'):
                                        dic['BraidStopMessage6'] = "Joint Bobbin"
                                elif(dic['BraidStop6_1'] == '3'):
                                        dic['BraidStopMessage6'] = "Liner Cut"
                                elif(dic['BraidStop6_1'] == '4'):
                                        dic['BraidStopMessage6'] = "Mandrel Broken"
                                elif(dic['BraidStop6_1'] == '5'):
                                        dic['BraidStopMessage6'] = "Pitch Problem"
                                elif(dic['BraidStop6_1'] == '6'):
                                        dic['BraidStopMessage6'] = "Ply Cut Joint"
                                elif(dic['BraidStop6_1'] == '7'):
                                        dic['BraidStopMessage6'] = "Power Cut"
                                elif(dic['BraidStop6_1'] == '8'):
                                        dic['BraidStopMessage6'] = "Push Back"
                                elif(dic['BraidStop6_1'] == '9'):
                                        dic['BraidStopMessage6'] = "Setting Joint"
                                elif(dic['BraidStop6_1'] == '10'):
                                        dic['BraidStopMessage6'] = "Tube Joint"
                                elif(dic['BraidStop6_1'] == '11'):
                                        dic['BraidStopMessage6'] = "Wire Break"
                                elif(dic['BraidStop6_1'] == '12'):
                                        dic['BraidStopMessage6'] = "Wire Loose"
                                elif(dic['BraidStop6_1'] == '13'):
                                        dic['BraidStopMessage6'] = "Over Heating"
                                elif(dic['BraidStop6_1'] == '14'):
                                        dic['BraidStopMessage6'] = "M/C Stop"
                                elif(dic['BraidStop6_1'] == '15'):
                                        dic['BraidStopMessage6'] = "No Tube"
                                elif(dic['BraidStop6_1'] == '16'):
                                        dic['BraidStopMessage6'] = "No Braider Wire"
                                elif(dic['BraidStop6_1'] == '17'):
                                        dic['BraidStopMessage6'] = "Break Down"
                                elif(dic['BraidStop6_1'] == '18'):
                                        dic['BraidStopMessage6'] = "PM"
                                elif(dic['BraidStop6_1'] == '19'):
                                        dic['BraidStopMessage6'] = "No Plan"
                                elif(dic['BraidStop6_1'] == '20'):
                                        dic['BraidStopMessage6'] = "Setting Time"

                                if(findBool(dic['BraidStop6_2']) == True):
                                        sql = "INSERT INTO braidstoppage6 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid6_1'], dic['Braid6_2'], int(dic['BraidStop6_1']), dic['BraidStopMessage6'], findBool(dic['BraidStop6_2']))
                                        mycursor.execute(sql, val)

                                else:
                                        sql = "INSERT INTO braidstoppage6 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid6_1'], dic['Braid6_2'], globalBS.tempBraidStopID6, dic['BraidStopMessage6'], findBool(dic['BraidStop6_2']))
                                        mycursor.execute(sql, val)



                        if(globalBS.tempBraidStop7 != findBool(dic['BraidStop7_2'])):
                                globalBS.tempBraidStop7 = findBool(dic['BraidStop7_2'])
                                if(findBool(dic['BraidStop7_2']) == True):
                                        globalBS.tempBraidStopID7 = int(dic['BraidStop7_1'])
                                if(dic['BraidStop7_1'] == '1'):
                                        dic['BraidStopMessage7'] = "Carrier Problem"
                                elif(dic['BraidStop7_1'] == '2'):
                                        dic['BraidStopMessage7'] = "Joint Bobbin"
                                elif(dic['BraidStop7_1'] == '3'):
                                        dic['BraidStopMessage7'] = "Liner Cut"
                                elif(dic['BraidStop7_1'] == '4'):
                                        dic['BraidStopMessage7'] = "Mandrel Broken"
                                elif(dic['BraidStop7_1'] == '5'):
                                        dic['BraidStopMessage7'] = "Pitch Problem"
                                elif(dic['BraidStop7_1'] == '6'):
                                        dic['BraidStopMessage7'] = "Ply Cut Joint"
                                elif(dic['BraidStop7_1'] == '7'):
                                        dic['BraidStopMessage7'] = "Power Cut"
                                elif(dic['BraidStop7_1'] == '8'):
                                        dic['BraidStopMessage7'] = "Push Back"
                                elif(dic['BraidStop7_1'] == '9'):
                                        dic['BraidStopMessage7'] = "Setting Joint"
                                elif(dic['BraidStop7_1'] == '10'):
                                        dic['BraidStopMessage7'] = "Tube Joint"
                                elif(dic['BraidStop7_1'] == '11'):
                                        dic['BraidStopMessage7'] = "Wire Break"
                                elif(dic['BraidStop7_1'] == '12'):
                                        dic['BraidStopMessage7'] = "Wire Loose"
                                elif(dic['BraidStop7_1'] == '13'):
                                        dic['BraidStopMessage7'] = "Over Heating"
                                elif(dic['BraidStop7_1'] == '14'):
                                        dic['BraidStopMessage7'] = "M/C Stop"
                                elif(dic['BraidStop7_1'] == '15'):
                                        dic['BraidStopMessage7'] = "No Tube"
                                elif(dic['BraidStop7_1'] == '16'):
                                        dic['BraidStopMessage7'] = "No Braider Wire"
                                elif(dic['BraidStop7_1'] == '17'):
                                        dic['BraidStopMessage7'] = "Break Down"
                                elif(dic['BraidStop7_1'] == '18'):
                                        dic['BraidStopMessage7'] = "PM"
                                elif(dic['BraidStop7_1'] == '19'):
                                        dic['BraidStopMessage7'] = "No Plan"
                                elif(dic['BraidStop7_1'] == '20'):
                                        dic['BraidStopMessage7'] = "Setting Time"

                                if(findBool(dic['BraidStop7_2']) == True):
                                        sql = "INSERT INTO braidstoppage7 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid7_1'], dic['Braid7_2'], int(dic['BraidStop7_1']), dic['BraidStopMessage7'], findBool(dic['BraidStop7_2']))
                                        mycursor.execute(sql, val)

                                else:
                                        sql = "INSERT INTO braidstoppage7 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid7_1'], dic['Braid7_2'], globalBS.tempBraidStopID7, dic['BraidStopMessage7'], findBool(dic['BraidStop7_2']))
                                        mycursor.execute(sql, val)



                        if(globalBS.tempBraidStop8 != findBool(dic['BraidStop8_2'])):
                                globalBS.tempBraidStop8 = findBool(dic['BraidStop8_2'])
                                if(findBool(dic['BraidStop8_2']) == True):
                                        globalBS.tempBraidStopID8 = int(dic['BraidStop8_1'])
                                if(dic['BraidStop8_1'] == '1'):
                                        dic['BraidStopMessage8'] = "Carrier Problem"
                                elif(dic['BraidStop8_1'] == '2'):
                                        dic['BraidStopMessage8'] = "Joint Bobbin"
                                elif(dic['BraidStop8_1'] == '3'):
                                        dic['BraidStopMessage8'] = "Liner Cut"
                                elif(dic['BraidStop8_1'] == '4'):
                                        dic['BraidStopMessage8'] = "Mandrel Broken"
                                elif(dic['BraidStop8_1'] == '5'):
                                        dic['BraidStopMessage8'] = "Pitch Problem"
                                elif(dic['BraidStop8_1'] == '6'):
                                        dic['BraidStopMessage8'] = "Ply Cut Joint"
                                elif(dic['BraidStop8_1'] == '7'):
                                        dic['BraidStopMessage8'] = "Power Cut"
                                elif(dic['BraidStop8_1'] == '8'):
                                        dic['BraidStopMessage8'] = "Push Back"
                                elif(dic['BraidStop8_1'] == '9'):
                                        dic['BraidStopMessage8'] = "Setting Joint"
                                elif(dic['BraidStop8_1'] == '10'):
                                        dic['BraidStopMessage8'] = "Tube Joint"
                                elif(dic['BraidStop8_1'] == '11'):
                                        dic['BraidStopMessage8'] = "Wire Break"
                                elif(dic['BraidStop8_1'] == '12'):
                                        dic['BraidStopMessage8'] = "Wire Loose"
                                elif(dic['BraidStop8_1'] == '13'):
                                        dic['BraidStopMessage8'] = "Over Heating"
                                elif(dic['BraidStop8_1'] == '14'):
                                        dic['BraidStopMessage8'] = "M/C Stop"
                                elif(dic['BraidStop8_1'] == '15'):
                                        dic['BraidStopMessage8'] = "No Tube"
                                elif(dic['BraidStop8_1'] == '16'):
                                        dic['BraidStopMessage8'] = "No Braider Wire"
                                elif(dic['BraidStop8_1'] == '17'):
                                        dic['BraidStopMessage8'] = "Break Down"
                                elif(dic['BraidStop8_1'] == '18'):
                                        dic['BraidStopMessage8'] = "PM"
                                elif(dic['BraidStop8_1'] == '19'):
                                        dic['BraidStopMessage8'] = "No Plan"
                                elif(dic['BraidStop8_1'] == '20'):
                                        dic['BraidStopMessage8'] = "Setting Time"

                                if(findBool(dic['BraidStop8_2']) == True):
                                        sql = "INSERT INTO braidstoppage8 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid8_1'], dic['Braid8_2'], int(dic['BraidStop8_1']), dic['BraidStopMessage8'], findBool(dic['BraidStop8_2']))
                                        mycursor.execute(sql, val)

                                else:
                                        sql = "INSERT INTO braidstoppage8 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                        val = (dic['Braid8_1'], dic['Braid8_2'], globalBS.tempBraidStopID8, dic['BraidStopMessage8'], findBool(dic['BraidStop8_2']))
                                        mycursor.execute(sql, val)
                                        

            if(count1 >= 60):
                count1 = 0
                #updateLang('english')
                print("Thread1: Data Processing")
                json_data = str(message.payload.decode("utf-8","ignore"))
                if(is_valid_json(json_data)):
                        
                        json_obj = json.loads(json_data)
                        if(findBool(json_obj['connected'])):
                            #dic['tags'] = json_obj.tags
                            dic['Braid1_1'] = fixedInt(json_obj['M-B_R_1-0']) #PIR
                            dic['Braid1_2'] = fixedInt(json_obj['M-B_R_1-1']) #operator name
                            dic['Braid1_3'] = fixedInt(json_obj['M-B_R_1-2']) #deck set speed
                            dic['Braid1_4'] = fixedInt(json_obj['M-B_R_1-3']) #deck act speed
                            dic['Braid1_5'] = fixedInt(json_obj['M-B_R_1-4']) #production meter
                            dic['Braid1_6'] = fixedInt(json_obj['M-B_R_1-5']) #total running hrs
                            dic['Braid1_7'] = fixedInt(json_obj['M-B_R_1-6']) #blower ser temperature 
                            dic['Braid1_8'] = fixedInt(json_obj['M-B_R_1-7']) #blower act temperature
                            dic['Braid1_9'] = fixedInt(json_obj['M-B_R_1-8']) #N2 set temperature
                            dic['Braid1_10'] = fixedInt(json_obj['M-B_R_1-9']) #N2 inlet temperature
                            dic['Braid1_11'] = fixedInt(json_obj['M-B_R_1-10']) #N2 outlet temperature
                            dic['Braid1_12'] = fixedInt(json_obj['M-B_R_1-11']) #N2 pressure


                            dic['Braid1_13'] = fixedInt(json_obj['M-B_H_1-21']) #Tube Dia
                            dic['Braid1_14'] = fixedInt(json_obj['M-B_H_1-22']) #No. of ends
                            dic['Braid1_15'] = fixedInt(json_obj['M-B_H_1-23']) #Wire Dia
                            dic['Braid1_16'] = fixedInt(json_obj['M-B_H_1-7']) #Tag Date
                            dic['Braid1_17'] = fixedInt(json_obj['M-B_H_1-8']) #Deck Gear 1
                            dic['Braid1_18'] = fixedInt(json_obj['M-B_H_1-9']) #Deck Gear 2
                            dic['Braid1_19'] = fixedInt(json_obj['M-B_H_1-10']) #Haul Gear 1
                            dic['Braid1_20'] = fixedInt(json_obj['M-B_H_1-11']) #Haul Gear 2
                            dic['Braid1_21'] = fixedInt(json_obj['M-B_H_1-12']) #Drum in
                            dic['Braid1_22'] = fixedInt(json_obj['M-B_H_1-13']) #Drum out
                            dic['Braid1_23'] = fixedInt(json_obj['M-B_H_1-14']) #Insulation
                            dic['Braid1_24'] = fixedInt(json_obj['M-B_H_1-15']) #Batch No
                            dic['Braid1_25'] = fixedInt(json_obj['M-B_H_1-17']) #Ply Thickness setvalue
                            dic['Braid1_26'] = fixedInt(json_obj['M-B_H_1-18']) #Ply Thickness actvalue
                            dic['Braid1_27'] = fixedInt(json_obj['M-B_H_1-19']) #Ply Width set value
                            dic['Braid1_28'] = fixedInt(json_obj['M-B_H_1-20']) #Ply Width act value
                            dic['Braid1_29'] = fixedInt(json_obj['M-B_H_1-16']) #Machine number
                            dic['Braid1_30'] = fixedInt(json_obj['M-B_H_1-24']) #Rein OD spec 1
                            dic['Braid1_31'] = fixedInt(json_obj['M-B_H_1-25']) #Rein Pitch Spec 1
                            dic['Braid1_32'] = fixedInt(json_obj['M-B_H_1-26']) #Rein OD spec 2
                            dic['Braid1_33'] = fixedInt(json_obj['M-B_H_1-27']) #Rein Pitch Spec 2
                            dic['Braid1_34'] = fixedInt(json_obj['M-B_H_1-28']) #Rein OD spec 3
                            dic['Braid1_35'] = fixedInt(json_obj['M-B_H_1-29']) #Rein Pitch Spec 3
                            dic['Braid1_36'] = fixedInt(json_obj['M-B_H_1-30']) #Rein OD fact 1
                            dic['Braid1_37'] = fixedInt(json_obj['M-B_H_1-31']) #Rein OD mact 1
                            dic['Braid1_38'] = fixedInt(json_obj['M-B_H_1-32']) #Rein OD lact 1
                            dic['Braid1_39'] = fixedInt(json_obj['M-B_H_1-33']) #Rein Pitch fact 1
                            dic['Braid1_40'] = fixedInt(json_obj['M-B_H_1-34']) #Rein Pitch mact 1
                            dic['Braid1_41'] = fixedInt(json_obj['M-B_H_1-35']) #Rein Pitch lact 1
                            dic['Braid1_42'] = fixedInt(json_obj['M-B_H_1-36']) #Rein OD fact 2
                            dic['Braid1_43'] = fixedInt(json_obj['M-B_H_1-37']) #Rein OD mact 2
                            dic['Braid1_44'] = fixedInt(json_obj['M-B_H_1-38']) #Rein OD lact 2
                            dic['Braid1_45'] = fixedInt(json_obj['M-B_H_1-39']) #Rein Pitch fact 2
                            dic['Braid1_46'] = fixedInt(json_obj['M-B_H_1-40']) #Rein Pitch mact 2
                            dic['Braid1_47'] = fixedInt(json_obj['M-B_H_1-41']) #Rein Pitch lact 2
                            dic['Braid1_48'] = fixedInt(json_obj['M-B_H_1-42']) #Rein OD fact 3
                            dic['Braid1_49'] = fixedInt(json_obj['M-B_H_1-43']) #Rein OD mact 3
                            dic['Braid1_50'] = fixedInt(json_obj['M-B_H_1-44']) #Rein OD lact 3
                            dic['Braid1_51'] = fixedInt(json_obj['M-B_H_1-45']) #Rein Pitch fact 3
                            dic['Braid1_52'] = fixedInt(json_obj['M-B_H_1-46']) #Rein Pitch mact 3
                            dic['Braid1_53'] = fixedInt(json_obj['M-B_H_1-47']) #Rein Pitch lact 3
                            dic['Braid1_54'] = fixedInt(json_obj['M-B_H_1-48']) #Rein OD spec tol 1
                            dic['Braid1_55'] = fixedInt(json_obj['M-B_H_1-49']) #Rein Pitch spec tol 1
                            dic['Braid1_56'] = fixedInt(json_obj['M-B_H_1-50']) #Rein OD spec tol 2
                            dic['Braid1_57'] = fixedInt(json_obj['M-B_H_1-51']) #Rein Pitch spec tol 2
                            dic['Braid1_58'] = fixedInt(json_obj['M-B_H_1-52']) #Rein OD spec tol 3
                            dic['Braid1_59'] = fixedInt(json_obj['M-B_H_1-53']) #Rein Pitch spec tol 3
                            dic['Braid1_60'] = fixedInt(json_obj['M-B_H_1-54']) #Operator ID
                            dic['Braid1_61'] = fixedInt(json_obj['M-B_H_1-55']) #Supervisor
                            dic['Braid1_62'] = fixedInt(json_obj['M-B_H_1-56']) #QA Approval

                            
                            dic['Braid2_13'] = fixedInt(json_obj['M-B_H_2-21']) #Tube Dia
                            dic['Braid2_14'] = fixedInt(json_obj['M-B_H_2-22']) #No. of ends
                            dic['Braid2_15'] = fixedInt(json_obj['M-B_H_2-23']) #Wire Dia
                            dic['Braid2_16'] = fixedInt(json_obj['M-B_H_2-7']) #Tag Date
                            dic['Braid2_17'] = fixedInt(json_obj['M-B_H_2-8']) #Deck Gear 1
                            dic['Braid2_18'] = fixedInt(json_obj['M-B_H_2-9']) #Deck Gear 2
                            dic['Braid2_19'] = fixedInt(json_obj['M-B_H_2-10']) #Haul Gear 1
                            dic['Braid2_20'] = fixedInt(json_obj['M-B_H_2-11']) #Haul Gear 2
                            dic['Braid2_21'] = fixedInt(json_obj['M-B_H_2-12']) #Drum in
                            dic['Braid2_22'] = fixedInt(json_obj['M-B_H_2-13']) #Drum out
                            dic['Braid2_23'] = fixedInt(json_obj['M-B_H_2-14']) #Insulation
                            dic['Braid2_24'] = fixedInt(json_obj['M-B_H_2-15']) #Batch No
                            dic['Braid2_25'] = fixedInt(json_obj['M-B_H_2-17']) #Ply Thickness setvalue
                            dic['Braid2_26'] = fixedInt(json_obj['M-B_H_2-18']) #Ply Thickness actvalue
                            dic['Braid2_27'] = fixedInt(json_obj['M-B_H_2-19']) #Ply Width set value
                            dic['Braid2_28'] = fixedInt(json_obj['M-B_H_2-20']) #Ply Width act value
                            dic['Braid2_29'] = fixedInt(json_obj['M-B_H_2-16']) #Machine number
                            dic['Braid2_30'] = fixedInt(json_obj['M-B_H_2-24']) #Rein OD spec 1
                            dic['Braid2_31'] = fixedInt(json_obj['M-B_H_2-25']) #Rein Pitch Spec 1
                            dic['Braid2_32'] = fixedInt(json_obj['M-B_H_2-26']) #Rein OD spec 2
                            dic['Braid2_33'] = fixedInt(json_obj['M-B_H_2-27']) #Rein Pitch Spec 2
                            dic['Braid2_34'] = fixedInt(json_obj['M-B_H_2-28']) #Rein OD spec 3
                            dic['Braid2_35'] = fixedInt(json_obj['M-B_H_2-29']) #Rein Pitch Spec 3
                            dic['Braid2_36'] = fixedInt(json_obj['M-B_H_2-30']) #Rein OD fact 1
                            dic['Braid2_37'] = fixedInt(json_obj['M-B_H_2-31']) #Rein OD mact 1
                            dic['Braid2_38'] = fixedInt(json_obj['M-B_H_2-32']) #Rein OD lact 1
                            dic['Braid2_39'] = fixedInt(json_obj['M-B_H_2-33']) #Rein Pitch fact 1
                            dic['Braid2_40'] = fixedInt(json_obj['M-B_H_2-34']) #Rein Pitch mact 1
                            dic['Braid2_41'] = fixedInt(json_obj['M-B_H_2-35']) #Rein Pitch lact 1
                            dic['Braid2_42'] = fixedInt(json_obj['M-B_H_2-36']) #Rein OD fact 2
                            dic['Braid2_43'] = fixedInt(json_obj['M-B_H_2-37']) #Rein OD mact 2
                            dic['Braid2_44'] = fixedInt(json_obj['M-B_H_2-38']) #Rein OD lact 2
                            dic['Braid2_45'] = fixedInt(json_obj['M-B_H_2-39']) #Rein Pitch fact 2
                            dic['Braid2_46'] = fixedInt(json_obj['M-B_H_2-40']) #Rein Pitch mact 2
                            dic['Braid2_47'] = fixedInt(json_obj['M-B_H_2-41']) #Rein Pitch lact 2
                            dic['Braid2_48'] = fixedInt(json_obj['M-B_H_2-42']) #Rein OD fact 3
                            dic['Braid2_49'] = fixedInt(json_obj['M-B_H_2-43']) #Rein OD mact 3
                            dic['Braid2_50'] = fixedInt(json_obj['M-B_H_2-44']) #Rein OD lact 3
                            dic['Braid2_51'] = fixedInt(json_obj['M-B_H_2-45']) #Rein Pitch fact 3
                            dic['Braid2_52'] = fixedInt(json_obj['M-B_H_2-46']) #Rein Pitch mact 3
                            dic['Braid2_53'] = fixedInt(json_obj['M-B_H_2-47']) #Rein Pitch lact 3
                            dic['Braid2_54'] = fixedInt(json_obj['M-B_H_2-48']) #Rein OD spec tol 1
                            dic['Braid2_55'] = fixedInt(json_obj['M-B_H_2-49']) #Rein Pitch spec tol 1
                            dic['Braid2_56'] = fixedInt(json_obj['M-B_H_2-50']) #Rein OD spec tol 2
                            dic['Braid2_57'] = fixedInt(json_obj['M-B_H_2-51']) #Rein Pitch spec tol 2
                            dic['Braid2_58'] = fixedInt(json_obj['M-B_H_2-52']) #Rein OD spec tol 3
                            dic['Braid2_59'] = fixedInt(json_obj['M-B_H_2-53']) #Rein Pitch spec tol 3
                            dic['Braid2_60'] = fixedInt(json_obj['M-B_H_2-54']) #Operator ID
                            dic['Braid2_61'] = fixedInt(json_obj['M-B_H_2-55']) #Supervisor
                            dic['Braid2_62'] = fixedInt(json_obj['M-B_H_2-56']) #QA Approval


                            
                            dic['Braid3_13'] = fixedInt(json_obj['M-B_H_3-21']) #Tube Dia
                            dic['Braid3_14'] = fixedInt(json_obj['M-B_H_3-22']) #No. of ends
                            dic['Braid3_15'] = fixedInt(json_obj['M-B_H_3-23']) #Wire Dia
                            dic['Braid3_16'] = fixedInt(json_obj['M-B_H_3-7']) #Tag Date
                            dic['Braid3_17'] = fixedInt(json_obj['M-B_H_3-8']) #Deck Gear 1
                            dic['Braid3_18'] = fixedInt(json_obj['M-B_H_3-9']) #Deck Gear 2
                            dic['Braid3_19'] = fixedInt(json_obj['M-B_H_3-10']) #Haul Gear 1
                            dic['Braid3_20'] = fixedInt(json_obj['M-B_H_3-11']) #Haul Gear 2
                            dic['Braid3_21'] = fixedInt(json_obj['M-B_H_3-12']) #Drum in
                            dic['Braid3_22'] = fixedInt(json_obj['M-B_H_3-13']) #Drum out
                            dic['Braid3_23'] = fixedInt(json_obj['M-B_H_3-14']) #Insulation
                            dic['Braid3_24'] = fixedInt(json_obj['M-B_H_3-15']) #Batch No
                            dic['Braid3_25'] = fixedInt(json_obj['M-B_H_3-17']) #Ply Thickness setvalue
                            dic['Braid3_26'] = fixedInt(json_obj['M-B_H_3-18']) #Ply Thickness actvalue
                            dic['Braid3_27'] = fixedInt(json_obj['M-B_H_3-19']) #Ply Width set value
                            dic['Braid3_28'] = fixedInt(json_obj['M-B_H_3-20']) #Ply Width act value
                            dic['Braid3_29'] = fixedInt(json_obj['M-B_H_3-16']) #Machine number
                            dic['Braid3_30'] = fixedInt(json_obj['M-B_H_3-24']) #Rein OD spec 1
                            dic['Braid3_31'] = fixedInt(json_obj['M-B_H_3-25']) #Rein Pitch Spec 1
                            dic['Braid3_32'] = fixedInt(json_obj['M-B_H_3-26']) #Rein OD spec 2
                            dic['Braid3_33'] = fixedInt(json_obj['M-B_H_3-27']) #Rein Pitch Spec 2
                            dic['Braid3_34'] = fixedInt(json_obj['M-B_H_3-28']) #Rein OD spec 3
                            dic['Braid3_35'] = fixedInt(json_obj['M-B_H_3-29']) #Rein Pitch Spec 3
                            dic['Braid3_36'] = fixedInt(json_obj['M-B_H_3-30']) #Rein OD fact 1
                            dic['Braid3_37'] = fixedInt(json_obj['M-B_H_3-31']) #Rein OD mact 1
                            dic['Braid3_38'] = fixedInt(json_obj['M-B_H_3-32']) #Rein OD lact 1
                            dic['Braid3_39'] = fixedInt(json_obj['M-B_H_3-33']) #Rein Pitch fact 1
                            dic['Braid3_40'] = fixedInt(json_obj['M-B_H_3-34']) #Rein Pitch mact 1
                            dic['Braid3_41'] = fixedInt(json_obj['M-B_H_3-35']) #Rein Pitch lact 1
                            dic['Braid3_42'] = fixedInt(json_obj['M-B_H_3-36']) #Rein OD fact 2
                            dic['Braid3_43'] = fixedInt(json_obj['M-B_H_3-37']) #Rein OD mact 2
                            dic['Braid3_44'] = fixedInt(json_obj['M-B_H_3-38']) #Rein OD lact 2
                            dic['Braid3_45'] = fixedInt(json_obj['M-B_H_3-39']) #Rein Pitch fact 2
                            dic['Braid3_46'] = fixedInt(json_obj['M-B_H_3-40']) #Rein Pitch mact 2
                            dic['Braid3_47'] = fixedInt(json_obj['M-B_H_3-41']) #Rein Pitch lact 2
                            dic['Braid3_48'] = fixedInt(json_obj['M-B_H_3-42']) #Rein OD fact 3
                            dic['Braid3_49'] = fixedInt(json_obj['M-B_H_3-43']) #Rein OD mact 3
                            dic['Braid3_50'] = fixedInt(json_obj['M-B_H_3-44']) #Rein OD lact 3
                            dic['Braid3_51'] = fixedInt(json_obj['M-B_H_3-45']) #Rein Pitch fact 3
                            dic['Braid3_52'] = fixedInt(json_obj['M-B_H_3-46']) #Rein Pitch mact 3
                            dic['Braid3_53'] = fixedInt(json_obj['M-B_H_3-47']) #Rein Pitch lact 3
                            dic['Braid3_54'] = fixedInt(json_obj['M-B_H_3-48']) #Rein OD spec tol 1
                            dic['Braid3_55'] = fixedInt(json_obj['M-B_H_3-49']) #Rein Pitch spec tol 1
                            dic['Braid3_56'] = fixedInt(json_obj['M-B_H_3-50']) #Rein OD spec tol 2
                            dic['Braid3_57'] = fixedInt(json_obj['M-B_H_3-51']) #Rein Pitch spec tol 2
                            dic['Braid3_58'] = fixedInt(json_obj['M-B_H_3-52']) #Rein OD spec tol 3
                            dic['Braid3_59'] = fixedInt(json_obj['M-B_H_3-53']) #Rein Pitch spec tol 3
                            dic['Braid3_60'] = fixedInt(json_obj['M-B_H_3-54']) #Operator ID
                            dic['Braid3_61'] = fixedInt(json_obj['M-B_H_3-55']) #Supervisor
                            dic['Braid3_62'] = fixedInt(json_obj['M-B_H_3-56']) #QA Approval


                            
                            dic['Braid4_13'] = fixedInt(json_obj['M-B_H_4-21']) #Tube Dia
                            dic['Braid4_14'] = fixedInt(json_obj['M-B_H_4-22']) #No. of ends
                            dic['Braid4_15'] = fixedInt(json_obj['M-B_H_4-23']) #Wire Dia
                            dic['Braid4_16'] = fixedInt(json_obj['M-B_H_4-7']) #Tag Date
                            dic['Braid4_17'] = fixedInt(json_obj['M-B_H_4-8']) #Deck Gear 1
                            dic['Braid4_18'] = fixedInt(json_obj['M-B_H_4-9']) #Deck Gear 2
                            dic['Braid4_19'] = fixedInt(json_obj['M-B_H_4-10']) #Haul Gear 1
                            dic['Braid4_20'] = fixedInt(json_obj['M-B_H_4-11']) #Haul Gear 2
                            dic['Braid4_21'] = fixedInt(json_obj['M-B_H_4-12']) #Drum in
                            dic['Braid4_22'] = fixedInt(json_obj['M-B_H_4-13']) #Drum out
                            dic['Braid4_23'] = fixedInt(json_obj['M-B_H_4-14']) #Insulation
                            dic['Braid4_24'] = fixedInt(json_obj['M-B_H_4-15']) #Batch No
                            dic['Braid4_25'] = fixedInt(json_obj['M-B_H_4-17']) #Ply Thickness setvalue
                            dic['Braid4_26'] = fixedInt(json_obj['M-B_H_4-18']) #Ply Thickness actvalue
                            dic['Braid4_27'] = fixedInt(json_obj['M-B_H_4-19']) #Ply Width set value
                            dic['Braid4_28'] = fixedInt(json_obj['M-B_H_4-20']) #Ply Width act value
                            dic['Braid4_29'] = fixedInt(json_obj['M-B_H_4-16']) #Machine number
                            dic['Braid4_30'] = fixedInt(json_obj['M-B_H_4-24']) #Rein OD spec 1
                            dic['Braid4_31'] = fixedInt(json_obj['M-B_H_4-25']) #Rein Pitch Spec 1
                            dic['Braid4_32'] = fixedInt(json_obj['M-B_H_4-26']) #Rein OD spec 2
                            dic['Braid4_33'] = fixedInt(json_obj['M-B_H_4-27']) #Rein Pitch Spec 2
                            dic['Braid4_34'] = fixedInt(json_obj['M-B_H_4-28']) #Rein OD spec 3
                            dic['Braid4_35'] = fixedInt(json_obj['M-B_H_4-29']) #Rein Pitch Spec 3
                            dic['Braid4_36'] = fixedInt(json_obj['M-B_H_4-30']) #Rein OD fact 1
                            dic['Braid4_37'] = fixedInt(json_obj['M-B_H_4-31']) #Rein OD mact 1
                            dic['Braid4_38'] = fixedInt(json_obj['M-B_H_4-32']) #Rein OD lact 1
                            dic['Braid4_39'] = fixedInt(json_obj['M-B_H_4-33']) #Rein Pitch fact 1
                            dic['Braid4_40'] = fixedInt(json_obj['M-B_H_4-34']) #Rein Pitch mact 1
                            dic['Braid4_41'] = fixedInt(json_obj['M-B_H_4-35']) #Rein Pitch lact 1
                            dic['Braid4_42'] = fixedInt(json_obj['M-B_H_4-36']) #Rein OD fact 2
                            dic['Braid4_43'] = fixedInt(json_obj['M-B_H_4-37']) #Rein OD mact 2
                            dic['Braid4_44'] = fixedInt(json_obj['M-B_H_4-38']) #Rein OD lact 2
                            dic['Braid4_45'] = fixedInt(json_obj['M-B_H_4-39']) #Rein Pitch fact 2
                            dic['Braid4_46'] = fixedInt(json_obj['M-B_H_4-40']) #Rein Pitch mact 2
                            dic['Braid4_47'] = fixedInt(json_obj['M-B_H_4-41']) #Rein Pitch lact 2
                            dic['Braid4_48'] = fixedInt(json_obj['M-B_H_4-42']) #Rein OD fact 3
                            dic['Braid4_49'] = fixedInt(json_obj['M-B_H_4-43']) #Rein OD mact 3
                            dic['Braid4_50'] = fixedInt(json_obj['M-B_H_4-44']) #Rein OD lact 3
                            dic['Braid4_51'] = fixedInt(json_obj['M-B_H_4-45']) #Rein Pitch fact 3
                            dic['Braid4_52'] = fixedInt(json_obj['M-B_H_4-46']) #Rein Pitch mact 3
                            dic['Braid4_53'] = fixedInt(json_obj['M-B_H_4-47']) #Rein Pitch lact 3
                            dic['Braid4_54'] = fixedInt(json_obj['M-B_H_4-48']) #Rein OD spec tol 1
                            dic['Braid4_55'] = fixedInt(json_obj['M-B_H_4-49']) #Rein Pitch spec tol 1
                            dic['Braid4_56'] = fixedInt(json_obj['M-B_H_4-50']) #Rein OD spec tol 2
                            dic['Braid4_57'] = fixedInt(json_obj['M-B_H_4-51']) #Rein Pitch spec tol 2
                            dic['Braid4_58'] = fixedInt(json_obj['M-B_H_4-52']) #Rein OD spec tol 3
                            dic['Braid4_59'] = fixedInt(json_obj['M-B_H_4-53']) #Rein Pitch spec tol 3
                            dic['Braid4_60'] = fixedInt(json_obj['M-B_H_4-54']) #Operator ID
                            dic['Braid4_61'] = fixedInt(json_obj['M-B_H_4-55']) #Supervisor
                            dic['Braid4_62'] = fixedInt(json_obj['M-B_H_4-56']) #QA Approval

                            
                            dic['Braid5_13'] = fixedInt(json_obj['M-B_H_5-21']) #Tube Dia
                            dic['Braid5_14'] = fixedInt(json_obj['M-B_H_5-22']) #No. of ends
                            dic['Braid5_15'] = fixedInt(json_obj['M-B_H_5-23']) #Wire Dia
                            dic['Braid5_16'] = fixedInt(json_obj['M-B_H_5-7']) #Tag Date
                            dic['Braid5_17'] = fixedInt(json_obj['M-B_H_5-8']) #Deck Gear 1
                            dic['Braid5_18'] = fixedInt(json_obj['M-B_H_5-9']) #Deck Gear 2
                            dic['Braid5_19'] = fixedInt(json_obj['M-B_H_5-10']) #Haul Gear 1
                            dic['Braid5_20'] = fixedInt(json_obj['M-B_H_5-11']) #Haul Gear 2
                            dic['Braid5_21'] = fixedInt(json_obj['M-B_H_5-12']) #Drum in
                            dic['Braid5_22'] = fixedInt(json_obj['M-B_H_5-13']) #Drum out
                            dic['Braid5_23'] = fixedInt(json_obj['M-B_H_5-14']) #Insulation
                            dic['Braid5_24'] = fixedInt(json_obj['M-B_H_5-15']) #Batch No
                            dic['Braid5_25'] = fixedInt(json_obj['M-B_H_5-17']) #Ply Thickness setvalue
                            dic['Braid5_26'] = fixedInt(json_obj['M-B_H_5-18']) #Ply Thickness actvalue
                            dic['Braid5_27'] = fixedInt(json_obj['M-B_H_5-19']) #Ply Width set value
                            dic['Braid5_28'] = fixedInt(json_obj['M-B_H_5-20']) #Ply Width act value
                            dic['Braid5_29'] = fixedInt(json_obj['M-B_H_5-16']) #Machine number
                            dic['Braid5_30'] = fixedInt(json_obj['M-B_H_5-24']) #Rein OD spec 1
                            dic['Braid5_31'] = fixedInt(json_obj['M-B_H_5-25']) #Rein Pitch Spec 1
                            dic['Braid5_32'] = fixedInt(json_obj['M-B_H_5-26']) #Rein OD spec 2
                            dic['Braid5_33'] = fixedInt(json_obj['M-B_H_5-27']) #Rein Pitch Spec 2
                            dic['Braid5_34'] = fixedInt(json_obj['M-B_H_5-28']) #Rein OD spec 3
                            dic['Braid5_35'] = fixedInt(json_obj['M-B_H_5-29']) #Rein Pitch Spec 3
                            dic['Braid5_36'] = fixedInt(json_obj['M-B_H_5-30']) #Rein OD fact 1
                            dic['Braid5_37'] = fixedInt(json_obj['M-B_H_5-31']) #Rein OD mact 1
                            dic['Braid5_38'] = fixedInt(json_obj['M-B_H_5-32']) #Rein OD lact 1
                            dic['Braid5_39'] = fixedInt(json_obj['M-B_H_5-33']) #Rein Pitch fact 1
                            dic['Braid5_40'] = fixedInt(json_obj['M-B_H_5-34']) #Rein Pitch mact 1
                            dic['Braid5_41'] = fixedInt(json_obj['M-B_H_5-35']) #Rein Pitch lact 1
                            dic['Braid5_42'] = fixedInt(json_obj['M-B_H_5-36']) #Rein OD fact 2
                            dic['Braid5_43'] = fixedInt(json_obj['M-B_H_5-37']) #Rein OD mact 2
                            dic['Braid5_44'] = fixedInt(json_obj['M-B_H_5-38']) #Rein OD lact 2
                            dic['Braid5_45'] = fixedInt(json_obj['M-B_H_5-39']) #Rein Pitch fact 2
                            dic['Braid5_46'] = fixedInt(json_obj['M-B_H_5-40']) #Rein Pitch mact 2
                            dic['Braid5_47'] = fixedInt(json_obj['M-B_H_5-41']) #Rein Pitch lact 2
                            dic['Braid5_48'] = fixedInt(json_obj['M-B_H_5-42']) #Rein OD fact 3
                            dic['Braid5_49'] = fixedInt(json_obj['M-B_H_5-43']) #Rein OD mact 3
                            dic['Braid5_50'] = fixedInt(json_obj['M-B_H_5-44']) #Rein OD lact 3
                            dic['Braid5_51'] = fixedInt(json_obj['M-B_H_5-45']) #Rein Pitch fact 3
                            dic['Braid5_52'] = fixedInt(json_obj['M-B_H_5-46']) #Rein Pitch mact 3
                            dic['Braid5_53'] = fixedInt(json_obj['M-B_H_5-47']) #Rein Pitch lact 3
                            dic['Braid5_54'] = fixedInt(json_obj['M-B_H_5-48']) #Rein OD spec tol 1
                            dic['Braid5_55'] = fixedInt(json_obj['M-B_H_5-49']) #Rein Pitch spec tol 1
                            dic['Braid5_56'] = fixedInt(json_obj['M-B_H_5-50']) #Rein OD spec tol 2
                            dic['Braid5_57'] = fixedInt(json_obj['M-B_H_5-51']) #Rein Pitch spec tol 2
                            dic['Braid5_58'] = fixedInt(json_obj['M-B_H_5-52']) #Rein OD spec tol 3
                            dic['Braid5_59'] = fixedInt(json_obj['M-B_H_5-53']) #Rein Pitch spec tol 3
                            dic['Braid5_60'] = fixedInt(json_obj['M-B_H_5-54']) #Operator ID
                            dic['Braid5_61'] = fixedInt(json_obj['M-B_H_5-55']) #Supervisor
                            dic['Braid5_62'] = fixedInt(json_obj['M-B_H_5-56']) #QA Approval

                            
                            dic['Braid6_13'] = fixedInt(json_obj['M-B_H_6-21']) #Tube Dia
                            dic['Braid6_14'] = fixedInt(json_obj['M-B_H_6-22']) #No. of ends
                            dic['Braid6_15'] = fixedInt(json_obj['M-B_H_6-23']) #Wire Dia
                            dic['Braid6_16'] = fixedInt(json_obj['M-B_H_6-7']) #Tag Date
                            dic['Braid6_17'] = fixedInt(json_obj['M-B_H_6-8']) #Deck Gear 1
                            dic['Braid6_18'] = fixedInt(json_obj['M-B_H_6-9']) #Deck Gear 2
                            dic['Braid6_19'] = fixedInt(json_obj['M-B_H_6-10']) #Haul Gear 1
                            dic['Braid6_20'] = fixedInt(json_obj['M-B_H_6-11']) #Haul Gear 2
                            dic['Braid6_21'] = fixedInt(json_obj['M-B_H_6-12']) #Drum in
                            dic['Braid6_22'] = fixedInt(json_obj['M-B_H_6-13']) #Drum out
                            dic['Braid6_23'] = fixedInt(json_obj['M-B_H_6-14']) #Insulation
                            dic['Braid6_24'] = fixedInt(json_obj['M-B_H_6-15']) #Batch No
                            dic['Braid6_25'] = fixedInt(json_obj['M-B_H_6-17']) #Ply Thickness setvalue
                            dic['Braid6_26'] = fixedInt(json_obj['M-B_H_6-18']) #Ply Thickness actvalue
                            dic['Braid6_27'] = fixedInt(json_obj['M-B_H_6-19']) #Ply Width set value
                            dic['Braid6_28'] = fixedInt(json_obj['M-B_H_6-20']) #Ply Width act value
                            dic['Braid6_29'] = fixedInt(json_obj['M-B_H_6-16']) #Machine number
                            dic['Braid6_30'] = fixedInt(json_obj['M-B_H_6-24']) #Rein OD spec 1
                            dic['Braid6_31'] = fixedInt(json_obj['M-B_H_6-25']) #Rein Pitch Spec 1
                            dic['Braid6_32'] = fixedInt(json_obj['M-B_H_6-26']) #Rein OD spec 2
                            dic['Braid6_33'] = fixedInt(json_obj['M-B_H_6-27']) #Rein Pitch Spec 2
                            dic['Braid6_34'] = fixedInt(json_obj['M-B_H_6-28']) #Rein OD spec 3
                            dic['Braid6_35'] = fixedInt(json_obj['M-B_H_6-29']) #Rein Pitch Spec 3
                            dic['Braid6_36'] = fixedInt(json_obj['M-B_H_6-30']) #Rein OD fact 1
                            dic['Braid6_37'] = fixedInt(json_obj['M-B_H_6-31']) #Rein OD mact 1
                            dic['Braid6_38'] = fixedInt(json_obj['M-B_H_6-32']) #Rein OD lact 1
                            dic['Braid6_39'] = fixedInt(json_obj['M-B_H_6-33']) #Rein Pitch fact 1
                            dic['Braid6_40'] = fixedInt(json_obj['M-B_H_6-34']) #Rein Pitch mact 1
                            dic['Braid6_41'] = fixedInt(json_obj['M-B_H_6-35']) #Rein Pitch lact 1
                            dic['Braid6_42'] = fixedInt(json_obj['M-B_H_6-36']) #Rein OD fact 2
                            dic['Braid6_43'] = fixedInt(json_obj['M-B_H_6-37']) #Rein OD mact 2
                            dic['Braid6_44'] = fixedInt(json_obj['M-B_H_6-38']) #Rein OD lact 2
                            dic['Braid6_45'] = fixedInt(json_obj['M-B_H_6-39']) #Rein Pitch fact 2
                            dic['Braid6_46'] = fixedInt(json_obj['M-B_H_6-40']) #Rein Pitch mact 2
                            dic['Braid6_47'] = fixedInt(json_obj['M-B_H_6-41']) #Rein Pitch lact 2
                            dic['Braid6_48'] = fixedInt(json_obj['M-B_H_6-42']) #Rein OD fact 3
                            dic['Braid6_49'] = fixedInt(json_obj['M-B_H_6-43']) #Rein OD mact 3
                            dic['Braid6_50'] = fixedInt(json_obj['M-B_H_6-44']) #Rein OD lact 3
                            dic['Braid6_51'] = fixedInt(json_obj['M-B_H_6-45']) #Rein Pitch fact 3
                            dic['Braid6_52'] = fixedInt(json_obj['M-B_H_6-46']) #Rein Pitch mact 3
                            dic['Braid6_53'] = fixedInt(json_obj['M-B_H_6-47']) #Rein Pitch lact 3
                            dic['Braid6_54'] = fixedInt(json_obj['M-B_H_6-48']) #Rein OD spec tol 1
                            dic['Braid6_55'] = fixedInt(json_obj['M-B_H_6-49']) #Rein Pitch spec tol 1
                            dic['Braid6_56'] = fixedInt(json_obj['M-B_H_6-50']) #Rein OD spec tol 2
                            dic['Braid6_57'] = fixedInt(json_obj['M-B_H_6-51']) #Rein Pitch spec tol 2
                            dic['Braid6_58'] = fixedInt(json_obj['M-B_H_6-52']) #Rein OD spec tol 3
                            dic['Braid6_59'] = fixedInt(json_obj['M-B_H_6-53']) #Rein Pitch spec tol 3
                            dic['Braid6_60'] = fixedInt(json_obj['M-B_H_6-54']) #Operator ID
                            dic['Braid6_61'] = fixedInt(json_obj['M-B_H_6-55']) #Supervisor
                            dic['Braid6_62'] = fixedInt(json_obj['M-B_H_6-56']) #QA Approval

                            
                            dic['Braid7_13'] = fixedInt(json_obj['M-B_H_7-21']) #Tube Dia
                            dic['Braid7_14'] = fixedInt(json_obj['M-B_H_7-22']) #No. of ends
                            dic['Braid7_15'] = fixedInt(json_obj['M-B_H_7-23']) #Wire Dia
                            dic['Braid7_16'] = fixedInt(json_obj['M-B_H_7-7']) #Tag Date
                            dic['Braid7_17'] = fixedInt(json_obj['M-B_H_7-8']) #Deck Gear 1
                            dic['Braid7_18'] = fixedInt(json_obj['M-B_H_7-9']) #Deck Gear 2
                            dic['Braid7_19'] = fixedInt(json_obj['M-B_H_7-10']) #Haul Gear 1
                            dic['Braid7_20'] = fixedInt(json_obj['M-B_H_7-11']) #Haul Gear 2
                            dic['Braid7_21'] = fixedInt(json_obj['M-B_H_7-12']) #Drum in
                            dic['Braid7_22'] = fixedInt(json_obj['M-B_H_7-13']) #Drum out
                            dic['Braid7_23'] = fixedInt(json_obj['M-B_H_7-14']) #Insulation
                            dic['Braid7_24'] = fixedInt(json_obj['M-B_H_7-15']) #Batch No
                            dic['Braid7_25'] = fixedInt(json_obj['M-B_H_7-17']) #Ply Thickness setvalue
                            dic['Braid7_26'] = fixedInt(json_obj['M-B_H_7-18']) #Ply Thickness actvalue
                            dic['Braid7_27'] = fixedInt(json_obj['M-B_H_7-19']) #Ply Width set value
                            dic['Braid7_28'] = fixedInt(json_obj['M-B_H_7-20']) #Ply Width act value
                            dic['Braid7_29'] = fixedInt(json_obj['M-B_H_7-16']) #Machine number
                            dic['Braid7_30'] = fixedInt(json_obj['M-B_H_7-24']) #Rein OD spec 1
                            dic['Braid7_31'] = fixedInt(json_obj['M-B_H_7-25']) #Rein Pitch Spec 1
                            dic['Braid7_32'] = fixedInt(json_obj['M-B_H_7-26']) #Rein OD spec 2
                            dic['Braid7_33'] = fixedInt(json_obj['M-B_H_7-27']) #Rein Pitch Spec 2
                            dic['Braid7_34'] = fixedInt(json_obj['M-B_H_7-28']) #Rein OD spec 3
                            dic['Braid7_35'] = fixedInt(json_obj['M-B_H_7-29']) #Rein Pitch Spec 3
                            dic['Braid7_36'] = fixedInt(json_obj['M-B_H_7-30']) #Rein OD fact 1
                            dic['Braid7_37'] = fixedInt(json_obj['M-B_H_7-31']) #Rein OD mact 1
                            dic['Braid7_38'] = fixedInt(json_obj['M-B_H_7-32']) #Rein OD lact 1
                            dic['Braid7_39'] = fixedInt(json_obj['M-B_H_7-33']) #Rein Pitch fact 1
                            dic['Braid7_40'] = fixedInt(json_obj['M-B_H_7-34']) #Rein Pitch mact 1
                            dic['Braid7_41'] = fixedInt(json_obj['M-B_H_7-35']) #Rein Pitch lact 1
                            dic['Braid7_42'] = fixedInt(json_obj['M-B_H_7-36']) #Rein OD fact 2
                            dic['Braid7_43'] = fixedInt(json_obj['M-B_H_7-37']) #Rein OD mact 2
                            dic['Braid7_44'] = fixedInt(json_obj['M-B_H_7-38']) #Rein OD lact 2
                            dic['Braid7_45'] = fixedInt(json_obj['M-B_H_7-39']) #Rein Pitch fact 2
                            dic['Braid7_46'] = fixedInt(json_obj['M-B_H_7-40']) #Rein Pitch mact 2
                            dic['Braid7_47'] = fixedInt(json_obj['M-B_H_7-41']) #Rein Pitch lact 2
                            dic['Braid7_48'] = fixedInt(json_obj['M-B_H_7-42']) #Rein OD fact 3
                            dic['Braid7_49'] = fixedInt(json_obj['M-B_H_7-43']) #Rein OD mact 3
                            dic['Braid7_50'] = fixedInt(json_obj['M-B_H_7-44']) #Rein OD lact 3
                            dic['Braid7_51'] = fixedInt(json_obj['M-B_H_7-45']) #Rein Pitch fact 3
                            dic['Braid7_52'] = fixedInt(json_obj['M-B_H_7-46']) #Rein Pitch mact 3
                            dic['Braid7_53'] = fixedInt(json_obj['M-B_H_7-47']) #Rein Pitch lact 3
                            dic['Braid7_54'] = fixedInt(json_obj['M-B_H_7-48']) #Rein OD spec tol 1
                            dic['Braid7_55'] = fixedInt(json_obj['M-B_H_7-49']) #Rein Pitch spec tol 1
                            dic['Braid7_56'] = fixedInt(json_obj['M-B_H_7-50']) #Rein OD spec tol 2
                            dic['Braid7_57'] = fixedInt(json_obj['M-B_H_7-51']) #Rein Pitch spec tol 2
                            dic['Braid7_58'] = fixedInt(json_obj['M-B_H_7-52']) #Rein OD spec tol 3
                            dic['Braid7_59'] = fixedInt(json_obj['M-B_H_7-53']) #Rein Pitch spec tol 3
                            dic['Braid7_60'] = fixedInt(json_obj['M-B_H_7-54']) #Operator ID
                            dic['Braid7_61'] = fixedInt(json_obj['M-B_H_7-55']) #Supervisor
                            dic['Braid7_62'] = fixedInt(json_obj['M-B_H_7-56']) #QA Approval


                            
                            dic['Braid8_13'] = fixedInt(json_obj['M-B_H_8-21']) #Tube Dia
                            dic['Braid8_14'] = fixedInt(json_obj['M-B_H_8-22']) #No. of ends
                            dic['Braid8_15'] = fixedInt(json_obj['M-B_H_8-23']) #Wire Dia
                            dic['Braid8_16'] = fixedInt(json_obj['M-B_H_8-7']) #Tag Date
                            dic['Braid8_17'] = fixedInt(json_obj['M-B_H_8-8']) #Deck Gear 1
                            dic['Braid8_18'] = fixedInt(json_obj['M-B_H_8-9']) #Deck Gear 2
                            dic['Braid8_19'] = fixedInt(json_obj['M-B_H_8-10']) #Haul Gear 1
                            dic['Braid8_20'] = fixedInt(json_obj['M-B_H_8-11']) #Haul Gear 2
                            dic['Braid8_21'] = fixedInt(json_obj['M-B_H_8-12']) #Drum in
                            dic['Braid8_22'] = fixedInt(json_obj['M-B_H_8-13']) #Drum out
                            dic['Braid8_23'] = fixedInt(json_obj['M-B_H_8-14']) #Insulation
                            dic['Braid8_24'] = fixedInt(json_obj['M-B_H_8-15']) #Batch No
                            dic['Braid8_25'] = fixedInt(json_obj['M-B_H_8-17']) #Ply Thickness setvalue
                            dic['Braid8_26'] = fixedInt(json_obj['M-B_H_8-18']) #Ply Thickness actvalue
                            dic['Braid8_27'] = fixedInt(json_obj['M-B_H_8-19']) #Ply Width set value
                            dic['Braid8_28'] = fixedInt(json_obj['M-B_H_8-20']) #Ply Width act value
                            dic['Braid8_29'] = fixedInt(json_obj['M-B_H_8-16']) #Machine number
                            dic['Braid8_30'] = fixedInt(json_obj['M-B_H_8-24']) #Rein OD spec 1
                            dic['Braid8_31'] = fixedInt(json_obj['M-B_H_8-25']) #Rein Pitch Spec 1
                            dic['Braid8_32'] = fixedInt(json_obj['M-B_H_8-26']) #Rein OD spec 2
                            dic['Braid8_33'] = fixedInt(json_obj['M-B_H_8-27']) #Rein Pitch Spec 2
                            dic['Braid8_34'] = fixedInt(json_obj['M-B_H_8-28']) #Rein OD spec 3
                            dic['Braid8_35'] = fixedInt(json_obj['M-B_H_8-29']) #Rein Pitch Spec 3
                            dic['Braid8_36'] = fixedInt(json_obj['M-B_H_8-30']) #Rein OD fact 1
                            dic['Braid8_37'] = fixedInt(json_obj['M-B_H_8-31']) #Rein OD mact 1
                            dic['Braid8_38'] = fixedInt(json_obj['M-B_H_8-32']) #Rein OD lact 1
                            dic['Braid8_39'] = fixedInt(json_obj['M-B_H_8-33']) #Rein Pitch fact 1
                            dic['Braid8_40'] = fixedInt(json_obj['M-B_H_8-34']) #Rein Pitch mact 1
                            dic['Braid8_41'] = fixedInt(json_obj['M-B_H_8-35']) #Rein Pitch lact 1
                            dic['Braid8_42'] = fixedInt(json_obj['M-B_H_8-36']) #Rein OD fact 2
                            dic['Braid8_43'] = fixedInt(json_obj['M-B_H_8-37']) #Rein OD mact 2
                            dic['Braid8_44'] = fixedInt(json_obj['M-B_H_8-38']) #Rein OD lact 2
                            dic['Braid8_45'] = fixedInt(json_obj['M-B_H_8-39']) #Rein Pitch fact 2
                            dic['Braid8_46'] = fixedInt(json_obj['M-B_H_8-40']) #Rein Pitch mact 2
                            dic['Braid8_47'] = fixedInt(json_obj['M-B_H_8-41']) #Rein Pitch lact 2
                            dic['Braid8_48'] = fixedInt(json_obj['M-B_H_8-42']) #Rein OD fact 3
                            dic['Braid8_49'] = fixedInt(json_obj['M-B_H_8-43']) #Rein OD mact 3
                            dic['Braid8_50'] = fixedInt(json_obj['M-B_H_8-44']) #Rein OD lact 3
                            dic['Braid8_51'] = fixedInt(json_obj['M-B_H_8-45']) #Rein Pitch fact 3
                            dic['Braid8_52'] = fixedInt(json_obj['M-B_H_8-46']) #Rein Pitch mact 3
                            dic['Braid8_53'] = fixedInt(json_obj['M-B_H_8-47']) #Rein Pitch lact 3
                            dic['Braid8_54'] = fixedInt(json_obj['M-B_H_8-48']) #Rein OD spec tol 1
                            dic['Braid8_55'] = fixedInt(json_obj['M-B_H_8-49']) #Rein Pitch spec tol 1
                            dic['Braid8_56'] = fixedInt(json_obj['M-B_H_8-50']) #Rein OD spec tol 2
                            dic['Braid8_57'] = fixedInt(json_obj['M-B_H_8-51']) #Rein Pitch spec tol 2
                            dic['Braid8_58'] = fixedInt(json_obj['M-B_H_8-52']) #Rein OD spec tol 3
                            dic['Braid8_59'] = fixedInt(json_obj['M-B_H_8-53']) #Rein Pitch spec tol 3
                            dic['Braid8_60'] = fixedInt(json_obj['M-B_H_8-54']) #Operator ID
                            dic['Braid8_61'] = fixedInt(json_obj['M-B_H_8-55']) #Supervisor
                            dic['Braid8_62'] = fixedInt(json_obj['M-B_H_8-56']) #QA Approval



                            dic['Braid2_1'] = fixedInt(json_obj['M-B_R_2-0']) #PIR
                            dic['Braid2_2'] = fixedInt(json_obj['M-B_R_2-1']) #operator name
                            dic['Braid2_3'] = fixedInt(json_obj['M-B_R_2-2']) #deck set speed
                            dic['Braid2_4'] = fixedInt(json_obj['M-B_R_2-3']) #deck act speed
                            dic['Braid2_5'] = fixedInt(json_obj['M-B_R_2-4']) #production meter
                            dic['Braid2_6'] = fixedInt(json_obj['M-B_R_2-5']) #total running hrs
                            dic['Braid2_7'] = fixedInt(json_obj['M-B_R_2-6']) #blower ser temperature 
                            dic['Braid2_8'] = fixedInt(json_obj['M-B_R_2-7']) #blower act temperature
                            dic['Braid2_9'] = fixedInt(json_obj['M-B_R_2-8']) #N2 set temperature
                            dic['Braid2_10'] = fixedInt(json_obj['M-B_R_2-9']) #N2 inlet temperature
                            dic['Braid2_11'] = fixedInt(json_obj['M-B_R_2-10']) #N2 outlet temperature
                            dic['Braid2_12'] = fixedInt(json_obj['M-B_R_2-11'])#N2 pressure

                            dic['Braid3_1'] = fixedInt(json_obj['M-B_R_3-0']) #PIR
                            dic['Braid3_2'] = fixedInt(json_obj['M-B_R_3-1']) #operator name
                            dic['Braid3_3'] = fixedInt(json_obj['M-B_R_3-2']) #deck set speed
                            dic['Braid3_4'] = fixedInt(json_obj['M-B_R_3-3']) #deck act speed
                            dic['Braid3_5'] = fixedInt(json_obj['M-B_R_3-4']) #production meter
                            dic['Braid3_6'] = fixedInt(json_obj['M-B_R_3-5']) #total running hrs
                            dic['Braid3_7'] = fixedInt(json_obj['M-B_R_3-6']) #blower ser temperature 
                            dic['Braid3_8'] = fixedInt(json_obj['M-B_R_3-7']) #blower act temperature
                            dic['Braid3_9'] = fixedInt(json_obj['M-B_R_3-8']) #N2 set temperature
                            dic['Braid3_10'] = fixedInt(json_obj['M-B_R_3-9']) #N2 inlet temperature
                            dic['Braid3_11'] = fixedInt(json_obj['M-B_R_3-10']) #N2 outlet temperature
                            dic['Braid3_12'] = fixedInt(json_obj['M-B_R_3-11']) #N2 pressure

                            dic['Braid4_1'] = fixedInt(json_obj['M-B_R_4-0']) #PIR
                            dic['Braid4_2'] = fixedInt(json_obj['M-B_R_4-1']) #operator name
                            dic['Braid4_3'] = fixedInt(json_obj['M-B_R_4-2']) #deck set speed
                            dic['Braid4_4'] = fixedInt(json_obj['M-B_R_4-3']) #deck act speed
                            dic['Braid4_5'] = fixedInt(json_obj['M-B_R_4-4']) #production meter
                            dic['Braid4_6'] = fixedInt(json_obj['M-B_R_4-5']) #total running hrs
                            dic['Braid4_7'] = fixedInt(json_obj['M-B_R_4-6']) #blower ser temperature 
                            dic['Braid4_8'] = fixedInt(json_obj['M-B_R_4-7']) #blower act temperature
                            dic['Braid4_9'] = fixedInt(json_obj['M-B_R_4-8']) #N2 set temperature
                            dic['Braid4_10'] = fixedInt(json_obj['M-B_R_4-9']) #N2 inlet temperature
                            dic['Braid4_11'] = fixedInt(json_obj['M-B_R_4-10']) #N2 outlet temperature
                            dic['Braid4_12'] = fixedInt(json_obj['M-B_R_4-11']) #N2 pressure

                            dic['Braid5_1'] = fixedInt(json_obj['M-B_R_5-0']) #PIR
                            dic['Braid5_2'] = fixedInt(json_obj['M-B_R_5-1']) #operator name
                            dic['Braid5_3'] = fixedInt(json_obj['M-B_R_5-2']) #deck set speed
                            dic['Braid5_4'] = fixedInt(json_obj['M-B_R_5-3']) #deck act speed
                            dic['Braid5_5'] = fixedInt(json_obj['M-B_R_5-4']) #production meter
                            dic['Braid5_6'] = fixedInt(json_obj['M-B_R_5-5']) #total running hrs
                            dic['Braid5_7'] = fixedInt(json_obj['M-B_R_5-6']) #blower ser temperature 
                            dic['Braid5_8'] = fixedInt(json_obj['M-B_R_5-7']) #blower act temperature
                            dic['Braid5_9'] = fixedInt(json_obj['M-B_R_5-8']) #N2 set temperature
                            dic['Braid5_10'] = fixedInt(json_obj['M-B_R_5-9']) #N2 inlet temperature
                            dic['Braid5_11'] = fixedInt(json_obj['M-B_R_5-10']) #N2 outlet temperature
                            dic['Braid5_12'] = fixedInt(json_obj['M-B_R_5-11']) #N2 pressure

                            dic['Braid6_1'] = fixedInt(json_obj['M-B_R_6-0']) #PIR
                            dic['Braid6_2'] = fixedInt(json_obj['M-B_R_6-1']) #operator name
                            dic['Braid6_3'] = fixedInt(json_obj['M-B_R_6-2']) #deck set speed
                            dic['Braid6_4'] = fixedInt(json_obj['M-B_R_6-3']) #deck act speed
                            dic['Braid6_5'] = fixedInt(json_obj['M-B_R_6-4']) #production meter
                            dic['Braid6_6'] = fixedInt(json_obj['M-B_R_6-5']) #total running hrs
                            dic['Braid6_7'] = fixedInt(json_obj['M-B_R_6-6']) #blower ser temperature 
                            dic['Braid6_8'] = fixedInt(json_obj['M-B_R_6-7']) #blower act temperature
                            dic['Braid6_9'] = fixedInt(json_obj['M-B_R_6-8']) #N2 set temperature
                            dic['Braid6_10'] = fixedInt(json_obj['M-B_R_6-9']) #N2 inlet temperature
                            dic['Braid6_11'] = fixedInt(json_obj['M-B_R_6-10']) #N2 outlet temperature
                            dic['Braid6_12'] = fixedInt(json_obj['M-B_R_6-11']) #N2 pressure

                            dic['Braid7_1'] = fixedInt(json_obj['M-B_R_7-0']) #PIR
                            dic['Braid7_2'] = fixedInt(json_obj['M-B_R_7-1']) #operator name
                            dic['Braid7_3'] = fixedInt(json_obj['M-B_R_7-2']) #deck set speed
                            dic['Braid7_4'] = fixedInt(json_obj['M-B_R_7-3']) #deck act speed
                            dic['Braid7_5'] = fixedInt(json_obj['M-B_R_7-4']) #production meter
                            dic['Braid7_6'] = fixedInt(json_obj['M-B_R_7-5']) #total running hrs
                            dic['Braid7_7'] = fixedInt(json_obj['M-B_R_7-6']) #blower ser temperature 
                            dic['Braid7_8'] = fixedInt(json_obj['M-B_R_7-7']) #blower act temperature
                            dic['Braid7_9'] = fixedInt(json_obj['M-B_R_7-8']) #N2 set temperature
                            dic['Braid7_10'] = fixedInt(json_obj['M-B_R_7-9']) #N2 inlet temperature
                            dic['Braid7_11'] = fixedInt(json_obj['M-B_R_7-10']) #N2 outlet temperature
                            dic['Braid7_12'] = fixedInt(json_obj['M-B_R_7-11']) #N2 pressure

                            dic['Braid8_1'] = fixedInt(json_obj['M-B_R_8-0']) #PIR
                            dic['Braid8_2'] = fixedInt(json_obj['M-B_R_8-1']) #operator name
                            dic['Braid8_3'] = fixedInt(json_obj['M-B_R_8-2']) #deck set speed
                            dic['Braid8_4'] = fixedInt(json_obj['M-B_R_8-3']) #deck act speed
                            dic['Braid8_5'] = fixedInt(json_obj['M-B_R_8-4']) #production meter
                            dic['Braid8_6'] = fixedInt(json_obj['M-B_R_8-5']) #total running hrs
                            dic['Braid8_7'] = fixedInt(json_obj['M-B_R_8-6']) #blower ser temperature 
                            dic['Braid8_8'] = fixedInt(json_obj['M-B_R_8-7']) #blower act temperature
                            dic['Braid8_9'] = fixedInt(json_obj['M-B_R_8-8']) #N2 set temperature
                            dic['Braid8_10'] = fixedInt(json_obj['M-B_R_8-9']) #N2 inlet temperature
                            dic['Braid8_11'] = fixedInt(json_obj['M-B_R_8-10']) #N2 outlet temperature
                            dic['Braid8_12'] = fixedInt(json_obj['M-B_R_8-11']) #N2 pressure
                            

                            # Braider PIMS1 Tags
                            '''
                            dic['BraidPims1_1'] = fixedInt(json_obj['M-B_P_1-0']) #DRUM IN
                            dic['BraidPims1_2'] = fixedInt(json_obj['M-B_P_1-1']) #DRUM OUT
                            dic['BraidPims1_3'] = fixedInt(json_obj['M-B_P_1-2']) #RED TAPE METER 1
                            dic['BraidPims1_4'] = fixedInt(json_obj['M-B_P_1-3']) #RED TAPE METER 2
                            dic['BraidPims1_5'] = fixedInt(json_obj['M-B_P_1-4']) #RED TAPE METER 3
                            dic['BraidPims1_6'] = fixedInt(json_obj['M-B_P_1-5']) #RED TAPE METER 4
                            dic['BraidPims1_7'] = fixedInt(json_obj['M-B_P_1-6']) #RED TAPE METER 5
                            dic['BraidPims1_8'] = fixedInt(json_obj['M-B_P_1-7']) #RED TAPE METER 6
                            dic['BraidPims1_9'] = fixedInt(json_obj['M-B_P_1-8']) #RED TAPE METER 7
                            dic['BraidPims1_10'] = fixedInt(json_obj['M-B_P_1-9']) #RED TAPE METER 8
                            dic['BraidPims1_11'] = fixedInt(json_obj['M-B_P_1-10']) #RED TAPE METER 9
                            dic['BraidPims1_12'] = fixedInt(json_obj['M-B_P_1-11']) #RED TAPE METER 10
                            dic['BraidPims1_13'] = fixedInt(json_obj['M-B_P_1-12']) #RED TAPE METER 11
                            dic['BraidPims1_14'] = fixedInt(json_obj['M-B_P_1-13']) #RED TAPE METER 12
                            dic['BraidPims1_15'] = fixedInt(json_obj['M-B_P_1-14']) #RED TAPE METER 13
                            dic['BraidPims1_16'] = fixedInt(json_obj['M-B_P_1-15'])#RED TAPE METER 14
                            dic['BraidPims1_17'] = fixedInt(json_obj['M-B_P_1-16']) #RED TAPE METER 15
                            dic['BraidPims1_18'] = fixedInt(json_obj['M-B_P_1-17']) #RED TAPE METER 16
                            dic['BraidPims1_19'] = fixedInt(json_obj['M-B_P_1-18']) #RED TAPE METER 17
                            dic['BraidPims1_20'] = fixedInt(json_obj['M-B_P_1-19']) #RED TAPE METER 18
                            dic['BraidPims1_21'] = fixedInt(json_obj['M-B_P_1-20']) #RED TAPE METER 19
                            dic['BraidPims1_22'] = fixedInt(json_obj['M-B_P_1-21']) #RED TAPE METER 20
                            dic['BraidPims1_23'] = fixedInt(json_obj['M-B_P_1-22']) #RED TAPE METER 21
                            dic['BraidPims1_24'] = fixedInt(json_obj['M-B_P_1-23']) #RED TAPE METER 22
                            dic['BraidPims1_25'] = fixedInt(json_obj['M-B_P_1-24']) #RED TAPE METER 23
                            dic['BraidPims1_26'] = fixedInt(json_obj['M-B_P_1-25']) #RED TAPE METER 24
                            dic['BraidPims1_27'] = fixedInt(json_obj['M-B_P_1-26']) #RED TAPE METER 25
                            dic['BraidPims1_28'] = fixedInt(json_obj['M-B_P_1-27']) #RED TAPE METER 26
                            dic['BraidPims1_29'] = fixedInt(json_obj['M-B_P_1-28']) #RED TAPE METER 27
                            dic['BraidPims1_30'] = fixedInt(json_obj['M-B_P_1-29']) #RED TAPE METER 28
                            dic['BraidPims1_31'] = fixedInt(json_obj['M-B_P_1-30']) #RED TAPE METER 29
                            dic['BraidPims1_32'] = fixedInt(json_obj['M-B_P_1-31']) #RED TAPE METER 30
                            dic['BraidPims1_33'] = fixedInt(json_obj['M-B_P_1-32']) #RED TAPE METER 31
                            dic['BraidPims1_34'] = fixedInt(json_obj['M-B_P_1-33']) #RED TAPE METER 32
                            dic['BraidPims1_35'] = fixedInt(json_obj['M-B_P_1-34']) #RED TAPE METER 33
                            dic['BraidPims1_36'] = fixedInt(json_obj['M-B_P_1-35']) #RED TAPE METER 34
                            dic['BraidPims1_37'] = fixedInt(json_obj['M-B_P_1-36']) #RED TAPE METER 35
                            dic['BraidPims1_38'] = fixedInt(json_obj['M-B_P_1-37']) #RED TAPE METER 36
                            dic['BraidPims1_39'] = fixedInt(json_obj['M-B_P_1-38']) #RED TAPE METER 37
                            dic['BraidPims1_40'] = fixedInt(json_obj['M-B_P_1-39']) #RED TAPE METER 38
                            dic['BraidPims1_41'] = fixedInt(json_obj['M-B_P_1-40']) #RED TAPE METER 39
                            dic['BraidPims1_42'] = fixedInt(json_obj['M-B_P_1-41']) #RED TAPE METER 40
                            dic['BraidPims1_43'] = fixedInt(json_obj['M-B_P_1-42']) #RED TAPE METER 41
                            dic['BraidPims1_44'] = fixedInt(json_obj['M-B_P_1-43']) #RED TAPE METER 42
                            dic['BraidPims1_45'] = fixedInt(json_obj['M-B_P_1-44']) #RED TAPE METER 43
                            dic['BraidPims1_46'] = fixedInt(json_obj['M-B_P_1-45']) #RED TAPE METER 44
                            dic['BraidPims1_47'] = fixedInt(json_obj['M-B_P_1-46']) #RED TAPE METER 45
                            dic['BraidPims1_48'] = fixedInt(json_obj['M-B_P_1-47']) #RED TAPE METER 46
                            dic['BraidPims1_49'] = fixedInt(json_obj['M-B_P_1-48']) #RED TAPE METER 47
                            dic['BraidPims1_50'] = fixedInt(json_obj['M-B_P_1-49']) #RED TAPE METER 48
                            dic['BraidPims1_51'] = fixedInt(json_obj['M-B_P_1-50']) #RED TAPE METER 49
                            dic['BraidPims1_52'] = fixedInt(json_obj['M-B_P_1-51'])#RED TAPE METER 50
                            dic['BraidPims1_53'] = fixedInt(json_obj['M-B_P_1-52']) #RED TAPE METER 51
                            dic['BraidPims1_54'] = fixedInt(json_obj['M-B_P_1-53']) #RED TAPE METER 52
                            dic['BraidPims1_55'] = fixedInt(json_obj['M-B_P_1-54']) #RED TAPE METER 53
                            dic['BraidPims1_56'] = fixedInt(json_obj['M-B_P_1-55']) #RED TAPE METER 54
                            dic['BraidPims1_57'] = fixedInt(json_obj['M-B_P_1-56']) #RED TAPE METER 55
                            dic['BraidPims1_58'] = fixedInt(json_obj['M-B_P_1-57']) #RED TAPE METER 56
                            dic['BraidPims1_59'] = fixedInt(json_obj['M-B_P_1-58']) #RED TAPE METER 57
                            dic['BraidPims1_60'] = fixedInt(json_obj['M-B_P_1-59']) #RED TAPE METER 58
                            dic['BraidPims1_61'] = fixedInt(json_obj['M-B_P_1-60']) #RED TAPE METER 59
                            dic['BraidPims1_62'] = fixedInt(json_obj['M-B_P_1-61']) #RED TAPE METER 60
                            dic['BraidPims1_63'] = fixedInt(json_obj['M-B_P_1-62']) #RED TAPE METER 61
                            dic['BraidPims1_64'] = fixedInt(json_obj['M-B_P_1-63']) #RED TAPE METER 62
                            dic['BraidPims1_65'] = fixedInt(json_obj['M-B_P_1-64']) #RED TAPE METER 63
                            dic['BraidPims1_66'] = fixedInt(json_obj['M-B_P_1-65']) #RED TAPE METER 64
                            dic['BraidPims1_67'] = fixedInt(json_obj['M-B_P_1-66']) #RED TAPE METER 65
                            dic['BraidPims1_68'] = fixedInt(json_obj['M-B_P_1-67'])#RED TAPE METER 66
                            dic['BraidPims1_69'] = fixedInt(json_obj['M-B_P_1-68']) #RED TAPE METER 67
                            dic['BraidPims1_70'] = fixedInt(json_obj['M-B_P_1-69']) #RED TAPE METER 68
                            dic['BraidPims1_71'] = fixedInt(json_obj['M-B_P_1-70']) #RED TAPE METER 69
                            dic['BraidPims1_72'] = fixedInt(json_obj['M-B_P_1-71']) #RED TAPE METER 70
                            dic['BraidPims1_73'] = fixedInt(json_obj['M-B_P_1-72']) #RED TAPE METER 71
                            dic['BraidPims1_74'] = fixedInt(json_obj['M-B_P_1-73']) #RED TAPE METER 72
                            dic['BraidPims1_75'] = fixedInt(json_obj['M-B_P_1-74']) #RED TAPE METER 73
                            dic['BraidPims1_76'] = fixedInt(json_obj['M-B_P_1-75']) #RED TAPE METER 74
                            dic['BraidPims1_77'] = fixedInt(json_obj['M-B_P_1-76']) #RED TAPE METER 75
                            dic['BraidPims1_78'] = fixedInt(json_obj['M-B_P_1-77']) #RED TAPE METER 76
                            dic['BraidPims1_79'] = fixedInt(json_obj['M-B_P_1-78']) #RED TAPE METER 77
                            dic['BraidPims1_80'] = fixedInt(json_obj['M-B_P_1-79']) #RED TAPE METER 78
                            dic['BraidPims1_81'] = fixedInt(json_obj['M-B_P_1-80']) #RED TAPE METER 79
                            dic['BraidPims1_82'] = fixedInt(json_obj['M-B_P_1-81']) #RED TAPE METER 80

                            dic['BraidPims2_1'] = fixedInt(json_obj['M-B_P_2-0']) #DRUM IN
                            dic['BraidPims2_2'] = fixedInt(json_obj['M-B_P_2-1']) #DRUM OUT
                            dic['BraidPims2_3'] = fixedInt(json_obj['M-B_P_2-2']) #RED TAPE METER 1
                            dic['BraidPims2_4'] = fixedInt(json_obj['M-B_P_2-3']) #RED TAPE METER 2
                            dic['BraidPims2_5'] = fixedInt(json_obj['M-B_P_2-4']) #RED TAPE METER 3
                            dic['BraidPims2_6'] = fixedInt(json_obj['M-B_P_2-5']) #RED TAPE METER 4
                            dic['BraidPims2_7'] = fixedInt(json_obj['M-B_P_2-6']) #RED TAPE METER 5
                            dic['BraidPims2_8'] = fixedInt(json_obj['M-B_P_2-7']) #RED TAPE METER 6
                            dic['BraidPims2_9'] = fixedInt(json_obj['M-B_P_2-8']) #RED TAPE METER 7
                            dic['BraidPims2_10'] = fixedInt(json_obj['M-B_P_2-9']) #RED TAPE METER 8
                            dic['BraidPims2_11'] = fixedInt(json_obj['M-B_P_2-10']) #RED TAPE METER 9
                            dic['BraidPims2_12'] = fixedInt(json_obj['M-B_P_2-11']) #RED TAPE METER 10
                            dic['BraidPims2_13'] = fixedInt(json_obj['M-B_P_2-12']) #RED TAPE METER 11
                            dic['BraidPims2_14'] = fixedInt(json_obj['M-B_P_2-13']) #RED TAPE METER 12
                            dic['BraidPims2_15'] = fixedInt(json_obj['M-B_P_2-14']) #RED TAPE METER 13
                            dic['BraidPims2_16'] = fixedInt(json_obj['M-B_P_2-15'])#RED TAPE METER 14
                            dic['BraidPims2_17'] = fixedInt(json_obj['M-B_P_2-16']) #RED TAPE METER 15
                            dic['BraidPims2_18'] = fixedInt(json_obj['M-B_P_2-17']) #RED TAPE METER 16
                            dic['BraidPims2_19'] = fixedInt(json_obj['M-B_P_2-18']) #RED TAPE METER 17
                            dic['BraidPims2_20'] = fixedInt(json_obj['M-B_P_2-19']) #RED TAPE METER 18
                            dic['BraidPims2_21'] = fixedInt(json_obj['M-B_P_2-20']) #RED TAPE METER 19
                            dic['BraidPims2_22'] = fixedInt(json_obj['M-B_P_2-21']) #RED TAPE METER 20
                            dic['BraidPims2_23'] = fixedInt(json_obj['M-B_P_2-22']) #RED TAPE METER 21
                            dic['BraidPims2_24'] = fixedInt(json_obj['M-B_P_2-23']) #RED TAPE METER 22
                            dic['BraidPims2_25'] = fixedInt(json_obj['M-B_P_2-24']) #RED TAPE METER 23
                            dic['BraidPims2_26'] = fixedInt(json_obj['M-B_P_2-25']) #RED TAPE METER 24
                            dic['BraidPims2_27'] = fixedInt(json_obj['M-B_P_2-26']) #RED TAPE METER 25
                            dic['BraidPims2_28'] = fixedInt(json_obj['M-B_P_2-27']) #RED TAPE METER 26
                            dic['BraidPims2_29'] = fixedInt(json_obj['M-B_P_2-28']) #RED TAPE METER 27
                            dic['BraidPims2_30'] = fixedInt(json_obj['M-B_P_2-29']) #RED TAPE METER 28
                            dic['BraidPims2_31'] = fixedInt(json_obj['M-B_P_2-30']) #RED TAPE METER 29
                            dic['BraidPims2_32'] = fixedInt(json_obj['M-B_P_2-31'])#RED TAPE METER 30
                            dic['BraidPims2_33'] = fixedInt(json_obj['M-B_P_2-32']) #RED TAPE METER 31
                            dic['BraidPims2_34'] = fixedInt(json_obj['M-B_P_2-33']) #RED TAPE METER 32
                            dic['BraidPims2_35'] = fixedInt(json_obj['M-B_P_2-34']) #RED TAPE METER 33
                            dic['BraidPims2_36'] = fixedInt(json_obj['M-B_P_2-35']) #RED TAPE METER 34
                            dic['BraidPims2_37'] = fixedInt(json_obj['M-B_P_2-36']) #RED TAPE METER 35
                            dic['BraidPims2_38'] = fixedInt(json_obj['M-B_P_2-37']) #RED TAPE METER 36
                            dic['BraidPims2_39'] = fixedInt(json_obj['M-B_P_2-38']) #RED TAPE METER 37
                            dic['BraidPims2_40'] = fixedInt(json_obj['M-B_P_2-39']) #RED TAPE METER 38
                            dic['BraidPims2_41'] = fixedInt(json_obj['M-B_P_2-40']) #RED TAPE METER 39
                            dic['BraidPims2_42'] = fixedInt(json_obj['M-B_P_2-41']) #RED TAPE METER 40
                            dic['BraidPims2_43'] = fixedInt(json_obj['M-B_P_2-42']) #RED TAPE METER 41
                            dic['BraidPims2_44'] = fixedInt(json_obj['M-B_P_2-43']) #RED TAPE METER 42
                            dic['BraidPims2_45'] = fixedInt(json_obj['M-B_P_2-44']) #RED TAPE METER 43
                            dic['BraidPims2_46'] = fixedInt(json_obj['M-B_P_2-45']) #RED TAPE METER 44
                            dic['BraidPims2_47'] = fixedInt(json_obj['M-B_P_2-46']) #RED TAPE METER 45
                            dic['BraidPims2_48'] = fixedInt(json_obj['M-B_P_2-47']) #RED TAPE METER 46
                            dic['BraidPims2_49'] = fixedInt(json_obj['M-B_P_2-48']) #RED TAPE METER 47
                            dic['BraidPims2_50'] = fixedInt(json_obj['M-B_P_2-49']) #RED TAPE METER 48
                            dic['BraidPims2_51'] = fixedInt(json_obj['M-B_P_2-50']) #RED TAPE METER 49
                            dic['BraidPims2_52'] = fixedInt(json_obj['M-B_P_2-51'])#RED TAPE METER 50
                            dic['BraidPims2_53'] = fixedInt(json_obj['M-B_P_2-52']) #RED TAPE METER 51
                            dic['BraidPims2_54'] = fixedInt(json_obj['M-B_P_2-53']) #RED TAPE METER 52
                            dic['BraidPims2_55'] = fixedInt(json_obj['M-B_P_2-54']) #RED TAPE METER 53
                            dic['BraidPims2_56'] = fixedInt(json_obj['M-B_P_2-55']) #RED TAPE METER 54
                            dic['BraidPims2_57'] = fixedInt(json_obj['M-B_P_2-56']) #RED TAPE METER 55
                            dic['BraidPims2_58'] = fixedInt(json_obj['M-B_P_2-57']) #RED TAPE METER 56
                            dic['BraidPims2_59'] = fixedInt(json_obj['M-B_P_2-58']) #RED TAPE METER 57
                            dic['BraidPims2_60'] = fixedInt(json_obj['M-B_P_2-59']) #RED TAPE METER 58
                            dic['BraidPims2_61'] = fixedInt(json_obj['M-B_P_2-60']) #RED TAPE METER 59
                            dic['BraidPims2_62'] = fixedInt(json_obj['M-B_P_2-61']) #RED TAPE METER 60
                            dic['BraidPims2_63'] = fixedInt(json_obj['M-B_P_2-62']) #RED TAPE METER 61
                            dic['BraidPims2_64'] = fixedInt(json_obj['M-B_P_2-63']) #RED TAPE METER 62
                            dic['BraidPims2_65'] = fixedInt(json_obj['M-B_P_2-64']) #RED TAPE METER 63
                            dic['BraidPims2_66'] = fixedInt(json_obj['M-B_P_2-65']) #RED TAPE METER 64
                            dic['BraidPims2_67'] = fixedInt(json_obj['M-B_P_2-66']) #RED TAPE METER 65
                            dic['BraidPims2_68'] = fixedInt(json_obj['M-B_P_2-67'])#RED TAPE METER 66
                            dic['BraidPims2_69'] = fixedInt(json_obj['M-B_P_2-68']) #RED TAPE METER 67
                            dic['BraidPims2_70'] = fixedInt(json_obj['M-B_P_2-69']) #RED TAPE METER 68
                            dic['BraidPims2_71'] = fixedInt(json_obj['M-B_P_2-70']) #RED TAPE METER 69
                            dic['BraidPims2_72'] = fixedInt(json_obj['M-B_P_2-71']) #RED TAPE METER 70
                            dic['BraidPims2_73'] = fixedInt(json_obj['M-B_P_2-72']) #RED TAPE METER 71
                            dic['BraidPims2_74'] = fixedInt(json_obj['M-B_P_2-73']) #RED TAPE METER 72
                            dic['BraidPims2_75'] = fixedInt(json_obj['M-B_P_2-74']) #RED TAPE METER 73
                            dic['BraidPims2_76'] = fixedInt(json_obj['M-B_P_2-75']) #RED TAPE METER 74
                            dic['BraidPims2_77'] = fixedInt(json_obj['M-B_P_2-76']) #RED TAPE METER 75
                            dic['BraidPims2_78'] = fixedInt(json_obj['M-B_P_2-77']) #RED TAPE METER 76
                            dic['BraidPims2_79'] = fixedInt(json_obj['M-B_P_2-78']) #RED TAPE METER 77
                            dic['BraidPims2_80'] = fixedInt(json_obj['M-B_P_2-79']) #RED TAPE METER 78
                            dic['BraidPims2_81'] = fixedInt(json_obj['M-B_P_2-80']) #RED TAPE METER 79
                            dic['BraidPims2_82'] = fixedInt(json_obj['M-B_P_2-81']) #RED TAPE METER 80

                            dic['BraidPims3_1'] = fixedInt(json_obj['M-B_P_3-0']) #DRUM IN
                            dic['BraidPims3_2'] = fixedInt(json_obj['M-B_P_3-1']) #DRUM OUT
                            dic['BraidPims3_3'] = fixedInt(json_obj['M-B_P_3-2']) #RED TAPE METER 1
                            dic['BraidPims3_4'] = fixedInt(json_obj['M-B_P_3-3']) #RED TAPE METER 2
                            dic['BraidPims3_5'] = fixedInt(json_obj['M-B_P_3-4']) #RED TAPE METER 3
                            dic['BraidPims3_6'] = fixedInt(json_obj['M-B_P_3-5']) #RED TAPE METER 4
                            dic['BraidPims3_7'] = fixedInt(json_obj['M-B_P_3-6']) #RED TAPE METER 5
                            dic['BraidPims3_8'] = fixedInt(json_obj['M-B_P_3-7']) #RED TAPE METER 6
                            dic['BraidPims3_9'] = fixedInt(json_obj['M-B_P_3-8']) #RED TAPE METER 7
                            dic['BraidPims3_10'] = fixedInt(json_obj['M-B_P_3-9']) #RED TAPE METER 8
                            dic['BraidPims3_11'] = fixedInt(json_obj['M-B_P_3-10']) #RED TAPE METER 9
                            dic['BraidPims3_12'] = fixedInt(json_obj['M-B_P_3-11']) #RED TAPE METER 10
                            dic['BraidPims3_13'] = fixedInt(json_obj['M-B_P_3-12']) #RED TAPE METER 11
                            dic['BraidPims3_14'] = fixedInt(json_obj['M-B_P_3-13']) #RED TAPE METER 12
                            dic['BraidPims3_15'] = fixedInt(json_obj['M-B_P_3-14']) #RED TAPE METER 13
                            dic['BraidPims3_16'] = fixedInt(json_obj['M-B_P_3-15'])#RED TAPE METER 14
                            dic['BraidPims3_17'] = fixedInt(json_obj['M-B_P_3-16']) #RED TAPE METER 15
                            dic['BraidPims3_18'] = fixedInt(json_obj['M-B_P_3-17']) #RED TAPE METER 16
                            dic['BraidPims3_19'] = fixedInt(json_obj['M-B_P_3-18']) #RED TAPE METER 17
                            dic['BraidPims3_20'] = fixedInt(json_obj['M-B_P_3-19']) #RED TAPE METER 18
                            dic['BraidPims3_21'] = fixedInt(json_obj['M-B_P_3-20']) #RED TAPE METER 19
                            dic['BraidPims3_22'] = fixedInt(json_obj['M-B_P_3-21']) #RED TAPE METER 20
                            dic['BraidPims3_23'] = fixedInt(json_obj['M-B_P_3-22']) #RED TAPE METER 21
                            dic['BraidPims3_24'] = fixedInt(json_obj['M-B_P_3-23']) #RED TAPE METER 22
                            dic['BraidPims3_25'] = fixedInt(json_obj['M-B_P_3-24']) #RED TAPE METER 23
                            dic['BraidPims3_26'] = fixedInt(json_obj['M-B_P_3-25']) #RED TAPE METER 24
                            dic['BraidPims3_27'] = fixedInt(json_obj['M-B_P_3-26']) #RED TAPE METER 25
                            dic['BraidPims3_28'] = fixedInt(json_obj['M-B_P_3-27']) #RED TAPE METER 26
                            dic['BraidPims3_29'] = fixedInt(json_obj['M-B_P_3-28']) #RED TAPE METER 27
                            dic['BraidPims3_30'] = fixedInt(json_obj['M-B_P_3-29']) #RED TAPE METER 28
                            dic['BraidPims3_31'] = fixedInt(json_obj['M-B_P_3-30']) #RED TAPE METER 29
                            dic['BraidPims3_32'] = fixedInt(json_obj['M-B_P_3-31'])#RED TAPE METER 30
                            dic['BraidPims3_33'] = fixedInt(json_obj['M-B_P_3-32']) #RED TAPE METER 31
                            dic['BraidPims3_34'] = fixedInt(json_obj['M-B_P_3-33']) #RED TAPE METER 32
                            dic['BraidPims3_35'] = fixedInt(json_obj['M-B_P_3-34']) #RED TAPE METER 33
                            dic['BraidPims3_36'] = fixedInt(json_obj['M-B_P_3-35']) #RED TAPE METER 34
                            dic['BraidPims3_37'] = fixedInt(json_obj['M-B_P_3-36']) #RED TAPE METER 35
                            dic['BraidPims3_38'] = fixedInt(json_obj['M-B_P_3-37']) #RED TAPE METER 36
                            dic['BraidPims3_39'] = fixedInt(json_obj['M-B_P_3-38']) #RED TAPE METER 37
                            dic['BraidPims3_40'] = fixedInt(json_obj['M-B_P_3-39']) #RED TAPE METER 38
                            dic['BraidPims3_41'] = fixedInt(json_obj['M-B_P_3-40']) #RED TAPE METER 39
                            dic['BraidPims3_42'] = fixedInt(json_obj['M-B_P_3-41']) #RED TAPE METER 40
                            dic['BraidPims3_43'] = fixedInt(json_obj['M-B_P_3-42']) #RED TAPE METER 41
                            dic['BraidPims3_44'] = fixedInt(json_obj['M-B_P_3-43']) #RED TAPE METER 42
                            dic['BraidPims3_45'] = fixedInt(json_obj['M-B_P_3-44']) #RED TAPE METER 43
                            dic['BraidPims3_46'] = fixedInt(json_obj['M-B_P_3-45']) #RED TAPE METER 44
                            dic['BraidPims3_47'] = fixedInt(json_obj['M-B_P_3-46']) #RED TAPE METER 45
                            dic['BraidPims3_48'] = fixedInt(json_obj['M-B_P_3-47']) #RED TAPE METER 46
                            dic['BraidPims3_49'] = fixedInt(json_obj['M-B_P_3-48']) #RED TAPE METER 47
                            dic['BraidPims3_50'] = fixedInt(json_obj['M-B_P_3-49']) #RED TAPE METER 48
                            dic['BraidPims3_51'] = fixedInt(json_obj['M-B_P_3-50']) #RED TAPE METER 49
                            dic['BraidPims3_52'] = fixedInt(json_obj['M-B_P_3-51'])#RED TAPE METER 50
                            dic['BraidPims3_53'] = fixedInt(json_obj['M-B_P_3-52']) #RED TAPE METER 51
                            dic['BraidPims3_54'] = fixedInt(json_obj['M-B_P_3-53']) #RED TAPE METER 52
                            dic['BraidPims3_55'] = fixedInt(json_obj['M-B_P_3-54']) #RED TAPE METER 53
                            dic['BraidPims3_56'] = fixedInt(json_obj['M-B_P_3-55']) #RED TAPE METER 54
                            dic['BraidPims3_57'] = fixedInt(json_obj['M-B_P_3-56']) #RED TAPE METER 55
                            dic['BraidPims3_58'] = fixedInt(json_obj['M-B_P_3-57']) #RED TAPE METER 56
                            dic['BraidPims3_59'] = fixedInt(json_obj['M-B_P_3-58']) #RED TAPE METER 57
                            dic['BraidPims3_60'] = fixedInt(json_obj['M-B_P_3-59']) #RED TAPE METER 58
                            dic['BraidPims3_61'] = fixedInt(json_obj['M-B_P_3-60']) #RED TAPE METER 59
                            dic['BraidPims3_62'] = fixedInt(json_obj['M-B_P_3-61']) #RED TAPE METER 60
                            dic['BraidPims3_63'] = fixedInt(json_obj['M-B_P_3-62']) #RED TAPE METER 61
                            dic['BraidPims3_64'] = fixedInt(json_obj['M-B_P_3-63']) #RED TAPE METER 62
                            dic['BraidPims3_65'] = fixedInt(json_obj['M-B_P_3-64']) #RED TAPE METER 63
                            dic['BraidPims3_66'] = fixedInt(json_obj['M-B_P_3-65']) #RED TAPE METER 64
                            dic['BraidPims3_67'] = fixedInt(json_obj['M-B_P_3-66']) #RED TAPE METER 65
                            dic['BraidPims3_68'] = fixedInt(json_obj['M-B_P_3-67'])#RED TAPE METER 66
                            dic['BraidPims3_69'] = fixedInt(json_obj['M-B_P_3-68']) #RED TAPE METER 67
                            dic['BraidPims3_70'] = fixedInt(json_obj['M-B_P_3-69']) #RED TAPE METER 68
                            dic['BraidPims3_71'] = fixedInt(json_obj['M-B_P_3-70']) #RED TAPE METER 69
                            dic['BraidPims3_72'] = fixedInt(json_obj['M-B_P_3-71']) #RED TAPE METER 70
                            dic['BraidPims3_73'] = fixedInt(json_obj['M-B_P_3-72']) #RED TAPE METER 71
                            dic['BraidPims3_74'] = fixedInt(json_obj['M-B_P_3-73']) #RED TAPE METER 72
                            dic['BraidPims3_75'] = fixedInt(json_obj['M-B_P_3-74']) #RED TAPE METER 73
                            dic['BraidPims3_76'] = fixedInt(json_obj['M-B_P_3-75']) #RED TAPE METER 74
                            dic['BraidPims3_77'] = fixedInt(json_obj['M-B_P_3-76']) #RED TAPE METER 75
                            dic['BraidPims3_78'] = fixedInt(json_obj['M-B_P_3-77']) #RED TAPE METER 76
                            dic['BraidPims3_79'] = fixedInt(json_obj['M-B_P_3-78']) #RED TAPE METER 77
                            dic['BraidPims3_80'] = fixedInt(json_obj['M-B_P_3-79']) #RED TAPE METER 78
                            dic['BraidPims3_81'] = fixedInt(json_obj['M-B_P_3-80']) #RED TAPE METER 79
                            dic['BraidPims3_82'] = fixedInt(json_obj['M-B_P_3-81']) #RED TAPE METER 80

                            dic['BraidPims4_1'] = fixedInt(json_obj['M-B_P_4-0']) #DRUM IN
                            dic['BraidPims4_2'] = fixedInt(json_obj['M-B_P_4-1']) #DRUM OUT
                            dic['BraidPims4_3'] = fixedInt(json_obj['M-B_P_4-2']) #RED TAPE METER 1
                            dic['BraidPims4_4'] = fixedInt(json_obj['M-B_P_4-3']) #RED TAPE METER 2
                            dic['BraidPims4_5'] = fixedInt(json_obj['M-B_P_4-4']) #RED TAPE METER 3
                            dic['BraidPims4_6'] = fixedInt(json_obj['M-B_P_4-5']) #RED TAPE METER 4
                            dic['BraidPims4_7'] = fixedInt(json_obj['M-B_P_4-6']) #RED TAPE METER 5
                            dic['BraidPims4_8'] = fixedInt(json_obj['M-B_P_4-7']) #RED TAPE METER 6
                            dic['BraidPims4_9'] = fixedInt(json_obj['M-B_P_4-8']) #RED TAPE METER 7
                            dic['BraidPims4_10'] = fixedInt(json_obj['M-B_P_4-9']) #RED TAPE METER 8
                            dic['BraidPims4_11'] = fixedInt(json_obj['M-B_P_4-10']) #RED TAPE METER 9
                            dic['BraidPims4_12'] = fixedInt(json_obj['M-B_P_4-11']) #RED TAPE METER 10
                            dic['BraidPims4_13'] = fixedInt(json_obj['M-B_P_4-12']) #RED TAPE METER 11
                            dic['BraidPims4_14'] = fixedInt(json_obj['M-B_P_4-13']) #RED TAPE METER 12
                            dic['BraidPims4_15'] = fixedInt(json_obj['M-B_P_4-14']) #RED TAPE METER 13
                            dic['BraidPims4_16'] = fixedInt(json_obj['M-B_P_4-15'])#RED TAPE METER 14
                            dic['BraidPims4_17'] = fixedInt(json_obj['M-B_P_4-16']) #RED TAPE METER 15
                            dic['BraidPims4_18'] = fixedInt(json_obj['M-B_P_4-17']) #RED TAPE METER 16
                            dic['BraidPims4_19'] = fixedInt(json_obj['M-B_P_4-18']) #RED TAPE METER 17
                            dic['BraidPims4_20'] = fixedInt(json_obj['M-B_P_4-19']) #RED TAPE METER 18
                            dic['BraidPims4_21'] = fixedInt(json_obj['M-B_P_4-20']) #RED TAPE METER 19
                            dic['BraidPims4_22'] = fixedInt(json_obj['M-B_P_4-21']) #RED TAPE METER 20
                            dic['BraidPims4_23'] = fixedInt(json_obj['M-B_P_4-22']) #RED TAPE METER 21
                            dic['BraidPims4_24'] = fixedInt(json_obj['M-B_P_4-23']) #RED TAPE METER 22
                            dic['BraidPims4_25'] = fixedInt(json_obj['M-B_P_4-24']) #RED TAPE METER 23
                            dic['BraidPims4_26'] = fixedInt(json_obj['M-B_P_4-25']) #RED TAPE METER 24
                            dic['BraidPims4_27'] = fixedInt(json_obj['M-B_P_4-26']) #RED TAPE METER 25
                            dic['BraidPims4_28'] = fixedInt(json_obj['M-B_P_4-27']) #RED TAPE METER 26
                            dic['BraidPims4_29'] = fixedInt(json_obj['M-B_P_4-28']) #RED TAPE METER 27
                            dic['BraidPims4_30'] = fixedInt(json_obj['M-B_P_4-29']) #RED TAPE METER 28
                            dic['BraidPims4_31'] = fixedInt(json_obj['M-B_P_4-30']) #RED TAPE METER 29
                            dic['BraidPims4_32'] = fixedInt(json_obj['M-B_P_4-31'])#RED TAPE METER 30
                            dic['BraidPims4_33'] = fixedInt(json_obj['M-B_P_4-32']) #RED TAPE METER 31
                            dic['BraidPims4_34'] = fixedInt(json_obj['M-B_P_4-33']) #RED TAPE METER 32
                            dic['BraidPims4_35'] = fixedInt(json_obj['M-B_P_4-34']) #RED TAPE METER 33
                            dic['BraidPims4_36'] = fixedInt(json_obj['M-B_P_4-35']) #RED TAPE METER 34
                            dic['BraidPims4_37'] = fixedInt(json_obj['M-B_P_4-36']) #RED TAPE METER 35
                            dic['BraidPims4_38'] = fixedInt(json_obj['M-B_P_4-37']) #RED TAPE METER 36
                            dic['BraidPims4_39'] = fixedInt(json_obj['M-B_P_4-38']) #RED TAPE METER 37
                            dic['BraidPims4_40'] = fixedInt(json_obj['M-B_P_4-39']) #RED TAPE METER 38
                            dic['BraidPims4_41'] = fixedInt(json_obj['M-B_P_4-40']) #RED TAPE METER 39
                            dic['BraidPims4_42'] = fixedInt(json_obj['M-B_P_4-41']) #RED TAPE METER 40
                            dic['BraidPims4_43'] = fixedInt(json_obj['M-B_P_4-42']) #RED TAPE METER 41
                            dic['BraidPims4_44'] = fixedInt(json_obj['M-B_P_4-43']) #RED TAPE METER 42
                            dic['BraidPims4_45'] = fixedInt(json_obj['M-B_P_4-44']) #RED TAPE METER 43
                            dic['BraidPims4_46'] = fixedInt(json_obj['M-B_P_4-45']) #RED TAPE METER 44
                            dic['BraidPims4_47'] = fixedInt(json_obj['M-B_P_4-46']) #RED TAPE METER 45
                            dic['BraidPims4_48'] = fixedInt(json_obj['M-B_P_4-47']) #RED TAPE METER 46
                            dic['BraidPims4_49'] = fixedInt(json_obj['M-B_P_4-48']) #RED TAPE METER 47
                            dic['BraidPims4_50'] = fixedInt(json_obj['M-B_P_4-49']) #RED TAPE METER 48
                            dic['BraidPims4_51'] = fixedInt(json_obj['M-B_P_4-50']) #RED TAPE METER 49
                            dic['BraidPims4_52'] = fixedInt(json_obj['M-B_P_4-51'])#RED TAPE METER 50
                            dic['BraidPims4_53'] = fixedInt(json_obj['M-B_P_4-52']) #RED TAPE METER 51
                            dic['BraidPims4_54'] = fixedInt(json_obj['M-B_P_4-53']) #RED TAPE METER 52
                            dic['BraidPims4_55'] = fixedInt(json_obj['M-B_P_4-54']) #RED TAPE METER 53
                            dic['BraidPims4_56'] = fixedInt(json_obj['M-B_P_4-55']) #RED TAPE METER 54
                            dic['BraidPims4_57'] = fixedInt(json_obj['M-B_P_4-56']) #RED TAPE METER 55
                            dic['BraidPims4_58'] = fixedInt(json_obj['M-B_P_4-57']) #RED TAPE METER 56
                            dic['BraidPims4_59'] = fixedInt(json_obj['M-B_P_4-58']) #RED TAPE METER 57
                            dic['BraidPims4_60'] = fixedInt(json_obj['M-B_P_4-59']) #RED TAPE METER 58
                            dic['BraidPims4_61'] = fixedInt(json_obj['M-B_P_4-60']) #RED TAPE METER 59
                            dic['BraidPims4_62'] = fixedInt(json_obj['M-B_P_4-61']) #RED TAPE METER 60
                            dic['BraidPims4_63'] = fixedInt(json_obj['M-B_P_4-62']) #RED TAPE METER 61
                            dic['BraidPims4_64'] = fixedInt(json_obj['M-B_P_4-63']) #RED TAPE METER 62
                            dic['BraidPims4_65'] = fixedInt(json_obj['M-B_P_4-64']) #RED TAPE METER 63
                            dic['BraidPims4_66'] = fixedInt(json_obj['M-B_P_4-65']) #RED TAPE METER 64
                            dic['BraidPims4_67'] = fixedInt(json_obj['M-B_P_4-66']) #RED TAPE METER 65
                            dic['BraidPims4_68'] = fixedInt(json_obj['M-B_P_4-67'])#RED TAPE METER 66
                            dic['BraidPims4_69'] = fixedInt(json_obj['M-B_P_4-68']) #RED TAPE METER 67
                            dic['BraidPims4_70'] = fixedInt(json_obj['M-B_P_4-69']) #RED TAPE METER 68
                            dic['BraidPims4_71'] = fixedInt(json_obj['M-B_P_4-70']) #RED TAPE METER 69
                            dic['BraidPims4_72'] = fixedInt(json_obj['M-B_P_4-71']) #RED TAPE METER 70
                            dic['BraidPims4_73'] = fixedInt(json_obj['M-B_P_4-72']) #RED TAPE METER 71
                            dic['BraidPims4_74'] = fixedInt(json_obj['M-B_P_4-73']) #RED TAPE METER 72
                            dic['BraidPims4_75'] = fixedInt(json_obj['M-B_P_4-74']) #RED TAPE METER 73
                            dic['BraidPims4_76'] = fixedInt(json_obj['M-B_P_4-75']) #RED TAPE METER 74
                            dic['BraidPims4_77'] = fixedInt(json_obj['M-B_P_4-76']) #RED TAPE METER 75
                            dic['BraidPims4_78'] = fixedInt(json_obj['M-B_P_4-77']) #RED TAPE METER 76
                            dic['BraidPims4_79'] = fixedInt(json_obj['M-B_P_4-78']) #RED TAPE METER 77
                            dic['BraidPims4_80'] = fixedInt(json_obj['M-B_P_4-79']) #RED TAPE METER 78
                            dic['BraidPims4_81'] = fixedInt(json_obj['M-B_P_4-80']) #RED TAPE METER 79
                            dic['BraidPims4_82'] = fixedInt(json_obj['M-B_P_4-81']) #RED TAPE METER 80

                            dic['BraidPims5_1'] = fixedInt(json_obj['M-B_P_5-0']) #DRUM IN
                            dic['BraidPims5_2'] = fixedInt(json_obj['M-B_P_5-1']) #DRUM OUT
                            dic['BraidPims5_3'] = fixedInt(json_obj['M-B_P_5-2']) #RED TAPE METER 1
                            dic['BraidPims5_4'] = fixedInt(json_obj['M-B_P_5-3']) #RED TAPE METER 2
                            dic['BraidPims5_5'] = fixedInt(json_obj['M-B_P_5-4']) #RED TAPE METER 3
                            dic['BraidPims5_6'] = fixedInt(json_obj['M-B_P_5-5']) #RED TAPE METER 4
                            dic['BraidPims5_7'] = fixedInt(json_obj['M-B_P_5-6']) #RED TAPE METER 5
                            dic['BraidPims5_8'] = fixedInt(json_obj['M-B_P_5-7']) #RED TAPE METER 6
                            dic['BraidPims5_9'] = fixedInt(json_obj['M-B_P_5-8']) #RED TAPE METER 7
                            dic['BraidPims5_10'] = fixedInt(json_obj['M-B_P_5-9']) #RED TAPE METER 8
                            dic['BraidPims5_11'] = fixedInt(json_obj['M-B_P_5-10']) #RED TAPE METER 9
                            dic['BraidPims5_12'] = fixedInt(json_obj['M-B_P_5-11']) #RED TAPE METER 10
                            dic['BraidPims5_13'] = fixedInt(json_obj['M-B_P_5-12']) #RED TAPE METER 11
                            dic['BraidPims5_14'] = fixedInt(json_obj['M-B_P_5-13']) #RED TAPE METER 12
                            dic['BraidPims5_15'] = fixedInt(json_obj['M-B_P_5-14']) #RED TAPE METER 13
                            dic['BraidPims5_16'] = fixedInt(json_obj['M-B_P_5-15'])#RED TAPE METER 14
                            dic['BraidPims5_17'] = fixedInt(json_obj['M-B_P_5-16']) #RED TAPE METER 15
                            dic['BraidPims5_18'] = fixedInt(json_obj['M-B_P_5-17']) #RED TAPE METER 16
                            dic['BraidPims5_19'] = fixedInt(json_obj['M-B_P_5-18']) #RED TAPE METER 17
                            dic['BraidPims5_20'] = fixedInt(json_obj['M-B_P_5-19']) #RED TAPE METER 18
                            dic['BraidPims5_21'] = fixedInt(json_obj['M-B_P_5-20']) #RED TAPE METER 19
                            dic['BraidPims5_22'] = fixedInt(json_obj['M-B_P_5-21']) #RED TAPE METER 20
                            dic['BraidPims5_23'] = fixedInt(json_obj['M-B_P_5-22']) #RED TAPE METER 21
                            dic['BraidPims5_24'] = fixedInt(json_obj['M-B_P_5-23']) #RED TAPE METER 22
                            dic['BraidPims5_25'] = fixedInt(json_obj['M-B_P_5-24']) #RED TAPE METER 23
                            dic['BraidPims5_26'] = fixedInt(json_obj['M-B_P_5-25']) #RED TAPE METER 24
                            dic['BraidPims5_27'] = fixedInt(json_obj['M-B_P_5-26']) #RED TAPE METER 25
                            dic['BraidPims5_28'] = fixedInt(json_obj['M-B_P_5-27']) #RED TAPE METER 26
                            dic['BraidPims5_29'] = fixedInt(json_obj['M-B_P_5-28']) #RED TAPE METER 27
                            dic['BraidPims5_30'] = fixedInt(json_obj['M-B_P_5-29']) #RED TAPE METER 28
                            dic['BraidPims5_31'] = fixedInt(json_obj['M-B_P_5-30']) #RED TAPE METER 29
                            dic['BraidPims5_32'] = fixedInt(json_obj['M-B_P_5-31'])#RED TAPE METER 30
                            dic['BraidPims5_33'] = fixedInt(json_obj['M-B_P_5-32']) #RED TAPE METER 31
                            dic['BraidPims5_34'] = fixedInt(json_obj['M-B_P_5-33']) #RED TAPE METER 32
                            dic['BraidPims5_35'] = fixedInt(json_obj['M-B_P_5-34']) #RED TAPE METER 33
                            dic['BraidPims5_36'] = fixedInt(json_obj['M-B_P_5-35']) #RED TAPE METER 34
                            dic['BraidPims5_37'] = fixedInt(json_obj['M-B_P_5-36']) #RED TAPE METER 35
                            dic['BraidPims5_38'] = fixedInt(json_obj['M-B_P_5-37']) #RED TAPE METER 36
                            dic['BraidPims5_39'] = fixedInt(json_obj['M-B_P_5-38']) #RED TAPE METER 37
                            dic['BraidPims5_40'] = fixedInt(json_obj['M-B_P_5-39']) #RED TAPE METER 38
                            dic['BraidPims5_41'] = fixedInt(json_obj['M-B_P_5-40']) #RED TAPE METER 39
                            dic['BraidPims5_42'] = fixedInt(json_obj['M-B_P_5-41']) #RED TAPE METER 40
                            dic['BraidPims5_43'] = fixedInt(json_obj['M-B_P_5-42']) #RED TAPE METER 41
                            dic['BraidPims5_44'] = fixedInt(json_obj['M-B_P_5-43']) #RED TAPE METER 42
                            dic['BraidPims5_45'] = fixedInt(json_obj['M-B_P_5-44']) #RED TAPE METER 43
                            dic['BraidPims5_46'] = fixedInt(json_obj['M-B_P_5-45']) #RED TAPE METER 44
                            dic['BraidPims5_47'] = fixedInt(json_obj['M-B_P_5-46']) #RED TAPE METER 45
                            dic['BraidPims5_48'] = fixedInt(json_obj['M-B_P_5-47']) #RED TAPE METER 46
                            dic['BraidPims5_49'] = fixedInt(json_obj['M-B_P_5-48']) #RED TAPE METER 47
                            dic['BraidPims5_50'] = fixedInt(json_obj['M-B_P_5-49']) #RED TAPE METER 48
                            dic['BraidPims5_51'] = fixedInt(json_obj['M-B_P_5-50']) #RED TAPE METER 49
                            dic['BraidPims5_52'] = fixedInt(json_obj['M-B_P_5-51'])#RED TAPE METER 50
                            dic['BraidPims5_53'] = fixedInt(json_obj['M-B_P_5-52']) #RED TAPE METER 51
                            dic['BraidPims5_54'] = fixedInt(json_obj['M-B_P_5-53']) #RED TAPE METER 52
                            dic['BraidPims5_55'] = fixedInt(json_obj['M-B_P_5-54']) #RED TAPE METER 53
                            dic['BraidPims5_56'] = fixedInt(json_obj['M-B_P_5-55']) #RED TAPE METER 54
                            dic['BraidPims5_57'] = fixedInt(json_obj['M-B_P_5-56']) #RED TAPE METER 55
                            dic['BraidPims5_58'] = fixedInt(json_obj['M-B_P_5-57']) #RED TAPE METER 56
                            dic['BraidPims5_59'] = fixedInt(json_obj['M-B_P_5-58']) #RED TAPE METER 57
                            dic['BraidPims5_60'] = fixedInt(json_obj['M-B_P_5-59']) #RED TAPE METER 58
                            dic['BraidPims5_61'] = fixedInt(json_obj['M-B_P_5-60']) #RED TAPE METER 59
                            dic['BraidPims5_62'] = fixedInt(json_obj['M-B_P_5-61']) #RED TAPE METER 60
                            dic['BraidPims5_63'] = fixedInt(json_obj['M-B_P_5-62']) #RED TAPE METER 61
                            dic['BraidPims5_64'] = fixedInt(json_obj['M-B_P_5-63']) #RED TAPE METER 62
                            dic['BraidPims5_65'] = fixedInt(json_obj['M-B_P_5-64']) #RED TAPE METER 63
                            dic['BraidPims5_66'] = fixedInt(json_obj['M-B_P_5-65']) #RED TAPE METER 64
                            dic['BraidPims5_67'] = fixedInt(json_obj['M-B_P_5-66']) #RED TAPE METER 65
                            dic['BraidPims5_68'] = fixedInt(json_obj['M-B_P_5-67'])#RED TAPE METER 66
                            dic['BraidPims5_69'] = fixedInt(json_obj['M-B_P_5-68']) #RED TAPE METER 67
                            dic['BraidPims5_70'] = fixedInt(json_obj['M-B_P_5-69']) #RED TAPE METER 68
                            dic['BraidPims5_71'] = fixedInt(json_obj['M-B_P_5-70']) #RED TAPE METER 69
                            dic['BraidPims5_72'] = fixedInt(json_obj['M-B_P_5-71']) #RED TAPE METER 70
                            dic['BraidPims5_73'] = fixedInt(json_obj['M-B_P_5-72']) #RED TAPE METER 71
                            dic['BraidPims5_74'] = fixedInt(json_obj['M-B_P_5-73']) #RED TAPE METER 72
                            dic['BraidPims5_75'] = fixedInt(json_obj['M-B_P_5-74']) #RED TAPE METER 73
                            dic['BraidPims5_76'] = fixedInt(json_obj['M-B_P_5-75']) #RED TAPE METER 74
                            dic['BraidPims5_77'] = fixedInt(json_obj['M-B_P_5-76']) #RED TAPE METER 75
                            dic['BraidPims5_78'] = fixedInt(json_obj['M-B_P_5-77']) #RED TAPE METER 76
                            dic['BraidPims5_79'] = fixedInt(json_obj['M-B_P_5-78']) #RED TAPE METER 77
                            dic['BraidPims5_80'] = fixedInt(json_obj['M-B_P_5-79']) #RED TAPE METER 78
                            dic['BraidPims5_81'] = fixedInt(json_obj['M-B_P_5-80']) #RED TAPE METER 79
                            dic['BraidPims5_82'] = fixedInt(json_obj['M-B_P_5-81']) #RED TAPE METER 80

                            dic['BraidPims6_1'] = fixedInt(json_obj['M-B_P_6-0']) #DRUM IN
                            dic['BraidPims6_2'] = fixedInt(json_obj['M-B_P_6-1']) #DRUM OUT
                            dic['BraidPims6_3'] = fixedInt(json_obj['M-B_P_6-2']) #RED TAPE METER 1
                            dic['BraidPims6_4'] = fixedInt(json_obj['M-B_P_6-3']) #RED TAPE METER 2
                            dic['BraidPims6_5'] = fixedInt(json_obj['M-B_P_6-4']) #RED TAPE METER 3
                            dic['BraidPims6_6'] = fixedInt(json_obj['M-B_P_6-5']) #RED TAPE METER 4
                            dic['BraidPims6_7'] = fixedInt(json_obj['M-B_P_6-6']) #RED TAPE METER 5
                            dic['BraidPims6_8'] = fixedInt(json_obj['M-B_P_6-7']) #RED TAPE METER 6
                            dic['BraidPims6_9'] = fixedInt(json_obj['M-B_P_6-8']) #RED TAPE METER 7
                            dic['BraidPims6_10'] = fixedInt(json_obj['M-B_P_6-9']) #RED TAPE METER 8
                            dic['BraidPims6_11'] = fixedInt(json_obj['M-B_P_6-10']) #RED TAPE METER 9
                            dic['BraidPims6_12'] = fixedInt(json_obj['M-B_P_6-11']) #RED TAPE METER 10
                            dic['BraidPims6_13'] = fixedInt(json_obj['M-B_P_6-12']) #RED TAPE METER 11
                            dic['BraidPims6_14'] = fixedInt(json_obj['M-B_P_6-13']) #RED TAPE METER 12
                            dic['BraidPims6_15'] = fixedInt(json_obj['M-B_P_6-14']) #RED TAPE METER 13
                            dic['BraidPims6_16'] = fixedInt(json_obj['M-B_P_6-15'])#RED TAPE METER 14
                            dic['BraidPims6_17'] = fixedInt(json_obj['M-B_P_6-16']) #RED TAPE METER 15
                            dic['BraidPims6_18'] = fixedInt(json_obj['M-B_P_6-17']) #RED TAPE METER 16
                            dic['BraidPims6_19'] = fixedInt(json_obj['M-B_P_6-18']) #RED TAPE METER 17
                            dic['BraidPims6_20'] = fixedInt(json_obj['M-B_P_6-19']) #RED TAPE METER 18
                            dic['BraidPims6_21'] = fixedInt(json_obj['M-B_P_6-20']) #RED TAPE METER 19
                            dic['BraidPims6_22'] = fixedInt(json_obj['M-B_P_6-21']) #RED TAPE METER 20
                            dic['BraidPims6_23'] = fixedInt(json_obj['M-B_P_6-22']) #RED TAPE METER 21
                            dic['BraidPims6_24'] = fixedInt(json_obj['M-B_P_6-23']) #RED TAPE METER 22
                            dic['BraidPims6_25'] = fixedInt(json_obj['M-B_P_6-24']) #RED TAPE METER 23
                            dic['BraidPims6_26'] = fixedInt(json_obj['M-B_P_6-25']) #RED TAPE METER 24
                            dic['BraidPims6_27'] = fixedInt(json_obj['M-B_P_6-26']) #RED TAPE METER 25
                            dic['BraidPims6_28'] = fixedInt(json_obj['M-B_P_6-27']) #RED TAPE METER 26
                            dic['BraidPims6_29'] = fixedInt(json_obj['M-B_P_6-28']) #RED TAPE METER 27
                            dic['BraidPims6_30'] = fixedInt(json_obj['M-B_P_6-29']) #RED TAPE METER 28
                            dic['BraidPims6_31'] = fixedInt(json_obj['M-B_P_6-30']) #RED TAPE METER 29
                            dic['BraidPims6_32'] = fixedInt(json_obj['M-B_P_6-31'])#RED TAPE METER 30
                            dic['BraidPims6_33'] = fixedInt(json_obj['M-B_P_6-32']) #RED TAPE METER 31
                            dic['BraidPims6_34'] = fixedInt(json_obj['M-B_P_6-33']) #RED TAPE METER 32
                            dic['BraidPims6_35'] = fixedInt(json_obj['M-B_P_6-34']) #RED TAPE METER 33
                            dic['BraidPims6_36'] = fixedInt(json_obj['M-B_P_6-35']) #RED TAPE METER 34
                            dic['BraidPims6_37'] = fixedInt(json_obj['M-B_P_6-36']) #RED TAPE METER 35
                            dic['BraidPims6_38'] = fixedInt(json_obj['M-B_P_6-37']) #RED TAPE METER 36
                            dic['BraidPims6_39'] = fixedInt(json_obj['M-B_P_6-38']) #RED TAPE METER 37
                            dic['BraidPims6_40'] = fixedInt(json_obj['M-B_P_6-39']) #RED TAPE METER 38
                            dic['BraidPims6_41'] = fixedInt(json_obj['M-B_P_6-40']) #RED TAPE METER 39
                            dic['BraidPims6_42'] = fixedInt(json_obj['M-B_P_6-41']) #RED TAPE METER 40
                            dic['BraidPims6_43'] = fixedInt(json_obj['M-B_P_6-42']) #RED TAPE METER 41
                            dic['BraidPims6_44'] = fixedInt(json_obj['M-B_P_6-43']) #RED TAPE METER 42
                            dic['BraidPims6_45'] = fixedInt(json_obj['M-B_P_6-44']) #RED TAPE METER 43
                            dic['BraidPims6_46'] = fixedInt(json_obj['M-B_P_6-45']) #RED TAPE METER 44
                            dic['BraidPims6_47'] = fixedInt(json_obj['M-B_P_6-46']) #RED TAPE METER 45
                            dic['BraidPims6_48'] = fixedInt(json_obj['M-B_P_6-47']) #RED TAPE METER 46
                            dic['BraidPims6_49'] = fixedInt(json_obj['M-B_P_6-48']) #RED TAPE METER 47
                            dic['BraidPims6_50'] = fixedInt(json_obj['M-B_P_6-49']) #RED TAPE METER 48
                            dic['BraidPims6_51'] = fixedInt(json_obj['M-B_P_6-50']) #RED TAPE METER 49
                            dic['BraidPims6_52'] = fixedInt(json_obj['M-B_P_6-51'])#RED TAPE METER 50
                            dic['BraidPims6_53'] = fixedInt(json_obj['M-B_P_6-52']) #RED TAPE METER 51
                            dic['BraidPims6_54'] = fixedInt(json_obj['M-B_P_6-53']) #RED TAPE METER 52
                            dic['BraidPims6_55'] = fixedInt(json_obj['M-B_P_6-54']) #RED TAPE METER 53
                            dic['BraidPims6_56'] = fixedInt(json_obj['M-B_P_6-55']) #RED TAPE METER 54
                            dic['BraidPims6_57'] = fixedInt(json_obj['M-B_P_6-56']) #RED TAPE METER 55
                            dic['BraidPims6_58'] = fixedInt(json_obj['M-B_P_6-57']) #RED TAPE METER 56
                            dic['BraidPims6_59'] = fixedInt(json_obj['M-B_P_6-58']) #RED TAPE METER 57
                            dic['BraidPims6_60'] = fixedInt(json_obj['M-B_P_6-59']) #RED TAPE METER 58
                            dic['BraidPims6_61'] = fixedInt(json_obj['M-B_P_6-60']) #RED TAPE METER 59
                            dic['BraidPims6_62'] = fixedInt(json_obj['M-B_P_6-61']) #RED TAPE METER 60
                            dic['BraidPims6_63'] = fixedInt(json_obj['M-B_P_6-62']) #RED TAPE METER 61
                            dic['BraidPims6_64'] = fixedInt(json_obj['M-B_P_6-63']) #RED TAPE METER 62
                            dic['BraidPims6_65'] = fixedInt(json_obj['M-B_P_6-64']) #RED TAPE METER 63
                            dic['BraidPims6_66'] = fixedInt(json_obj['M-B_P_6-65']) #RED TAPE METER 64
                            dic['BraidPims6_67'] = fixedInt(json_obj['M-B_P_6-66']) #RED TAPE METER 65
                            dic['BraidPims6_68'] = fixedInt(json_obj['M-B_P_6-67'])#RED TAPE METER 66
                            dic['BraidPims6_69'] = fixedInt(json_obj['M-B_P_6-68']) #RED TAPE METER 67
                            dic['BraidPims6_70'] = fixedInt(json_obj['M-B_P_6-69']) #RED TAPE METER 68
                            dic['BraidPims6_71'] = fixedInt(json_obj['M-B_P_6-70']) #RED TAPE METER 69
                            dic['BraidPims6_72'] = fixedInt(json_obj['M-B_P_6-71']) #RED TAPE METER 70
                            dic['BraidPims6_73'] = fixedInt(json_obj['M-B_P_6-72']) #RED TAPE METER 71
                            dic['BraidPims6_74'] = fixedInt(json_obj['M-B_P_6-73']) #RED TAPE METER 72
                            dic['BraidPims6_75'] = fixedInt(json_obj['M-B_P_6-74']) #RED TAPE METER 73
                            dic['BraidPims6_76'] = fixedInt(json_obj['M-B_P_6-75']) #RED TAPE METER 74
                            dic['BraidPims6_77'] = fixedInt(json_obj['M-B_P_6-76']) #RED TAPE METER 75
                            dic['BraidPims6_78'] = fixedInt(json_obj['M-B_P_6-77']) #RED TAPE METER 76
                            dic['BraidPims6_79'] = fixedInt(json_obj['M-B_P_6-78']) #RED TAPE METER 77
                            dic['BraidPims6_80'] = fixedInt(json_obj['M-B_P_6-79']) #RED TAPE METER 78
                            dic['BraidPims6_81'] = fixedInt(json_obj['M-B_P_6-80']) #RED TAPE METER 79
                            dic['BraidPims6_82'] = fixedInt(json_obj['M-B_P_6-81']) #RED TAPE METER 80

                            dic['BraidPims7_1'] = fixedInt(json_obj['M-B_P_7-0']) #DRUM IN
                            dic['BraidPims7_2'] = fixedInt(json_obj['M-B_P_7-1']) #DRUM OUT
                            dic['BraidPims7_3'] = fixedInt(json_obj['M-B_P_7-2']) #RED TAPE METER 1
                            dic['BraidPims7_4'] = fixedInt(json_obj['M-B_P_7-3']) #RED TAPE METER 2
                            dic['BraidPims7_5'] = fixedInt(json_obj['M-B_P_7-4']) #RED TAPE METER 3
                            dic['BraidPims7_6'] = fixedInt(json_obj['M-B_P_7-5']) #RED TAPE METER 4
                            dic['BraidPims7_7'] = fixedInt(json_obj['M-B_P_7-6']) #RED TAPE METER 5
                            dic['BraidPims7_8'] = fixedInt(json_obj['M-B_P_7-7']) #RED TAPE METER 6
                            dic['BraidPims7_9'] = fixedInt(json_obj['M-B_P_7-8']) #RED TAPE METER 7
                            dic['BraidPims7_10'] = fixedInt(json_obj['M-B_P_7-9']) #RED TAPE METER 8
                            dic['BraidPims7_11'] = fixedInt(json_obj['M-B_P_7-10']) #RED TAPE METER 9
                            dic['BraidPims7_12'] = fixedInt(json_obj['M-B_P_7-11']) #RED TAPE METER 10
                            dic['BraidPims7_13'] = fixedInt(json_obj['M-B_P_7-12']) #RED TAPE METER 11
                            dic['BraidPims7_14'] = fixedInt(json_obj['M-B_P_7-13']) #RED TAPE METER 12
                            dic['BraidPims7_15'] = fixedInt(json_obj['M-B_P_7-14']) #RED TAPE METER 13
                            dic['BraidPims7_16'] = fixedInt(json_obj['M-B_P_7-15'])#RED TAPE METER 14
                            dic['BraidPims7_17'] = fixedInt(json_obj['M-B_P_7-16']) #RED TAPE METER 15
                            dic['BraidPims7_18'] = fixedInt(json_obj['M-B_P_7-17']) #RED TAPE METER 16
                            dic['BraidPims7_19'] = fixedInt(json_obj['M-B_P_7-18']) #RED TAPE METER 17
                            dic['BraidPims7_20'] = fixedInt(json_obj['M-B_P_7-19']) #RED TAPE METER 18
                            dic['BraidPims7_21'] = fixedInt(json_obj['M-B_P_7-20']) #RED TAPE METER 19
                            dic['BraidPims7_22'] = fixedInt(json_obj['M-B_P_7-21']) #RED TAPE METER 20
                            dic['BraidPims7_23'] = fixedInt(json_obj['M-B_P_7-22']) #RED TAPE METER 21
                            dic['BraidPims7_24'] = fixedInt(json_obj['M-B_P_7-23']) #RED TAPE METER 22
                            dic['BraidPims7_25'] = fixedInt(json_obj['M-B_P_7-24']) #RED TAPE METER 23
                            dic['BraidPims7_26'] = fixedInt(json_obj['M-B_P_7-25']) #RED TAPE METER 24
                            dic['BraidPims7_27'] = fixedInt(json_obj['M-B_P_7-26']) #RED TAPE METER 25
                            dic['BraidPims7_28'] = fixedInt(json_obj['M-B_P_7-27']) #RED TAPE METER 26
                            dic['BraidPims7_29'] = fixedInt(json_obj['M-B_P_7-28']) #RED TAPE METER 27
                            dic['BraidPims7_30'] = fixedInt(json_obj['M-B_P_7-29']) #RED TAPE METER 28
                            dic['BraidPims7_31'] = fixedInt(json_obj['M-B_P_7-30']) #RED TAPE METER 29
                            dic['BraidPims7_32'] = fixedInt(json_obj['M-B_P_7-31'])#RED TAPE METER 30
                            dic['BraidPims7_33'] = fixedInt(json_obj['M-B_P_7-32']) #RED TAPE METER 31
                            dic['BraidPims7_34'] = fixedInt(json_obj['M-B_P_7-33']) #RED TAPE METER 32
                            dic['BraidPims7_35'] = fixedInt(json_obj['M-B_P_7-34']) #RED TAPE METER 33
                            dic['BraidPims7_36'] = fixedInt(json_obj['M-B_P_7-35']) #RED TAPE METER 34
                            dic['BraidPims7_37'] = fixedInt(json_obj['M-B_P_7-36']) #RED TAPE METER 35
                            dic['BraidPims7_38'] = fixedInt(json_obj['M-B_P_7-37']) #RED TAPE METER 36
                            dic['BraidPims7_39'] = fixedInt(json_obj['M-B_P_7-38']) #RED TAPE METER 37
                            dic['BraidPims7_40'] = fixedInt(json_obj['M-B_P_7-39']) #RED TAPE METER 38
                            dic['BraidPims7_41'] = fixedInt(json_obj['M-B_P_7-40']) #RED TAPE METER 39
                            dic['BraidPims7_42'] = fixedInt(json_obj['M-B_P_7-41']) #RED TAPE METER 40
                            dic['BraidPims7_43'] = fixedInt(json_obj['M-B_P_7-42']) #RED TAPE METER 41
                            dic['BraidPims7_44'] = fixedInt(json_obj['M-B_P_7-43']) #RED TAPE METER 42
                            dic['BraidPims7_45'] = fixedInt(json_obj['M-B_P_7-44']) #RED TAPE METER 43
                            dic['BraidPims7_46'] = fixedInt(json_obj['M-B_P_7-45']) #RED TAPE METER 44
                            dic['BraidPims7_47'] = fixedInt(json_obj['M-B_P_7-46']) #RED TAPE METER 45
                            dic['BraidPims7_48'] = fixedInt(json_obj['M-B_P_7-47']) #RED TAPE METER 46
                            dic['BraidPims7_49'] = fixedInt(json_obj['M-B_P_7-48']) #RED TAPE METER 47
                            dic['BraidPims7_50'] = fixedInt(json_obj['M-B_P_7-49']) #RED TAPE METER 48
                            dic['BraidPims7_51'] = fixedInt(json_obj['M-B_P_7-50']) #RED TAPE METER 49
                            dic['BraidPims7_52'] = fixedInt(json_obj['M-B_P_7-51'])#RED TAPE METER 50
                            dic['BraidPims7_53'] = fixedInt(json_obj['M-B_P_7-52']) #RED TAPE METER 51
                            dic['BraidPims7_54'] = fixedInt(json_obj['M-B_P_7-53']) #RED TAPE METER 52
                            dic['BraidPims7_55'] = fixedInt(json_obj['M-B_P_7-54']) #RED TAPE METER 53
                            dic['BraidPims7_56'] = fixedInt(json_obj['M-B_P_7-55']) #RED TAPE METER 54
                            dic['BraidPims7_57'] = fixedInt(json_obj['M-B_P_7-56']) #RED TAPE METER 55
                            dic['BraidPims7_58'] = fixedInt(json_obj['M-B_P_7-57']) #RED TAPE METER 56
                            dic['BraidPims7_59'] = fixedInt(json_obj['M-B_P_7-58']) #RED TAPE METER 57
                            dic['BraidPims7_60'] = fixedInt(json_obj['M-B_P_7-59']) #RED TAPE METER 58
                            dic['BraidPims7_61'] = fixedInt(json_obj['M-B_P_7-60']) #RED TAPE METER 59
                            dic['BraidPims7_62'] = fixedInt(json_obj['M-B_P_7-61']) #RED TAPE METER 60
                            dic['BraidPims7_63'] = fixedInt(json_obj['M-B_P_7-62']) #RED TAPE METER 61
                            dic['BraidPims7_64'] = fixedInt(json_obj['M-B_P_7-63']) #RED TAPE METER 62
                            dic['BraidPims7_65'] = fixedInt(json_obj['M-B_P_7-64']) #RED TAPE METER 63
                            dic['BraidPims7_66'] = fixedInt(json_obj['M-B_P_7-65']) #RED TAPE METER 64
                            dic['BraidPims7_67'] = fixedInt(json_obj['M-B_P_7-66']) #RED TAPE METER 65
                            dic['BraidPims7_68'] = fixedInt(json_obj['M-B_P_7-67'])#RED TAPE METER 66
                            dic['BraidPims7_69'] = fixedInt(json_obj['M-B_P_7-68']) #RED TAPE METER 67
                            dic['BraidPims7_70'] = fixedInt(json_obj['M-B_P_7-69']) #RED TAPE METER 68
                            dic['BraidPims7_71'] = fixedInt(json_obj['M-B_P_7-70']) #RED TAPE METER 69
                            dic['BraidPims7_72'] = fixedInt(json_obj['M-B_P_7-71']) #RED TAPE METER 70
                            dic['BraidPims7_73'] = fixedInt(json_obj['M-B_P_7-72']) #RED TAPE METER 71
                            dic['BraidPims7_74'] = fixedInt(json_obj['M-B_P_7-73']) #RED TAPE METER 72
                            dic['BraidPims7_75'] = fixedInt(json_obj['M-B_P_7-74']) #RED TAPE METER 73
                            dic['BraidPims7_76'] = fixedInt(json_obj['M-B_P_7-75']) #RED TAPE METER 74
                            dic['BraidPims7_77'] = fixedInt(json_obj['M-B_P_7-76']) #RED TAPE METER 75
                            dic['BraidPims7_78'] = fixedInt(json_obj['M-B_P_7-77']) #RED TAPE METER 76
                            dic['BraidPims7_79'] = fixedInt(json_obj['M-B_P_7-78']) #RED TAPE METER 77
                            dic['BraidPims7_80'] = fixedInt(json_obj['M-B_P_7-79']) #RED TAPE METER 78
                            dic['BraidPims7_81'] = fixedInt(json_obj['M-B_P_7-80']) #RED TAPE METER 79
                            dic['BraidPims7_82'] = fixedInt(json_obj['M-B_P_7-81']) #RED TAPE METER 80

                            dic['BraidPims8_1'] = fixedInt(json_obj['M-B_P_8-0']) #DRUM IN
                            dic['BraidPims8_2'] = fixedInt(json_obj['M-B_P_8-1']) #DRUM OUT
                            dic['BraidPims8_3'] = fixedInt(json_obj['M-B_P_8-2']) #RED TAPE METER 1
                            dic['BraidPims8_4'] = fixedInt(json_obj['M-B_P_8-3']) #RED TAPE METER 2
                            dic['BraidPims8_5'] = fixedInt(json_obj['M-B_P_8-4']) #RED TAPE METER 3
                            dic['BraidPims8_6'] = fixedInt(json_obj['M-B_P_8-5']) #RED TAPE METER 4
                            dic['BraidPims8_7'] = fixedInt(json_obj['M-B_P_8-6']) #RED TAPE METER 5
                            dic['BraidPims8_8'] = fixedInt(json_obj['M-B_P_8-7']) #RED TAPE METER 6
                            dic['BraidPims8_9'] = fixedInt(json_obj['M-B_P_8-8']) #RED TAPE METER 7
                            dic['BraidPims8_10'] = fixedInt(json_obj['M-B_P_8-9']) #RED TAPE METER 8
                            dic['BraidPims8_11'] = fixedInt(json_obj['M-B_P_8-10']) #RED TAPE METER 9
                            dic['BraidPims8_12'] = fixedInt(json_obj['M-B_P_8-11']) #RED TAPE METER 10
                            dic['BraidPims8_13'] = fixedInt(json_obj['M-B_P_8-12']) #RED TAPE METER 11
                            dic['BraidPims8_14'] = fixedInt(json_obj['M-B_P_8-13']) #RED TAPE METER 12
                            dic['BraidPims8_15'] = fixedInt(json_obj['M-B_P_8-14']) #RED TAPE METER 13
                            dic['BraidPims8_16'] = fixedInt(json_obj['M-B_P_8-15'])#RED TAPE METER 14
                            dic['BraidPims8_17'] = fixedInt(json_obj['M-B_P_8-16']) #RED TAPE METER 15
                            dic['BraidPims8_18'] = fixedInt(json_obj['M-B_P_8-17']) #RED TAPE METER 16
                            dic['BraidPims8_19'] = fixedInt(json_obj['M-B_P_8-18']) #RED TAPE METER 17
                            dic['BraidPims8_20'] = fixedInt(json_obj['M-B_P_8-19']) #RED TAPE METER 18
                            dic['BraidPims8_21'] = fixedInt(json_obj['M-B_P_8-20']) #RED TAPE METER 19
                            dic['BraidPims8_22'] = fixedInt(json_obj['M-B_P_8-21']) #RED TAPE METER 20
                            dic['BraidPims8_23'] = fixedInt(json_obj['M-B_P_8-22']) #RED TAPE METER 21
                            dic['BraidPims8_24'] = fixedInt(json_obj['M-B_P_8-23']) #RED TAPE METER 22
                            dic['BraidPims8_25'] = fixedInt(json_obj['M-B_P_8-24']) #RED TAPE METER 23
                            dic['BraidPims8_26'] = fixedInt(json_obj['M-B_P_8-25']) #RED TAPE METER 24
                            dic['BraidPims8_27'] = fixedInt(json_obj['M-B_P_8-26']) #RED TAPE METER 25
                            dic['BraidPims8_28'] = fixedInt(json_obj['M-B_P_8-27']) #RED TAPE METER 26
                            dic['BraidPims8_29'] = fixedInt(json_obj['M-B_P_8-28']) #RED TAPE METER 27
                            dic['BraidPims8_30'] = fixedInt(json_obj['M-B_P_8-29']) #RED TAPE METER 28
                            dic['BraidPims8_31'] = fixedInt(json_obj['M-B_P_8-30']) #RED TAPE METER 29
                            dic['BraidPims8_32'] = fixedInt(json_obj['M-B_P_8-31'])#RED TAPE METER 30
                            dic['BraidPims8_33'] = fixedInt(json_obj['M-B_P_8-32']) #RED TAPE METER 31
                            dic['BraidPims8_34'] = fixedInt(json_obj['M-B_P_8-33']) #RED TAPE METER 32
                            dic['BraidPims8_35'] = fixedInt(json_obj['M-B_P_8-34']) #RED TAPE METER 33
                            dic['BraidPims8_36'] = fixedInt(json_obj['M-B_P_8-35']) #RED TAPE METER 34
                            dic['BraidPims8_37'] = fixedInt(json_obj['M-B_P_8-36']) #RED TAPE METER 35
                            dic['BraidPims8_38'] = fixedInt(json_obj['M-B_P_8-37']) #RED TAPE METER 36
                            dic['BraidPims8_39'] = fixedInt(json_obj['M-B_P_8-38']) #RED TAPE METER 37
                            dic['BraidPims8_40'] = fixedInt(json_obj['M-B_P_8-39']) #RED TAPE METER 38
                            dic['BraidPims8_41'] = fixedInt(json_obj['M-B_P_8-40']) #RED TAPE METER 39
                            dic['BraidPims8_42'] = fixedInt(json_obj['M-B_P_8-41']) #RED TAPE METER 40
                            dic['BraidPims8_43'] = fixedInt(json_obj['M-B_P_8-42']) #RED TAPE METER 41
                            dic['BraidPims8_44'] = fixedInt(json_obj['M-B_P_8-43']) #RED TAPE METER 42
                            dic['BraidPims8_45'] = fixedInt(json_obj['M-B_P_8-44']) #RED TAPE METER 43
                            dic['BraidPims8_46'] = fixedInt(json_obj['M-B_P_8-45']) #RED TAPE METER 44
                            dic['BraidPims8_47'] = fixedInt(json_obj['M-B_P_8-46']) #RED TAPE METER 45
                            dic['BraidPims8_48'] = fixedInt(json_obj['M-B_P_8-47']) #RED TAPE METER 46
                            dic['BraidPims8_49'] = fixedInt(json_obj['M-B_P_8-48']) #RED TAPE METER 47
                            dic['BraidPims8_50'] = fixedInt(json_obj['M-B_P_8-49']) #RED TAPE METER 48
                            dic['BraidPims8_51'] = fixedInt(json_obj['M-B_P_8-50']) #RED TAPE METER 49
                            dic['BraidPims8_52'] = fixedInt(json_obj['M-B_P_8-51'])#RED TAPE METER 50
                            dic['BraidPims8_53'] = fixedInt(json_obj['M-B_P_8-52']) #RED TAPE METER 51
                            dic['BraidPims8_54'] = fixedInt(json_obj['M-B_P_8-53']) #RED TAPE METER 52
                            dic['BraidPims8_55'] = fixedInt(json_obj['M-B_P_8-54']) #RED TAPE METER 53
                            dic['BraidPims8_56'] = fixedInt(json_obj['M-B_P_8-55']) #RED TAPE METER 54
                            dic['BraidPims8_57'] = fixedInt(json_obj['M-B_P_8-56']) #RED TAPE METER 55
                            dic['BraidPims8_58'] = fixedInt(json_obj['M-B_P_8-57']) #RED TAPE METER 56
                            dic['BraidPims8_59'] = fixedInt(json_obj['M-B_P_8-58']) #RED TAPE METER 57
                            dic['BraidPims8_60'] = fixedInt(json_obj['M-B_P_8-59']) #RED TAPE METER 58
                            dic['BraidPims8_61'] = fixedInt(json_obj['M-B_P_8-60']) #RED TAPE METER 59
                            dic['BraidPims8_62'] = fixedInt(json_obj['M-B_P_8-61']) #RED TAPE METER 60
                            dic['BraidPims8_63'] = fixedInt(json_obj['M-B_P_8-62']) #RED TAPE METER 61
                            dic['BraidPims8_64'] = fixedInt(json_obj['M-B_P_8-63']) #RED TAPE METER 62
                            dic['BraidPims8_65'] = fixedInt(json_obj['M-B_P_8-64']) #RED TAPE METER 63
                            dic['BraidPims8_66'] = fixedInt(json_obj['M-B_P_8-65']) #RED TAPE METER 64
                            dic['BraidPims8_67'] = fixedInt(json_obj['M-B_P_8-66']) #RED TAPE METER 65
                            dic['BraidPims8_68'] = fixedInt(json_obj['M-B_P_8-67'])#RED TAPE METER 66
                            dic['BraidPims8_69'] = fixedInt(json_obj['M-B_P_8-68']) #RED TAPE METER 67
                            dic['BraidPims8_70'] = fixedInt(json_obj['M-B_P_8-69']) #RED TAPE METER 68
                            dic['BraidPims8_71'] = fixedInt(json_obj['M-B_P_8-70']) #RED TAPE METER 69
                            dic['BraidPims8_72'] = fixedInt(json_obj['M-B_P_8-71']) #RED TAPE METER 70
                            dic['BraidPims8_73'] = fixedInt(json_obj['M-B_P_8-72']) #RED TAPE METER 71
                            dic['BraidPims8_74'] = fixedInt(json_obj['M-B_P_8-73']) #RED TAPE METER 72
                            dic['BraidPims8_75'] = fixedInt(json_obj['M-B_P_8-74']) #RED TAPE METER 73
                            dic['BraidPims8_76'] = fixedInt(json_obj['M-B_P_8-75']) #RED TAPE METER 74
                            dic['BraidPims8_77'] = fixedInt(json_obj['M-B_P_8-76']) #RED TAPE METER 75
                            dic['BraidPims8_78'] = fixedInt(json_obj['M-B_P_8-77']) #RED TAPE METER 76
                            dic['BraidPims8_79'] = fixedInt(json_obj['M-B_P_8-78']) #RED TAPE METER 77
                            dic['BraidPims8_80'] = fixedInt(json_obj['M-B_P_8-79']) #RED TAPE METER 78
                            dic['BraidPims8_81'] = fixedInt(json_obj['M-B_P_8-80']) #RED TAPE METER 79
                            dic['BraidPims8_82'] = fixedInt(json_obj['M-B_P_8-81']) #RED TAPE METER 80
                            '''

                            sqlDump()
    except(error):
        print("Error ::", error)
        #continue



def findBool(val):
    return val.lower() in ['1', 'true', 't']

def on_disconnect(client, userdata, rc=0):
    print("disconnect")
    client.loop_stop()



def sqlDump():
    try:
        '''sql = "INSERT INTO demo ( tag1, tag2, tag3, tag4, tag5, tag6, tag7, tag8, tag9, tag10) VALUES (%s, %s, %s ,%s,%s,%s,%s,%s,%s,%s)"
        val = (str(dic['Tag1']), str(dic['Tag2']), str(dic['Tag3']), str(dic['Tag4']), str(dic['Tag5']), str(dic['Tag6']), str(dic['Tag7']), str(dic['Tag8']), str(dic['Tag9']), str(dic['Tag10']))
        mycursor.execute(sql, val)
        '''
        if(int(dic['Braid1_1']) != 0 and int(dic['Braid1_1']) != 1) :
                sql = "INSERT INTO braiderreport1 ( pir , operator_name , deck_set_speed , deck_act_speed , prod_meter , tot_run_hours , blower_set_temp , blower_act_temp , n2_set_temp , n2_inlet_temp , n2_outlet_temp , n2_pressure, tube_dia, no_of_ends, wire_dia, tag_date, deck_gear_1, deck_gear_2, drum_in, drum_out, insulation, batch_no, ply_thick_setvalue, ply_thick_actvalue, ply_width_setvalue, ply_width_actvalue, mach_no, rein_od_spec_1, rein_pitch_spec_1, rein_od_spec_2, rein_pitch_spec_2, rein_od_spec_3, rein_pitch_spec_3, rein_od_fact_1, rein_od_mact_1, rein_od_lact_1, rein_pitch_fact_1, rein_pitch_mact_1, rein_pitch_lact_1, rein_od_fact_2, rein_od_mact_2, rein_od_lact_2, rein_pitch_fact_2, rein_pitch_mact_2, rein_pitch_lact_2, rein_od_fact_3, rein_od_mact_3, rein_od_lact_3, rein_pitch_fact_3, rein_pitch_mact_3, rein_pitch_lact_3, haul_gear_1, haul_gear_2, rein_od_spec_tol_1, rein_pitch_spec_tol_1, rein_od_spec_tol_2, rein_pitch_spec_tol_2, rein_od_spec_tol_3, rein_pitch_spec_tol_3, operator_id, supervisor, oa_approval ) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (str(dic['Braid1_1']), str(dic['Braid1_2']), int(dic['Braid1_3']), int(dic['Braid1_4']), findFloat(float(dic['Braid1_5'])), findFloat(float(dic['Braid1_6'])), findFloat(float(dic['Braid1_7'])), findFloat(float(dic['Braid1_8'])), findFloat(float(dic['Braid1_9'])), findFloat(float(dic['Braid1_10'])), findFloat(float(dic['Braid1_11'])), findFloat(float(dic['Braid1_12'])), str(dic['Braid1_13']), str(dic['Braid1_14']), str(dic['Braid1_15']), str(dic['Braid1_16']), str(dic['Braid1_17']), str(dic['Braid1_18']), str(dic['Braid1_19']), str(dic['Braid1_20']), str(dic['Braid1_21']), str(dic['Braid1_22']), str(dic['Braid1_23']), findFloat(float(dic['Braid1_24'])), str(dic['Braid1_25']), findFloat(float(dic['Braid1_26'])), str(dic['Braid1_27']), findFloat(float(dic['Braid1_28'])), findFloat(float(dic['Braid1_29'])), findFloat(float(dic['Braid1_30'])), findFloat(float(dic['Braid1_31'])), findFloat(float(dic['Braid1_32'])), findFloat(float(dic['Braid1_33'])), findFloat(float(dic['Braid1_34'])), findFloat(float(dic['Braid1_35'])), findFloat(float(dic['Braid1_36'])), findFloat(float(dic['Braid1_37'])), findFloat(float(dic['Braid1_38'])), findFloat(float(dic['Braid1_39'])), findFloat(float(dic['Braid1_40'])), findFloat(float(dic['Braid1_41'])), findFloat(float(dic['Braid1_42'])), findFloat(float(dic['Braid1_43'])), findFloat(float(dic['Braid1_44'])), findFloat(float(dic['Braid1_45'])), findFloat(float(dic['Braid1_46'])), findFloat(float(dic['Braid1_47'])), findFloat(float(dic['Braid1_48'])), findFloat(float(dic['Braid1_49'])), findFloat(float(dic['Braid1_50'])), findFloat(float(dic['Braid1_51'])), str(dic['Braid1_52']), str(dic['Braid1_53']), findFloat(float(dic['Braid1_54'])), findFloat(float(dic['Braid1_55'])), findFloat(float(dic['Braid1_56'])), findFloat(float(dic['Braid1_57'])), findFloat(float(dic['Braid1_58'])), findFloat(float(dic['Braid1_59'])), str(dic['Braid1_60']), str(dic['Braid1_61']), str(dic['Braid1_62']))
                mycursor.execute(sql, val)
        
        if(int(dic['Braid2_1']) != 0 and int(dic['Braid2_1']) != 1) :
                sql = "INSERT INTO braiderreport2 ( pir , operator_name , deck_set_speed , deck_act_speed , prod_meter , tot_run_hours , blower_set_temp , blower_act_temp , n2_set_temp , n2_inlet_temp , n2_outlet_temp , n2_pressure, tube_dia, no_of_ends, wire_dia, tag_date, deck_gear_1, deck_gear_2, drum_in, drum_out, insulation, batch_no, ply_thick_setvalue, ply_thick_actvalue, ply_width_setvalue, ply_width_actvalue, mach_no, rein_od_spec_1, rein_pitch_spec_1, rein_od_spec_2, rein_pitch_spec_2, rein_od_spec_3, rein_pitch_spec_3, rein_od_fact_1, rein_od_mact_1, rein_od_lact_1, rein_pitch_fact_1, rein_pitch_mact_1, rein_pitch_lact_1, rein_od_fact_2, rein_od_mact_2, rein_od_lact_2, rein_pitch_fact_2, rein_pitch_mact_2, rein_pitch_lact_2, rein_od_fact_3, rein_od_mact_3, rein_od_lact_3, rein_pitch_fact_3, rein_pitch_mact_3, rein_pitch_lact_3, haul_gear_1, haul_gear_2, rein_od_spec_tol_1, rein_pitch_spec_tol_1, rein_od_spec_tol_2, rein_pitch_spec_tol_2, rein_od_spec_tol_3, rein_pitch_spec_tol_3, operator_id, supervisor, oa_approval ) VALUES (%s, %s, %s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (str(dic['Braid2_1']), str(dic['Braid2_2']), int(dic['Braid2_3']), int(dic['Braid2_4']), findFloat(float(dic['Braid2_5'])), findFloat(float(dic['Braid2_6'])), findFloat(float(dic['Braid2_7'])), findFloat(float(dic['Braid2_8'])), findFloat(float(dic['Braid2_9'])), findFloat(float(dic['Braid2_10'])), findFloat(float(dic['Braid2_11'])), findFloat(float(dic['Braid2_12'])), str(dic['Braid2_13']), str(dic['Braid2_14']), str(dic['Braid2_15']), str(dic['Braid2_16']), str(dic['Braid2_17']), str(dic['Braid2_18']), str(dic['Braid2_19']), str(dic['Braid2_20']), str(dic['Braid2_21']), str(dic['Braid2_22']), str(dic['Braid2_23']), findFloat(float(dic['Braid2_24'])), str(dic['Braid2_25']), findFloat(float(dic['Braid2_26'])), str(dic['Braid2_27']), findFloat(float(dic['Braid2_28'])), findFloat(float(dic['Braid2_29'])), findFloat(float(dic['Braid2_30'])), findFloat(float(dic['Braid2_31'])), findFloat(float(dic['Braid2_32'])), findFloat(float(dic['Braid2_33'])), findFloat(float(dic['Braid2_34'])), findFloat(float(dic['Braid2_35'])), findFloat(float(dic['Braid2_36'])), findFloat(float(dic['Braid2_37'])), findFloat(float(dic['Braid2_38'])), findFloat(float(dic['Braid2_39'])), findFloat(float(dic['Braid2_40'])), findFloat(float(dic['Braid2_41'])), findFloat(float(dic['Braid2_42'])), findFloat(float(dic['Braid2_43'])), findFloat(float(dic['Braid2_44'])), findFloat(float(dic['Braid2_45'])), findFloat(float(dic['Braid2_46'])), findFloat(float(dic['Braid2_47'])), findFloat(float(dic['Braid2_48'])), findFloat(float(dic['Braid2_49'])), findFloat(float(dic['Braid2_50'])), findFloat(float(dic['Braid2_51'])), str(dic['Braid2_52']), str(dic['Braid2_53']), findFloat(float(dic['Braid2_54'])), findFloat(float(dic['Braid2_55'])), findFloat(float(dic['Braid2_56'])), findFloat(float(dic['Braid2_57'])), findFloat(float(dic['Braid2_58'])), findFloat(float(dic['Braid2_59'])), str(dic['Braid2_60']), str(dic['Braid2_61']), str(dic['Braid2_62']))
                mycursor.execute(sql, val)
        
        if(int(dic['Braid3_1']) != 0 and int(dic['Braid3_1']) != 1) :
                sql = "INSERT INTO braiderreport3 ( pir , operator_name , deck_set_speed , deck_act_speed , prod_meter , tot_run_hours , blower_set_temp , blower_act_temp , n2_set_temp , n2_inlet_temp , n2_outlet_temp , n2_pressure,  tube_dia, no_of_ends, wire_dia, tag_date, deck_gear_1, deck_gear_2, drum_in, drum_out, insulation, batch_no, ply_thick_setvalue, ply_thick_actvalue, ply_width_setvalue, ply_width_actvalue, mach_no, rein_od_spec_1, rein_pitch_spec_1, rein_od_spec_2, rein_pitch_spec_2, rein_od_spec_3, rein_pitch_spec_3, rein_od_fact_1, rein_od_mact_1, rein_od_lact_1, rein_pitch_fact_1, rein_pitch_mact_1, rein_pitch_lact_1, rein_od_fact_2, rein_od_mact_2, rein_od_lact_2, rein_pitch_fact_2, rein_pitch_mact_2, rein_pitch_lact_2, rein_od_fact_3, rein_od_mact_3, rein_od_lact_3, rein_pitch_fact_3, rein_pitch_mact_3, rein_pitch_lact_3, haul_gear_1, haul_gear_2, rein_od_spec_tol_1, rein_pitch_spec_tol_1, rein_od_spec_tol_2, rein_pitch_spec_tol_2, rein_od_spec_tol_3, rein_pitch_spec_tol_3, operator_id, supervisor, oa_approval ) VALUES (%s, %s, %s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (str(dic['Braid3_1']), str(dic['Braid3_2']), int(dic['Braid3_3']), int(dic['Braid3_4']), findFloat(float(dic['Braid3_5'])), findFloat(float(dic['Braid3_6'])), findFloat(float(dic['Braid3_7'])), findFloat(float(dic['Braid3_8'])), findFloat(float(dic['Braid3_9'])), findFloat(float(dic['Braid3_10'])), findFloat(float(dic['Braid3_11'])), findFloat(float(dic['Braid3_12'])), str(dic['Braid3_13']), str(dic['Braid3_14']), str(dic['Braid3_15']), str(dic['Braid3_16']), str(dic['Braid3_17']), str(dic['Braid3_18']), str(dic['Braid3_19']), str(dic['Braid3_20']), str(dic['Braid3_21']), str(dic['Braid3_22']), str(dic['Braid3_23']), findFloat(float(dic['Braid3_24'])), str(dic['Braid3_25']), findFloat(float(dic['Braid3_26'])), str(dic['Braid3_27']), findFloat(float(dic['Braid3_28'])), findFloat(float(dic['Braid3_29'])), findFloat(float(dic['Braid3_30'])), findFloat(float(dic['Braid3_31'])), findFloat(float(dic['Braid3_32'])), findFloat(float(dic['Braid3_33'])), findFloat(float(dic['Braid3_34'])), findFloat(float(dic['Braid3_35'])), findFloat(float(dic['Braid3_36'])), findFloat(float(dic['Braid3_37'])), findFloat(float(dic['Braid3_38'])), findFloat(float(dic['Braid3_39'])), findFloat(float(dic['Braid3_40'])), findFloat(float(dic['Braid3_41'])), findFloat(float(dic['Braid3_42'])), findFloat(float(dic['Braid3_43'])), findFloat(float(dic['Braid3_44'])), findFloat(float(dic['Braid3_45'])), findFloat(float(dic['Braid3_46'])), findFloat(float(dic['Braid3_47'])), findFloat(float(dic['Braid3_48'])), findFloat(float(dic['Braid3_49'])), findFloat(float(dic['Braid3_50'])), findFloat(float(dic['Braid3_51'])), str(dic['Braid3_52']), str(dic['Braid3_53']), findFloat(float(dic['Braid3_54'])), findFloat(float(dic['Braid3_55'])), findFloat(float(dic['Braid3_56'])), findFloat(float(dic['Braid3_57'])), findFloat(float(dic['Braid3_58'])), findFloat(float(dic['Braid3_59'])), str(dic['Braid3_60']), str(dic['Braid3_61']), str(dic['Braid3_62']))
                mycursor.execute(sql, val)
        
        if(int(dic['Braid4_1']) != 0 and int(dic['Braid4_1']) != 1) :
                sql = "INSERT INTO braiderreport4 ( pir , operator_name , deck_set_speed , deck_act_speed , prod_meter , tot_run_hours , blower_set_temp , blower_act_temp , n2_set_temp , n2_inlet_temp , n2_outlet_temp , n2_pressure, tube_dia, no_of_ends, wire_dia, tag_date, deck_gear_1, deck_gear_2, drum_in, drum_out, insulation, batch_no, ply_thick_setvalue, ply_thick_actvalue, ply_width_setvalue, ply_width_actvalue, mach_no, rein_od_spec_1, rein_pitch_spec_1, rein_od_spec_2, rein_pitch_spec_2, rein_od_spec_3, rein_pitch_spec_3, rein_od_fact_1, rein_od_mact_1, rein_od_lact_1, rein_pitch_fact_1, rein_pitch_mact_1, rein_pitch_lact_1, rein_od_fact_2, rein_od_mact_2, rein_od_lact_2, rein_pitch_fact_2, rein_pitch_mact_2, rein_pitch_lact_2, rein_od_fact_3, rein_od_mact_3, rein_od_lact_3, rein_pitch_fact_3, rein_pitch_mact_3, rein_pitch_lact_3, haul_gear_1, haul_gear_2, rein_od_spec_tol_1, rein_pitch_spec_tol_1, rein_od_spec_tol_2, rein_pitch_spec_tol_2, rein_od_spec_tol_3, rein_pitch_spec_tol_3, operator_id, supervisor, oa_approval ) VALUES (%s, %s, %s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (str(dic['Braid4_1']), str(dic['Braid4_2']), int(dic['Braid4_3']), int(dic['Braid4_4']), findFloat(float(dic['Braid4_5'])), findFloat(float(dic['Braid4_6'])), findFloat(float(dic['Braid4_7'])), findFloat(float(dic['Braid4_8'])), findFloat(float(dic['Braid4_9'])), findFloat(float(dic['Braid4_10'])), findFloat(float(dic['Braid4_11'])), findFloat(float(dic['Braid4_12'])), str(dic['Braid4_13']), str(dic['Braid4_14']), str(dic['Braid4_15']), str(dic['Braid4_16']), str(dic['Braid4_17']), str(dic['Braid4_18']), str(dic['Braid4_19']), str(dic['Braid4_20']), str(dic['Braid4_21']), str(dic['Braid4_22']), str(dic['Braid4_23']), findFloat(float(dic['Braid4_24'])), str(dic['Braid4_25']), findFloat(float(dic['Braid4_26'])), str(dic['Braid4_27']), findFloat(float(dic['Braid4_28'])), findFloat(float(dic['Braid4_29'])), findFloat(float(dic['Braid4_30'])), findFloat(float(dic['Braid4_31'])), findFloat(float(dic['Braid4_32'])), findFloat(float(dic['Braid4_33'])), findFloat(float(dic['Braid4_34'])), findFloat(float(dic['Braid4_35'])), findFloat(float(dic['Braid4_36'])), findFloat(float(dic['Braid4_37'])), findFloat(float(dic['Braid4_38'])), findFloat(float(dic['Braid4_39'])), findFloat(float(dic['Braid4_40'])), findFloat(float(dic['Braid4_41'])), findFloat(float(dic['Braid4_42'])), findFloat(float(dic['Braid4_43'])), findFloat(float(dic['Braid4_44'])), findFloat(float(dic['Braid4_45'])), findFloat(float(dic['Braid4_46'])), findFloat(float(dic['Braid4_47'])), findFloat(float(dic['Braid4_48'])), findFloat(float(dic['Braid4_49'])), findFloat(float(dic['Braid4_50'])), findFloat(float(dic['Braid4_51'])), str(dic['Braid4_52']), str(dic['Braid4_53']), findFloat(float(dic['Braid4_54'])), findFloat(float(dic['Braid4_55'])), findFloat(float(dic['Braid4_56'])), findFloat(float(dic['Braid4_57'])), findFloat(float(dic['Braid4_58'])), findFloat(float(dic['Braid4_59'])), str(dic['Braid4_60']), str(dic['Braid4_61']), str(dic['Braid4_62']))
                mycursor.execute(sql, val)
        
        if(int(dic['Braid5_1']) != 0 and int(dic['Braid5_1']) != 1) :
                sql = "INSERT INTO braiderreport5 ( pir , operator_name , deck_set_speed , deck_act_speed , prod_meter , tot_run_hours , blower_set_temp , blower_act_temp , n2_set_temp , n2_inlet_temp , n2_outlet_temp , n2_pressure,  tube_dia, no_of_ends, wire_dia, tag_date, deck_gear_1, deck_gear_2, drum_in, drum_out, insulation, batch_no, ply_thick_setvalue, ply_thick_actvalue, ply_width_setvalue, ply_width_actvalue, mach_no, rein_od_spec_1, rein_pitch_spec_1, rein_od_spec_2, rein_pitch_spec_2, rein_od_spec_3, rein_pitch_spec_3, rein_od_fact_1, rein_od_mact_1, rein_od_lact_1, rein_pitch_fact_1, rein_pitch_mact_1, rein_pitch_lact_1, rein_od_fact_2, rein_od_mact_2, rein_od_lact_2, rein_pitch_fact_2, rein_pitch_mact_2, rein_pitch_lact_2, rein_od_fact_3, rein_od_mact_3, rein_od_lact_3, rein_pitch_fact_3, rein_pitch_mact_3, rein_pitch_lact_3, haul_gear_1, haul_gear_2, rein_od_spec_tol_1, rein_pitch_spec_tol_1, rein_od_spec_tol_2, rein_pitch_spec_tol_2, rein_od_spec_tol_3, rein_pitch_spec_tol_3, operator_id, supervisor, oa_approval ) VALUES (%s, %s, %s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (str(dic['Braid5_1']), str(dic['Braid5_2']), int(dic['Braid5_3']), int(dic['Braid5_4']), findFloat(float(dic['Braid5_5'])), findFloat(float(dic['Braid5_6'])), findFloat(float(dic['Braid5_7'])), findFloat(float(dic['Braid5_8'])), findFloat(float(dic['Braid5_9'])), findFloat(float(dic['Braid5_10'])), findFloat(float(dic['Braid5_11'])), findFloat(float(dic['Braid5_12'])), str(dic['Braid5_13']), str(dic['Braid5_14']), str(dic['Braid5_15']), str(dic['Braid5_16']), str(dic['Braid5_17']), str(dic['Braid5_18']), str(dic['Braid5_19']), str(dic['Braid5_20']), str(dic['Braid5_21']), str(dic['Braid5_22']), str(dic['Braid5_23']), findFloat(float(dic['Braid5_24'])), str(dic['Braid5_25']), findFloat(float(dic['Braid5_26'])), str(dic['Braid5_27']), findFloat(float(dic['Braid5_28'])), findFloat(float(dic['Braid5_29'])), findFloat(float(dic['Braid5_30'])), findFloat(float(dic['Braid5_31'])), findFloat(float(dic['Braid5_32'])), findFloat(float(dic['Braid5_33'])), findFloat(float(dic['Braid5_34'])), findFloat(float(dic['Braid5_35'])), findFloat(float(dic['Braid5_36'])), findFloat(float(dic['Braid5_37'])), findFloat(float(dic['Braid5_38'])), findFloat(float(dic['Braid5_39'])), findFloat(float(dic['Braid5_40'])), findFloat(float(dic['Braid5_41'])), findFloat(float(dic['Braid5_42'])), findFloat(float(dic['Braid5_43'])), findFloat(float(dic['Braid5_44'])), findFloat(float(dic['Braid5_45'])), findFloat(float(dic['Braid5_46'])), findFloat(float(dic['Braid5_47'])), findFloat(float(dic['Braid5_48'])), findFloat(float(dic['Braid5_49'])), findFloat(float(dic['Braid5_50'])), findFloat(float(dic['Braid5_51'])), str(dic['Braid5_52']), str(dic['Braid5_53']), findFloat(float(dic['Braid5_54'])), findFloat(float(dic['Braid5_55'])), findFloat(float(dic['Braid5_56'])), findFloat(float(dic['Braid5_57'])), findFloat(float(dic['Braid5_58'])), findFloat(float(dic['Braid5_59'])), str(dic['Braid5_60']), str(dic['Braid5_61']), str(dic['Braid5_62']))
                mycursor.execute(sql, val)
        
        if(int(dic['Braid6_1']) != 0 and int(dic['Braid6_1']) != 1) : 
                sql = "INSERT INTO braiderreport6 ( pir , operator_name , deck_set_speed , deck_act_speed , prod_meter , tot_run_hours , blower_set_temp , blower_act_temp , n2_set_temp , n2_inlet_temp , n2_outlet_temp , n2_pressure,  tube_dia, no_of_ends, wire_dia, tag_date, deck_gear_1, deck_gear_2, drum_in, drum_out, insulation, batch_no, ply_thick_setvalue, ply_thick_actvalue, ply_width_setvalue, ply_width_actvalue, mach_no, rein_od_spec_1, rein_pitch_spec_1, rein_od_spec_2, rein_pitch_spec_2, rein_od_spec_3, rein_pitch_spec_3, rein_od_fact_1, rein_od_mact_1, rein_od_lact_1, rein_pitch_fact_1, rein_pitch_mact_1, rein_pitch_lact_1, rein_od_fact_2, rein_od_mact_2, rein_od_lact_2, rein_pitch_fact_2, rein_pitch_mact_2, rein_pitch_lact_2, rein_od_fact_3, rein_od_mact_3, rein_od_lact_3, rein_pitch_fact_3, rein_pitch_mact_3, rein_pitch_lact_3, haul_gear_1, haul_gear_2, rein_od_spec_tol_1, rein_pitch_spec_tol_1, rein_od_spec_tol_2, rein_pitch_spec_tol_2, rein_od_spec_tol_3, rein_pitch_spec_tol_3, operator_id, supervisor, oa_approval ) VALUES (%s, %s, %s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (str(dic['Braid6_1']), str(dic['Braid6_2']), int(dic['Braid6_3']), int(dic['Braid6_4']), findFloat(float(dic['Braid6_5'])), findFloat(float(dic['Braid6_6'])), findFloat(float(dic['Braid6_7'])), findFloat(float(dic['Braid6_8'])), findFloat(float(dic['Braid6_9'])), findFloat(float(dic['Braid6_10'])), findFloat(float(dic['Braid6_11'])), findFloat(float(dic['Braid6_12'])), str(dic['Braid6_13']), str(dic['Braid6_14']), str(dic['Braid6_15']), str(dic['Braid6_16']), str(dic['Braid6_17']), str(dic['Braid6_18']), str(dic['Braid6_19']), str(dic['Braid6_20']), str(dic['Braid6_21']), str(dic['Braid6_22']), str(dic['Braid6_23']), findFloat(float(dic['Braid6_24'])), str(dic['Braid6_25']), findFloat(float(dic['Braid6_26'])), str(dic['Braid6_27']), findFloat(float(dic['Braid6_28'])), findFloat(float(dic['Braid6_29'])), findFloat(float(dic['Braid6_30'])), findFloat(float(dic['Braid6_31'])), findFloat(float(dic['Braid6_32'])), findFloat(float(dic['Braid6_33'])), findFloat(float(dic['Braid6_34'])), findFloat(float(dic['Braid6_35'])), findFloat(float(dic['Braid6_36'])), findFloat(float(dic['Braid6_37'])), findFloat(float(dic['Braid6_38'])), findFloat(float(dic['Braid6_39'])), findFloat(float(dic['Braid6_40'])), findFloat(float(dic['Braid6_41'])), findFloat(float(dic['Braid6_42'])), findFloat(float(dic['Braid6_43'])), findFloat(float(dic['Braid6_44'])), findFloat(float(dic['Braid6_45'])), findFloat(float(dic['Braid6_46'])), findFloat(float(dic['Braid6_47'])), findFloat(float(dic['Braid6_48'])), findFloat(float(dic['Braid6_49'])), findFloat(float(dic['Braid6_50'])), findFloat(float(dic['Braid6_51'])), str(dic['Braid6_52']), str(dic['Braid6_53']), findFloat(float(dic['Braid6_54'])), findFloat(float(dic['Braid6_55'])), findFloat(float(dic['Braid6_56'])), findFloat(float(dic['Braid6_57'])), findFloat(float(dic['Braid6_58'])), findFloat(float(dic['Braid6_59'])), str(dic['Braid6_60']), str(dic['Braid6_61']), str(dic['Braid6_62']))
                mycursor.execute(sql, val)
        
        if(int(dic['Braid7_1']) != 0 and int(dic['Braid7_1']) != 1) : 
                sql = "INSERT INTO braiderreport7 ( pir , operator_name , deck_set_speed , deck_act_speed , prod_meter , tot_run_hours , blower_set_temp , blower_act_temp , n2_set_temp , n2_inlet_temp , n2_outlet_temp , n2_pressure,  tube_dia, no_of_ends, wire_dia, tag_date, deck_gear_1, deck_gear_2, drum_in, drum_out, insulation, batch_no, ply_thick_setvalue, ply_thick_actvalue, ply_width_setvalue, ply_width_actvalue, mach_no, rein_od_spec_1, rein_pitch_spec_1, rein_od_spec_2, rein_pitch_spec_2, rein_od_spec_3, rein_pitch_spec_3, rein_od_fact_1, rein_od_mact_1, rein_od_lact_1, rein_pitch_fact_1, rein_pitch_mact_1, rein_pitch_lact_1, rein_od_fact_2, rein_od_mact_2, rein_od_lact_2, rein_pitch_fact_2, rein_pitch_mact_2, rein_pitch_lact_2, rein_od_fact_3, rein_od_mact_3, rein_od_lact_3, rein_pitch_fact_3, rein_pitch_mact_3, rein_pitch_lact_3, haul_gear_1, haul_gear_2, rein_od_spec_tol_1, rein_pitch_spec_tol_1, rein_od_spec_tol_2, rein_pitch_spec_tol_2, rein_od_spec_tol_3, rein_pitch_spec_tol_3, operator_id, supervisor, oa_approval ) VALUES (%s, %s, %s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (str(dic['Braid7_1']), str(dic['Braid7_2']), int(dic['Braid7_3']), int(dic['Braid7_4']), findFloat(float(dic['Braid7_5'])), findFloat(float(dic['Braid7_6'])), findFloat(float(dic['Braid7_7'])), findFloat(float(dic['Braid7_8'])), findFloat(float(dic['Braid7_9'])), findFloat(float(dic['Braid7_10'])), findFloat(float(dic['Braid7_11'])), findFloat(float(dic['Braid7_12'])), str(dic['Braid7_13']), str(dic['Braid7_14']), str(dic['Braid7_15']), str(dic['Braid7_16']), str(dic['Braid7_17']), str(dic['Braid7_18']), str(dic['Braid7_19']), str(dic['Braid7_20']), str(dic['Braid7_21']), str(dic['Braid7_22']), str(dic['Braid7_23']), findFloat(float(dic['Braid7_24'])), str(dic['Braid7_25']), findFloat(float(dic['Braid7_26'])), str(dic['Braid7_27']), findFloat(float(dic['Braid7_28'])), findFloat(float(dic['Braid7_29'])), findFloat(float(dic['Braid7_30'])), findFloat(float(dic['Braid7_31'])), findFloat(float(dic['Braid7_32'])), findFloat(float(dic['Braid7_33'])), findFloat(float(dic['Braid7_34'])), findFloat(float(dic['Braid7_35'])), findFloat(float(dic['Braid7_36'])), findFloat(float(dic['Braid7_37'])), findFloat(float(dic['Braid7_38'])), findFloat(float(dic['Braid7_39'])), findFloat(float(dic['Braid7_40'])), findFloat(float(dic['Braid7_41'])), findFloat(float(dic['Braid7_42'])), findFloat(float(dic['Braid7_43'])), findFloat(float(dic['Braid7_44'])), findFloat(float(dic['Braid7_45'])), findFloat(float(dic['Braid7_46'])), findFloat(float(dic['Braid7_47'])), findFloat(float(dic['Braid7_48'])), findFloat(float(dic['Braid7_49'])), findFloat(float(dic['Braid7_50'])), findFloat(float(dic['Braid7_51'])), str(dic['Braid7_52']), str(dic['Braid7_53']), findFloat(float(dic['Braid7_54'])), findFloat(float(dic['Braid7_55'])), findFloat(float(dic['Braid7_56'])), findFloat(float(dic['Braid7_57'])), findFloat(float(dic['Braid7_58'])), findFloat(float(dic['Braid7_59'])), str(dic['Braid7_60']), str(dic['Braid7_61']), str(dic['Braid7_62']))
                mycursor.execute(sql, val)
        
        if(int(dic['Braid8_1']) != 0 and int(dic['Braid8_1']) != 1) : 
                sql = "INSERT INTO braiderreport8 ( pir , operator_name , deck_set_speed , deck_act_speed , prod_meter , tot_run_hours , blower_set_temp , blower_act_temp , n2_set_temp , n2_inlet_temp , n2_outlet_temp , n2_pressure,  tube_dia, no_of_ends, wire_dia, tag_date, deck_gear_1, deck_gear_2, drum_in, drum_out, insulation, batch_no, ply_thick_setvalue, ply_thick_actvalue, ply_width_setvalue, ply_width_actvalue, mach_no, rein_od_spec_1, rein_pitch_spec_1, rein_od_spec_2, rein_pitch_spec_2, rein_od_spec_3, rein_pitch_spec_3, rein_od_fact_1, rein_od_mact_1, rein_od_lact_1, rein_pitch_fact_1, rein_pitch_mact_1, rein_pitch_lact_1, rein_od_fact_2, rein_od_mact_2, rein_od_lact_2, rein_pitch_fact_2, rein_pitch_mact_2, rein_pitch_lact_2, rein_od_fact_3, rein_od_mact_3, rein_od_lact_3, rein_pitch_fact_3, rein_pitch_mact_3, rein_pitch_lact_3, haul_gear_1, haul_gear_2, rein_od_spec_tol_1, rein_pitch_spec_tol_1, rein_od_spec_tol_2, rein_pitch_spec_tol_2, rein_od_spec_tol_3, rein_pitch_spec_tol_3, operator_id, supervisor, oa_approval ) VALUES (%s, %s, %s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (str(dic['Braid8_1']), str(dic['Braid8_2']), int(dic['Braid8_3']), int(dic['Braid8_4']), findFloat(float(dic['Braid8_5'])), findFloat(float(dic['Braid8_6'])), findFloat(float(dic['Braid8_7'])), findFloat(float(dic['Braid8_8'])), findFloat(float(dic['Braid8_9'])), findFloat(float(dic['Braid8_10'])), findFloat(float(dic['Braid8_11'])), findFloat(float(dic['Braid8_12'])), str(dic['Braid8_13']), str(dic['Braid8_14']), str(dic['Braid8_15']), str(dic['Braid8_16']), str(dic['Braid8_17']), str(dic['Braid8_18']), str(dic['Braid8_19']), str(dic['Braid8_20']), str(dic['Braid8_21']), str(dic['Braid8_22']), str(dic['Braid8_23']), findFloat(float(dic['Braid8_24'])), str(dic['Braid8_25']), findFloat(float(dic['Braid8_26'])), str(dic['Braid8_27']), findFloat(float(dic['Braid8_28'])), findFloat(float(dic['Braid8_29'])), findFloat(float(dic['Braid8_30'])), findFloat(float(dic['Braid8_31'])), findFloat(float(dic['Braid8_32'])), findFloat(float(dic['Braid8_33'])), findFloat(float(dic['Braid8_34'])), findFloat(float(dic['Braid8_35'])), findFloat(float(dic['Braid8_36'])), findFloat(float(dic['Braid8_37'])), findFloat(float(dic['Braid8_38'])), findFloat(float(dic['Braid8_39'])), findFloat(float(dic['Braid8_40'])), findFloat(float(dic['Braid8_41'])), findFloat(float(dic['Braid8_42'])), findFloat(float(dic['Braid8_43'])), findFloat(float(dic['Braid8_44'])), findFloat(float(dic['Braid8_45'])), findFloat(float(dic['Braid8_46'])), findFloat(float(dic['Braid8_47'])), findFloat(float(dic['Braid8_48'])), findFloat(float(dic['Braid8_49'])), findFloat(float(dic['Braid8_50'])), findFloat(float(dic['Braid8_51'])), str(dic['Braid8_52']), str(dic['Braid8_53']), findFloat(float(dic['Braid8_54'])), findFloat(float(dic['Braid8_55'])), findFloat(float(dic['Braid8_56'])), findFloat(float(dic['Braid8_57'])), findFloat(float(dic['Braid8_58'])), findFloat(float(dic['Braid8_59'])), str(dic['Braid8_60']), str(dic['Braid8_61']), str(dic['Braid8_62']))
                mycursor.execute(sql, val)
        

        #braid downtime
        '''
        if(int(dic['BraidStop1_1']) == '21'):
                globalBS.tempBraidSetup1 = True
        else:
                globalBS.tempBraidSetup1 = False
        sql = "INSERT INTO braiddowntime1 ( pir, status, setup ) VALUES (%s,%s,%s)"
        val = (str(dic['BraidProd1_1']), findBool(dic['BraidProd1_9']), globalBS.tempBraidSetup1)
        mycursor.execute(sql, val)
        '''
        '''
        if(int(dic['BraidStop2_1']) == '21'):
                globalBS.tempBraidSetup2 = True
        else:
                globalBS.tempBraidSetup2 = False
        sql = "INSERT INTO braiddowntime2 ( pir, status, setup ) VALUES (%s,%s,%s)"
        val = (str(dic['BraidProd2_1']), findBool(dic['BraidProd2_9']), globalBS.tempBraidSetup2)
        mycursor.execute(sql, val)
        '''
        ''' 
        if(int(dic['BraidStop3_1']) == '21'):
                globalBS.tempBraidSetup3 = True
        else:
                globalBS.tempBraidSetup3 = False
        sql = "INSERT INTO braiddowntime3 ( pir, status, setup ) VALUES (%s,%s,%s)"
        val = (str(dic['BraidProd3_1']), findBool(dic['BraidProd3_9']), globalBS.tempBraidSetup3)
        mycursor.execute(sql, val)
        '''
        '''
        if(int(dic['BraidStop4_1']) == '21'):
                globalBS.tempBraidSetup4 = True
        else:
                globalBS.tempBraidSetup4 = False
        sql = "INSERT INTO braiddowntime4 ( pir, status, setup ) VALUES (%s,%s,%s)"
        val = (str(dic['BraidProd4_1']), findBool(dic['BraidProd4_9']), globalBS.tempBraidSetup4)
        mycursor.execute(sql, val)
        '''
        ''' 
        if(int(dic['BraidStop5_1']) == '21'):
                globalBS.tempBraidSetup5 = True
        else:
                globalBS.tempBraidSetup5 = False
        sql = "INSERT INTO braiddowntime5 ( pir, status, setup ) VALUES (%s,%s,%s)"
        val = (str(dic['BraidProd5_1']), findBool(dic['BraidProd5_9']), globalBS.tempBraidSetup5)
        mycursor.execute(sql, val)
        '''

        '''
        if(int(dic['BraidStop6_1']) == '21'):
                globalBS.tempBraidSetup6 = True
        else:
                globalBS.tempBraidSetup6 = False
        sql = "INSERT INTO braiddowntime6 ( pir, status, setup ) VALUES (%s,%s,%s)"
        val = (str(dic['BraidProd6_1']), findBool(dic['BraidProd6_9']), globalBS.tempBraidSetup6)
        mycursor.execute(sql, val)
        


        if(int(dic['BraidStop7_1']) == '21'):
                globalBS.tempBraidSetup7 = True
        else:
                globalBS.tempBraidSetup7 = False
        sql = "INSERT INTO braiddowntime7 ( pir, status, setup ) VALUES (%s,%s,%s)"
        val = (str(dic['BraidProd7_1']), findBool(dic['BraidProd7_9']), globalBS.tempBraidSetup7)
        mycursor.execute(sql, val)
        '''
        '''
        if(int(dic['BraidStop8_1']) == '21'):
                globalBS.tempBraidSetup8 = True
        else:
                globalBS.tempBraidSetup8 = False
        sql = "INSERT INTO braiddowntime8 ( pir, status, setup ) VALUES (%s,%s,%s)"
        val = (str(dic['BraidProd8_1']), findBool(dic['BraidProd8_9']), globalBS.tempBraidSetup8)
        mycursor.execute(sql, val)
        '''


        

        
                

        '''
        sql = "INSERT INTO braiderpims1 ( b1_drum_in , b1_drum_out , b1_rtm_1 , b1_rtm_2 , b1_rtm_3 , b1_rtm_4 , b1_rtm_5, b1_rtm_6, b1_rtm_7, b1_rtm_8, b1_rtm_9, b1_rtm_10, b1_rtm_11 , b1_rtm_12 , b1_rtm_13 , b1_rtm_14 , b1_rtm_15, b1_rtm_16, b1_rtm_17, b1_rtm_18, b1_rtm_19, b1_rtm_20, b1_rtm_21 , b1_rtm_22 , b1_rtm_23 , b1_rtm_24 , b1_rtm_25, b1_rtm_26, b1_rtm_27, b1_rtm_28, b1_rtm_29, b1_rtm_30, b1_rtm_31 , b1_rtm_32 , b1_rtm_33 , b1_rtm_34 , b1_rtm_35, b1_rtm_36, b1_rtm_37, b1_rtm_38, b1_rtm_39, b1_rtm_40, b1_rtm_41 , b1_rtm_42 , b1_rtm_43 , b1_rtm_44 , b1_rtm_45, b1_rtm_46, b1_rtm_47, b1_rtm_48, b1_rtm_49, b1_rtm_50, b1_rtm_51 , b1_rtm_52 , b1_rtm_53 , b1_rtm_54 , b1_rtm_55, b1_rtm_56, b1_rtm_57, b1_rtm_58, b1_rtm_59, b1_rtm_60, b1_rtm_61 , b1_rtm_62 , b1_rtm_63 , b1_rtm_64 , b1_rtm_65, b1_rtm_66, b1_rtm_67, b1_rtm_68, b1_rtm_69, b1_rtm_70, b1_rtm_71 , b1_rtm_72 , b1_rtm_73 , b1_rtm_74 , b1_rtm_75, b1_rtm_76, b1_rtm_77, b1_rtm_78, b1_rtm_79, b1_rtm_80) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (str(dic['BraidPims1_1']), str(dic['BraidPims1_2']), findFloat(float(dic['BraidPims1_3'])), findFloat(float(dic['BraidPims1_4'])),findFloat(float(dic['BraidPims1_5'])), findFloat(float(dic['BraidPims1_6'])), findFloat(float(dic['BraidPims1_7'])), findFloat(float(dic['BraidPims1_8'])), findFloat(float(dic['BraidPims1_9'])), findFloat(float(dic['BraidPims1_10'])), findFloat(float(dic['BraidPims1_11'])), findFloat(float(dic['BraidPims1_12'])), findFloat(float(dic['BraidPims1_13'])), findFloat(float(dic['BraidPims1_14'])), findFloat(float(dic['BraidPims1_15'])), findFloat(float(dic['BraidPims1_16'])), findFloat(float(dic['BraidPims1_17'])), findFloat(float(dic['BraidPims1_18'])), findFloat(float(dic['BraidPims1_19'])), findFloat(float(dic['BraidPims1_20'])), findFloat(float(dic['BraidPims1_21'])), findFloat(float(dic['BraidPims1_22'])), findFloat(float(dic['BraidPims1_23'])), findFloat(float(dic['BraidPims1_24'])), findFloat(float(dic['BraidPims1_25'])), findFloat(float(dic['BraidPims1_26'])), findFloat(float(dic['BraidPims1_27'])), findFloat(float(dic['BraidPims1_28'])), findFloat(float(dic['BraidPims1_29'])), findFloat(float(dic['BraidPims1_30'])), findFloat(float(dic['BraidPims1_31'])), findFloat(float(dic['BraidPims1_32'])), findFloat(float(dic['BraidPims1_33'])), findFloat(float(dic['BraidPims1_34'])),
                findFloat(float(dic['BraidPims1_35'])), findFloat(float(dic['BraidPims1_36'])), findFloat(float(dic['BraidPims1_37'])), findFloat(float(dic['BraidPims1_38'])), findFloat(float(dic['BraidPims1_39'])), findFloat(float(dic['BraidPims1_40'])), findFloat(float(dic['BraidPims1_41'])), findFloat(float(dic['BraidPims1_42'])), findFloat(float(dic['BraidPims1_43'])), findFloat(float(dic['BraidPims1_44'])), findFloat(float(dic['BraidPims1_45'])), findFloat(float(dic['BraidPims1_46'])), findFloat(float(dic['BraidPims1_47'])), findFloat(float(dic['BraidPims1_48'])), findFloat(float(dic['BraidPims1_49'])), findFloat(float(dic['BraidPims1_50'])), findFloat(float(dic['BraidPims1_51'])), findFloat(float(dic['BraidPims1_52'])), findFloat(float(dic['BraidPims1_53'])), findFloat(float(dic['BraidPims1_54'])), findFloat(float(dic['BraidPims1_55'])), findFloat(float(dic['BraidPims1_56'])), findFloat(float(dic['BraidPims1_57'])), findFloat(float(dic['BraidPims1_58'])), findFloat(float(dic['BraidPims1_59'])), findFloat(float(dic['BraidPims1_60'])), findFloat(float(dic['BraidPims1_61'])), findFloat(float(dic['BraidPims1_62'])), findFloat(float(dic['BraidPims1_63'])), findFloat(float(dic['BraidPims1_64'])), findFloat(float(dic['BraidPims1_65'])), findFloat(float(dic['BraidPims1_66'])), findFloat(float(dic['BraidPims1_67'])), findFloat(float(dic['BraidPims1_68'])), findFloat(float(dic['BraidPims1_69'])),
                findFloat(float(dic['BraidPims1_70'])), findFloat(float(dic['BraidPims1_71'])), findFloat(float(dic['BraidPims1_72'])), findFloat(float(dic['BraidPims1_73'])), findFloat(float(dic['BraidPims1_74'])), findFloat(float(dic['BraidPims1_75'])), findFloat(float(dic['BraidPims1_76'])), findFloat(float(dic['BraidPims1_77'])), findFloat(float(dic['BraidPims1_78'])), findFloat(float(dic['BraidPims1_79'])), findFloat(float(dic['BraidPims1_80'])), findFloat(float(dic['BraidPims1_81'])), findFloat(float(dic['BraidPims1_82'])))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO braiderpims2 ( b2_drum_in , b2_drum_out , b2_rtm_1 , b2_rtm_2 , b2_rtm_3 , b2_rtm_4 , b2_rtm_5, b2_rtm_6, b2_rtm_7, b2_rtm_8, b2_rtm_9, b2_rtm_10, b2_rtm_11 , b2_rtm_12 , b2_rtm_13 , b2_rtm_14 , b2_rtm_15, b2_rtm_16, b2_rtm_17, b2_rtm_18, b2_rtm_19, b2_rtm_20, b2_rtm_21 , b2_rtm_22 , b2_rtm_23 , b2_rtm_24 , b2_rtm_25, b2_rtm_26, b2_rtm_27, b2_rtm_28, b2_rtm_29, b2_rtm_30, b2_rtm_31 , b2_rtm_32 , b2_rtm_33 , b2_rtm_34 , b2_rtm_35, b2_rtm_36, b2_rtm_37, b2_rtm_38, b2_rtm_39, b2_rtm_40, b2_rtm_41 , b2_rtm_42 , b2_rtm_43 , b2_rtm_44 , b2_rtm_45, b2_rtm_46, b2_rtm_47, b2_rtm_48, b2_rtm_49, b2_rtm_50, b2_rtm_51 , b2_rtm_52 , b2_rtm_53 , b2_rtm_54 , b2_rtm_55, b2_rtm_56, b2_rtm_57, b2_rtm_58, b2_rtm_59, b2_rtm_60, b2_rtm_61 , b2_rtm_62 , b2_rtm_63 , b2_rtm_64 , b2_rtm_65, b2_rtm_66, b2_rtm_67, b2_rtm_68, b2_rtm_69, b2_rtm_70, b2_rtm_71 , b2_rtm_72 , b2_rtm_73 , b2_rtm_74 , b2_rtm_75, b2_rtm_76, b2_rtm_77, b2_rtm_78, b2_rtm_79, b2_rtm_80) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (str(dic['BraidPims2_1']), str(dic['BraidPims2_2']), findFloat(float(dic['BraidPims2_3'])), findFloat(float(dic['BraidPims2_4'])),findFloat(float(dic['BraidPims2_5'])), findFloat(float(dic['BraidPims2_6'])), findFloat(float(dic['BraidPims2_7'])), findFloat(float(dic['BraidPims2_8'])), findFloat(float(dic['BraidPims2_9'])), findFloat(float(dic['BraidPims2_10'])), findFloat(float(dic['BraidPims2_11'])), findFloat(float(dic['BraidPims2_12'])), findFloat(float(dic['BraidPims2_13'])), findFloat(float(dic['BraidPims2_14'])), findFloat(float(dic['BraidPims2_15'])), findFloat(float(dic['BraidPims2_16'])), findFloat(float(dic['BraidPims2_17'])), findFloat(float(dic['BraidPims2_18'])), findFloat(float(dic['BraidPims2_19'])), findFloat(float(dic['BraidPims2_20'])), findFloat(float(dic['BraidPims2_21'])), findFloat(float(dic['BraidPims2_22'])), findFloat(float(dic['BraidPims2_23'])), findFloat(float(dic['BraidPims2_24'])), findFloat(float(dic['BraidPims2_25'])), findFloat(float(dic['BraidPims2_26'])), findFloat(float(dic['BraidPims2_27'])), findFloat(float(dic['BraidPims2_28'])), findFloat(float(dic['BraidPims2_29'])), findFloat(float(dic['BraidPims2_30'])), findFloat(float(dic['BraidPims2_31'])), findFloat(float(dic['BraidPims2_32'])), findFloat(float(dic['BraidPims2_33'])), findFloat(float(dic['BraidPims2_34'])),
                findFloat(float(dic['BraidPims2_35'])), findFloat(float(dic['BraidPims2_36'])), findFloat(float(dic['BraidPims2_37'])), findFloat(float(dic['BraidPims2_38'])), findFloat(float(dic['BraidPims2_39'])), findFloat(float(dic['BraidPims2_40'])), findFloat(float(dic['BraidPims2_41'])), findFloat(float(dic['BraidPims2_42'])), findFloat(float(dic['BraidPims2_43'])), findFloat(float(dic['BraidPims2_44'])), findFloat(float(dic['BraidPims2_45'])), findFloat(float(dic['BraidPims2_46'])), findFloat(float(dic['BraidPims2_47'])), findFloat(float(dic['BraidPims2_48'])), findFloat(float(dic['BraidPims2_49'])), findFloat(float(dic['BraidPims2_50'])), findFloat(float(dic['BraidPims2_51'])), findFloat(float(dic['BraidPims2_52'])), findFloat(float(dic['BraidPims2_53'])), findFloat(float(dic['BraidPims2_54'])), findFloat(float(dic['BraidPims2_55'])), findFloat(float(dic['BraidPims2_56'])), findFloat(float(dic['BraidPims2_57'])), findFloat(float(dic['BraidPims2_58'])), findFloat(float(dic['BraidPims2_59'])), findFloat(float(dic['BraidPims2_60'])), findFloat(float(dic['BraidPims2_61'])), findFloat(float(dic['BraidPims2_62'])), findFloat(float(dic['BraidPims2_63'])), findFloat(float(dic['BraidPims2_64'])), findFloat(float(dic['BraidPims2_65'])), findFloat(float(dic['BraidPims2_66'])), findFloat(float(dic['BraidPims2_67'])), findFloat(float(dic['BraidPims2_68'])), findFloat(float(dic['BraidPims2_69'])),
                findFloat(float(dic['BraidPims2_70'])), findFloat(float(dic['BraidPims2_71'])), findFloat(float(dic['BraidPims2_72'])), findFloat(float(dic['BraidPims2_73'])), findFloat(float(dic['BraidPims2_74'])), findFloat(float(dic['BraidPims2_75'])), findFloat(float(dic['BraidPims2_76'])), findFloat(float(dic['BraidPims2_77'])), findFloat(float(dic['BraidPims2_78'])), findFloat(float(dic['BraidPims2_79'])), findFloat(float(dic['BraidPims2_80'])), findFloat(float(dic['BraidPims2_81'])), findFloat(float(dic['BraidPims2_82'])))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO braiderpims3 ( b3_drum_in , b3_drum_out , b3_rtm_1 , b3_rtm_2 , b3_rtm_3 , b3_rtm_4 , b3_rtm_5, b3_rtm_6, b3_rtm_7, b3_rtm_8, b3_rtm_9, b3_rtm_10, b3_rtm_11 , b3_rtm_12 , b3_rtm_13 , b3_rtm_14 , b3_rtm_15, b3_rtm_16, b3_rtm_17, b3_rtm_18, b3_rtm_19, b3_rtm_20, b3_rtm_21 , b3_rtm_22 , b3_rtm_23 , b3_rtm_24 , b3_rtm_25, b3_rtm_26, b3_rtm_27, b3_rtm_28, b3_rtm_29, b3_rtm_30, b3_rtm_31 , b3_rtm_32 , b3_rtm_33 , b3_rtm_34 , b3_rtm_35, b3_rtm_36, b3_rtm_37, b3_rtm_38, b3_rtm_39, b3_rtm_40, b3_rtm_41 , b3_rtm_42 , b3_rtm_43 , b3_rtm_44 , b3_rtm_45, b3_rtm_46, b3_rtm_47, b3_rtm_48, b3_rtm_49, b3_rtm_50, b3_rtm_51 , b3_rtm_52 , b3_rtm_53 , b3_rtm_54 , b3_rtm_55, b3_rtm_56, b3_rtm_57, b3_rtm_58, b3_rtm_59, b3_rtm_60, b3_rtm_61 , b3_rtm_62 , b3_rtm_63 , b3_rtm_64 , b3_rtm_65, b3_rtm_66, b3_rtm_67, b3_rtm_68, b3_rtm_69, b3_rtm_70, b3_rtm_71 , b3_rtm_72 , b3_rtm_73 , b3_rtm_74 , b3_rtm_75, b3_rtm_76, b3_rtm_77, b3_rtm_78, b3_rtm_79, b3_rtm_80) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( str(dic['BraidPims3_1']), str(dic['BraidPims3_2']),
                findFloat(float(dic['BraidPims3_3'])), findFloat(float(dic['BraidPims3_4'])),
                findFloat(float(dic['BraidPims3_5'])), findFloat(float(dic['BraidPims3_6'])), 
                findFloat(float(dic['BraidPims3_7'])), findFloat(float(dic['BraidPims3_8'])), 
                findFloat(float(dic['BraidPims3_9'])), findFloat(float(dic['BraidPims3_10'])), 
                findFloat(float(dic['BraidPims3_11'])), findFloat(float(dic['BraidPims3_12'])), 
                findFloat(float(dic['BraidPims3_13'])), findFloat(float(dic['BraidPims3_14'])), 
                findFloat(float(dic['BraidPims3_15'])), findFloat(float(dic['BraidPims3_16'])), 
                findFloat(float(dic['BraidPims3_17'])), findFloat(float(dic['BraidPims3_18'])), 
                findFloat(float(dic['BraidPims3_19'])), findFloat(float(dic['BraidPims3_20'])), 
                findFloat(float(dic['BraidPims3_21'])), findFloat(float(dic['BraidPims3_22'])), 
                findFloat(float(dic['BraidPims3_23'])), findFloat(float(dic['BraidPims3_24'])), 
                findFloat(float(dic['BraidPims3_25'])), findFloat(float(dic['BraidPims3_26'])), 
                findFloat(float(dic['BraidPims3_27'])), findFloat(float(dic['BraidPims3_28'])), 
                findFloat(float(dic['BraidPims3_29'])), findFloat(float(dic['BraidPims3_30'])), 
                findFloat(float(dic['BraidPims3_31'])), findFloat(float(dic['BraidPims3_32'])), 
                findFloat(float(dic['BraidPims3_33'])), findFloat(float(dic['BraidPims3_34'])),
                findFloat(float(dic['BraidPims3_35'])), findFloat(float(dic['BraidPims3_36'])), 
                findFloat(float(dic['BraidPims3_37'])), findFloat(float(dic['BraidPims3_38'])), 
                findFloat(float(dic['BraidPims3_39'])), findFloat(float(dic['BraidPims3_40'])), 
                findFloat(float(dic['BraidPims3_41'])), findFloat(float(dic['BraidPims3_42'])), 
                findFloat(float(dic['BraidPims3_43'])), findFloat(float(dic['BraidPims3_44'])), 
                findFloat(float(dic['BraidPims3_45'])), findFloat(float(dic['BraidPims3_46'])), 
                findFloat(float(dic['BraidPims3_47'])), findFloat(float(dic['BraidPims3_48'])), 
                findFloat(float(dic['BraidPims3_49'])), findFloat(float(dic['BraidPims3_50'])), 
                findFloat(float(dic['BraidPims3_51'])), findFloat(float(dic['BraidPims3_52'])), 
                findFloat(float(dic['BraidPims3_53'])), findFloat(float(dic['BraidPims3_54'])), 
                findFloat(float(dic['BraidPims3_55'])), findFloat(float(dic['BraidPims3_56'])), 
                findFloat(float(dic['BraidPims3_57'])), findFloat(float(dic['BraidPims3_58'])), 
                findFloat(float(dic['BraidPims3_59'])), findFloat(float(dic['BraidPims3_60'])), 
                findFloat(float(dic['BraidPims3_61'])), findFloat(float(dic['BraidPims3_62'])), 
                findFloat(float(dic['BraidPims3_63'])), findFloat(float(dic['BraidPims3_64'])), 
                findFloat(float(dic['BraidPims3_65'])), findFloat(float(dic['BraidPims3_66'])), 
                findFloat(float(dic['BraidPims3_67'])), findFloat(float(dic['BraidPims3_68'])), 
                findFloat(float(dic['BraidPims3_69'])), findFloat(float(dic['BraidPims3_70'])), 
                findFloat(float(dic['BraidPims3_71'])), findFloat(float(dic['BraidPims3_72'])), 
                findFloat(float(dic['BraidPims3_73'])), findFloat(float(dic['BraidPims3_74'])), 
                findFloat(float(dic['BraidPims3_75'])), findFloat(float(dic['BraidPims3_76'])), 
                findFloat(float(dic['BraidPims3_77'])), findFloat(float(dic['BraidPims3_78'])), 
                findFloat(float(dic['BraidPims3_79'])), findFloat(float(dic['BraidPims3_80'])), 
                findFloat(float(dic['BraidPims3_81'])), findFloat(float(dic['BraidPims3_82'])))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO braiderpims4 ( b4_drum_in , b4_drum_out , b4_rtm_1 , b4_rtm_2 , b4_rtm_3 , b4_rtm_4 , b4_rtm_5, b4_rtm_6, b4_rtm_7, b4_rtm_8, b4_rtm_9, b4_rtm_10, b4_rtm_11 , b4_rtm_12 , b4_rtm_13 , b4_rtm_14 , b4_rtm_15, b4_rtm_16, b4_rtm_17, b4_rtm_18, b4_rtm_19, b4_rtm_20, b4_rtm_21 , b4_rtm_22 , b4_rtm_23 , b4_rtm_24 , b4_rtm_25, b4_rtm_26, b4_rtm_27, b4_rtm_28, b4_rtm_29, b4_rtm_30, b4_rtm_31 , b4_rtm_32 , b4_rtm_33 , b4_rtm_34 , b4_rtm_35, b4_rtm_36, b4_rtm_37, b4_rtm_38, b4_rtm_39, b4_rtm_40, b4_rtm_41 , b4_rtm_42 , b4_rtm_43 , b4_rtm_44 , b4_rtm_45, b4_rtm_46, b4_rtm_47, b4_rtm_48, b4_rtm_49, b4_rtm_50, b4_rtm_51 , b4_rtm_52 , b4_rtm_53 , b4_rtm_54 , b4_rtm_55, b4_rtm_56, b4_rtm_57, b4_rtm_58, b4_rtm_59, b4_rtm_60, b4_rtm_61 , b4_rtm_62 , b4_rtm_63 , b4_rtm_64 , b4_rtm_65, b4_rtm_66, b4_rtm_67, b4_rtm_68, b4_rtm_69, b4_rtm_70, b4_rtm_71 , b4_rtm_72 , b4_rtm_73 , b4_rtm_74 , b4_rtm_75, b4_rtm_76, b4_rtm_77, b4_rtm_78, b4_rtm_79, b4_rtm_80) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( str(dic['BraidPims4_1']), str(dic['BraidPims4_2']),
                findFloat(float(dic['BraidPims4_3'])), findFloat(float(dic['BraidPims4_4'])),
                findFloat(float(dic['BraidPims4_5'])), findFloat(float(dic['BraidPims4_6'])), 
                findFloat(float(dic['BraidPims4_7'])), findFloat(float(dic['BraidPims4_8'])), 
                findFloat(float(dic['BraidPims4_9'])), findFloat(float(dic['BraidPims4_10'])), 
                findFloat(float(dic['BraidPims4_11'])), findFloat(float(dic['BraidPims4_12'])), 
                findFloat(float(dic['BraidPims4_13'])), findFloat(float(dic['BraidPims4_14'])), 
                findFloat(float(dic['BraidPims4_15'])), findFloat(float(dic['BraidPims4_16'])), 
                findFloat(float(dic['BraidPims4_17'])), findFloat(float(dic['BraidPims4_18'])), 
                findFloat(float(dic['BraidPims4_19'])), findFloat(float(dic['BraidPims4_20'])), 
                findFloat(float(dic['BraidPims4_21'])), findFloat(float(dic['BraidPims4_22'])), 
                findFloat(float(dic['BraidPims4_23'])), findFloat(float(dic['BraidPims4_24'])), 
                findFloat(float(dic['BraidPims4_25'])), findFloat(float(dic['BraidPims4_26'])), 
                findFloat(float(dic['BraidPims4_27'])), findFloat(float(dic['BraidPims4_28'])), 
                findFloat(float(dic['BraidPims4_29'])), findFloat(float(dic['BraidPims4_30'])), 
                findFloat(float(dic['BraidPims4_31'])), findFloat(float(dic['BraidPims4_32'])), 
                findFloat(float(dic['BraidPims4_33'])), findFloat(float(dic['BraidPims4_34'])),
                findFloat(float(dic['BraidPims4_35'])), findFloat(float(dic['BraidPims4_36'])), 
                findFloat(float(dic['BraidPims4_37'])), findFloat(float(dic['BraidPims4_38'])), 
                findFloat(float(dic['BraidPims4_39'])), findFloat(float(dic['BraidPims4_40'])), 
                findFloat(float(dic['BraidPims4_41'])), findFloat(float(dic['BraidPims4_42'])), 
                findFloat(float(dic['BraidPims4_43'])), findFloat(float(dic['BraidPims4_44'])), 
                findFloat(float(dic['BraidPims4_45'])), findFloat(float(dic['BraidPims4_46'])), 
                findFloat(float(dic['BraidPims4_47'])), findFloat(float(dic['BraidPims4_48'])), 
                findFloat(float(dic['BraidPims4_49'])), findFloat(float(dic['BraidPims4_50'])), 
                findFloat(float(dic['BraidPims4_51'])), findFloat(float(dic['BraidPims4_52'])), 
                findFloat(float(dic['BraidPims4_53'])), findFloat(float(dic['BraidPims4_54'])), 
                findFloat(float(dic['BraidPims4_55'])), findFloat(float(dic['BraidPims4_56'])), 
                findFloat(float(dic['BraidPims4_57'])), findFloat(float(dic['BraidPims4_58'])), 
                findFloat(float(dic['BraidPims4_59'])), findFloat(float(dic['BraidPims4_60'])), 
                findFloat(float(dic['BraidPims4_61'])), findFloat(float(dic['BraidPims4_62'])), 
                findFloat(float(dic['BraidPims4_63'])), findFloat(float(dic['BraidPims4_64'])), 
                findFloat(float(dic['BraidPims4_65'])), findFloat(float(dic['BraidPims4_66'])), 
                findFloat(float(dic['BraidPims4_67'])), findFloat(float(dic['BraidPims4_68'])), 
                findFloat(float(dic['BraidPims4_69'])), findFloat(float(dic['BraidPims4_70'])), 
                findFloat(float(dic['BraidPims4_71'])), findFloat(float(dic['BraidPims4_72'])), 
                findFloat(float(dic['BraidPims4_73'])), findFloat(float(dic['BraidPims4_74'])), 
                findFloat(float(dic['BraidPims4_75'])), findFloat(float(dic['BraidPims4_76'])), 
                findFloat(float(dic['BraidPims4_77'])), findFloat(float(dic['BraidPims4_78'])), 
                findFloat(float(dic['BraidPims4_79'])), findFloat(float(dic['BraidPims4_80'])), 
                findFloat(float(dic['BraidPims4_81'])), findFloat(float(dic['BraidPims4_82'])))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO braiderpims5 ( b5_drum_in , b5_drum_out , b5_rtm_1 , b5_rtm_2 , b5_rtm_3 , b5_rtm_4 , b5_rtm_5, b5_rtm_6, b5_rtm_7, b5_rtm_8, b5_rtm_9, b5_rtm_10, b5_rtm_11 , b5_rtm_12 , b5_rtm_13 , b5_rtm_14 , b5_rtm_15, b5_rtm_16, b5_rtm_17, b5_rtm_18, b5_rtm_19, b5_rtm_20, b5_rtm_21 , b5_rtm_22 , b5_rtm_23 , b5_rtm_24 , b5_rtm_25, b5_rtm_26, b5_rtm_27, b5_rtm_28, b5_rtm_29, b5_rtm_30, b5_rtm_31 , b5_rtm_32 , b5_rtm_33 , b5_rtm_34 , b5_rtm_35, b5_rtm_36, b5_rtm_37, b5_rtm_38, b5_rtm_39, b5_rtm_40, b5_rtm_41 , b5_rtm_42 , b5_rtm_43 , b5_rtm_44 , b5_rtm_45, b5_rtm_46, b5_rtm_47, b5_rtm_48, b5_rtm_49, b5_rtm_50, b5_rtm_51 , b5_rtm_52 , b5_rtm_53 , b5_rtm_54 , b5_rtm_55, b5_rtm_56, b5_rtm_57, b5_rtm_58, b5_rtm_59, b5_rtm_60, b5_rtm_61 , b5_rtm_62 , b5_rtm_63 , b5_rtm_64 , b5_rtm_65, b5_rtm_66, b5_rtm_67, b5_rtm_68, b5_rtm_69, b5_rtm_70, b5_rtm_71 , b5_rtm_72 , b5_rtm_73 , b5_rtm_74 , b5_rtm_75, b5_rtm_76, b5_rtm_77, b5_rtm_78, b5_rtm_79, b5_rtm_80) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( str(dic['BraidPims5_1']), str(dic['BraidPims5_2']),
                findFloat(float(dic['BraidPims5_3'])), findFloat(float(dic['BraidPims5_4'])),
                findFloat(float(dic['BraidPims5_5'])), findFloat(float(dic['BraidPims5_6'])), 
                findFloat(float(dic['BraidPims5_7'])), findFloat(float(dic['BraidPims5_8'])), 
                findFloat(float(dic['BraidPims5_9'])), findFloat(float(dic['BraidPims5_10'])), 
                findFloat(float(dic['BraidPims5_11'])), findFloat(float(dic['BraidPims5_12'])), 
                findFloat(float(dic['BraidPims5_13'])), findFloat(float(dic['BraidPims5_14'])), 
                findFloat(float(dic['BraidPims5_15'])), findFloat(float(dic['BraidPims5_16'])), 
                findFloat(float(dic['BraidPims5_17'])), findFloat(float(dic['BraidPims5_18'])), 
                findFloat(float(dic['BraidPims5_19'])), findFloat(float(dic['BraidPims5_20'])), 
                findFloat(float(dic['BraidPims5_21'])), findFloat(float(dic['BraidPims5_22'])), 
                findFloat(float(dic['BraidPims5_23'])), findFloat(float(dic['BraidPims5_24'])), 
                findFloat(float(dic['BraidPims5_25'])), findFloat(float(dic['BraidPims5_26'])), 
                findFloat(float(dic['BraidPims5_27'])), findFloat(float(dic['BraidPims5_28'])), 
                findFloat(float(dic['BraidPims5_29'])), findFloat(float(dic['BraidPims5_30'])), 
                findFloat(float(dic['BraidPims5_31'])), findFloat(float(dic['BraidPims5_32'])), 
                findFloat(float(dic['BraidPims5_33'])), findFloat(float(dic['BraidPims5_34'])),
                findFloat(float(dic['BraidPims5_35'])), findFloat(float(dic['BraidPims5_36'])), 
                findFloat(float(dic['BraidPims5_37'])), findFloat(float(dic['BraidPims5_38'])), 
                findFloat(float(dic['BraidPims5_39'])), findFloat(float(dic['BraidPims5_40'])), 
                findFloat(float(dic['BraidPims5_41'])), findFloat(float(dic['BraidPims5_42'])), 
                findFloat(float(dic['BraidPims5_43'])), findFloat(float(dic['BraidPims5_44'])), 
                findFloat(float(dic['BraidPims5_45'])), findFloat(float(dic['BraidPims5_46'])), 
                findFloat(float(dic['BraidPims5_47'])), findFloat(float(dic['BraidPims5_48'])), 
                findFloat(float(dic['BraidPims5_49'])), findFloat(float(dic['BraidPims5_50'])), 
                findFloat(float(dic['BraidPims5_51'])), findFloat(float(dic['BraidPims5_52'])), 
                findFloat(float(dic['BraidPims5_53'])), findFloat(float(dic['BraidPims5_54'])), 
                findFloat(float(dic['BraidPims5_55'])), findFloat(float(dic['BraidPims5_56'])), 
                findFloat(float(dic['BraidPims5_57'])), findFloat(float(dic['BraidPims5_58'])), 
                findFloat(float(dic['BraidPims5_59'])), findFloat(float(dic['BraidPims5_60'])), 
                findFloat(float(dic['BraidPims5_61'])), findFloat(float(dic['BraidPims5_62'])), 
                findFloat(float(dic['BraidPims5_63'])), findFloat(float(dic['BraidPims5_64'])), 
                findFloat(float(dic['BraidPims5_65'])), findFloat(float(dic['BraidPims5_66'])), 
                findFloat(float(dic['BraidPims5_67'])), findFloat(float(dic['BraidPims5_68'])), 
                findFloat(float(dic['BraidPims5_69'])), findFloat(float(dic['BraidPims5_70'])), 
                findFloat(float(dic['BraidPims5_71'])), findFloat(float(dic['BraidPims5_72'])), 
                findFloat(float(dic['BraidPims5_73'])), findFloat(float(dic['BraidPims5_74'])), 
                findFloat(float(dic['BraidPims5_75'])), findFloat(float(dic['BraidPims5_76'])), 
                findFloat(float(dic['BraidPims5_77'])), findFloat(float(dic['BraidPims5_78'])), 
                findFloat(float(dic['BraidPims5_79'])), findFloat(float(dic['BraidPims5_80'])), 
                findFloat(float(dic['BraidPims5_81'])), findFloat(float(dic['BraidPims5_82'])))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO braiderpims6 ( b6_drum_in , b6_drum_out , b6_rtm_1 , b6_rtm_2 , b6_rtm_3 , b6_rtm_4 , b6_rtm_5, b6_rtm_6, b6_rtm_7, b6_rtm_8, b6_rtm_9, b6_rtm_10, b6_rtm_11 , b6_rtm_12 , b6_rtm_13 , b6_rtm_14 , b6_rtm_15, b6_rtm_16, b6_rtm_17, b6_rtm_18, b6_rtm_19, b6_rtm_20, b6_rtm_21 , b6_rtm_22 , b6_rtm_23 , b6_rtm_24 , b6_rtm_25, b6_rtm_26, b6_rtm_27, b6_rtm_28, b6_rtm_29, b6_rtm_30, b6_rtm_31 , b6_rtm_32 , b6_rtm_33 , b6_rtm_34 , b6_rtm_35, b6_rtm_36, b6_rtm_37, b6_rtm_38, b6_rtm_39, b6_rtm_40, b6_rtm_41 , b6_rtm_42 , b6_rtm_43 , b6_rtm_44 , b6_rtm_45, b6_rtm_46, b6_rtm_47, b6_rtm_48, b6_rtm_49, b6_rtm_50, b6_rtm_51 , b6_rtm_52 , b6_rtm_53 , b6_rtm_54 , b6_rtm_55, b6_rtm_56, b6_rtm_57, b6_rtm_58, b6_rtm_59, b6_rtm_60, b6_rtm_61 , b6_rtm_62 , b6_rtm_63 , b6_rtm_64 , b6_rtm_65, b6_rtm_66, b6_rtm_67, b6_rtm_68, b6_rtm_69, b6_rtm_70, b6_rtm_71 , b6_rtm_72 , b6_rtm_73 , b6_rtm_74 , b6_rtm_75, b6_rtm_76, b6_rtm_77, b6_rtm_78, b6_rtm_79, b6_rtm_80) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( str(dic['BraidPims6_1']), str(dic['BraidPims6_2']),
                findFloat(float(dic['BraidPims6_3'])), findFloat(float(dic['BraidPims6_4'])),
                findFloat(float(dic['BraidPims6_5'])), findFloat(float(dic['BraidPims6_6'])), 
                findFloat(float(dic['BraidPims6_7'])), findFloat(float(dic['BraidPims6_8'])), 
                findFloat(float(dic['BraidPims6_9'])), findFloat(float(dic['BraidPims6_10'])), 
                findFloat(float(dic['BraidPims6_11'])), findFloat(float(dic['BraidPims6_12'])), 
                findFloat(float(dic['BraidPims6_13'])), findFloat(float(dic['BraidPims6_14'])), 
                findFloat(float(dic['BraidPims6_15'])), findFloat(float(dic['BraidPims6_16'])), 
                findFloat(float(dic['BraidPims6_17'])), findFloat(float(dic['BraidPims6_18'])), 
                findFloat(float(dic['BraidPims6_19'])), findFloat(float(dic['BraidPims6_20'])), 
                findFloat(float(dic['BraidPims6_21'])), findFloat(float(dic['BraidPims6_22'])), 
                findFloat(float(dic['BraidPims6_23'])), findFloat(float(dic['BraidPims6_24'])), 
                findFloat(float(dic['BraidPims6_25'])), findFloat(float(dic['BraidPims6_26'])), 
                findFloat(float(dic['BraidPims6_27'])), findFloat(float(dic['BraidPims6_28'])), 
                findFloat(float(dic['BraidPims6_29'])), findFloat(float(dic['BraidPims6_30'])), 
                findFloat(float(dic['BraidPims6_31'])), findFloat(float(dic['BraidPims6_32'])), 
                findFloat(float(dic['BraidPims6_33'])), findFloat(float(dic['BraidPims6_34'])),
                findFloat(float(dic['BraidPims6_35'])), findFloat(float(dic['BraidPims6_36'])), 
                findFloat(float(dic['BraidPims6_37'])), findFloat(float(dic['BraidPims6_38'])), 
                findFloat(float(dic['BraidPims6_39'])), findFloat(float(dic['BraidPims6_40'])), 
                findFloat(float(dic['BraidPims6_41'])), findFloat(float(dic['BraidPims6_42'])), 
                findFloat(float(dic['BraidPims6_43'])), findFloat(float(dic['BraidPims6_44'])), 
                findFloat(float(dic['BraidPims6_45'])), findFloat(float(dic['BraidPims6_46'])), 
                findFloat(float(dic['BraidPims6_47'])), findFloat(float(dic['BraidPims6_48'])), 
                findFloat(float(dic['BraidPims6_49'])), findFloat(float(dic['BraidPims6_50'])), 
                findFloat(float(dic['BraidPims6_51'])), findFloat(float(dic['BraidPims6_52'])), 
                findFloat(float(dic['BraidPims6_53'])), findFloat(float(dic['BraidPims6_54'])), 
                findFloat(float(dic['BraidPims6_55'])), findFloat(float(dic['BraidPims6_56'])), 
                findFloat(float(dic['BraidPims6_57'])), findFloat(float(dic['BraidPims6_58'])), 
                findFloat(float(dic['BraidPims6_59'])), findFloat(float(dic['BraidPims6_60'])), 
                findFloat(float(dic['BraidPims6_61'])), findFloat(float(dic['BraidPims6_62'])), 
                findFloat(float(dic['BraidPims6_63'])), findFloat(float(dic['BraidPims6_64'])), 
                findFloat(float(dic['BraidPims6_65'])), findFloat(float(dic['BraidPims6_66'])), 
                findFloat(float(dic['BraidPims6_67'])), findFloat(float(dic['BraidPims6_68'])), 
                findFloat(float(dic['BraidPims6_69'])), findFloat(float(dic['BraidPims6_70'])), 
                findFloat(float(dic['BraidPims6_71'])), findFloat(float(dic['BraidPims6_72'])), 
                findFloat(float(dic['BraidPims6_73'])), findFloat(float(dic['BraidPims6_74'])), 
                findFloat(float(dic['BraidPims6_75'])), findFloat(float(dic['BraidPims6_76'])), 
                findFloat(float(dic['BraidPims6_77'])), findFloat(float(dic['BraidPims6_78'])), 
                findFloat(float(dic['BraidPims6_79'])), findFloat(float(dic['BraidPims6_80'])), 
                findFloat(float(dic['BraidPims6_81'])), findFloat(float(dic['BraidPims6_82'])))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO braiderpims7 ( b7_drum_in , b7_drum_out , b7_rtm_1 , b7_rtm_2 , b7_rtm_3 , b7_rtm_4 , b7_rtm_5, b7_rtm_6, b7_rtm_7, b7_rtm_8, b7_rtm_9, b7_rtm_10, b7_rtm_11 , b7_rtm_12 , b7_rtm_13 , b7_rtm_14 , b7_rtm_15, b7_rtm_16, b7_rtm_17, b7_rtm_18, b7_rtm_19, b7_rtm_20, b7_rtm_21 , b7_rtm_22 , b7_rtm_23 , b7_rtm_24 , b7_rtm_25, b7_rtm_26, b7_rtm_27, b7_rtm_28, b7_rtm_29, b7_rtm_30, b7_rtm_31 , b7_rtm_32 , b7_rtm_33 , b7_rtm_34 , b7_rtm_35, b7_rtm_36, b7_rtm_37, b7_rtm_38, b7_rtm_39, b7_rtm_40, b7_rtm_41 , b7_rtm_42 , b7_rtm_43 , b7_rtm_44 , b7_rtm_45, b7_rtm_46, b7_rtm_47, b7_rtm_48, b7_rtm_49, b7_rtm_50, b7_rtm_51 , b7_rtm_52 , b7_rtm_53 , b7_rtm_54 , b7_rtm_55, b7_rtm_56, b7_rtm_57, b7_rtm_58, b7_rtm_59, b7_rtm_60, b7_rtm_61 , b7_rtm_62 , b7_rtm_63 , b7_rtm_64 , b7_rtm_65, b7_rtm_66, b7_rtm_67, b7_rtm_68, b7_rtm_69, b7_rtm_70, b7_rtm_71 , b7_rtm_72 , b7_rtm_73 , b7_rtm_74 , b7_rtm_75, b7_rtm_76, b7_rtm_77, b7_rtm_78, b7_rtm_79, b7_rtm_80) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( str(dic['BraidPims7_1']), str(dic['BraidPims7_2']),
                findFloat(float(dic['BraidPims7_3'])), findFloat(float(dic['BraidPims7_4'])),
                findFloat(float(dic['BraidPims7_5'])), findFloat(float(dic['BraidPims7_6'])), 
                findFloat(float(dic['BraidPims7_7'])), findFloat(float(dic['BraidPims7_8'])), 
                findFloat(float(dic['BraidPims7_9'])), findFloat(float(dic['BraidPims7_10'])), 
                findFloat(float(dic['BraidPims7_11'])), findFloat(float(dic['BraidPims7_12'])), 
                findFloat(float(dic['BraidPims7_13'])), findFloat(float(dic['BraidPims7_14'])), 
                findFloat(float(dic['BraidPims7_15'])), findFloat(float(dic['BraidPims7_16'])), 
                findFloat(float(dic['BraidPims7_17'])), findFloat(float(dic['BraidPims7_18'])), 
                findFloat(float(dic['BraidPims7_19'])), findFloat(float(dic['BraidPims7_20'])), 
                findFloat(float(dic['BraidPims7_21'])), findFloat(float(dic['BraidPims7_22'])), 
                findFloat(float(dic['BraidPims7_23'])), findFloat(float(dic['BraidPims7_24'])), 
                findFloat(float(dic['BraidPims7_25'])), findFloat(float(dic['BraidPims7_26'])), 
                findFloat(float(dic['BraidPims7_27'])), findFloat(float(dic['BraidPims7_28'])), 
                findFloat(float(dic['BraidPims7_29'])), findFloat(float(dic['BraidPims7_30'])), 
                findFloat(float(dic['BraidPims7_31'])), findFloat(float(dic['BraidPims7_32'])), 
                findFloat(float(dic['BraidPims7_33'])), findFloat(float(dic['BraidPims7_34'])),
                findFloat(float(dic['BraidPims7_35'])), findFloat(float(dic['BraidPims7_36'])), 
                findFloat(float(dic['BraidPims7_37'])), findFloat(float(dic['BraidPims7_38'])), 
                findFloat(float(dic['BraidPims7_39'])), findFloat(float(dic['BraidPims7_40'])), 
                findFloat(float(dic['BraidPims7_41'])), findFloat(float(dic['BraidPims7_42'])), 
                findFloat(float(dic['BraidPims7_43'])), findFloat(float(dic['BraidPims7_44'])), 
                findFloat(float(dic['BraidPims7_45'])), findFloat(float(dic['BraidPims7_46'])), 
                findFloat(float(dic['BraidPims7_47'])), findFloat(float(dic['BraidPims7_48'])), 
                findFloat(float(dic['BraidPims7_49'])), findFloat(float(dic['BraidPims7_50'])), 
                findFloat(float(dic['BraidPims7_51'])), findFloat(float(dic['BraidPims7_52'])), 
                findFloat(float(dic['BraidPims7_53'])), findFloat(float(dic['BraidPims7_54'])), 
                findFloat(float(dic['BraidPims7_55'])), findFloat(float(dic['BraidPims7_56'])), 
                findFloat(float(dic['BraidPims7_57'])), findFloat(float(dic['BraidPims7_58'])), 
                findFloat(float(dic['BraidPims7_59'])), findFloat(float(dic['BraidPims7_60'])), 
                findFloat(float(dic['BraidPims7_61'])), findFloat(float(dic['BraidPims7_62'])), 
                findFloat(float(dic['BraidPims7_63'])), findFloat(float(dic['BraidPims7_64'])), 
                findFloat(float(dic['BraidPims7_65'])), findFloat(float(dic['BraidPims7_66'])), 
                findFloat(float(dic['BraidPims7_67'])), findFloat(float(dic['BraidPims7_68'])), 
                findFloat(float(dic['BraidPims7_69'])), findFloat(float(dic['BraidPims7_70'])), 
                findFloat(float(dic['BraidPims7_71'])), findFloat(float(dic['BraidPims7_72'])), 
                findFloat(float(dic['BraidPims7_73'])), findFloat(float(dic['BraidPims7_74'])), 
                findFloat(float(dic['BraidPims7_75'])), findFloat(float(dic['BraidPims7_76'])), 
                findFloat(float(dic['BraidPims7_77'])), findFloat(float(dic['BraidPims7_78'])), 
                findFloat(float(dic['BraidPims7_79'])), findFloat(float(dic['BraidPims7_80'])), 
                findFloat(float(dic['BraidPims7_81'])), findFloat(float(dic['BraidPims7_82'])))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO braiderpims8 ( b8_drum_in , b8_drum_out , b8_rtm_1 , b8_rtm_2 , b8_rtm_3 , b8_rtm_4 , b8_rtm_5, b8_rtm_6, b8_rtm_7, b8_rtm_8, b8_rtm_9, b8_rtm_10, b8_rtm_11 , b8_rtm_12 , b8_rtm_13 , b8_rtm_14 , b8_rtm_15, b8_rtm_16, b8_rtm_17, b8_rtm_18, b8_rtm_19, b8_rtm_20, b8_rtm_21 , b8_rtm_22 , b8_rtm_23 , b8_rtm_24 , b8_rtm_25, b8_rtm_26, b8_rtm_27, b8_rtm_28, b8_rtm_29, b8_rtm_30, b8_rtm_31 , b8_rtm_32 , b8_rtm_33 , b8_rtm_34 , b8_rtm_35, b8_rtm_36, b8_rtm_37, b8_rtm_38, b8_rtm_39, b8_rtm_40, b8_rtm_41 , b8_rtm_42 , b8_rtm_43 , b8_rtm_44 , b8_rtm_45, b8_rtm_46, b8_rtm_47, b8_rtm_48, b8_rtm_49, b8_rtm_50, b8_rtm_51 , b8_rtm_52 , b8_rtm_53 , b8_rtm_54 , b8_rtm_55, b8_rtm_56, b8_rtm_57, b8_rtm_58, b8_rtm_59, b8_rtm_60, b8_rtm_61 , b8_rtm_62 , b8_rtm_63 , b8_rtm_64 , b8_rtm_65, b8_rtm_66, b8_rtm_67, b8_rtm_68, b8_rtm_69, b8_rtm_70, b8_rtm_71 , b8_rtm_72 , b8_rtm_73 , b8_rtm_74 , b8_rtm_75, b8_rtm_76, b8_rtm_77, b8_rtm_78, b8_rtm_79, b8_rtm_80) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( str(dic['BraidPims8_1']), str(dic['BraidPims8_2']),
                findFloat(float(dic['BraidPims8_3'])), findFloat(float(dic['BraidPims8_4'])),
                findFloat(float(dic['BraidPims8_5'])), findFloat(float(dic['BraidPims8_6'])), 
                findFloat(float(dic['BraidPims8_7'])), findFloat(float(dic['BraidPims8_8'])), 
                findFloat(float(dic['BraidPims8_9'])), findFloat(float(dic['BraidPims8_10'])), 
                findFloat(float(dic['BraidPims8_11'])), findFloat(float(dic['BraidPims8_12'])), 
                findFloat(float(dic['BraidPims8_13'])), findFloat(float(dic['BraidPims8_14'])), 
                findFloat(float(dic['BraidPims8_15'])), findFloat(float(dic['BraidPims8_16'])), 
                findFloat(float(dic['BraidPims8_17'])), findFloat(float(dic['BraidPims8_18'])), 
                findFloat(float(dic['BraidPims8_19'])), findFloat(float(dic['BraidPims8_20'])), 
                findFloat(float(dic['BraidPims8_21'])), findFloat(float(dic['BraidPims8_22'])), 
                findFloat(float(dic['BraidPims8_23'])), findFloat(float(dic['BraidPims8_24'])), 
                findFloat(float(dic['BraidPims8_25'])), findFloat(float(dic['BraidPims8_26'])), 
                findFloat(float(dic['BraidPims8_27'])), findFloat(float(dic['BraidPims8_28'])), 
                findFloat(float(dic['BraidPims8_29'])), findFloat(float(dic['BraidPims8_30'])), 
                findFloat(float(dic['BraidPims8_31'])), findFloat(float(dic['BraidPims8_32'])), 
                findFloat(float(dic['BraidPims8_33'])), findFloat(float(dic['BraidPims8_34'])),
                findFloat(float(dic['BraidPims8_35'])), findFloat(float(dic['BraidPims8_36'])), 
                findFloat(float(dic['BraidPims8_37'])), findFloat(float(dic['BraidPims8_38'])), 
                findFloat(float(dic['BraidPims8_39'])), findFloat(float(dic['BraidPims8_40'])), 
                findFloat(float(dic['BraidPims8_41'])), findFloat(float(dic['BraidPims8_42'])), 
                findFloat(float(dic['BraidPims8_43'])), findFloat(float(dic['BraidPims8_44'])), 
                findFloat(float(dic['BraidPims8_45'])), findFloat(float(dic['BraidPims8_46'])), 
                findFloat(float(dic['BraidPims8_47'])), findFloat(float(dic['BraidPims8_48'])), 
                findFloat(float(dic['BraidPims8_49'])), findFloat(float(dic['BraidPims8_50'])), 
                findFloat(float(dic['BraidPims8_51'])), findFloat(float(dic['BraidPims8_52'])), 
                findFloat(float(dic['BraidPims8_53'])), findFloat(float(dic['BraidPims8_54'])), 
                findFloat(float(dic['BraidPims8_55'])), findFloat(float(dic['BraidPims8_56'])), 
                findFloat(float(dic['BraidPims8_57'])), findFloat(float(dic['BraidPims8_58'])), 
                findFloat(float(dic['BraidPims8_59'])), findFloat(float(dic['BraidPims8_60'])), 
                findFloat(float(dic['BraidPims8_61'])), findFloat(float(dic['BraidPims8_62'])), 
                findFloat(float(dic['BraidPims8_63'])), findFloat(float(dic['BraidPims8_64'])), 
                findFloat(float(dic['BraidPims8_65'])), findFloat(float(dic['BraidPims8_66'])), 
                findFloat(float(dic['BraidPims8_67'])), findFloat(float(dic['BraidPims8_68'])), 
                findFloat(float(dic['BraidPims8_69'])), findFloat(float(dic['BraidPims8_70'])), 
                findFloat(float(dic['BraidPims8_71'])), findFloat(float(dic['BraidPims8_72'])), 
                findFloat(float(dic['BraidPims8_73'])), findFloat(float(dic['BraidPims8_74'])), 
                findFloat(float(dic['BraidPims8_75'])), findFloat(float(dic['BraidPims8_76'])), 
                findFloat(float(dic['BraidPims8_77'])), findFloat(float(dic['BraidPims8_78'])), 
                findFloat(float(dic['BraidPims8_79'])), findFloat(float(dic['BraidPims8_80'])), 
                findFloat(float(dic['BraidPims8_81'])), findFloat(float(dic['BraidPims8_82'])))
        mycursor.execute(sql, val)
        '''
       
        print("Thread1: Data Dumped")

        

    except(error):
        print("Error ::", error)
        #continue



def update():
    pass




# display loop (in main thread)
if __name__ == "__main__":
        try:
                print("Thread1:PushedClient Initialized")
                client = mqttClient.Client("MQTT3899886465")
                client.username_pw_set("", "")
                client.on_message=on_message
                client.on_connect=on_connect
                #client.on_log=on_log
                client.on_disconnect=on_disconnect
                client.connect('localhost', 1883)
                client.loop_forever()
        except KeyboardInterrupt:
                client.disconnect()
