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
        
        tempExtStop1 = tempExtStop2 = tempExtStop3 = tempExtStop4 = False
        tempExtStopID1 = tempExtStopID2 = tempExtStopID3 = tempExtStopID4 = False
        tempManStop1 = tempManStop2 = tempManStop3 = False
        tempManStopID1 = tempManStopID2 = tempManStopID3 = False
        tempVulStop1 = False
        tempVulStopID1 = False
        tempTestStop1 = tempTestStop2 = tempTestStop3 = False
        tempTestStopID1 = tempTestStopID2 = tempTestStopID3 = False

        tempExtSetup1 = tempExtSetup2 = tempExtSetup3 = tempExtSetup4 = False
        tempExtOpt1 = tempExtOpt2 = tempExtOpt3 = tempExtOpt4 = False
        tempExtClean1 = tempExtClean2 = tempExtClean3 = tempExtClean4 = False
        
        
        tempMan1_1 = tempMan1_2 = tempMan1_3 = tempMan1_4 = tempMan1_5 = tempMan1_6 = tempMan1_7 = tempMan1_8 = tempMan1_9 = tempMan1_10 = tempMan1_11 = tempMan1_12 = tempMan1_13 = tempMan1_14 = tempMan1_15 = tempMan1_16 = tempMan1_17 = tempMan1_18 = False
        tempMan2_1 = tempMan2_2 = tempMan2_3 = tempMan2_4 = tempMan2_5 = tempMan2_6 = tempMan2_7 = tempMan2_8 = tempMan2_9 = tempMan2_10 = tempMan2_11 = tempMan2_12 = tempMan2_13 = tempMan2_14 = tempMan2_15 = tempMan2_16 = tempMan2_17 = tempMan2_18 = False 
        tempMan3_1 = tempMan3_2 = tempMan3_3 = tempMan3_4 = tempMan3_5 = tempMan3_6 = tempMan3_7 = tempMan3_8 = tempMan3_9 = tempMan3_10 = tempMan3_11 = tempMan3_12 = tempMan3_13 = tempMan3_14 = tempMan3_15 = tempMan3_16 = tempMan3_17 = tempMan3_18 = False 
        
        tempPlc_1 = tempPlc_2 = tempPlc_3 = tempPlc_4 = tempPlc_5 = tempPlc_6 = tempPlc_7 = tempPlc_8 = tempPlc_9 = False

        tempExt1_1 = tempExt1_2 = tempExt1_3 = tempExt1_4 = tempExt1_5 = tempExt1_6 = tempExt1_7 = tempExt1_8 = tempExt1_9 = tempExt1_10 = tempExt1_11 = tempExt1_12 = tempExt1_13 = tempExt1_14 = tempExt1_15 = tempExt1_16 = tempExt1_17 = tempExt1_18 = tempExt1_19 = tempExt1_20 = tempExt1_21 = tempExt1_22 = tempExt1_23 = tempExt1_24 = tempExt1_25 = tempExt1_26 = tempExt1_27 = tempExt1_28 = tempExt1_29 = tempExt1_30 = tempExt1_31 = tempExt1_32 =False
        tempExt2_1 = tempExt2_2 = tempExt2_3 = tempExt2_4 = tempExt2_5 = tempExt2_6 = tempExt2_7 = tempExt2_8 = tempExt2_9 = tempExt2_10 = tempExt2_11 = tempExt2_12 = tempExt2_13 = tempExt2_14 = tempExt2_15 = tempExt2_16 = tempExt2_17 = tempExt2_18 = tempExt2_19 = tempExt2_20 = tempExt2_21 = tempExt2_22 = tempExt2_23 = tempExt2_24 = tempExt2_25 = tempExt2_26 = tempExt2_27 = tempExt2_28 = tempExt2_29 = tempExt2_30 = tempExt2_31 = tempExt2_32 =False 
        tempExt3_1 = tempExt3_2 = tempExt3_3 = tempExt3_4 = tempExt3_5 = tempExt3_6 = tempExt3_7 = tempExt3_8 = tempExt3_9 = tempExt3_10 = tempExt3_11 = tempExt3_12 = tempExt3_13 = tempExt3_14 = tempExt3_15 = tempExt3_16 = tempExt3_17 = tempExt3_18 = tempExt3_19 = tempExt3_20 = tempExt3_21 = tempExt3_22 = tempExt3_23 = tempExt3_24 = tempExt3_25 = tempExt3_26 = tempExt3_27 = tempExt3_28 = tempExt3_29 = tempExt3_30 = tempExt3_31 = tempExt3_32 =False 
        tempExt4_1 = tempExt4_2 = tempExt4_3 = tempExt4_4 = tempExt4_5 = tempExt4_6 = tempExt4_7 = tempExt4_8 = tempExt4_9 = tempExt4_10 = tempExt4_11 = tempExt4_12 = tempExt4_13 = tempExt4_14 = tempExt4_15 = tempExt4_16 = tempExt4_17 = tempExt4_18 = tempExt4_19 = tempExt4_20 = tempExt4_21 = tempExt4_22 = tempExt4_23 = tempExt4_24 = tempExt4_25 = tempExt4_26 = tempExt4_27 = tempExt4_28 = tempExt4_29 = tempExt4_30 = tempExt4_31 = tempExt4_32 =False 
        
        tempExtProd1 = False
        tempExtProd2 = False
        tempExtProd3 = False
        tempExtProd4 = False

        tempExtStart1 = tempExtStart2 = tempExtStart3 = tempExtStart4 = False
        tempExtDT1 = tempExtDT2 = tempExtDT3 = tempExtDT4 = False
        tempExtEnd1 = tempExtEnd2 = tempExtEnd3 = tempExtEnd4 = False
        tempExtElapsed1 = tempExtElapsed2 = tempExtElapsed3 = tempExtElapsed4 = False

        tempVulProd1 = tempVulProd2 = tempVulProd3 = tempVulProd4 = False
        tempVulStart1 = tempVulStart2 = tempVulStart3 = tempVulStart4 = False
        tempVulDT1 = tempVulDT2 = tempVulDT3 = tempVulDT4 = False
        tempVulEnd1 = tempVulEnd2 = tempVulEnd3 = tempVulEnd4 = False

        tempManProd1 = tempManProd2 = tempManProd3 = tempManProd4 = False
        tempManStart1 = tempManStart2 = tempManStart3 = tempManStart4 = False
        tempManDT1 = tempManDT2 = tempManDT3 = tempManDT4 = False
        tempManEnd1 = tempManEnd2 = tempManEnd3 = tempManEnd4 = False

        tempTestProd1 = tempTestProd2 = tempTestProd3 = tempTestProd4 = False
        tempTestStart1 = tempTestStart2 = tempTestStart3 = tempTestStart4 = False
        tempTestDT1 = tempTestDT2 = tempTestDT3 = tempTestDT4 = False
        tempTestEnd1 = tempTestEnd2 = tempTestEnd3 = tempTestEnd4 = False

        
        tempVul1_1 = tempVul1_2 = tempVul1_3 = tempVul1_4 = tempVul1_5 = tempVul1_6 = tempVul1_7 = tempVul1_8 = tempVul1_9 = tempVul1_10 = tempVul1_11 = tempVul1_12 = tempVul1_13 = tempVul1_14 = tempVul1_15 = tempVul1_16 = tempVul1_17 = tempVul1_18 = tempVul1_19 = tempVul1_20 = tempVul1_21 = tempVul1_22 = tempVul1_23 = tempVul1_24 = tempVul1_25 = tempVul1_26 = tempVul1_27 = tempVul1_28 = tempVul1_29 = tempVul1_30 = tempVul1_31 = tempVul1_32 =False

        tempTest1_1 = tempTest1_2 = tempTest1_3 = tempTest1_4 = tempTest1_5 = tempTest1_6 = tempTest1_7 = tempTest1_8 = tempTest1_9 = tempTest1_10 = tempTest1_11 = tempTest1_12 = tempTest1_13 = tempTest1_14 = tempTest1_15 = tempTest1_16 = False
        tempTest2_1 = tempTest2_2 = tempTest2_3 = tempTest2_4 = tempTest2_5 = tempTest2_6 = tempTest2_7 = tempTest2_8 = tempTest2_9 = tempTest2_10 = tempTest2_11 = tempTest2_12 = tempTest2_13 = tempTest2_14 = tempTest2_15 = tempTest2_16 = False 
        tempTest3_1 = tempTest3_2 = tempTest3_3 = tempTest3_4 = tempTest3_5 = tempTest3_6 = tempTest3_7 = tempTest3_8 = tempTest3_9 = tempTest3_10 = tempTest3_11 = tempTest3_12 = tempTest3_13 = tempTest3_14 = tempTest3_15 = tempTest3_16 = False 

 
regs = []
dic = {}

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


def is_valid_json(data):
        try:
                json_obj = json.loads(data)
        except ValueError as e:
                connection.ping(reconnect=True)
                if(globalBS.tempPlc_9 != True):
                        globalBS.tempPlc_9 = True
                        sql = "INSERT INTO plcstatus ( col_id, client2 ) VALUES (%s,%s)"
                        val = (18, True)
                        mycursor.execute(sql, val)
                print("Invalid data found")
                return False
        return True

#subscribing
def sub(topic):
    client = mqttClient.Client("MQTT")
    client.username_pw_set(username, pwd)
    client.connect(broker_add, port_no)
    client.subscribe(topic)
    client.disconnect()



def on_connect2(client, userdata, flags, rc):
    client.subscribe('polyhose2/')
    print("Thread2: subscribed")


def on_message2(client, userdata, message):
        try:    
                global count2
                connection.ping(reconnect=True)
                if message.topic == 'polyhose2/':
                        count2 += 1
                        json_data = str(message.payload.decode("utf-8","ignore"))
                        if(is_valid_json(json_data)):
                                json_obj = json.loads(json_data)
                                if(findBool(json_obj['connected'])):
                                        if(globalBS.tempPlc_9 != False):
                                                globalBS.tempPlc_9 = False
                                                sql = "INSERT INTO plcstatus ( col_id, client2 ) VALUES (%s,%s)"
                                                val = (18, False)
                                                mycursor.execute(sql, val)

                                        dic['Plc_1'] = fixedInt(json_obj['M-M_A_1-18']) #Mandrel 1
                                        dic['Plc_2'] = fixedInt(json_obj['M-M_A_2-18']) #Mandrel 2
                                        dic['Plc_3'] = fixedInt(json_obj['M-E_A_1-32']) #Extruder 1
                                        dic['Plc_4'] = fixedInt(json_obj['M-E_A_3-32']) #Extruder 3
                                        dic['Plc_5'] = fixedInt(json_obj['M-V_A_1-32']) #Vulcanizer 1
                                        dic['Plc_6'] = fixedInt(json_obj['M-T_A_1-16']) #Testing 1
                                        dic['Plc_7'] = fixedInt(json_obj['M-T_A_2-16']) #Testing 2
                                        dic['Plc_8'] = fixedInt(json_obj['M-T_A_3-16']) #Testing 3

                                        dic['ExtProd1_1'] = fixedInt(json_obj['M-E_H_1-0']) #PIR
                                        dic['ExtProd1_2'] = fixedInt(json_obj['M-E_R_1-1']) #OPERATOR NAME
                                        dic['ExtProd1_3'] = fixedInt(json_obj['M-E_H_1-56']) #MPIR
                                        dic['ExtProd1_4'] = fixedInt(json_obj['M-E_H_1-37']) #ACT_KG
                                        dic['ExtProd1_5'] = fixedInt(json_obj['M-E_R_1-16']) #Actual Speed
                                        dic['ExtProd1_6'] = fixedInt(json_obj['M-E_R_1-14']) #Ex HD PR
                                        dic['ExtProd1_7'] = fixedInt(json_obj['M-E_H_1-47']) #Start Temp
                                        dic['ExtProd1_8'] = fixedInt(json_obj['M-E_H_1-44']) #Process Start Bit
                                        dic['ExtProd1_9'] = fixedInt(json_obj['M-E_H_1-49']) #Last Temp
                                        dic['ExtProd1_10'] = fixedInt(json_obj['M-E_P_1-0']) #drum in
                                        dic['ExtProd1_11'] = fixedInt(json_obj['M-E_P_1-1']) #drum out
                                        dic['ExtProd1_12'] = fixedInt(json_obj['M-E_H_1-48']) #Middle temp
                                        dic['ExtProd1_13'] = fixedInt(json_obj['M-E_H_1-50']) #Machine run fb
                                        dic['ExtProd1_14'] = fixedInt(json_obj['M-E_H_1-54']) #Hose_type
                                        dic['ExtProd1_15'] = fixedInt(json_obj['M-E_H_1-55']) #Hose_size
                                        dic['ExtProd3_1'] = fixedInt(json_obj['M-E_H_3-0']) #PIR
                                        dic['ExtProd3_2'] = fixedInt(json_obj['M-E_R_3-1']) #OPERATOR NAME
                                        dic['ExtProd3_3'] = fixedInt(json_obj['M-M_H_1-0']) #MPIR
                                        dic['ExtProd3_4'] = fixedInt(json_obj['M-E_H_3-37']) #ACT_KG
                                        dic['ExtProd3_5'] = fixedInt(json_obj['M-E_R_3-16']) #Actual Speed
                                        dic['ExtProd3_6'] = fixedInt(json_obj['M-E_R_3-14']) #Ex HD PR
                                        dic['ExtProd3_7'] = fixedInt(json_obj['M-E_H_3-47']) #Start Temp
                                        dic['ExtProd3_8'] = fixedInt(json_obj['M-E_H_3-44']) #Process Start Bit
                                        dic['ExtProd3_9'] = fixedInt(json_obj['M-E_H_3-49']) #Last Temp
                                        dic['ExtProd3_10'] = fixedInt(json_obj['M-E_P_3-0']) #drum in
                                        dic['ExtProd3_11'] = fixedInt(json_obj['M-E_P_3-1']) #drum out
                                        dic['ExtProd3_12'] = fixedInt(json_obj['M-E_H_3-48']) #Middle temp
                                        dic['ExtProd3_13'] = fixedInt(json_obj['M-E_H_3-50']) #Machine run fb
                                        dic['ExtProd3_14'] = fixedInt(json_obj['M-E_H_3-54']) #Hose_type
                                        dic['ExtProd3_15'] = fixedInt(json_obj['M-E_H_3-55']) #Hose_si
                                        dic['VulProd1_1'] = fixedInt(json_obj['M-V_R_1-0']) #PIR
                                        dic['VulProd1_2'] = fixedInt(json_obj['M-V_R_1-1']) #OPERATOR NAME
                                        dic['VulProd1_3'] = fixedInt(json_obj['M-V_H_1-3']) # PIR_2
                                        dic['VulProd1_4'] = fixedInt(json_obj['M-V_H_1-4']) # PIR 3
                                        dic['VulProd1_5'] = fixedInt(json_obj['M-V_H_1-5']) # PIR 4
                                        dic['VulProd1_6'] = fixedInt(json_obj['M-V_H_1-6']) # PIR 5
                                        dic['VulProd1_7'] = fixedInt(json_obj['M-V_H_1-7']) # PIR 6
                                        dic['VulProd1_8'] = fixedInt(json_obj['M-V_H_1-8']) #Process Start Bit
                                        dic['VulProd1_9'] = fixedInt(json_obj['M-V_P_1-0']) #DRUM IN
                                        dic['VulProd1_10'] = fixedInt(json_obj['M-V_H_1-2']) # Machine Run FB
                                        dic['VulProd1_11'] = fixedInt(json_obj['M-V_H_1-14']) # Hose Type 1
                                        dic['VulProd1_12'] = fixedInt(json_obj['M-V_H_1-37']) # Hose_type 2
                                        dic['VulProd1_13'] = fixedInt(json_obj['M-V_H_1-38']) # Hose_type 3
                                        dic['VulProd1_14'] = fixedInt(json_obj['M-V_H_1-39']) # Hose_type 4
                                        dic['VulProd1_15'] = fixedInt(json_obj['M-V_H_1-40']) # Hose_type 5
                                        dic['VulProd1_16'] = fixedInt(json_obj['M-V_H_1-41']) # Hose_type 6
                                        dic['VulProd1_17'] = fixedInt(json_obj['M-V_H_1-15']) # Hose_size 1
                                        dic['VulProd1_18'] = fixedInt(json_obj['M-V_H_1-42']) # Hose_size 2
                                        dic['VulProd1_19'] = fixedInt(json_obj['M-V_H_1-43']) # Hose_size 3
                                        dic['VulProd1_20'] = fixedInt(json_obj['M-V_H_1-44']) # Hose_size 4
                                        dic['VulProd1_21'] = fixedInt(json_obj['M-V_H_1-45']) # Hose_size 5
                                        dic['VulProd1_22'] = fixedInt(json_obj['M-V_H_1-46']) # Hose_size
                                        dic['ManProd1_1'] = fixedInt(json_obj['M-M_R_1-0']) #PIR
                                        dic['ManProd1_2'] = fixedInt(json_obj['M-M_R_1-1']) #OPERATOR NAME
                                        dic['ManProd1_3'] = fixedInt(json_obj['M-M_H_1-0']) #New PIR 1
                                        dic['ManProd1_4'] = fixedInt(json_obj['M-M_H_1-1']) #Old PIR 1
                                        dic['ManProd1_5'] = fixedInt(json_obj['M-M_H_1-2']) #Old PIR 2
                                        dic['ManProd1_6'] = fixedInt(json_obj['M-M_H_1-3']) #Old PIR 3
                                        dic['ManProd1_7'] = fixedInt(json_obj['M-M_P_1-0']) #DRUM IN
                                        dic['ManProd1_8'] = fixedInt(json_obj['M-M_H_1-4']) #Process Start Bit
                                        dic['ManProd1_9'] = fixedInt(json_obj['M-M_H_1-7']) #Q
                                        dic['ManProd2_1'] = fixedInt(json_obj['M-M_R_2-0']) #PIR
                                        dic['ManProd2_2'] = fixedInt(json_obj['M-M_R_2-1']) #OPERATOR NAME
                                        dic['ManProd2_3'] = fixedInt(json_obj['M-M_H_2-0']) #New PIR 1
                                        dic['ManProd2_4'] = fixedInt(json_obj['M-M_H_2-1']) #Old PIR 1
                                        dic['ManProd2_5'] = fixedInt(json_obj['M-M_H_2-2']) #Old PIR 2
                                        dic['ManProd2_6'] = fixedInt(json_obj['M-M_H_2-3']) #Old PIR 3
                                        dic['ManProd2_7'] = fixedInt(json_obj['M-M_P_2-0']) #DRUM IN
                                        dic['ManProd2_8'] = fixedInt(json_obj['M-M_H_2-4']) #Process Start Bit
                                        dic['ManProd2_9'] = fixedInt(json_obj['M-M_H_2-7']) #Q
                                        dic['TestProd1_1'] = fixedInt(json_obj['M-T_R_1-0']) #PIR
                                        dic['TestProd1_2'] = fixedInt(json_obj['M-T_R_1-1']) #OPERATOR NAME
                                        dic['TestProd1_3'] = fixedInt(json_obj['M-T_R_1-5']) #Proof Pres
                                        dic['TestProd1_4'] = fixedInt(json_obj['M-T_H_1-2']) #Scrap Len
                                        dic['TestProd1_5'] = fixedInt(json_obj['M-T_P_1-0']) #DRUM IN
                                        dic['TestProd1_6'] = fixedInt(json_obj['M-T_P_1-1']) #DRUM OUT
                                        dic['TestProd1_8'] = fixedInt(json_obj['M-T_H_1-0']) #Process Start Bit
                                        dic['TestProd1_9'] = fixedInt(json_obj['M-T_H_1-4']) #Status
                                        dic['TestProd1_10'] = fixedInt(json_obj['M-T_H_1-10']) #Hose_size
                                        dic['TestProd1_11'] = fixedInt(json_obj['M-T_H_1-9']) #Hose_type

                                        dic['TestProd2_1'] = fixedInt(json_obj['M-T_R_2-0']) #PIR
                                        dic['TestProd2_2'] = fixedInt(json_obj['M-T_R_2-1']) #OPERATOR NAME
                                        dic['TestProd2_3'] = fixedInt(json_obj['M-T_R_2-5']) #Proof Pres
                                        dic['TestProd2_4'] = fixedInt(json_obj['M-T_H_2-2']) #Scrap Len
                                        dic['TestProd2_5'] = fixedInt(json_obj['M-T_P_2-0']) #DRUM IN
                                        dic['TestProd2_6'] = fixedInt(json_obj['M-T_P_2-1']) #DRUM OUT
                                        dic['TestProd2_8'] = fixedInt(json_obj['M-T_H_2-0']) #Process Start Bit
                                        dic['TestProd2_9'] = fixedInt(json_obj['M-T_H_2-4']) #Status
                                        dic['TestProd2_10'] = fixedInt(json_obj['M-T_H_2-10']) #Hose_size
                                        dic['TestProd2_11'] = fixedInt(json_obj['M-T_H_2-9']) #Hose_ty
                                        dic['TestProd3_1'] = fixedInt(json_obj['M-T_R_3-0']) #PIR
                                        dic['TestProd3_2'] = fixedInt(json_obj['M-T_R_3-1']) #OPERATOR NAME
                                        dic['TestProd3_3'] = fixedInt(json_obj['M-T_R_3-5']) #Proof Pres
                                        dic['TestProd3_4'] = fixedInt(json_obj['M-T_H_3-2']) #Scrap Len
                                        dic['TestProd3_5'] = fixedInt(json_obj['M-T_P_3-0']) #DRUM IN
                                        dic['TestProd3_6'] = fixedInt(json_obj['M-T_P_3-1']) #DRUM OUT
                                        dic['TestProd3_8'] = fixedInt(json_obj['M-T_H_3-0']) #Process Start Bit
                                        dic['TestProd3_9'] = fixedInt(json_obj['M-T_H_3-4']) #Status
                                        dic['TestProd3_10'] = fixedInt(json_obj['M-T_H_3-10']) #Hose_size
                                        dic['TestProd3_11'] = fixedInt(json_obj['M-T_H_3-9']) #Hose_type

                                        dic['ManAlarm1_1'] = fixedInt(json_obj['M-M_A_1-0']) #TCI-1 PUMP MPCB TRIPPED 
                                        dic['ManAlarm1_2'] = fixedInt(json_obj['M-M_A_1-1']) #TCI-1 AGITATOR MPCB TRIPPED
                                        dic['ManAlarm1_3'] = fixedInt(json_obj['M-M_A_1-2']) #TCI-2 PUMP MPCB TRIPPED
                                        dic['ManAlarm1_4'] = fixedInt(json_obj['M-M_A_1-3']) #TCI=2 AGITATOR MPCB TRIPPED
                                        dic['ManAlarm1_5'] = fixedInt(json_obj['M-M_A_1-4']) #TAKEUP DRIVE FAULT
                                        dic['ManAlarm1_6'] = fixedInt(json_obj['M-M_A_1-5']) #TAKEUP DRIVE ALARM
                                        dic['ManAlarm1_7'] = fixedInt(json_obj['M-M_A_1-6']) #MANDREL OD HIGH LINE STOPPED
                                        dic['ManAlarm1_8'] = fixedInt(json_obj['M-M_A_1-7']) #MANDREL OD LOW LINE STOPPED
                                        dic['ManAlarm1_9'] = fixedInt(json_obj['M-M_A_1-8']) #PANEL EMERGENCY PRESSED
                                        dic['ManAlarm1_10'] = fixedInt(json_obj['M-M_A_1-9'] )#TAKEUP EMERGENCY PRESSED
                                        dic['ManAlarm1_11'] = fixedInt(json_obj['M-M_A_1-10']) #SPARE 1
                                        dic['ManAlarm1_12'] = fixedInt(json_obj['M-M_A_1-11']) #SPARE 2
                                        dic['ManAlarm1_13'] = fixedInt(json_obj['M-M_A_1-12']) #SPARE 3
                                        dic['ManAlarm1_14'] = fixedInt(json_obj['M-M_A_1-13']) #SPARE 4
                                        dic['ManAlarm1_15'] = fixedInt(json_obj['M-M_A_1-14']) #SPARE 5
                                        dic['ManAlarm1_16'] = fixedInt(json_obj['M-M_A_1-15']) #SPARE 6
                                        dic['ManAlarm1_17'] = fixedInt(json_obj['M-M_A_1-16']) #MANDREL OD HIGH
                                        dic['ManAlarm1_18'] = fixedInt(json_obj['M-M_A_1-17']) #MANDREL OD L
                                        dic['ManAlarm2_1'] = fixedInt(json_obj['M-M_A_2-0']) #TCI-1 PUMP MPCB TRIPPED 
                                        dic['ManAlarm2_2'] = fixedInt(json_obj['M-M_A_2-1']) #TCI-1 AGITATOR MPCB TRIPPED
                                        dic['ManAlarm2_3'] = fixedInt(json_obj['M-M_A_2-2']) #TCI-2 PUMP MPCB TRIPPED
                                        dic['ManAlarm2_4'] = fixedInt(json_obj['M-M_A_2-3']) #TCI=2 AGITATOR MPCB TRIPPED
                                        dic['ManAlarm2_5'] = fixedInt(json_obj['M-M_A_2-4']) #TAKEUP DRIVE FAULT
                                        dic['ManAlarm2_6'] = fixedInt(json_obj['M-M_A_2-5']) #TAKEUP DRIVE ALARM
                                        dic['ManAlarm2_7'] = fixedInt(json_obj['M-M_A_2-6']) #MANDREL OD HIGH LINE STOPPED
                                        dic['ManAlarm2_8'] = fixedInt(json_obj['M-M_A_2-7']) #MANDREL OD LOW LINE STOPPED
                                        dic['ManAlarm2_9'] = fixedInt(json_obj['M-M_A_2-8']) #PANEL EMERGENCY PRESSED
                                        dic['ManAlarm2_10'] = fixedInt(json_obj['M-M_A_2-9']) #TAKEUP EMERGENCY PRESSED
                                        dic['ManAlarm2_11'] = fixedInt(json_obj['M-M_A_2-10']) #SPARE 1
                                        dic['ManAlarm2_12'] = fixedInt(json_obj['M-M_A_2-11']) #SPARE 2
                                        dic['ManAlarm2_13'] = fixedInt(json_obj['M-M_A_2-12']) #SPARE 3
                                        dic['ManAlarm2_14'] = fixedInt(json_obj['M-M_A_2-13']) #SPARE 4
                                        dic['ManAlarm2_15'] = fixedInt(json_obj['M-M_A_2-14']) #SPARE 5
                                        dic['ManAlarm2_16'] = fixedInt(json_obj['M-M_A_2-15']) #SPARE 6
                                        dic['ManAlarm2_17'] = fixedInt(json_obj['M-M_A_2-16']) #MANDREL OD HIGH
                                        dic['ManAlarm2_18'] = fixedInt(json_obj['M-M_A_2-17']) #MANDREL OD LOW
                                        
                                        dic['ExtAlarm1_1'] = fixedInt(json_obj['M-E_A_1-0']) #THICKNESS  HIGH
                                        dic['ExtAlarm1_2'] = fixedInt(json_obj['M-E_A_1-1']) #THICKNESS LOW
                                        dic['ExtAlarm1_3'] = fixedInt(json_obj['M-E_A_1-2']) #HEAD TEMPERATURE HIGH
                                        dic['ExtAlarm1_4'] = fixedInt(json_obj['M-E_A_1-3']) #HEAD TEMPERATURE LOW
                                        dic['ExtAlarm1_5'] = fixedInt(json_obj['M-E_A_1-4']) #ZONE 2 TEMPERATURE HIGH
                                        dic['ExtAlarm1_6'] = fixedInt(json_obj['M-E_A_1-5']) #ZONE 2 TEMPERATURE LOW 
                                        dic['ExtAlarm1_7'] = fixedInt(json_obj['M-E_A_1-6']) #ZONE 3 TEMPERATURE HIGH
                                        dic['ExtAlarm1_8'] = fixedInt(json_obj['M-E_A_1-7']) #ZONE 3 TEMPERATURE LOW 
                                        dic['ExtAlarm1_9'] = fixedInt(json_obj['M-E_A_1-8']) #EXTRUDER CURRENT WARNING HIGH
                                        dic['ExtAlarm1_10'] = fixedInt(json_obj['M-E_A_1-9'] )#EXTRUDER CURRENT ALARM HIGH
                                        dic['ExtAlarm1_11'] = fixedInt(json_obj['M-E_A_1-10']) #EXTRUDER PRESSURE WANING HIGH
                                        dic['ExtAlarm1_12'] = fixedInt(json_obj['M-E_A_1-11']) #EXTRUDER PRESSURE ALARM HIGH
                                        dic['ExtAlarm1_13'] = fixedInt(json_obj['M-E_A_1-12']) #OUTER DIAMETER HIGH
                                        dic['ExtAlarm1_14'] = fixedInt(json_obj['M-E_A_1-13']) #OUTER DIAMETER LOW
                                        dic['ExtAlarm1_15'] = fixedInt(json_obj['M-E_A_1-14']) #INNER DIAMETER HIGH
                                        dic['ExtAlarm1_16'] = fixedInt(json_obj['M-E_A_1-15']) #INNER DIAMETER LOW
                                        dic['ExtAlarm1_17'] = fixedInt(json_obj['M-E_A_1-16']) #TAKEUP2 END LIMIT ACTIVATED
                                        dic['ExtAlarm1_18'] = fixedInt(json_obj['M-E_A_1-17']) #FEEDER EMERGENCY PRESSED
                                        dic['ExtAlarm1_19'] = fixedInt(json_obj['M-E_A_1-18']) #RED TAPE SENSOR DETECTED
                                        dic['ExtAlarm1_20'] = fixedInt(json_obj['M-E_A_1-19']) #EXTRUSION MATERIAL TEMPERATURE HIGH
                                        dic['ExtAlarm1_21'] = fixedInt(json_obj['M-E_A_1-20']) #EXTRUSION MATERIAL TEMPERATURE LOW 
                                        dic['ExtAlarm1_22'] = fixedInt(json_obj['M-E_A_1-21']) #SPARE-1
                                        dic['ExtAlarm1_23'] = fixedInt(json_obj['M-E_A_1-22']) #SPARE-2
                                        dic['ExtAlarm1_24'] = fixedInt(json_obj['M-E_A_1-23']) #SPARE-3
                                        dic['ExtAlarm1_25'] = fixedInt(json_obj['M-E_A_1-24']) #SCREW TEMPERATURE HIGH
                                        dic['ExtAlarm1_26'] = fixedInt(json_obj['M-E_A_1-25']) #SCREW TEMPERATURE LOW
                                        dic['ExtAlarm1_27'] = fixedInt(json_obj['M-E_A_1-26']) #EXTRUDER EMERGENCY PRESSED
                                        dic['ExtAlarm1_28'] = fixedInt(json_obj['M-E_A_1-27']) #INPUT CATTERPULLER EMERGENCY PRESSED
                                        dic['ExtAlarm1_29'] = fixedInt(json_obj['M-E_A_1-28']) #OUTPUT CATTERPULLER EMERGENCY PRESSED
                                        dic['ExtAlarm1_30'] = fixedInt(json_obj['M-E_A_1-29']) #TAKEUP1 EMERGENCY PRESSED
                                        dic['ExtAlarm1_31'] = fixedInt(json_obj['M-E_A_1-30']) #TAKEUP2 EMERGENCY PRESSED
                                        dic['ExtAlarm1_32'] = fixedInt(json_obj['M-E_A_1-31']) #TAKEUP1 END LIMIT ACTIVATED
                                       
                                        dic['ExtAlarm3_1'] = fixedInt(json_obj['M-E_A_3-0']) #THICKNESS  HIGH
                                        dic['ExtAlarm3_2'] = fixedInt(json_obj['M-E_A_3-1']) #THICKNESS LOW
                                        dic['ExtAlarm3_3'] = fixedInt(json_obj['M-E_A_3-2']) #HEAD TEMPERATURE HIGH
                                        dic['ExtAlarm3_4'] = fixedInt(json_obj['M-E_A_3-3']) #HEAD TEMPERATURE LOW
                                        dic['ExtAlarm3_5'] = fixedInt(json_obj['M-E_A_3-4']) #ZONE 2 TEMPERATURE HIGH
                                        dic['ExtAlarm3_6'] = fixedInt(json_obj['M-E_A_3-5']) #ZONE 2 TEMPERATURE LOW 
                                        dic['ExtAlarm3_7'] = fixedInt(json_obj['M-E_A_3-6']) #ZONE 3 TEMPERATURE HIGH
                                        dic['ExtAlarm3_8'] = fixedInt(json_obj['M-E_A_3-7']) #ZONE 3 TEMPERATURE LOW 
                                        dic['ExtAlarm3_9'] = fixedInt(json_obj['M-E_A_3-8']) #EXTRUDER CURRENT WARNING HIGH
                                        dic['ExtAlarm3_10'] = fixedInt(json_obj['M-E_A_3-9'] )#EXTRUDER CURRENT ALARM HIGH
                                        dic['ExtAlarm3_11'] = fixedInt(json_obj['M-E_A_3-10']) #EXTRUDER PRESSURE WANING HIGH
                                        dic['ExtAlarm3_12'] = fixedInt(json_obj['M-E_A_3-11']) #EXTRUDER PRESSURE ALARM HIGH
                                        dic['ExtAlarm3_13'] = fixedInt(json_obj['M-E_A_3-12']) #OUTER DIAMETER HIGH
                                        dic['ExtAlarm3_14'] = fixedInt(json_obj['M-E_A_3-13']) #OUTER DIAMETER LOW
                                        dic['ExtAlarm3_15'] = fixedInt(json_obj['M-E_A_3-14']) #INNER DIAMETER HIGH
                                        dic['ExtAlarm3_16'] = fixedInt(json_obj['M-E_A_3-15']) #INNER DIAMETER LOW
                                        dic['ExtAlarm3_17'] = fixedInt(json_obj['M-E_A_3-16']) #TAKEUP2 END LIMIT ACTIVATED
                                        dic['ExtAlarm3_18'] = fixedInt(json_obj['M-E_A_3-17']) #FEEDER EMERGENCY PRESSED
                                        dic['ExtAlarm3_19'] = fixedInt(json_obj['M-E_A_3-18']) #RED TAPE SENSOR DETECTED
                                        dic['ExtAlarm3_20'] = fixedInt(json_obj['M-E_A_3-19']) #EXTRUSION MATERIAL TEMPERATURE HIGH
                                        dic['ExtAlarm3_21'] = fixedInt(json_obj['M-E_A_3-20']) #EXTRUSION MATERIAL TEMPERATURE LOW 
                                        dic['ExtAlarm3_22'] = fixedInt(json_obj['M-E_A_3-21']) #SPARE-1
                                        dic['ExtAlarm3_23'] = fixedInt(json_obj['M-E_A_3-22']) #SPARE-2
                                        dic['ExtAlarm3_24'] = fixedInt(json_obj['M-E_A_3-23']) #SPARE-3
                                        dic['ExtAlarm3_25'] = fixedInt(json_obj['M-E_A_3-24']) #SCREW TEMPERATURE HIGH
                                        dic['ExtAlarm3_26'] = fixedInt(json_obj['M-E_A_3-25']) #SCREW TEMPERATURE LOW
                                        dic['ExtAlarm3_27'] = fixedInt(json_obj['M-E_A_3-26']) #EXTRUDER EMERGENCY PRESSED
                                        dic['ExtAlarm3_28'] = fixedInt(json_obj['M-E_A_3-27']) #INPUT CATTERPULLER EMERGENCY PRESSED
                                        dic['ExtAlarm3_29'] = fixedInt(json_obj['M-E_A_3-28']) #OUTPUT CATTERPULLER EMERGENCY PRESSED
                                        dic['ExtAlarm3_30'] = fixedInt(json_obj['M-E_A_3-29']) #TAKEUP1 EMERGENCY PRESSED
                                        dic['ExtAlarm3_31'] = fixedInt(json_obj['M-E_A_3-30']) #TAKEUP2 EMERGENCY PRESSED
                                        dic['ExtAlarm3_32'] = fixedInt(json_obj['M-E_A_3-31']) #TAKEUP1 END LIMIT ACTIVATED
                                      
                                        dic['VulAlarm1_1'] = fixedInt(json_obj['M-V_A_1-0']) #THICKNESS  HIGH
                                        dic['VulAlarm1_2'] = fixedInt(json_obj['M-V_A_1-1']) #THICKNESS LOW
                                        dic['VulAlarm1_3'] = fixedInt(json_obj['M-V_A_1-2']) #HEAD TEMPERATURE HIGH
                                        dic['VulAlarm1_4'] = fixedInt(json_obj['M-V_A_1-3']) #HEAD TEMPERATURE LOW
                                        dic['VulAlarm1_5'] = fixedInt(json_obj['M-V_A_1-4']) #ZONE 2 TEMPERATURE HIGH
                                        dic['VulAlarm1_6'] = fixedInt(json_obj['M-V_A_1-5']) #ZONE 2 TEMPERATURE LOW 
                                        dic['VulAlarm1_7'] = fixedInt(json_obj['M-V_A_1-6']) #ZONE 3 TEMPERATURE HIGH
                                        dic['VulAlarm1_8'] = fixedInt(json_obj['M-V_A_1-7']) #ZONE 3 TEMPERATURE LOW 
                                        dic['VulAlarm1_9'] = fixedInt(json_obj['M-V_A_1-8']) #EXTRUDER CURRENT WARNING HIGH
                                        dic['VulAlarm1_10'] = fixedInt(json_obj['M-V_A_1-9'] )#EXTRUDER CURRENT ALARM HIGH
                                        dic['VulAlarm1_11'] = fixedInt(json_obj['M-V_A_1-10']) #EXTRUDER PRESSURE WANING HIGH
                                        dic['VulAlarm1_12'] = fixedInt(json_obj['M-V_A_1-11']) #EXTRUDER PRESSURE ALARM HIGH
                                        dic['VulAlarm1_13'] = fixedInt(json_obj['M-V_A_1-12']) #OUTER DIAMETER HIGH
                                        dic['VulAlarm1_14'] = fixedInt(json_obj['M-V_A_1-13']) #OUTER DIAMETER LOW
                                        dic['VulAlarm1_15'] = fixedInt(json_obj['M-V_A_1-14']) #INNER DIAMETER HIGH
                                        dic['VulAlarm1_16'] = fixedInt(json_obj['M-V_A_1-15']) #INNER DIAMETER LOW
                                        dic['VulAlarm1_17'] = fixedInt(json_obj['M-V_A_1-16']) #TAKEUP2 END LIMIT ACTIVATED
                                        dic['VulAlarm1_18'] = fixedInt(json_obj['M-V_A_1-17']) #FEEDER EMERGENCY PRESSED
                                        dic['VulAlarm1_19'] = fixedInt(json_obj['M-V_A_1-18']) #RED TAPE SENSOR DETECTED
                                        dic['VulAlarm1_20'] = fixedInt(json_obj['M-V_A_1-19']) #EXTRUSION MATERIAL TEMPERATURE HIGH
                                        dic['VulAlarm1_21'] = fixedInt(json_obj['M-V_A_1-20']) #EXTRUSION MATERIAL TEMPERATURE LOW 
                                        dic['VulAlarm1_22'] = fixedInt(json_obj['M-V_A_1-21']) #SPARE-1
                                        dic['VulAlarm1_23'] = fixedInt(json_obj['M-V_A_1-22']) #SPARE-2
                                        dic['VulAlarm1_24'] = fixedInt(json_obj['M-V_A_1-23']) #SPARE-3
                                        dic['VulAlarm1_25'] = fixedInt(json_obj['M-V_A_1-24']) #SCREW TEMPERATURE HIGH
                                        dic['VulAlarm1_26'] = fixedInt(json_obj['M-V_A_1-25']) #SCREW TEMPERATURE LOW
                                        dic['VulAlarm1_27'] = fixedInt(json_obj['M-V_A_1-26']) #EXTRUDER EMERGENCY PRESSED
                                        dic['VulAlarm1_28'] = fixedInt(json_obj['M-V_A_1-27']) #INPUT CATTERPULLER EMERGENCY PRESSED
                                        dic['VulAlarm1_29'] = fixedInt(json_obj['M-V_A_1-28']) #OUTPUT CATTERPULLER EMERGENCY PRESSED
                                        dic['VulAlarm1_30'] = fixedInt(json_obj['M-V_A_1-29']) #TAKEUP1 EMERGENCY PRESSED
                                        dic['VulAlarm1_31'] = fixedInt(json_obj['M-V_A_1-30']) #TAKEUP2 EMERGENCY PRESSED
                                        dic['VulAlarm1_32'] = fixedInt(json_obj['M-V_A_1-31']) #TAKEUP1 END LIMIT ACTIVAT
                                        dic['TestAlarm1_1'] = fixedInt(json_obj['M-T_A_1-0']) #TCI-1 PUMP MPCB TRIPPED 
                                        dic['TestAlarm1_2'] = fixedInt(json_obj['M-T_A_1-1']) #TCI-1 AGITATOR MPCB TRIPPED
                                        dic['TestAlarm1_3'] = fixedInt(json_obj['M-T_A_1-2']) #TCI-2 PUMP MPCB TRIPPED
                                        dic['TestAlarm1_4'] = fixedInt(json_obj['M-T_A_1-3']) #TCI=2 AGITATOR MPCB TRIPPED
                                        dic['TestAlarm1_5'] = fixedInt(json_obj['M-T_A_1-4']) #TAKEUP DRIVE FAULT
                                        dic['TestAlarm1_6'] = fixedInt(json_obj['M-T_A_1-5']) #TAKEUP DRIVE ALARM
                                        dic['TestAlarm1_7'] = fixedInt(json_obj['M-T_A_1-6']) #MANDREL OD HIGH LINE STOPPED
                                        dic['TestAlarm1_8'] = fixedInt(json_obj['M-T_A_1-7']) #MANDREL OD LOW LINE STOPPED
                                        dic['TestAlarm1_9'] = fixedInt(json_obj['M-T_A_1-8']) #PANEL EMERGENCY PRESSED
                                        dic['TestAlarm1_10'] = fixedInt(json_obj['M-T_A_1-9'] )#TAKEUP EMERGENCY PRESSED
                                        dic['TestAlarm1_11'] = fixedInt(json_obj['M-T_A_1-10']) #SPARE 1
                                        dic['TestAlarm1_12'] = fixedInt(json_obj['M-T_A_1-11']) #SPARE 2
                                        dic['TestAlarm1_13'] = fixedInt(json_obj['M-T_A_1-12']) #SPARE 3
                                        dic['TestAlarm1_14'] = fixedInt(json_obj['M-T_A_1-13']) #SPARE 4
                                        dic['TestAlarm1_15'] = fixedInt(json_obj['M-T_A_1-14']) #SPARE 5
                                        dic['TestAlarm1_16'] = fixedInt(json_obj['M-T_A_1-15']) #SPARE
                                        dic['TestAlarm2_1'] = fixedInt(json_obj['M-T_A_2-0']) #TCI-1 PUMP MPCB TRIPPED 
                                        dic['TestAlarm2_2'] = fixedInt(json_obj['M-T_A_2-1']) #TCI-1 AGITATOR MPCB TRIPPED
                                        dic['TestAlarm2_3'] = fixedInt(json_obj['M-T_A_2-2']) #TCI-2 PUMP MPCB TRIPPED
                                        dic['TestAlarm2_4'] = fixedInt(json_obj['M-T_A_2-3']) #TCI=2 AGITATOR MPCB TRIPPED
                                        dic['TestAlarm2_5'] = fixedInt(json_obj['M-T_A_2-4']) #TAKEUP DRIVE FAULT
                                        dic['TestAlarm2_6'] = fixedInt(json_obj['M-T_A_2-5']) #TAKEUP DRIVE ALARM
                                        dic['TestAlarm2_7'] = fixedInt(json_obj['M-T_A_2-6']) #MANDREL OD HIGH LINE STOPPED
                                        dic['TestAlarm2_8'] = fixedInt(json_obj['M-T_A_2-7']) #MANDREL OD LOW LINE STOPPED
                                        dic['TestAlarm2_9'] = fixedInt(json_obj['M-T_A_2-8']) #PANEL EMERGENCY PRESSED
                                        dic['TestAlarm2_10'] = fixedInt(json_obj['M-T_A_2-9'] )#TAKEUP EMERGENCY PRESSED
                                        dic['TestAlarm2_11'] = fixedInt(json_obj['M-T_A_2-10']) #SPARE 1
                                        dic['TestAlarm2_12'] = fixedInt(json_obj['M-T_A_2-11']) #SPARE 2
                                        dic['TestAlarm2_13'] = fixedInt(json_obj['M-T_A_2-12']) #SPARE 3
                                        dic['TestAlarm2_14'] = fixedInt(json_obj['M-T_A_2-13']) #SPARE 4
                                        dic['TestAlarm2_15'] = fixedInt(json_obj['M-T_A_2-14']) #SPARE 5
                                        dic['TestAlarm2_16'] = fixedInt(json_obj['M-T_A_2-15']) #SPARE
                                        dic['TestAlarm3_1'] = fixedInt(json_obj['M-T_A_3-0']) #TCI-1 PUMP MPCB TRIPPED 
                                        dic['TestAlarm3_2'] = fixedInt(json_obj['M-T_A_3-1']) #TCI-1 AGITATOR MPCB TRIPPED
                                        dic['TestAlarm3_3'] = fixedInt(json_obj['M-T_A_3-2']) #TCI-2 PUMP MPCB TRIPPED
                                        dic['TestAlarm3_4'] = fixedInt(json_obj['M-T_A_3-3']) #TCI=2 AGITATOR MPCB TRIPPED
                                        dic['TestAlarm3_5'] = fixedInt(json_obj['M-T_A_3-4']) #TAKEUP DRIVE FAULT
                                        dic['TestAlarm3_6'] = fixedInt(json_obj['M-T_A_3-5']) #TAKEUP DRIVE ALARM
                                        dic['TestAlarm3_7'] = fixedInt(json_obj['M-T_A_3-6']) #MANDREL OD HIGH LINE STOPPED
                                        dic['TestAlarm3_8'] = fixedInt(json_obj['M-T_A_3-7']) #MANDREL OD LOW LINE STOPPED
                                        dic['TestAlarm3_9'] = fixedInt(json_obj['M-T_A_3-8']) #PANEL EMERGENCY PRESSED
                                        dic['TestAlarm3_10'] = fixedInt(json_obj['M-T_A_3-9'] )#TAKEUP EMERGENCY PRESSED
                                        dic['TestAlarm3_11'] = fixedInt(json_obj['M-T_A_3-10']) #SPARE 1
                                        dic['TestAlarm3_12'] = fixedInt(json_obj['M-T_A_3-11']) #SPARE 2
                                        dic['TestAlarm3_13'] = fixedInt(json_obj['M-T_A_3-12']) #SPARE 3
                                        dic['TestAlarm3_14'] = fixedInt(json_obj['M-T_A_3-13']) #SPARE 4
                                        dic['TestAlarm3_15'] = fixedInt(json_obj['M-T_A_3-14']) #SPARE 5
                                        dic['TestAlarm3_16'] = fixedInt(json_obj['M-T_A_3-15']) #SPARE 6


                                        dic['Mandrel1_1'] = fixedInt(json_obj['M-M_R_1-0']) #PIR
                                        dic['Mandrel1_2'] = fixedInt(json_obj['M-M_R_1-1']) #OPERATOR NAME
                                                                

                                        dic['Mandrel2_1'] = fixedInt(json_obj['M-M_R_2-0']) #PIR
                                        dic['Mandrel2_2'] = fixedInt(json_obj['M-M_R_2-1']) #OPERATOR NAME
                                                                
                                        dic['Extruder1_1'] = fixedInt(json_obj['M-E_R_1-0']) #PIR
                                        dic['Extruder1_2'] = fixedInt(json_obj['M-E_R_1-1']) #OPERATOR NAME
                                                                
                                        dic['Extruder3_1'] = fixedInt(json_obj['M-E_R_3-0']) #PIR
                                        dic['Extruder3_2'] = fixedInt(json_obj['M-E_R_3-1']) #OPERATOR NAME
                                                                

                                        dic['Vulcanizer1_1'] = fixedInt(json_obj['M-V_R_1-0']) #PIR
                                        dic['Vulcanizer1_2'] = fixedInt(json_obj['M-V_R_1-1']) #OPERATOR NAME
                                                                
                                        dic['Testing1_1'] = fixedInt(json_obj['M-T_R_1-0']) #PIR
                                        dic['Testing1_2'] = fixedInt(json_obj['M-T_R_1-1']) #OPERATOR NAME
                                                                
                                        dic['Testing2_1'] = fixedInt(json_obj['M-T_R_2-0']) #PIR
                                        dic['Testing2_2'] = fixedInt(json_obj['M-T_R_2-1']) #OPERATOR NAME
                                                                
                                        dic['Testing3_1'] = fixedInt(json_obj['M-T_R_3-0']) #PIR
                                        dic['Testing3_2'] = fixedInt(json_obj['M-T_R_3-1']) #OPERATOR NAME

                                        dic['ExtStop1_1'] = fixedInt(json_obj['M-E_S_1-0']) #Int value containing 1-20 value's
                                        dic['ExtStop1_2'] = json_obj['M-E_S_1-1'] #Boolean value containing on off status
                                        dic['ExtStopMessage1'] = ""
                                     
                                        dic['ExtStop3_1'] = fixedInt(json_obj['M-E_S_3-0']) #Int value containing 1-20 value's
                                        dic['ExtStop3_2'] = json_obj['M-E_S_3-1'] #Boolean value containing on off status
                                        dic['ExtStopMessage3'] = ""
                                     
                                        dic['ManStop1_1'] = fixedInt(json_obj['M-M_S_1-0']) #Int value containing 1-20 value's
                                        dic['ManStop1_2'] = json_obj['M-M_S_1-1'] #Boolean value containing on off status
                                        dic['ManStopMessage1'] = ""

                                        dic['ManStop2_1'] = fixedInt(json_obj['M-M_S_2-0']) #Int value containing 1-20 value's
                                        dic['ManStop2_2'] = json_obj['M-M_S_2-1'] #Boolean value containing on off status
                                        dic['ManStopMessage2'] = ""
                                     

                                        dic['VulStop1_1'] = fixedInt(json_obj['M-V_S_1-0']) #Int value containing 1-20 value's
                                        dic['VulStop1_2'] = json_obj['M-V_S_1-1'] #Boolean value containing on off status
                                        dic['VulStopMessage1'] = ""

                                        dic['TestStop1_1'] = fixedInt(json_obj['M-T_S_1-0']) #Int value containing 1-20 value's
                                        dic['TestStop1_2'] = json_obj['M-T_S_1-1'] #Boolean value containing on off status
                                        dic['TestStopMessage1'] = ""

                                        dic['TestStop2_1'] = fixedInt(json_obj['M-T_S_2-0']) #Int value containing 1-20 value's
                                        dic['TestStop2_2'] = json_obj['M-T_S_2-1'] #Boolean value containing on off status
                                        dic['TestStopMessage2'] = ""

                                        dic['TestStop3_1'] = fixedInt(json_obj['M-T_S_3-0']) #Int value containing 1-20 value's
                                        dic['TestStop3_2'] = json_obj['M-T_S_3-1'] #Boolean value containing on off status
                                        dic['TestStopMessage3'] = ""

                                        
                                                                
                                        if(globalBS.tempExtProd1 != findBool(dic['ExtProd1_8'])):
                                                #print("Before Ext1 value::", globalBS.tempExtProd1)
                                                globalBS.tempExtProd1 = findBool(dic['ExtProd1_8'])
                                                #print("After Ext1 value::", globalBS.tempExtProd1)
                                                if(findBool(dic['ExtProd1_8']) == True):
                                                        globalBS.tempExtStart1 = time.time()
                                                        globalBS.tempExtDT1 = datetime.datetime.now()
                                                if(findBool(dic['ExtProd1_8']) == False):
                                                        globalBS.tempExtEnd1 = time.time()
                                                        globalBS.tempExtElapsed1 = (globalBS.tempExtEnd1 - globalBS.tempExtStart1) / 60
                                                        sql = "INSERT INTO extproduction1 ( ontime, pir, operator_name, hose_type, hose_size, mpir, act_kg, actual_speed, prod_time, ex_hd_pr, start_temp, middle_temp, last_temp, drum_in, drum_out ) VALUES (%s, %s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                        val = (globalBS.tempExtDT1, str(dic['ExtProd1_1']), str(dic['ExtProd1_2']), str(dic['ExtProd1_14']), str(dic['ExtProd1_15']), str(dic['ExtProd1_3']), findFloat(float(dic['ExtProd1_4'])), findFloat(float(dic['ExtProd1_5'])), int(globalBS.tempExtElapsed1) , findFloat(float(dic['ExtProd1_6'])), findFloat(float(dic['ExtProd1_7'])), findFloat(float(dic['ExtProd1_12'])), findFloat(float(dic['ExtProd1_9'])), str(dic['ExtProd1_10']), str(dic['ExtProd1_11']))
                                                        mycursor.execute(sql, val)
                                                        #mycursor.execute(sql, val)
                                                        

                                        if(globalBS.tempExtProd3 != findBool(dic['ExtProd3_8'])):
                                                #print("Before Ext3 value::", globalBS.tempExtProd3)
                                                globalBS.tempExtProd3 = findBool(dic['ExtProd3_8'])
                                                #print("After Ext3 value::", globalBS.tempExtProd3)
                                                if(findBool(dic['ExtProd3_8']) == True):
                                                        globalBS.tempExtStart3 = time.time()
                                                        globalBS.tempExtDT3 = datetime.datetime.now()
                                                if(findBool(dic['ExtProd3_8']) == False):
                                                        globalBS.tempExtEnd3 = time.time()
                                                        globalBS.tempExtElapsed3 = (globalBS.tempExtEnd3 - globalBS.tempExtStart3) / 60
                                                        sql = "INSERT INTO extproduction3 ( ontime, pir, operator_name, hose_type, hose_size, mpir, act_kg, actual_speed, prod_time, ex_hd_pr, start_temp, middle_temp, last_temp, drum_in, drum_out ) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                        val = (globalBS.tempExtDT3, str(dic['ExtProd3_1']), str(dic['ExtProd3_2']), str(dic['ExtProd3_14']), str(dic['ExtProd3_15']), str(dic['ExtProd3_3']), findFloat(float(dic['ExtProd3_4'])), findFloat(float(dic['ExtProd3_5'])), int(globalBS.tempExtElapsed3) , findFloat(float(dic['ExtProd3_6'])), findFloat(float(dic['ExtProd3_7'])), findFloat(float(dic['ExtProd3_12'])), findFloat(float(dic['ExtProd3_9'])), str(dic['ExtProd3_10']), str(dic['ExtProd3_11']))
                                                        mycursor.execute(sql, val)
                                                        #mycursor.execute(sql, val)
                                                        


                                        if(globalBS.tempVulProd1 != findBool(dic['VulProd1_8'])):
                                                #print("Before Vul1 value::", globalBS.tempVulProd1)
                                                globalBS.tempVulProd1 = findBool(dic['VulProd1_8'])
                                                #print("After Vul1 value::", globalBS.tempVulProd1)
                                                if(findBool(dic['VulProd1_8']) == True):
                                                        globalBS.tempVulStart1 = time.time()
                                                        globalBS.tempVulDT1 = datetime.datetime.now()
                                                if(findBool(dic['VulProd1_8']) == False):
                                                        globalBS.tempVulEnd1 = time.time()
                                                        globalBS.tempVulElapsed1 = (globalBS.tempVulEnd1 - globalBS.tempVulStart1) / 60
                                                        sql = "INSERT INTO vulproduction1 ( ontime, pir_1, pir_2, pir_3, pir_4, pir_5, pir_6, operator_name, hose_type_1, hose_type_2, hose_type_3, hose_type_4, hose_type_5, hose_type_6, hose_size_1, hose_size_2, hose_size_3, hose_size_4, hose_size_5, hose_size_6, drum_no, total_vul_time ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                        val = (globalBS.tempVulDT1, str(dic['VulProd1_1']), str(dic['VulProd1_3']), str(dic['VulProd1_4']), str(dic['VulProd1_5']), str(dic['VulProd1_6']), str(dic['VulProd1_7']), str(dic['VulProd1_2']), str(dic['VulProd1_11']), str(dic['VulProd1_12']), str(dic['VulProd1_13']), str(dic['VulProd1_14']), str(dic['VulProd1_15']), str(dic['VulProd1_16']), str(dic['VulProd1_17']), str(dic['VulProd1_18']), str(dic['VulProd1_19']), str(dic['VulProd1_20']), str(dic['VulProd1_21']), str(dic['VulProd1_22']), str(dic['VulProd1_9']), int(globalBS.tempVulElapsed1))
                                                        mycursor.execute(sql, val)
                                                        #mycursor.execute(sql, val)
                                                        


                                        if(globalBS.tempManProd1 != findBool(dic['ManProd1_8'])):
                                                globalBS.tempManProd1 = findBool(dic['ManProd1_8'])
                                                if(findBool(dic['ManProd1_8']) == True):
                                                        #globalBS.tempManStart1 = time.time()
                                                        globalBS.tempManDT1 = datetime.datetime.now()
                                                if(findBool(dic['ManProd1_8']) == False):
                                                        #globalBS.tempManEnd1 = time.time()
                                                        #globalBS.tempManElapsed1 = (globalBS.tempManEnd1 - globalBS.tempManStart1) / 60
                                                        sql = "INSERT INTO manproduction1 ( ontime, pir, operator_name, new_pir_1, old_pir_1, old_pir_2, old_pir_3, qty_in_mtrs, drum_no) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                        val = (globalBS.tempManDT1, str(dic['ManProd1_1']), str(dic['ManProd1_2']), str(dic['ManProd1_3']), str(dic['ManProd1_4']), str(dic['ManProd1_5']), str(dic['ManProd1_6']), int(dic['ManProd1_9']), str(dic['ManProd1_7']))
                                                        mycursor.execute(sql, val)
                                                        #mycursor.execute(sql, val)
                                                        

                                        if(globalBS.tempManProd2 != findBool(dic['ManProd2_8'])):
                                                globalBS.tempManProd2 = findBool(dic['ManProd2_8'])
                                                if(findBool(dic['ManProd2_8']) == True):
                                                        #globalBS.tempManStart2 = time.time()
                                                        globalBS.tempManDT2 = datetime.datetime.now()
                                                if(findBool(dic['ManProd2_8']) == False):
                                                        #globalBS.tempManEnd2 = time.time()
                                                        #globalBS.tempManElapsed2 = (globalBS.tempManEnd2 - globalBS.tempManStart2) / 60
                                                        sql = "INSERT INTO manproduction2 ( ontime, pir, operator_name, new_pir_1, old_pir_1, old_pir_2, old_pir_3, qty_in_mtrs, drum_no) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                        val = (globalBS.tempManDT2, str(dic['ManProd2_1']), str(dic['ManProd2_2']), str(dic['ManProd2_3']), str(dic['ManProd2_4']), str(dic['ManProd2_5']), str(dic['ManProd2_6']), int(dic['ManProd2_9']), str(dic['ManProd2_7']))
                                                        mycursor.execute(sql, val)
                                                        #mycursor.execute(sql, val)
                                                        



                                        if(globalBS.tempTestProd1 != findBool(dic['TestProd1_8'])):
                                                globalBS.tempTestProd1 = findBool(dic['TestProd1_8'])
                                                if(findBool(dic['TestProd1_8']) == True):
                                                        globalBS.tempTestStart1 = time.time()
                                                        globalBS.tempTestDT1 = datetime.datetime.now()
                                                if(findBool(dic['TestProd1_8']) == False):
                                                        globalBS.tempTestEnd1 = time.time()
                                                        globalBS.tempTestElapsed1 = (globalBS.tempTestEnd1 - globalBS.tempTestStart1) / 60
                                                        sql = "INSERT INTO testproduction1 ( ontime, pir, hose_size, hose_type, operator_name, proof_pres, scrap_len, total_time, drum_in, drum_out) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                        val = (globalBS.tempTestDT1, str(dic['TestProd1_1']), str(dic['TestProd1_10']), str(dic['TestProd1_11']), str(dic['TestProd1_2']), str(dic['TestProd1_3']), str(dic['TestProd1_4']), int(globalBS.tempTestElapsed1), str(dic['TestProd1_5']), str(dic['TestProd1_6']))
                                                        mycursor.execute(sql, val)
                                                        #mycursor.execute(sql, val)
                                                        

                                        if(globalBS.tempTestProd2 != findBool(dic['TestProd2_8'])):
                                                globalBS.tempTestProd2 = findBool(dic['TestProd2_8'])
                                                if(findBool(dic['TestProd2_8']) == True):
                                                        globalBS.tempTestStart2 = time.time()
                                                        globalBS.tempTestDT2 = datetime.datetime.now()
                                                if(findBool(dic['TestProd2_8']) == False):
                                                        globalBS.tempTestEnd2 = time.time()
                                                        globalBS.tempTestElapsed2 = (globalBS.tempTestEnd2 - globalBS.tempTestStart2) / 60
                                                        sql = "INSERT INTO testproduction2 ( ontime, pir, hose_size, hose_type, operator_name, proof_pres, scrap_len, total_time, drum_in, drum_out) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                        val = (globalBS.tempTestDT2, str(dic['TestProd2_1']), str(dic['TestProd2_10']), str(dic['TestProd2_11']), str(dic['TestProd2_2']), str(dic['TestProd2_3']), str(dic['TestProd2_4']), int(globalBS.tempTestElapsed2), str(dic['TestProd2_5']), str(dic['TestProd2_6']))
                                                        mycursor.execute(sql, val)
                                                        #mycursor.execute(sql, val)
                                                        

                                        if(globalBS.tempTestProd3 != findBool(dic['TestProd3_8'])):
                                                globalBS.tempTestProd3 = findBool(dic['TestProd3_8'])
                                                if(findBool(dic['TestProd3_8']) == True):
                                                        globalBS.tempTestStart3 = time.time()
                                                        globalBS.tempTestDT3 = datetime.datetime.now()
                                                if(findBool(dic['TestProd3_8']) == False):
                                                        globalBS.tempTestEnd3 = time.time()
                                                        globalBS.tempTestElapsed3 = (globalBS.tempTestEnd3 - globalBS.tempTestStart3) / 60
                                                        sql = "INSERT INTO testproduction3 ( ontime, pir, hose_size, hose_type, operator_name, proof_pres, scrap_len, total_time, drum_in, drum_out) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                        val = (globalBS.tempTestDT3, str(dic['TestProd3_1']), str(dic['TestProd3_10']), str(dic['TestProd3_11']), str(dic['TestProd3_2']), str(dic['TestProd3_3']), str(dic['TestProd3_4']), int(globalBS.tempTestElapsed3), str(dic['TestProd3_5']), str(dic['TestProd3_6']))
                                                        mycursor.execute(sql, val)


                                        if(globalBS.tempMan1_1 != findBool(dic['ManAlarm1_1'])):
                                                globalBS.tempMan1_1 = findBool(dic['ManAlarm1_1'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 1, 'TCI-1 PUMP MPCB TRIPPED', findBool(dic['ManAlarm1_1']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_2 != findBool(dic['ManAlarm1_2'])):
                                                globalBS.tempMan1_2 = findBool(dic['ManAlarm1_2'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 2, 'TCI-1 AGITATOR MPCB TRIPPED', findBool(dic['ManAlarm1_2']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_3 != findBool(dic['ManAlarm1_3'])):
                                                globalBS.tempMan1_3 = findBool(dic['ManAlarm1_3'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 3, 'TCI-2 PUMP MPCB TRIPPED', findBool(dic['ManAlarm1_3']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_4 != findBool(dic['ManAlarm1_4'])):
                                                globalBS.tempMan1_4 = findBool(dic['ManAlarm1_4'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 4, 'TCI=2 AGITATOR MPCB TRIPPED', findBool(dic['ManAlarm1_4']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_5 != findBool(dic['ManAlarm1_5'])):
                                                globalBS.tempMan1_5 = findBool(dic['ManAlarm1_5'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 5, 'TAKEUP DRIVE FAULT', findBool(dic['ManAlarm1_5']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_6 != findBool(dic['ManAlarm1_6'])):
                                                globalBS.tempMan1_6 = findBool(dic['ManAlarm1_6'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 6, 'TAKEUP DRIVE ALARM', findBool(dic['ManAlarm1_6']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_7 != findBool(dic['ManAlarm1_7'])):
                                                globalBS.tempMan1_7 = findBool(dic['ManAlarm1_7'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 7, 'MANDREL OD HIGH LINE STOPPED', findBool(dic['ManAlarm1_7']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_8 != findBool(dic['ManAlarm1_8'])):
                                                globalBS.tempMan1_8 = findBool(dic['ManAlarm1_8'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 8, 'MANDREL OD LOW LINE STOPPED', findBool(dic['ManAlarm1_8']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_9 != findBool(dic['ManAlarm1_9'])):
                                                globalBS.tempMan1_9 = findBool(dic['ManAlarm1_9'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 9, 'PANEL EMERGENCY PRESSED', findBool(dic['ManAlarm1_9']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_10 != findBool(dic['ManAlarm1_10'])):
                                                globalBS.tempMan1_10 = findBool(dic['ManAlarm1_10'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 10, 'TAKEUP EMERGENCY PRESSED', findBool(dic['ManAlarm1_10']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_11 != findBool(dic['ManAlarm1_11'])):
                                                globalBS.tempMan1_11 = findBool(dic['ManAlarm1_11'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 11, 'SPARE 1', findBool(dic['ManAlarm1_11']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_12 != findBool(dic['ManAlarm1_12'])):
                                                globalBS.tempMan1_12 = findBool(dic['ManAlarm1_12'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 12, 'SPARE 2', findBool(dic['ManAlarm1_12']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_13 != findBool(dic['ManAlarm1_13'])):
                                                globalBS.tempMan1_13 = findBool(dic['ManAlarm1_13'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 13, 'SPARE 3', findBool(dic['ManAlarm1_13']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_14 != findBool(dic['ManAlarm1_14'])):
                                                globalBS.tempMan1_14 = findBool(dic['ManAlarm1_14'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 14, 'SPARE 4', findBool(dic['ManAlarm1_14']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_15 != findBool(dic['ManAlarm1_15'])):
                                                globalBS.tempMan1_15 = findBool(dic['ManAlarm1_15'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 15, 'SPARE 5', findBool(dic['ManAlarm1_15']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_16 != findBool(dic['ManAlarm1_16'])):
                                                globalBS.tempMan1_16 = findBool(dic['ManAlarm1_16'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 16, 'SPARE 6', findBool(dic['ManAlarm1_16']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_17 != findBool(dic['ManAlarm1_17'])):
                                                globalBS.tempMan1_17 = findBool(dic['ManAlarm1_17'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 17, 'MANDREL OD HIGH', findBool(dic['ManAlarm1_17']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan1_18 != findBool(dic['ManAlarm1_18'])):
                                                globalBS.tempMan1_18 = findBool(dic['ManAlarm1_18'])
                                                sql = "INSERT INTO manalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], 18, 'MANDREL OD LOW', findBool(dic['ManAlarm1_18']))
                                                mycursor.execute(sql, val)




                                        if(globalBS.tempMan2_1 != findBool(dic['ManAlarm2_1'])):
                                                globalBS.tempMan2_1 = findBool(dic['ManAlarm2_1'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 1, 'TCI-1 PUMP MPCB TRIPPED', findBool(dic['ManAlarm2_1']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_2 != findBool(dic['ManAlarm2_2'])):
                                                globalBS.tempMan2_2 = findBool(dic['ManAlarm2_2'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 2, 'TCI-1 AGITATOR MPCB TRIPPED', findBool(dic['ManAlarm2_2']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_3 != findBool(dic['ManAlarm2_3'])):
                                                globalBS.tempMan2_3 = findBool(dic['ManAlarm2_3'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 3, 'TCI-2 PUMP MPCB TRIPPED', findBool(dic['ManAlarm2_3']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_4 != findBool(dic['ManAlarm2_4'])):
                                                globalBS.tempMan2_4 = findBool(dic['ManAlarm2_4'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 4, 'TCI=2 AGITATOR MPCB TRIPPED', findBool(dic['ManAlarm2_4']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_5 != findBool(dic['ManAlarm2_5'])):
                                                globalBS.tempMan2_5 = findBool(dic['ManAlarm2_5'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 5, 'TAKEUP DRIVE FAULT', findBool(dic['ManAlarm2_5']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_6 != findBool(dic['ManAlarm2_6'])):
                                                globalBS.tempMan2_6 = findBool(dic['ManAlarm2_6'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 6, 'TAKEUP DRIVE ALARM', findBool(dic['ManAlarm2_6']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_7 != findBool(dic['ManAlarm2_7'])):
                                                globalBS.tempMan2_7 = findBool(dic['ManAlarm2_7'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 7, 'MANDREL OD HIGH LINE STOPPED', findBool(dic['ManAlarm2_7']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_8 != findBool(dic['ManAlarm2_8'])):
                                                globalBS.tempMan2_8 = findBool(dic['ManAlarm2_8'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 8, 'MANDREL OD LOW LINE STOPPED', findBool(dic['ManAlarm2_8']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_9 != findBool(dic['ManAlarm2_9'])):
                                                globalBS.tempMan2_9 = findBool(dic['ManAlarm2_9'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 9, 'PANEL EMERGENCY PRESSED', findBool(dic['ManAlarm2_9']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_10 != findBool(dic['ManAlarm2_10'])):
                                                globalBS.tempMan2_10 = findBool(dic['ManAlarm2_10'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 10, 'TAKEUP EMERGENCY PRESSED', findBool(dic['ManAlarm2_10']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_11 != findBool(dic['ManAlarm2_11'])):
                                                globalBS.tempMan2_11 = findBool(dic['ManAlarm2_11'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 11, 'SPARE 1', findBool(dic['ManAlarm2_11']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_12 != findBool(dic['ManAlarm2_12'])):
                                                globalBS.tempMan2_12 = findBool(dic['ManAlarm2_12'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 12, 'SPARE 2', findBool(dic['ManAlarm2_12']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_13 != findBool(dic['ManAlarm2_13'])):
                                                globalBS.tempMan2_13 = findBool(dic['ManAlarm2_13'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 13, 'SPARE 3', findBool(dic['ManAlarm2_13']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_14 != findBool(dic['ManAlarm2_14'])):
                                                globalBS.tempMan2_14 = findBool(dic['ManAlarm2_14'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 14, 'SPARE 4', findBool(dic['ManAlarm2_14']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_15 != findBool(dic['ManAlarm2_15'])):
                                                globalBS.tempMan2_15 = findBool(dic['ManAlarm2_15'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 15, 'SPARE 5', findBool(dic['ManAlarm2_15']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_16 != findBool(dic['ManAlarm2_16'])):
                                                globalBS.tempMan2_16 = findBool(dic['ManAlarm2_16'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 16, 'SPARE 6', findBool(dic['ManAlarm2_16']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_17 != findBool(dic['ManAlarm2_17'])):
                                                globalBS.tempMan2_17 = findBool(dic['ManAlarm2_17'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 17, 'MANDREL OD HIGH', findBool(dic['ManAlarm2_17']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempMan2_18 != findBool(dic['ManAlarm2_18'])):
                                                globalBS.tempMan2_18 = findBool(dic['ManAlarm2_18'])
                                                sql = "INSERT INTO manalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], 18, 'MANDREL OD LOW', findBool(dic['ManAlarm2_18']))
                                                mycursor.execute(sql, val)




                                        if(globalBS.tempExt1_1 != findBool(dic['ExtAlarm1_1'])):
                                                globalBS.tempExt1_1 = findBool(dic['ExtAlarm1_1'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 1, 'THICKNESS  HIGH', findBool(dic['ExtAlarm1_1']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_2 != findBool(dic['ExtAlarm1_2'])):
                                                globalBS.tempExt1_2 = findBool(dic['ExtAlarm1_2'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 2, 'THICKNESS LOW', findBool(dic['ExtAlarm1_2']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_3 != findBool(dic['ExtAlarm1_3'])):
                                                globalBS.tempExt1_3 = findBool(dic['ExtAlarm1_3'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 3, 'HEAD TEMPERATURE HIGH', findBool(dic['ExtAlarm1_3']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_4 != findBool(dic['ExtAlarm1_4'])):
                                                globalBS.tempExt1_4 = findBool(dic['ExtAlarm1_4'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 4, 'HEAD TEMPERATURE LOW', findBool(dic['ExtAlarm1_4']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_5 != findBool(dic['ExtAlarm1_5'])):
                                                globalBS.tempExt1_5 = findBool(dic['ExtAlarm1_5'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 5, 'ZONE 2 TEMPERATURE HIGH', findBool(dic['ExtAlarm1_5']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_6 != findBool(dic['ExtAlarm1_6'])):
                                                globalBS.tempExt1_6 = findBool(dic['ExtAlarm1_6'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 6, 'ZONE 2 TEMPERATURE LOW', findBool(dic['ExtAlarm1_6']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_7 != findBool(dic['ExtAlarm1_7'])):
                                                globalBS.tempExt1_7 = findBool(dic['ExtAlarm1_7'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 7, 'ZONE 3 TEMPERATURE HIGH', findBool(dic['ExtAlarm1_7']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_8 != findBool(dic['ExtAlarm1_8'])):
                                                globalBS.tempExt1_8 = findBool(dic['ExtAlarm1_8'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 8, 'ZONE 3 TEMPERATURE LOW', findBool(dic['ExtAlarm1_8']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_9 != findBool(dic['ExtAlarm1_9'])):
                                                globalBS.tempExt1_9 = findBool(dic['ExtAlarm1_9'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 9, 'EXTRUDER CURRENT WARNING HIGH', findBool(dic['ExtAlarm1_9']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_10 != findBool(dic['ExtAlarm1_10'])):
                                                globalBS.tempExt1_10 = findBool(dic['ExtAlarm1_10'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 10, 'EXTRUDER CURRENT ALARM HIGH', findBool(dic['ExtAlarm1_10']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_11 != findBool(dic['ExtAlarm1_11'])):
                                                globalBS.tempExt1_11 = findBool(dic['ExtAlarm1_11'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 11, 'EXTRUDER PRESSURE WANING HIGH', findBool(dic['ExtAlarm1_11']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_12 != findBool(dic['ExtAlarm1_12'])):
                                                globalBS.tempExt1_12 = findBool(dic['ExtAlarm1_12'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 12, 'EXTRUDER PRESSURE ALARM HIGH', findBool(dic['ExtAlarm1_12']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_13 != findBool(dic['ExtAlarm1_13'])):
                                                globalBS.tempExt1_13 = findBool(dic['ExtAlarm1_13'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 13, 'OUTER DIAMETER HIGH', findBool(dic['ExtAlarm1_13']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_14 != findBool(dic['ExtAlarm1_14'])):
                                                globalBS.tempExt1_14 = findBool(dic['ExtAlarm1_14'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 14, 'OUTER DIAMETER LOW', findBool(dic['ExtAlarm1_14']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_15 != findBool(dic['ExtAlarm1_15'])):
                                                globalBS.tempExt1_15 = findBool(dic['ExtAlarm1_15'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 15, 'INNER DIAMETER HIGH', findBool(dic['ExtAlarm1_15']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_16 != findBool(dic['ExtAlarm1_16'])):
                                                globalBS.tempExt1_16 = findBool(dic['ExtAlarm1_16'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 16, 'INNER DIAMETER LOW', findBool(dic['ExtAlarm1_16']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_17 != findBool(dic['ExtAlarm1_17'])):
                                                globalBS.tempExt1_17 = findBool(dic['ExtAlarm1_17'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 17, 'TAKEUP2 END LIMIT ACTIVATED', findBool(dic['ExtAlarm1_17']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_18 != findBool(dic['ExtAlarm1_18'])):
                                                globalBS.tempExt1_18 = findBool(dic['ExtAlarm1_18'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 18, 'FEEDER EMERGENCY PRESSED', findBool(dic['ExtAlarm1_18']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_19 != findBool(dic['ExtAlarm1_19'])):
                                                globalBS.tempExt1_19 = findBool(dic['ExtAlarm1_19'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 19, 'RED TAPE SENSOR DETECTED', findBool(dic['ExtAlarm1_19']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_20 != findBool(dic['ExtAlarm1_20'])):
                                                globalBS.tempExt1_20 = findBool(dic['ExtAlarm1_20'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 20, 'EXTRUSION MATERIAL TEMPERATURE HIGH', findBool(dic['ExtAlarm1_20']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_21 != findBool(dic['ExtAlarm1_21'])):
                                                globalBS.tempExt1_21 = findBool(dic['ExtAlarm1_21'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 21, 'EXTRUSION MATERIAL TEMPERATURE LOW', findBool(dic['ExtAlarm1_21']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_22 != findBool(dic['ExtAlarm1_22'])):
                                                globalBS.tempExt1_22 = findBool(dic['ExtAlarm1_22'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 22, 'SPARE-1', findBool(dic['ExtAlarm1_22']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_23 != findBool(dic['ExtAlarm1_23'])):
                                                globalBS.tempExt1_23 = findBool(dic['ExtAlarm1_23'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 23, 'SPARE-2', findBool(dic['ExtAlarm1_23']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_24 != findBool(dic['ExtAlarm1_24'])):
                                                globalBS.tempExt1_24 = findBool(dic['ExtAlarm1_24'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 24, 'SPARE-3', findBool(dic['ExtAlarm1_24']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_25 != findBool(dic['ExtAlarm1_25'])):
                                                globalBS.tempExt1_25 = findBool(dic['ExtAlarm1_25'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 25, 'SCREW TEMPERATURE HIGH', findBool(dic['ExtAlarm1_25']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_26 != findBool(dic['ExtAlarm1_26'])):
                                                globalBS.tempExt1_26 = findBool(dic['ExtAlarm1_26'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 26, 'SCREW TEMPERATURE LOW', findBool(dic['ExtAlarm1_26']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_27 != findBool(dic['ExtAlarm1_27'])):
                                                globalBS.tempExt1_27 = findBool(dic['ExtAlarm1_27'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 27, 'EXTRUDER EMERGENCY PRESSED', findBool(dic['ExtAlarm1_27']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_28 != findBool(dic['ExtAlarm1_28'])):
                                                globalBS.tempExt1_28 = findBool(dic['ExtAlarm1_28'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 28, 'INPUT CATTERPULLER EMERGENCY PRESSED', findBool(dic['ExtAlarm1_28']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_29 != findBool(dic['ExtAlarm1_29'])):
                                                globalBS.tempExt1_29 = findBool(dic['ExtAlarm1_29'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 29, 'OUTPUT CATTERPULLER EMERGENCY PRESSED', findBool(dic['ExtAlarm1_29']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_30 != findBool(dic['ExtAlarm1_30'])):
                                                globalBS.tempExt1_30 = findBool(dic['ExtAlarm1_30'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 30, 'TAKEUP1 EMERGENCY PRESSED', findBool(dic['ExtAlarm1_30']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_31 != findBool(dic['ExtAlarm1_31'])):
                                                globalBS.tempExt1_31 = findBool(dic['ExtAlarm1_31'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 31, 'TAKEUP2 EMERGENCY PRESSED', findBool(dic['ExtAlarm1_31']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt1_32 != findBool(dic['ExtAlarm1_32'])):
                                                globalBS.tempExt1_32 = findBool(dic['ExtAlarm1_32'])
                                                sql = "INSERT INTO extalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], 32, 'TAKEUP1 END LIMIT ACTIVATED', findBool(dic['ExtAlarm1_32']))
                                                mycursor.execute(sql, val)




                                        



                                        if(globalBS.tempExt3_1 != findBool(dic['ExtAlarm3_1'])):
                                                globalBS.tempExt3_1 = findBool(dic['ExtAlarm3_1'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 1, 'THICKNESS  HIGH', findBool(dic['ExtAlarm3_1']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_2 != findBool(dic['ExtAlarm3_2'])):
                                                globalBS.tempExt3_2 = findBool(dic['ExtAlarm3_2'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 2, 'THICKNESS LOW', findBool(dic['ExtAlarm3_2']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_3 != findBool(dic['ExtAlarm3_3'])):
                                                globalBS.tempExt3_3 = findBool(dic['ExtAlarm3_3'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 3, 'HEAD TEMPERATURE HIGH', findBool(dic['ExtAlarm3_3']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_4 != findBool(dic['ExtAlarm3_4'])):
                                                globalBS.tempExt3_4 = findBool(dic['ExtAlarm3_4'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 4, 'HEAD TEMPERATURE LOW', findBool(dic['ExtAlarm3_4']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_5 != findBool(dic['ExtAlarm3_5'])):
                                                globalBS.tempExt3_5 = findBool(dic['ExtAlarm3_5'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 5, 'ZONE 2 TEMPERATURE HIGH', findBool(dic['ExtAlarm3_5']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_6 != findBool(dic['ExtAlarm3_6'])):
                                                globalBS.tempExt3_6 = findBool(dic['ExtAlarm3_6'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 6, 'ZONE 2 TEMPERATURE LOW', findBool(dic['ExtAlarm3_6']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_7 != findBool(dic['ExtAlarm3_7'])):
                                                globalBS.tempExt3_7 = findBool(dic['ExtAlarm3_7'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 7, 'ZONE 3 TEMPERATURE HIGH', findBool(dic['ExtAlarm3_7']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_8 != findBool(dic['ExtAlarm3_8'])):
                                                globalBS.tempExt3_8 = findBool(dic['ExtAlarm3_8'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 8, 'ZONE 3 TEMPERATURE LOW', findBool(dic['ExtAlarm3_8']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_9 != findBool(dic['ExtAlarm3_9'])):
                                                globalBS.tempExt3_9 = findBool(dic['ExtAlarm3_9'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 9, 'EXTRUDER CURRENT WARNING HIGH', findBool(dic['ExtAlarm3_9']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_10 != findBool(dic['ExtAlarm3_10'])):
                                                globalBS.tempExt3_10 = findBool(dic['ExtAlarm3_10'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 10, 'EXTRUDER CURRENT ALARM HIGH', findBool(dic['ExtAlarm3_10']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_11 != findBool(dic['ExtAlarm3_11'])):
                                                globalBS.tempExt3_11 = findBool(dic['ExtAlarm3_11'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 11, 'EXTRUDER PRESSURE WANING HIGH', findBool(dic['ExtAlarm3_11']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_12 != findBool(dic['ExtAlarm3_12'])):
                                                globalBS.tempExt3_12 = findBool(dic['ExtAlarm3_12'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 12, 'EXTRUDER PRESSURE ALARM HIGH', findBool(dic['ExtAlarm3_12']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_13 != findBool(dic['ExtAlarm3_13'])):
                                                globalBS.tempExt3_13 = findBool(dic['ExtAlarm3_13'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 13, 'OUTER DIAMETER HIGH', findBool(dic['ExtAlarm3_13']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_14 != findBool(dic['ExtAlarm3_14'])):
                                                globalBS.tempExt3_14 = findBool(dic['ExtAlarm3_14'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 14, 'OUTER DIAMETER LOW', findBool(dic['ExtAlarm3_14']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_15 != findBool(dic['ExtAlarm3_15'])):
                                                globalBS.tempExt3_15 = findBool(dic['ExtAlarm3_15'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 15, 'INNER DIAMETER HIGH', findBool(dic['ExtAlarm3_15']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_16 != findBool(dic['ExtAlarm3_16'])):
                                                globalBS.tempExt3_16 = findBool(dic['ExtAlarm3_16'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 16, 'INNER DIAMETER LOW', findBool(dic['ExtAlarm3_16']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_17 != findBool(dic['ExtAlarm3_17'])):
                                                globalBS.tempExt3_17 = findBool(dic['ExtAlarm3_17'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 17, 'TAKEUP2 END LIMIT ACTIVATED', findBool(dic['ExtAlarm3_17']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_18 != findBool(dic['ExtAlarm3_18'])):
                                                globalBS.tempExt3_18 = findBool(dic['ExtAlarm3_18'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 18, 'FEEDER EMERGENCY PRESSED', findBool(dic['ExtAlarm3_18']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_19 != findBool(dic['ExtAlarm3_19'])):
                                                globalBS.tempExt3_19 = findBool(dic['ExtAlarm3_19'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 19, 'RED TAPE SENSOR DETECTED', findBool(dic['ExtAlarm3_19']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_20 != findBool(dic['ExtAlarm3_20'])):
                                                globalBS.tempExt3_20 = findBool(dic['ExtAlarm3_20'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 20, 'EXTRUSION MATERIAL TEMPERATURE HIGH', findBool(dic['ExtAlarm3_20']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_21 != findBool(dic['ExtAlarm3_21'])):
                                                globalBS.tempExt3_21 = findBool(dic['ExtAlarm3_21'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 21, 'EXTRUSION MATERIAL TEMPERATURE LOW', findBool(dic['ExtAlarm3_21']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_22 != findBool(dic['ExtAlarm3_22'])):
                                                globalBS.tempExt3_22 = findBool(dic['ExtAlarm3_22'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 22, 'SPARE-1', findBool(dic['ExtAlarm3_22']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_23 != findBool(dic['ExtAlarm3_23'])):
                                                globalBS.tempExt3_23 = findBool(dic['ExtAlarm3_23'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 23, 'SPARE-2', findBool(dic['ExtAlarm3_23']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_24 != findBool(dic['ExtAlarm3_24'])):
                                                globalBS.tempExt3_24 = findBool(dic['ExtAlarm3_24'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 24, 'SPARE-3', findBool(dic['ExtAlarm3_24']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_25 != findBool(dic['ExtAlarm3_25'])):
                                                globalBS.tempExt3_25 = findBool(dic['ExtAlarm3_25'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 25, 'SCREW TEMPERATURE HIGH', findBool(dic['ExtAlarm3_25']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_26 != findBool(dic['ExtAlarm3_26'])):
                                                globalBS.tempExt3_26 = findBool(dic['ExtAlarm3_26'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 26, 'SCREW TEMPERATURE LOW', findBool(dic['ExtAlarm3_26']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_27 != findBool(dic['ExtAlarm3_27'])):
                                                globalBS.tempExt3_27 = findBool(dic['ExtAlarm3_27'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 27, 'EXTRUDER EMERGENCY PRESSED', findBool(dic['ExtAlarm3_27']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_28 != findBool(dic['ExtAlarm3_28'])):
                                                globalBS.tempExt3_28 = findBool(dic['ExtAlarm3_28'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 28, 'INPUT CATTERPULLER EMERGENCY PRESSED', findBool(dic['ExtAlarm3_28']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_29 != findBool(dic['ExtAlarm3_29'])):
                                                globalBS.tempExt3_29 = findBool(dic['ExtAlarm3_29'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 29, 'OUTPUT CATTERPULLER EMERGENCY PRESSED', findBool(dic['ExtAlarm3_29']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_30 != findBool(dic['ExtAlarm3_30'])):
                                                globalBS.tempExt3_30 = findBool(dic['ExtAlarm3_30'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 30, 'TAKEUP1 EMERGENCY PRESSED', findBool(dic['ExtAlarm3_30']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_31 != findBool(dic['ExtAlarm3_31'])):
                                                globalBS.tempExt3_31 = findBool(dic['ExtAlarm3_31'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 31, 'TAKEUP2 EMERGENCY PRESSED', findBool(dic['ExtAlarm3_31']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExt3_32 != findBool(dic['ExtAlarm3_32'])):
                                                globalBS.tempExt3_32 = findBool(dic['ExtAlarm3_32'])
                                                sql = "INSERT INTO extalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], 32, 'TAKEUP1 END LIMIT ACTIVATED', findBool(dic['ExtAlarm3_32']))
                                                mycursor.execute(sql, val)


                                       
                                        #need to change for Testing Machine
                                        if(globalBS.tempTest1_1 != findBool(dic['TestAlarm1_1'])):
                                                globalBS.tempTest1_1 = findBool(dic['TestAlarm1_1']) 
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 1, 'HYDRAULIC MOTOR TRIPPED', findBool(dic['TestAlarm1_1']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_2 != findBool(dic['TestAlarm1_2'])):
                                                globalBS.tempTest1_2 = findBool(dic['TestAlarm1_2'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 2, 'WATER PUMP TRIPPED', findBool(dic['TestAlarm1_2']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_3 != findBool(dic['TestAlarm1_3'])):
                                                globalBS.tempTest1_3 = findBool(dic['TestAlarm1_3'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 3, 'HMI PANEL EMERGENCY PRESSED', findBool(dic['TestAlarm1_3']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_4 != findBool(dic['TestAlarm1_4'])):
                                                globalBS.tempTest1_4 = findBool(dic['TestAlarm1_4'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 4, 'MAIN DRIVE FAULT DETECTED', findBool(dic['TestAlarm1_4']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_5 != findBool(dic['TestAlarm1_5'])):
                                                globalBS.tempTest1_5 = findBool(dic['TestAlarm1_5'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 5, 'WATER FILTER CHOKED', findBool(dic['TestAlarm1_5']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_6 != findBool(dic['TestAlarm1_6'])):
                                                globalBS.tempTest1_6 = findBool(dic['TestAlarm1_6'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 6, 'WATER LEVEL LOW', findBool(dic['TestAlarm1_6']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_7 != findBool(dic['TestAlarm1_7'])):
                                                globalBS.tempTest1_7 = findBool(dic['TestAlarm1_7'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 7, 'AIR PRESSURE LOW', findBool(dic['TestAlarm1_7']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_8 != findBool(dic['TestAlarm1_8'])):
                                                globalBS.tempTest1_8 = findBool(dic['TestAlarm1_8'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 8, 'WATER MINIMUM PRESSURE NOT REACHED', findBool(dic['TestAlarm1_8']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_9 != findBool(dic['TestAlarm1_9'])):
                                                globalBS.tempTest1_9 = findBool(dic['TestAlarm1_9'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 9, 'PIR NUMBER NOT ENTERED', findBool(dic['TestAlarm1_9']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_10 != findBool(dic['TestAlarm1_10'])):
                                                globalBS.tempTest1_10 = findBool(dic['TestAlarm1_10'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 10, 'SET EXRACTION PRESSURE NOT ENTERED', findBool(dic['TestAlarm1_10']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_11 != findBool(dic['TestAlarm1_11'])):
                                                globalBS.tempTest1_11 = findBool(dic['TestAlarm1_11'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 11, 'SET TEST PRESSURE NOT ENTERED', findBool(dic['TestAlarm1_11']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_12 != findBool(dic['TestAlarm1_12'])):
                                                globalBS.tempTest1_12 = findBool(dic['TestAlarm1_12'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 12, 'RIGHT CLAMP EMERGENCY PRESSED', findBool(dic['TestAlarm1_12']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_13 != findBool(dic['TestAlarm1_13'])):
                                                globalBS.tempTest1_13 = findBool(dic['TestAlarm1_13'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 13, 'LEFT CLAMP EMERGENCY PRESSED', findBool(dic['TestAlarm1_13']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_14 != findBool(dic['TestAlarm1_14'])):
                                                globalBS.tempTest1_14 = findBool(dic['TestAlarm1_14'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 14, 'CHECK CLAMPING LIMIT PRESSURE', findBool(dic['TestAlarm1_14']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_15 != findBool(dic['TestAlarm1_15'])):
                                                globalBS.tempTest1_15 = findBool(dic['TestAlarm1_15'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 15, 'MAIN DRIVE NOT READY', findBool(dic['TestAlarm1_15']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest1_16 != findBool(dic['TestAlarm1_16'])):
                                                globalBS.tempTest1_16 = findBool(dic['TestAlarm1_16'])
                                                sql = "INSERT INTO testalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], 16, 'SPARE8', findBool(dic['TestAlarm1_16']))
                                                mycursor.execute(sql, val)



                                        if(globalBS.tempTest2_1 != findBool(dic['TestAlarm2_1'])):
                                                globalBS.tempTest2_1 = findBool(dic['TestAlarm2_1']) 
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 1, 'HYDRAULIC MOTOR TRIPPED', findBool(dic['TestAlarm2_1']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_2 != findBool(dic['TestAlarm2_2'])):
                                                globalBS.tempTest2_2 = findBool(dic['TestAlarm2_2'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 2, 'WATER PUMP TRIPPED', findBool(dic['TestAlarm2_2']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_3 != findBool(dic['TestAlarm2_3'])):
                                                globalBS.tempTest2_3 = findBool(dic['TestAlarm2_3'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 3, 'HMI PANEL EMERGENCY PRESSED', findBool(dic['TestAlarm2_3']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_4 != findBool(dic['TestAlarm2_4'])):
                                                globalBS.tempTest2_4 = findBool(dic['TestAlarm2_4'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 4, 'MAIN DRIVE FAULT DETECTED', findBool(dic['TestAlarm2_4']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_5 != findBool(dic['TestAlarm2_5'])):
                                                globalBS.tempTest2_5 = findBool(dic['TestAlarm2_5'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 5, 'WATER FILTER CHOKED', findBool(dic['TestAlarm2_5']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_6 != findBool(dic['TestAlarm2_6'])):
                                                globalBS.tempTest2_6 = findBool(dic['TestAlarm2_6'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 6, 'WATER LEVEL LOW', findBool(dic['TestAlarm2_6']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_7 != findBool(dic['TestAlarm2_7'])):
                                                globalBS.tempTest2_7 = findBool(dic['TestAlarm2_7'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 7, 'AIR PRESSURE LOW', findBool(dic['TestAlarm2_7']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_8 != findBool(dic['TestAlarm2_8'])):
                                                globalBS.tempTest2_8 = findBool(dic['TestAlarm2_8'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 8, 'WATER MINIMUM PRESSURE NOT REACHED', findBool(dic['TestAlarm2_8']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_9 != findBool(dic['TestAlarm2_9'])):
                                                globalBS.tempTest2_9 = findBool(dic['TestAlarm2_9'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 9, 'PIR NUMBER NOT ENTERED', findBool(dic['TestAlarm2_9']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_10 != findBool(dic['TestAlarm2_10'])):
                                                globalBS.tempTest2_10 = findBool(dic['TestAlarm2_10'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 10, 'SET EXRACTION PRESSURE NOT ENTERED', findBool(dic['TestAlarm2_10']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_11 != findBool(dic['TestAlarm2_11'])):
                                                globalBS.tempTest2_11 = findBool(dic['TestAlarm2_11'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 11, 'SET TEST PRESSURE NOT ENTERED', findBool(dic['TestAlarm2_11']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_12 != findBool(dic['TestAlarm2_12'])):
                                                globalBS.tempTest2_12 = findBool(dic['TestAlarm2_12'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 12, 'RIGHT CLAMP EMERGENCY PRESSED', findBool(dic['TestAlarm2_12']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_13 != findBool(dic['TestAlarm2_13'])):
                                                globalBS.tempTest2_13 = findBool(dic['TestAlarm2_13'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 13, 'LEFT CLAMP EMERGENCY PRESSED', findBool(dic['TestAlarm2_13']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_14 != findBool(dic['TestAlarm2_14'])):
                                                globalBS.tempTest2_14 = findBool(dic['TestAlarm2_14'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 14, 'CHECK CLAMPING LIMIT PRESSURE', findBool(dic['TestAlarm2_14']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_15 != findBool(dic['TestAlarm2_15'])):
                                                globalBS.tempTest2_15 = findBool(dic['TestAlarm2_15'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 15, 'MAIN DRIVE NOT READY', findBool(dic['TestAlarm2_15']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest2_16 != findBool(dic['TestAlarm2_16'])):
                                                globalBS.tempTest2_16 = findBool(dic['TestAlarm2_16'])
                                                sql = "INSERT INTO testalarm2 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], 16, 'SPARE8', findBool(dic['TestAlarm2_16']))
                                                mycursor.execute(sql, val)



                                        if(globalBS.tempTest3_1 != findBool(dic['TestAlarm3_1'])):
                                                globalBS.tempTest3_1 = findBool(dic['TestAlarm3_1']) 
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 1, 'HYDRAULIC MOTOR TRIPPED', findBool(dic['TestAlarm3_1']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_2 != findBool(dic['TestAlarm3_2'])):
                                                globalBS.tempTest3_2 = findBool(dic['TestAlarm3_2'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 2, 'WATER PUMP TRIPPED', findBool(dic['TestAlarm3_2']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_3 != findBool(dic['TestAlarm3_3'])):
                                                globalBS.tempTest3_3 = findBool(dic['TestAlarm3_3'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 3, 'HMI PANEL EMERGENCY PRESSED', findBool(dic['TestAlarm3_3']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_4 != findBool(dic['TestAlarm3_4'])):
                                                globalBS.tempTest3_4 = findBool(dic['TestAlarm3_4'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 4, 'MAIN DRIVE FAULT DETECTED', findBool(dic['TestAlarm3_4']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_5 != findBool(dic['TestAlarm3_5'])):
                                                globalBS.tempTest3_5 = findBool(dic['TestAlarm3_5'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 5, 'WATER FILTER CHOKED', findBool(dic['TestAlarm3_5']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_6 != findBool(dic['TestAlarm3_6'])):
                                                globalBS.tempTest3_6 = findBool(dic['TestAlarm3_6'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 6, 'WATER LEVEL LOW', findBool(dic['TestAlarm3_6']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_7 != findBool(dic['TestAlarm3_7'])):
                                                globalBS.tempTest3_7 = findBool(dic['TestAlarm3_7'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 7, 'AIR PRESSURE LOW', findBool(dic['TestAlarm3_7']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_8 != findBool(dic['TestAlarm3_8'])):
                                                globalBS.tempTest3_8 = findBool(dic['TestAlarm3_8'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 8, 'WATER MINIMUM PRESSURE NOT REACHED', findBool(dic['TestAlarm3_8']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_9 != findBool(dic['TestAlarm3_9'])):
                                                globalBS.tempTest3_9 = findBool(dic['TestAlarm3_9'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 9, 'PIR NUMBER NOT ENTERED', findBool(dic['TestAlarm3_9']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_10 != findBool(dic['TestAlarm3_10'])):
                                                globalBS.tempTest3_10 = findBool(dic['TestAlarm3_10'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 10, 'SET EXRACTION PRESSURE NOT ENTERED', findBool(dic['TestAlarm3_10']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_11 != findBool(dic['TestAlarm3_11'])):
                                                globalBS.tempTest3_11 = findBool(dic['TestAlarm3_11'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 11, 'SET TEST PRESSURE NOT ENTERED', findBool(dic['TestAlarm3_11']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_12 != findBool(dic['TestAlarm3_12'])):
                                                globalBS.tempTest3_12 = findBool(dic['TestAlarm3_12'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 12, 'RIGHT CLAMP EMERGENCY PRESSED', findBool(dic['TestAlarm3_12']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_13 != findBool(dic['TestAlarm3_13'])):
                                                globalBS.tempTest3_13 = findBool(dic['TestAlarm3_13'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 13, 'LEFT CLAMP EMERGENCY PRESSED', findBool(dic['TestAlarm3_13']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_14 != findBool(dic['TestAlarm3_14'])):
                                                globalBS.tempTest3_14 = findBool(dic['TestAlarm3_14'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 14, 'CHECK CLAMPING LIMIT PRESSURE', findBool(dic['TestAlarm3_14']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_15 != findBool(dic['TestAlarm3_15'])):
                                                globalBS.tempTest3_15 = findBool(dic['TestAlarm3_15'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 15, 'MAIN DRIVE NOT READY', findBool(dic['TestAlarm3_15']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempTest3_16 != findBool(dic['TestAlarm3_16'])):
                                                globalBS.tempTest3_16 = findBool(dic['TestAlarm3_16'])
                                                sql = "INSERT INTO testalarm3 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], 16, 'SPARE8', findBool(dic['TestAlarm3_16']))
                                                mycursor.execute(sql, val)



                                        #PLC Status
                                        if(globalBS.tempPlc_1 != findBool(dic['Plc_1'])):
                                                globalBS.tempPlc_1 = findBool(dic['Plc_1'])
                                                sql = "INSERT INTO plcstatus ( col_id, mandrel1 ) VALUES (%s,%s)"
                                                val = (9, findBool(dic['Plc_1']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempPlc_2 != findBool(dic['Plc_2'])):
                                                globalBS.tempPlc_2 = findBool(dic['Plc_2'])
                                                sql = "INSERT INTO plcstatus ( col_id, mandrel2 ) VALUES (%s,%s)"
                                                val = (10, findBool(dic['Plc_2']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempPlc_3 != findBool(dic['Plc_3'])):
                                                globalBS.tempPlc_3 = findBool(dic['Plc_3'])
                                                sql = "INSERT INTO plcstatus ( col_id, extruder1 ) VALUES (%s,%s)"
                                                val = (11, findBool(dic['Plc_3']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempPlc_4 != findBool(dic['Plc_4'])):
                                                globalBS.tempPlc_4 = findBool(dic['Plc_4'])
                                                sql = "INSERT INTO plcstatus ( col_id, extruder3 ) VALUES (%s,%s)"
                                                val = (12, findBool(dic['Plc_4']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempPlc_5 != findBool(dic['Plc_5'])):
                                                globalBS.tempPlc_5 = findBool(dic['Plc_5'])
                                                sql = "INSERT INTO plcstatus ( col_id, vulcanizer1 ) VALUES (%s,%s)"
                                                val = (13, findBool(dic['Plc_5']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempPlc_6 != findBool(dic['Plc_6'])):
                                                globalBS.tempPlc_6 = findBool(dic['Plc_6'])
                                                sql = "INSERT INTO plcstatus ( col_id, testing1 ) VALUES (%s,%s)"
                                                val = (14, findBool(dic['Plc_6']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempPlc_7 != findBool(dic['Plc_7'])):
                                                globalBS.tempPlc_7 = findBool(dic['Plc_7'])
                                                sql = "INSERT INTO plcstatus ( col_id, testing2 ) VALUES (%s,%s)"
                                                val = (15, findBool(dic['Plc_7']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempPlc_8 != findBool(dic['Plc_8'])):
                                                globalBS.tempPlc_8 = findBool(dic['Plc_8'])
                                                sql = "INSERT INTO plcstatus ( col_id, testing3 ) VALUES (%s,%s)"
                                                val = (16, findBool(dic['Plc_8']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempExtStop1 != findBool(dic['ExtStop1_2'])):
                                            globalBS.tempExtStop1 = findBool(dic['ExtStop1_2'])
                                           # print("globalBS.tempExtStop1 After:",globalBS.tempExtStop1)
                                           # print("findBool(dic['ExtStop1_2']):",findBool(dic['ExtStop1_2']))
                                            if(findBool(dic['ExtStop1_2']) == True):
                                                globalBS.tempExtStopID1 = int(dic['ExtStop1_1'])
                                            if(globalBS.tempExtStopID1 == '1'):
                                                dic['ExtStopMessage1'] = "Start Up Delay"
                                            elif(globalBS.tempExtStopID1 == '2'):
                                                dic['ExtStopMessage1'] = "Man Power Absent"
                                            elif(globalBS.tempExtStopID1 == '3'):
                                                dic['ExtStopMessage1'] = "Material Scortch"
                                            elif(globalBS.tempExtStopID1 == '4'):
                                                dic['ExtStopMessage1'] = "Hose Curebit Rejection"
                                            elif(globalBS.tempExtStopID1 == '5'):
                                                dic['ExtStopMessage1'] = "Cover/Tube Stripping"
                                            elif(globalBS.tempExtStopID1 == '6'):
                                                dic['ExtStopMessage1'] = "M/C Breakdown"
                                            elif(globalBS.tempExtStopID1 == '7'):
                                                dic['ExtStopMessage1'] = "Break Fast"
                                            elif(globalBS.tempExtStopID1 == '8'):
                                                dic['ExtStopMessage1'] = "Lunch"
                                            elif(globalBS.tempExtStopID1 == '9'):
                                                dic['ExtStopMessage1'] = "Dinner"
                                            elif(globalBS.tempExtStopID1 == '10'):
                                                dic['ExtStopMessage1'] = "Tea"
                                            elif(globalBS.tempExtStopID1 == '11'):
                                                dic['ExtStopMessage1'] = "Power Cut"
                                            elif(globalBS.tempExtStopID1 == '12'):
                                                dic['ExtStopMessage1'] = "Compount Shortage"
                                            elif(globalBS.tempExtStopID1 == '13'):
                                                dic['ExtStopMessage1'] = "No Plan/No Load"
                                            elif(globalBS.tempExtStopID1 == '14'):
                                                dic['ExtStopMessage1'] = "Speed Loss"
                                            elif(globalBS.tempExtStopID1 == '15'):
                                                dic['ExtStopMessage1'] = "Training"
                                            elif(globalBS.tempExtStopID1 == '16'):
                                                dic['ExtStopMessage1'] = "Mandrel Shortage"
                                            elif(globalBS.tempExtStopID1 == '17'):
                                                dic['ExtStopMessage1'] = "Drum shortage"
                                            elif(globalBS.tempExtStopID1 == '18'):
                                                dic['ExtStopMessage1'] = "Die/Pin Problem"
                                            elif(globalBS.tempExtStopID1 == '19'):
                                                dic['ExtStopMessage1'] = "5s & House keeping"
                                            elif(globalBS.tempExtStopID1 == '20'):
                                                dic['ExtStopMessage1'] = "Trial"
                                            elif(globalBS.tempExtStopID1 == '21'):
                                                dic['ExtStopMessage1'] = "Unaccountable Loss"
                                            elif(globalBS.tempExtStopID1 == '22'):
                                                dic['ExtStopMessage1'] = "Other"
                                            elif(globalBS.tempExtStopID1 == '23'):
                                                dic['ExtStopMessage1'] = "SetupTime"
                                            elif(globalBS.tempExtStopID1 == '24'):
                                                dic['ExtStopMessage1'] = "Machine Head Clean"

                                            if(findBool(dic['ExtStop1_2']) == True):
                                                sql = "INSERT INTO extstoppage1 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], int(dic['ExtStop1_1']), dic['ExtStopMessage1'], findBool(dic['ExtStop1_2']))
                                                mycursor.execute(sql, val)

                                            else:
                                                sql = "INSERT INTO extstoppage1 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder1_1'], dic['Extruder1_2'], globalBS.tempExtStopID1, dic['ExtStopMessage1'], findBool(dic['ExtStop1_2']))
                                                mycursor.execute(sql, val)



                                        if(globalBS.tempExtStop3 != findBool(dic['ExtStop3_2'])):
                                            globalBS.tempExtStop3 = findBool(dic['ExtStop3_2'])
                                            if(findBool(dic['ExtStop3_2']) == True):
                                                globalBS.tempExtStopID3 = int(dic['ExtStop3_1'])
                                            if(dic['ExtStop3_1'] == '1'):
                                                dic['ExtStopMessage3'] = "Start Up Delay"
                                            elif(dic['ExtStop3_1'] == '2'):
                                                dic['ExtStopMessage3'] = "Man Power Absent"
                                            elif(dic['ExtStop3_1'] == '3'):
                                                dic['ExtStopMessage3'] = "Material Scortch"
                                            elif(dic['ExtStop3_1'] == '4'):
                                                dic['ExtStopMessage3'] = "Hose Curebit Rejection"
                                            elif(dic['ExtStop3_1'] == '5'):
                                                dic['ExtStopMessage3'] = "Cover/Tube Stripping"
                                            elif(dic['ExtStop3_1'] == '6'):
                                                dic['ExtStopMessage3'] = "M/C Breakdown"
                                            elif(dic['ExtStop3_1'] == '7'):
                                                dic['ExtStopMessage3'] = "Break Fast"
                                            elif(dic['ExtStop3_1'] == '8'):
                                                dic['ExtStopMessage3'] = "Lunch"
                                            elif(dic['ExtStop3_1'] == '9'):
                                                dic['ExtStopMessage3'] = "Dinner"
                                            elif(dic['ExtStop3_1'] == '10'):
                                                dic['ExtStopMessage3'] = "Tea"
                                            elif(dic['ExtStop3_1'] == '11'):
                                                dic['ExtStopMessage3'] = "Power Cut"
                                            elif(dic['ExtStop3_1'] == '12'):
                                                dic['ExtStopMessage3'] = "Compount Shortage"
                                            elif(dic['ExtStop3_1'] == '13'):
                                                dic['ExtStopMessage3'] = "No Plan/No Load"
                                            elif(dic['ExtStop3_1'] == '14'):
                                                dic['ExtStopMessage3'] = "Speed Loss"
                                            elif(dic['ExtStop3_1'] == '15'):
                                                dic['ExtStopMessage3'] = "Training"
                                            elif(dic['ExtStop3_1'] == '16'):
                                                dic['ExtStopMessage3'] = "Mandrel Shortage"
                                            elif(dic['ExtStop3_1'] == '17'):
                                                dic['ExtStopMessage3'] = "Drum shortage"
                                            elif(dic['ExtStop3_1'] == '18'):
                                                dic['ExtStopMessage3'] = "Die/Pin Problem"
                                            elif(dic['ExtStop3_1'] == '19'):
                                                dic['ExtStopMessage3'] = "5s & House keeping"
                                            elif(dic['ExtStop3_1'] == '20'):
                                                dic['ExtStopMessage3'] = "Trial"
                                            elif(dic['ExtStop3_1'] == '21'):
                                                dic['ExtStopMessage3'] = "Unaccountable Loss"
                                            elif(dic['ExtStop3_1'] == '22'):
                                                dic['ExtStopMessage3'] = "Other"
                                            elif(dic['ExtStop3_1'] == '23'):
                                                dic['ExtStopMessage3'] = "SetupTime"
                                            elif(dic['ExtStop3_1'] == '24'):
                                                dic['ExtStopMessage3'] = "Machine Head Clean"

                                            if(findBool(dic['ExtStop3_2']) == True):
                                                sql = "INSERT INTO extstoppage3 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], int(dic['ExtStop3_1']), dic['ExtStopMessage1'], findBool(dic['ExtStop3_2']))
                                                mycursor.execute(sql, val)

                                            else:
                                                sql = "INSERT INTO extstoppage3 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Extruder3_1'], dic['Extruder3_2'], globalBS.tempExtStopID3, dic['ExtStopMessage1'], findBool(dic['ExtStop3_2']))
                                                mycursor.execute(sql, val)




                                        if(globalBS.tempManStop1 != findBool(dic['ManStop1_2'])):
                                            globalBS.tempManStop1 = findBool(dic['ManStop1_2'])
                                            if(findBool(dic['ManStop1_2']) == True):
                                                globalBS.tempManStopID1 = int(dic['ManStop1_1'])
                                            if(dic['ManStop1_1'] == '1'):
                                                dic['ManStopMessage1'] = "mandrel od over size"
                                            elif(dic['ManStop1_1'] == '2'):
                                                dic['ManStopMessage1'] = "mandrel od under size"
                                            elif(dic['ManStop1_1'] == '3'):
                                                dic['ManStopMessage1'] = "mandrel short length"
                                            elif(dic['ManStop1_1'] == '4'):
                                                dic['ManStopMessage1'] = "no plan/ no load"
                                            elif(dic['ManStop1_1'] == '5'):
                                                dic['ManStopMessage1'] = "drum shortage"
                                            elif(dic['ManStop1_1'] == '6'):
                                                dic['ManStopMessage1'] = "M/C break down"
                                            elif(dic['ManStop1_1'] == '7'):
                                                dic['ManStopMessage1'] = "manpower absent"
                                            elif(dic['ManStop1_1'] == '8'):
                                                dic['ManStopMessage1'] = "start up delay"
                                            elif(dic['ManStop1_1'] == '9'):
                                                dic['ManStopMessage1'] = "5s and house keeping"
                                            elif(dic['ManStop1_1'] == '10'):
                                                dic['ManStopMessage1'] = "lunch/break fast/ dinner"
                                            if(findBool(dic['ManStop1_2']) == True):
                                                sql = "INSERT INTO manstoppage1 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], int(dic['ManStop1_1']), dic['ManStopMessage1'], findBool(dic['ManStop1_2']))
                                                mycursor.execute(sql, val)

                                            else:
                                                sql = "INSERT INTO manstoppage1 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel1_1'], dic['Mandrel1_2'], globalBS.tempManStopID1, dic['ManStopMessage1'], findBool(dic['ManStop1_2']))
                                                mycursor.execute(sql, val)


                                        if(globalBS.tempManStop2 != findBool(dic['ManStop2_2'])):
                                            globalBS.tempManStop2 = findBool(dic['ManStop2_2'])
                                            if(findBool(dic['ManStop2_2']) == True):
                                                globalBS.tempManStopID2 = int(dic['ManStop2_1'])
                                            if(dic['ManStop2_1'] == '1'):
                                                dic['ManStopMessage2'] = "mandrel od over size"
                                            elif(dic['ManStop2_1'] == '2'):
                                                dic['ManStopMessage2'] = "mandrel od under size"
                                            elif(dic['ManStop2_1'] == '3'):
                                                dic['ManStopMessage2'] = "mandrel short length"
                                            elif(dic['ManStop2_1'] == '4'):
                                                dic['ManStopMessage2'] = "no plan/ no load"
                                            elif(dic['ManStop2_1'] == '5'):
                                                dic['ManStopMessage2'] = "drum shortage"
                                            elif(dic['ManStop2_1'] == '6'):
                                                dic['ManStopMessage2'] = "M/C break down"
                                            elif(dic['ManStop2_1'] == '7'):
                                                dic['ManStopMessage2'] = "manpower absent"
                                            elif(dic['ManStop2_1'] == '8'):
                                                dic['ManStopMessage2'] = "start up delay"
                                            elif(dic['ManStop2_1'] == '9'):
                                                dic['ManStopMessage2'] = "5s and house keeping"
                                            elif(dic['ManStop2_1'] == '10'):
                                                dic['ManStopMessage2'] = "lunch/break fast/ dinner"
                                            if(findBool(dic['ManStop2_2']) == True):
                                                sql = "INSERT INTO manstoppage2 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], int(dic['ManStop2_1']), dic['ManStopMessage2'], findBool(dic['ManStop2_2']))
                                                mycursor.execute(sql, val)

                                            else:
                                                sql = "INSERT INTO manstoppage2 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Mandrel2_1'], dic['Mandrel2_2'], globalBS.tempManStopID2, dic['ManStopMessage2'], findBool(dic['ManStop2_2']))
                                                mycursor.execute(sql, val)


                                        if(globalBS.tempVulStop1 != findBool(dic['VulStop1_2'])):
                                            globalBS.tempVulStop1 = findBool(dic['VulStop1_2'])
                                            if(findBool(dic['VulStop1_2']) == True):
                                                globalBS.tempVulStopID1 = int(dic['VulStop1_1'])
                                            if(dic['VulStop1_1'] == '1'):
                                                dic['VulStopMessage1'] = "Start Up Delay"
                                            elif(dic['VulStop1_1'] == '2'):
                                                dic['VulStopMessage1'] = "Man Power Absent"
                                            elif(dic['VulStop1_1'] == '3'):
                                                dic['VulStopMessage1'] = "Steam Delay"
                                            elif(dic['VulStop1_1'] == '4'):
                                                dic['VulStopMessage1'] = "Break Fast"
                                            elif(dic['VulStop1_1'] == '5'):
                                                dic['VulStopMessage1'] = "Lunch"
                                            elif(dic['VulStop1_1'] == '6'):
                                                dic['VulStopMessage1'] = "Dinner"
                                            elif(dic['VulStop1_1'] == '7'):
                                                dic['VulStopMessage1'] = "Tea"
                                            elif(dic['VulStop1_1'] == '8'):
                                                dic['VulStopMessage1'] = "Power Cut"
                                            elif(dic['VulStop1_1'] == '9'):
                                                dic['VulStopMessage1'] = "No Plan/No Load"
                                            elif(dic['VulStop1_1'] == '10'):
                                                dic['VulStopMessage1'] = "Steam Leakage"
                                            elif(dic['VulStop1_1'] == '11'):
                                                dic['VulStopMessage1'] = "Drum Shortage"
                                            elif(dic['VulStop1_1'] == '12'):
                                                dic['VulStopMessage1'] = "5s & House keeping "
                                            elif(dic['VulStop1_1'] == '13'):
                                                dic['VulStopMessage1'] = "Trail"
                                            elif(dic['VulStop1_1'] == '14'):
                                                dic['VulStopMessage1'] = "Dummy Cycle"
                                            elif(dic['VulStop1_1'] == '15'):
                                                dic['VulStopMessage1'] = "Vulc.Pre Heating"
                                            elif(dic['VulStop1_1'] == '16'):
                                                dic['VulStopMessage1'] = "UnAcc.Loss"
                                            elif(dic['VulStop1_1'] == '17'):
                                                dic['VulStopMessage1'] = "Others"

                                            if(findBool(dic['VulStop1_2']) == True):
                                                sql = "INSERT INTO vulstoppage1 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], int(dic['VulStop1_1']), dic['VulStopMessage1'], findBool(dic['VulStop1_2']))
                                                mycursor.execute(sql, val)

                                            else:
                                                sql = "INSERT INTO vulstoppage1 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], globalBS.tempVulStopID1, dic['VulStopMessage1'], findBool(dic['VulStop1_2']))
                                                mycursor.execute(sql, val)


                                        if(globalBS.tempTestStop1 != findBool(dic['TestStop1_2'])):
                                            globalBS.tempTestStop1 = findBool(dic['TestStop1_2'])
                                            if(findBool(dic['TestStop1_2']) == True):
                                                globalBS.tempTestStopID1 = int(dic['TestStop1_1'])
                                            if(dic['TestStop1_1'] == '1'):
                                                dic['TestStopMessage1'] = "Start Up Delay"
                                            elif(dic['TestStop1_1'] == '2'):
                                                dic['TestStopMessage1'] = "M/C Cleaning"
                                            elif(dic['TestStop1_1'] == '3'):
                                                dic['TestStopMessage1'] = "Man power Absent"
                                            elif(dic['TestStop1_1'] == '4'):
                                                dic['TestStopMessage1'] = "M/C Breakdown"
                                            elif(dic['TestStop1_1'] == '5'):
                                                dic['TestStopMessage1'] = "Power Cut"
                                            elif(dic['TestStop1_1'] == '6'):
                                                dic['TestStopMessage1'] = "Lunch & Tea"
                                            elif(dic['TestStop1_1'] == '7'):
                                                dic['TestStopMessage1'] = "No Plan/No Load"
                                            elif(dic['TestStop1_1'] == '8'):
                                                dic['TestStopMessage1'] = "Testing NO INFO  problem"
                                            elif(dic['TestStop1_1'] == '9'):
                                                dic['TestStopMessage1'] = "Nipple issue/Tool Broken"
                                            elif(dic['TestStop1_1'] == '10'):
                                                dic['TestStopMessage1'] = "Hose Leakage/Burst Issue"
                                            elif(dic['TestStop1_1'] == '11'):
                                                dic['TestStopMessage1'] = "Mandrel Skin Issue"
                                            elif(dic['TestStop1_1'] == '12'):
                                                dic['TestStopMessage1'] = "Mandrel Releasing Issue"
                                            elif(dic['TestStop1_1'] == '13'):
                                                dic['TestStopMessage1'] = "5S & House keeping"
                                            elif(dic['TestStop1_1'] == '14'):
                                                dic['TestStopMessage1'] = "Testing Fail"
                                            elif(dic['TestStop1_1'] == '15'):
                                                dic['TestStopMessage1'] = "Unaccount Loss Time"

                                            if(findBool(dic['TestStop1_2']) == True):
                                                sql = "INSERT INTO teststoppage1 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], int(dic['TestStop1_1']), dic['TestStopMessage1'], findBool(dic['TestStop1_2']))
                                                mycursor.execute(sql, val)

                                            else:
                                                sql = "INSERT INTO teststoppage1 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing1_1'], dic['Testing1_2'], globalBS.tempTestStopID1, dic['TestStopMessage1'], findBool(dic['TestStop1_2']))
                                                mycursor.execute(sql, val)


                                        if(globalBS.tempTestStop2 != findBool(dic['TestStop2_2'])):
                                            globalBS.tempTestStop2 = findBool(dic['TestStop2_2'])
                                            if(findBool(dic['TestStop2_2']) == True):
                                                globalBS.tempTestStopID2 = int(dic['TestStop2_1'])
                                            if(dic['TestStop2_1'] == '1'):
                                                dic['TestStopMessage2'] = "Start Up Delay"
                                            elif(dic['TestStop2_1'] == '2'):
                                                dic['TestStopMessage2'] = "M/C Cleaning"
                                            elif(dic['TestStop2_1'] == '3'):
                                                dic['TestStopMessage2'] = "Man power Absent"
                                            elif(dic['TestStop2_1'] == '4'):
                                                dic['TestStopMessage2'] = "M/C Breakdown"
                                            elif(dic['TestStop2_1'] == '5'):
                                                dic['TestStopMessage2'] = "Power Cut"
                                            elif(dic['TestStop2_1'] == '6'):
                                                dic['TestStopMessage2'] = "Lunch & Tea"
                                            elif(dic['TestStop2_1'] == '7'):
                                                dic['TestStopMessage2'] = "No Plan/No Load"
                                            elif(dic['TestStop2_1'] == '8'):
                                                dic['TestStopMessage2'] = "Testing NO INFO  problem"
                                            elif(dic['TestStop2_1'] == '9'):
                                                dic['TestStopMessage2'] = "Nipple issue/Tool Broken"
                                            elif(dic['TestStop2_1'] == '10'):
                                                dic['TestStopMessage2'] = "Hose Leakage/Burst Issue"
                                            elif(dic['TestStop2_1'] == '11'):
                                                dic['TestStopMessage2'] = "Mandrel Skin Issue"
                                            elif(dic['TestStop2_1'] == '12'):
                                                dic['TestStopMessage2'] = "Mandrel Releasing Issue"
                                            elif(dic['TestStop2_1'] == '13'):
                                                dic['TestStopMessage2'] = "5S & House keeping"
                                            elif(dic['TestStop2_1'] == '14'):
                                                dic['TestStopMessage2'] = "Testing Fail"
                                            elif(dic['TestStop2_1'] == '15'):
                                                dic['TestStopMessage2'] = "Unaccount Loss Time"

                                            if(findBool(dic['TestStop2_2']) == True):
                                                sql = "INSERT INTO teststoppage2 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], int(dic['TestStop2_1']), dic['TestStopMessage2'], findBool(dic['TestStop2_2']))
                                                mycursor.execute(sql, val)

                                            else:
                                                sql = "INSERT INTO teststoppage2 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing2_1'], dic['Testing2_2'], globalBS.tempTestStopID2, dic['TestStopMessage2'], findBool(dic['TestStop2_2']))
                                                mycursor.execute(sql, val)



                                        if(globalBS.tempTestStop3 != findBool(dic['TestStop3_2'])):
                                            globalBS.tempTestStop3 = findBool(dic['TestStop3_2'])
                                            if(findBool(dic['TestStop3_2']) == True):
                                                globalBS.tempTestStopID3 = int(dic['TestStop3_1'])
                                            if(dic['TestStop3_1'] == '1'):
                                                dic['TestStopMessage3'] = "Start Up Delay"
                                            elif(dic['TestStop3_1'] == '2'):
                                                dic['TestStopMessage3'] = "M/C Cleaning"
                                            elif(dic['TestStop3_1'] == '3'):
                                                dic['TestStopMessage3'] = "Man power Absent"
                                            elif(dic['TestStop3_1'] == '4'):
                                                dic['TestStopMessage3'] = "M/C Breakdown"
                                            elif(dic['TestStop3_1'] == '5'):
                                                dic['TestStopMessage3'] = "Power Cut"
                                            elif(dic['TestStop3_1'] == '6'):
                                                dic['TestStopMessage3'] = "Lunch & Tea"
                                            elif(dic['TestStop3_1'] == '7'):
                                                dic['TestStopMessage3'] = "No Plan/No Load"
                                            elif(dic['TestStop3_1'] == '8'):
                                                dic['TestStopMessage3'] = "Testing NO INFO  problem"
                                            elif(dic['TestStop3_1'] == '9'):
                                                dic['TestStopMessage3'] = "Nipple issue/Tool Broken"
                                            elif(dic['TestStop3_1'] == '10'):
                                                dic['TestStopMessage3'] = "Hose Leakage/Burst Issue"
                                            elif(dic['TestStop3_1'] == '11'):
                                                dic['TestStopMessage3'] = "Mandrel Skin Issue"
                                            elif(dic['TestStop3_1'] == '12'):
                                                dic['TestStopMessage3'] = "Mandrel Releasing Issue"
                                            elif(dic['TestStop3_1'] == '13'):
                                                dic['TestStopMessage3'] = "5S & House keeping"
                                            elif(dic['TestStop3_1'] == '14'):
                                                dic['TestStopMessage3'] = "Testing Fail"
                                            elif(dic['TestStop3_1'] == '15'):
                                                dic['TestStopMessage3'] = "Unaccount Loss Time"

                                            if(findBool(dic['TestStop3_2']) == True):
                                                sql = "INSERT INTO teststoppage3 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], int(dic['TestStop3_1']), dic['TestStopMessage3'], findBool(dic['TestStop3_2']))
                                                mycursor.execute(sql, val)

                                            else:
                                                sql = "INSERT INTO teststoppage3 ( pir, operator_name, stoppage_id, stoppage_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Testing3_1'], dic['Testing3_2'], globalBS.tempTestStopID3, dic['TestStopMessage3'], findBool(dic['TestStop3_2']))
                                                mycursor.execute(sql, val)



                                        if(globalBS.tempVul1_1 != findBool(dic['VulAlarm1_1'])):
                                                globalBS.tempVul1_1 = findBool(dic['VulAlarm1_1'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 1, 'DOOR OPEN TIME-PRESSURE HIGH', findBool(dic['VulAlarm1_1']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_2 != findBool(dic['VulAlarm1_2'])):
                                                globalBS.tempVul1_2 = findBool(dic['VulAlarm1_2'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 2, 'WATER PUMP TRIP', findBool(dic['VulAlarm1_2']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_3 != findBool(dic['VulAlarm1_3'])):
                                                globalBS.tempVul1_3 = findBool(dic['VulAlarm1_3'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 3, 'OPEN HAND VALVE', findBool(dic['VulAlarm1_3']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_4 != findBool(dic['VulAlarm1_4'])):
                                                globalBS.tempVul1_4 = findBool(dic['VulAlarm1_4'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 4, 'SPARE 1', findBool(dic['VulAlarm1_4']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_5 != findBool(dic['VulAlarm1_5'])):
                                                globalBS.tempVul1_5 = findBool(dic['VulAlarm1_5'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 5, 'HYDRAULIC MOTOR TRIP', findBool(dic['VulAlarm1_5']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_6 != findBool(dic['VulAlarm1_6'])):
                                                globalBS.tempVul1_6 = findBool(dic['VulAlarm1_6'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 6, 'HMI EMERGENCY PRESSED', findBool(dic['VulAlarm1_6']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_7 != findBool(dic['VulAlarm1_7'])):
                                                globalBS.tempVul1_7 = findBool(dic['VulAlarm1_7'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 7, 'SELECT AUTO MODE', findBool(dic['VulAlarm1_7']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_8 != findBool(dic['VulAlarm1_8'])):
                                                globalBS.tempVul1_8 = findBool(dic['VulAlarm1_8'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 8, 'MANUAL NOT SELECTED', findBool(dic['VulAlarm1_8']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_9 != findBool(dic['VulAlarm1_9'])):
                                                globalBS.tempVul1_9 = findBool(dic['VulAlarm1_9'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 9, 'PANEL EMERGENCY PRESSED', findBool(dic['VulAlarm1_9']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_10 != findBool(dic['VulAlarm1_10'])):
                                                globalBS.tempVul1_10 = findBool(dic['VulAlarm1_10'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 10, 'DOOR MOTOR TRIP', findBool(dic['VulAlarm1_10']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_11 != findBool(dic['VulAlarm1_11'])):
                                                globalBS.tempVul1_11 = findBool(dic['VulAlarm1_11'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 11, 'CLOSE HAND VALVE', findBool(dic['VulAlarm1_11']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_12 != findBool(dic['VulAlarm1_12'])):
                                                globalBS.tempVul1_12 = findBool(dic['VulAlarm1_12'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 12, 'HYDRAULIC MOTOR ON FEEDBACK NOT ON', findBool(dic['VulAlarm1_12']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_13 != findBool(dic['VulAlarm1_13'])):
                                                globalBS.tempVul1_13 = findBool(dic['VulAlarm1_13'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 13, 'RAMUP TEMPERATURE HIGH', findBool(dic['VulAlarm1_13']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_14 != findBool(dic['VulAlarm1_14'])):
                                                globalBS.tempVul1_14 = findBool(dic['VulAlarm1_14'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 14, 'CURING TEMPERATURE HIGH', findBool(dic['VulAlarm1_14']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_15 != findBool(dic['VulAlarm1_15'])):
                                                globalBS.tempVul1_15 = findBool(dic['VulAlarm1_15'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 15, 'PRESSURE HIGH', findBool(dic['VulAlarm1_15']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_16 != findBool(dic['VulAlarm1_16'])):
                                                globalBS.tempVul1_16 = findBool(dic['VulAlarm1_16'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 16, 'SPARE 2', findBool(dic['VulAlarm1_16']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_17 != findBool(dic['VulAlarm1_17'])):
                                                globalBS.tempVul1_17 = findBool(dic['VulAlarm1_17'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 17, 'SPARE 3', findBool(dic['VulAlarm1_17']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_18 != findBool(dic['VulAlarm1_18'])):
                                                globalBS.tempVul1_18 = findBool(dic['VulAlarm1_18'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 18, 'DOOR LOCK LIMIT SWITCH NOT ON', findBool(dic['VulAlarm1_18']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_19 != findBool(dic['VulAlarm1_19'])):
                                                globalBS.tempVul1_19 = findBool(dic['VulAlarm1_19'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 19, 'DOOR OPEN FB NOT ON', findBool(dic['VulAlarm1_19']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_20 != findBool(dic['VulAlarm1_20'])):
                                                globalBS.tempVul1_20 = findBool(dic['VulAlarm1_20'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 20, 'DOOR UNLOCK LIMIT SWITCH NOT ON', findBool(dic['VulAlarm1_20']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_21 != findBool(dic['VulAlarm1_21'])):
                                                globalBS.tempVul1_21 = findBool(dic['VulAlarm1_21'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 21, 'DOOR CLOSED FB NOT ON', findBool(dic['VulAlarm1_21']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_22 != findBool(dic['VulAlarm1_22'])):
                                                globalBS.tempVul1_22 = findBool(dic['VulAlarm1_22'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 22, 'COMPRESSOR PRESSURE LOW', findBool(dic['VulAlarm1_22']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_23 != findBool(dic['VulAlarm1_23'])):
                                                globalBS.tempVul1_23 = findBool(dic['VulAlarm1_23'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 23, 'RAMUP TEMPERATURE LOW', findBool(dic['VulAlarm1_23']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_24 != findBool(dic['VulAlarm1_24'])):
                                                globalBS.tempVul1_24 = findBool(dic['VulAlarm1_24'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 24, 'SPARE 4', findBool(dic['VulAlarm1_24']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_25 != findBool(dic['VulAlarm1_25'])):
                                                globalBS.tempVul1_25 = findBool(dic['VulAlarm1_25'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 25, 'RAMP OR CURING PRESSURE LOW', findBool(dic['VulAlarm1_25']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_26 != findBool(dic['VulAlarm1_26'])):
                                                globalBS.tempVul1_26 = findBool(dic['VulAlarm1_26'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 26, 'SPARE 5', findBool(dic['VulAlarm1_26']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_27 != findBool(dic['VulAlarm1_27'])):
                                                globalBS.tempVul1_27 = findBool(dic['VulAlarm1_27'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 27, 'LOW PRESSURE CHECK COMPRESSOR', findBool(dic['VulAlarm1_27']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_28 != findBool(dic['VulAlarm1_28'])):
                                                globalBS.tempVul1_28 = findBool(dic['VulAlarm1_28'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 28, 'CYCLE PAUSED', findBool(dic['VulAlarm1_28']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_29 != findBool(dic['VulAlarm1_29'])):
                                                globalBS.tempVul1_29 = findBool(dic['VulAlarm1_29'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 29, 'SPARE 6', findBool(dic['VulAlarm1_29']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_30 != findBool(dic['VulAlarm1_30'])):
                                                globalBS.tempVul1_30 = findBool(dic['VulAlarm1_30'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 30, 'SPARE 7', findBool(dic['VulAlarm1_30']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_31 != findBool(dic['VulAlarm1_31'])):
                                                globalBS.tempVul1_31 = findBool(dic['VulAlarm1_31'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 31, 'SPARE 8', findBool(dic['VulAlarm1_31']))
                                                mycursor.execute(sql, val)

                                        if(globalBS.tempVul1_32 != findBool(dic['VulAlarm1_32'])):
                                                globalBS.tempVul1_32 = findBool(dic['VulAlarm1_32'])
                                                sql = "INSERT INTO vulalarm1 ( pir, operator_name, alarm_id, alarm_name , status ) VALUES (%s,%s,%s,%s,%s)"
                                                val = (dic['Vulcanizer1_1'], dic['Vulcanizer1_2'], 32, 'SPARE 9', findBool(dic['VulAlarm1_32']))
                                                mycursor.execute(sql, val)
                                                        

                        if(count2 >= 60): #dumping like counting
                                count2 = 0;
                                #updateLang('english')
                                print("Thread2:Data Processing")
                                json_data = str(message.payload.decode("utf-8","ignore"))
                                if(is_valid_json(json_data)):
                                        json_obj = json.loads(json_data)
                                        if(findBool(json_obj['connected'])):
                                                #print(type(json_obj))
                                                dic['Mandrel1_1'] = fixedInt(json_obj['M-M_R_1-0']) #PIR
                                                dic['Mandrel1_2'] = fixedInt(json_obj['M-M_R_1-1']) #OPERATOR NAME
                                                dic['Mandrel1_3'] = fixedInt(json_obj['M-M_R_1-2']) #PROGRAM NAME
                                                dic['Mandrel1_4'] = fixedInt(json_obj['M-M_R_1-3']) #MANDREL ID 
                                                dic['Mandrel1_5'] = fixedInt(json_obj['M-M_R_1-4']) #ACTUAL OD
                                                dic['Mandrel1_6'] = fixedInt(json_obj['M-M_R_1-5']) #MINIMUM OD 
                                                dic['Mandrel1_7'] = fixedInt(json_obj['M-M_R_1-6']) #MAXMUM OD
                                                dic['Mandrel1_8'] = fixedInt(json_obj['M-M_R_1-7']) #FIXED BLOCK SET TEMP
                                                dic['Mandrel1_9'] = fixedInt(json_obj['M-M_R_1-8']) #MOVABLE BLOCK SET TEMP
                                                dic['Mandrel1_10'] = fixedInt(json_obj['M-M_R_1-9']) #FIXED BLOCK ACTUAL TEMP
                                                dic['Mandrel1_11'] = fixedInt(json_obj['M-M_R_1-10']) #MOVABLE BLOCK ACTUAL TEMP
                                                dic['Mandrel1_12'] = fixedInt(json_obj['M-M_H_1-0']) #MOVABLE BLOCK ACTUAL TEMP
                                                
                                                dic['Mandrel2_1'] = fixedInt(json_obj['M-M_R_2-0']) #PIR
                                                dic['Mandrel2_2'] = fixedInt(json_obj['M-M_R_2-1']) #OPERATOR NAME
                                                dic['Mandrel2_3'] = fixedInt(json_obj['M-M_R_2-2']) #PROGRAM NAME
                                                dic['Mandrel2_4'] = fixedInt(json_obj['M-M_R_2-3']) #MANDREL ID 
                                                dic['Mandrel2_5'] = fixedInt(json_obj['M-M_R_2-4']) #ACTUAL OD
                                                dic['Mandrel2_6'] = fixedInt(json_obj['M-M_R_2-5']) #MINIMUM OD 
                                                dic['Mandrel2_7'] = fixedInt(json_obj['M-M_R_2-6']) #MAXMUM OD
                                                dic['Mandrel2_8'] = fixedInt(json_obj['M-M_R_2-7']) #FIXED BLOCK SET TEMP
                                                dic['Mandrel2_9'] = fixedInt(json_obj['M-M_R_2-8']) #MOVABLE BLOCK SET TEMP
                                                dic['Mandrel2_10'] = fixedInt(json_obj['M-M_R_2-9'] )#FIXED BLOCK ACTUAL TEMP
                                                dic['Mandrel2_11'] = fixedInt(json_obj['M-M_R_2-10']) #MOVABLE BLOCK ACTUAL TEMP
                                                dic['Mandrel2_12'] = fixedInt(json_obj['M-M_H_2-0']) #MOVABLE BLOCK ACTUAL TEMP

                                                
                                                dic['Extruder1_1'] = fixedInt(json_obj['M-E_R_1-0']) #PIR
                                                dic['Extruder1_2'] = fixedInt(json_obj['M-E_R_1-1']) #OPERATOR NAME
                                                dic['Extruder1_3'] = fixedInt(json_obj['M-E_R_1-2']) #LINE RUN FEEDBACK
                                                dic['Extruder1_4'] = fixedInt(json_obj['M-E_R_1-3']) #OD SETPOINT
                                                dic['Extruder1_5'] = fixedInt(json_obj['M-E_R_1-4']) #OD ACTUAL / OD BASE
                                                dic['Extruder1_6'] = fixedInt(json_obj['M-E_R_1-5']) #ID SETPOINT
                                                dic['Extruder1_7'] = fixedInt(json_obj['M-E_R_1-6']) #ID ACTUAL
                                                dic['Extruder1_8'] = fixedInt(json_obj['M-E_R_1-7']) #THICKNESS SET / BASE
                                                dic['Extruder1_9'] = fixedInt(json_obj['M-E_R_1-8']) #THICKNESS ACT
                                                dic['Extruder1_10'] = fixedInt(json_obj['M-E_R_1-9'] )#EXTRUDER RPM SET
                                                dic['Extruder1_11'] = fixedInt(json_obj['M-E_R_1-10']) #EXTRUDER RPM ACT
                                                dic['Extruder1_12'] = fixedInt(json_obj['M-E_R_1-11']) #EXTRUDER CURRENT SET
                                                dic['Extruder1_13'] = fixedInt(json_obj['M-E_R_1-12']) #EXTRUDER CURRENT ACT
                                                dic['Extruder1_14'] = fixedInt(json_obj['M-E_R_1-13']) #EXTRUDER PRESSURE SET
                                                dic['Extruder1_15'] = fixedInt(json_obj['M-E_R_1-14']) #EXTRUDER PRESSURE ACT
                                                dic['Extruder1_16'] = fixedInt(json_obj['M-E_R_1-15']) #LINE MPM SET
                                                dic['Extruder1_17'] = fixedInt(json_obj['M-E_R_1-16']) #LINE MPM ACT
                                                dic['Extruder1_18'] = fixedInt(json_obj['M-E_R_1-17']) #PRODUCTION METER
                                                dic['Extruder1_19'] = fixedInt(json_obj['M-E_R_1-18']) #HEAD TEMP SETPOINT
                                                dic['Extruder1_20'] = fixedInt(json_obj['M-E_R_1-19']) #HEAD TEMP ACTUAL
                                                dic['Extruder1_21'] = fixedInt(json_obj['M-E_R_1-20']) #SCREW TEMP SETPOINT
                                                dic['Extruder1_22'] = fixedInt(json_obj['M-E_R_1-21']) #SCREW TEMP ACTUAL
                                                dic['Extruder1_23'] = fixedInt(json_obj['M-E_R_1-22']) #ZONE2 TEMP SETPOINT
                                                dic['Extruder1_24'] = fixedInt(json_obj['M-E_R_1-23']) #ZONE2 TEMP ACTUAL
                                                dic['Extruder1_25'] = fixedInt(json_obj['M-E_R_1-24']) #ZONE3 TEMP SETPOINT
                                                dic['Extruder1_26'] = fixedInt(json_obj['M-E_R_1-25']) #ZONE3 TEMP ACTUAL
                                                dic['Extruder1_27'] = fixedInt(json_obj['M-E_H_1-56']) #ZONE3 TEMP ACTUAL
                                                
                                                dic['Extruder1_27'] = fixedInt(json_obj['M-E_H_1-5']) #mesh
                                                dic['Extruder1_28'] = fixedInt(json_obj['M-E_H_1-7']) #Linear CUT
                                                dic['Extruder1_29'] = fixedInt(json_obj['M-E_H_1-12']) #tube hot od set
                                                dic['Extruder1_30'] = fixedInt(json_obj['M-E_H_1-13']) #tube hot od act
                                                dic['Extruder1_31'] = fixedInt(json_obj['M-E_H_1-14']) #tube_cold_od_set
                                                dic['Extruder1_32'] = fixedInt(json_obj['M-E_H_1-15']) #tube cold od act
                                                dic['Extruder1_33'] = fixedInt(json_obj['M-E_H_1-16']) #pin set value
                                                dic['Extruder1_34'] = fixedInt(json_obj['M-E_H_1-17']) #pin act value
                                                dic['Extruder1_35'] = fixedInt(json_obj['M-E_H_1-18']) #die set value
                                                dic['Extruder1_36'] = fixedInt(json_obj['M-E_H_1-19']) #die act value
                                                dic['Extruder1_37'] = fixedInt(json_obj['M-E_H_1-9']) #drum out no
                                                dic['Extruder1_38'] = fixedInt(json_obj['M-E_H_1-20']) #amps
                                                dic['Extruder1_39'] = fixedInt(json_obj['M-E_H_1-21']) #screw rpm
                                                dic['Extruder1_40'] = fixedInt(json_obj['M-E_H_1-22']) #line speed
                                                dic['Extruder1_41'] = fixedInt(json_obj['M-E_H_1-25']) #batches used
                                                dic['Extruder1_42'] = fixedInt(json_obj['M-E_H_1-23']) #extruder qty
                                                dic['Extruder1_43'] = fixedInt(json_obj['M-E_H_1-26']) #temp head set
                                                dic['Extruder1_44'] = fixedInt(json_obj['M-E_H_1-51']) #temp head act
                                                dic['Extruder1_45'] = fixedInt(json_obj['M-E_H_1-28']) #temp zone1 set
                                                dic['Extruder1_46'] = fixedInt(json_obj['M-E_H_1-27']) #temp zone1 act
                                                dic['Extruder1_47'] = fixedInt(json_obj['M-E_H_1-30']) #temp zone2 set 
                                                dic['Extruder1_48'] = fixedInt(json_obj['M-E_H_1-29']) #temp zone2 act
                                                dic['Extruder1_49'] = fixedInt(json_obj['M-E_H_1-52']) #tempo zone3 set
                                                dic['Extruder1_50'] = fixedInt(json_obj['M-E_H_1-31']) #temp zone3 act
                                                dic['Extruder1_51'] = fixedInt(json_obj['M-E_H_1-32']) #temp zone4 set
                                                dic['Extruder1_52'] = fixedInt(json_obj['M-E_H_1-33']) #temp zone4 act
                                                dic['Extruder1_53'] = fixedInt(json_obj['M-E_H_1-34']) #temp zone5 set
                                                dic['Extruder1_54'] = fixedInt(json_obj['M-E_H_1-35']) #temp zone5 act
                                                dic['Extruder1_55'] = fixedInt(json_obj['M-E_H_1-36']) #vaccumn set value
                                                dic['Extruder1_56'] = fixedInt(json_obj['M-E_H_1-37']) #vaccum act value
                                                dic['Extruder1_57'] = fixedInt(json_obj['M-E_H_1-38']) #wall thick spec
                                                dic['Extruder1_58'] = fixedInt(json_obj['M-E_H_1-39']) #wall thick act
                                                dic['Extruder1_59'] = fixedInt(json_obj['M-E_H_1-40']) #ecc set value
                                                dic['Extruder1_60'] = fixedInt(json_obj['M-E_H_1-41']) #ecc act value
                                                dic['Extruder1_61'] = fixedInt(json_obj['M-E_H_1-42']) #qa approval
                                                
                                                dic['Extruder3_27'] = fixedInt(json_obj['M-E_H_3-5']) #mesh
                                                dic['Extruder3_28'] = fixedInt(json_obj['M-E_H_3-7']) #Linear CUT
                                                dic['Extruder3_29'] = fixedInt(json_obj['M-E_H_3-12']) #tube hot od set
                                                dic['Extruder3_30'] = fixedInt(json_obj['M-E_H_3-13']) #tube hot od act
                                                dic['Extruder3_31'] = fixedInt(json_obj['M-E_H_3-14']) #tube_cold_od_set
                                                dic['Extruder3_32'] = fixedInt(json_obj['M-E_H_3-15']) #tube cold od act
                                                dic['Extruder3_33'] = fixedInt(json_obj['M-E_H_3-16']) #pin set value
                                                dic['Extruder3_34'] = fixedInt(json_obj['M-E_H_3-17']) #pin act value
                                                dic['Extruder3_35'] = fixedInt(json_obj['M-E_H_3-18']) #die set value
                                                dic['Extruder3_36'] = fixedInt(json_obj['M-E_H_3-19']) #die act value
                                                dic['Extruder3_37'] = fixedInt(json_obj['M-E_H_3-9']) #drum out no
                                                dic['Extruder3_38'] = fixedInt(json_obj['M-E_H_3-20']) #amps
                                                dic['Extruder3_39'] = fixedInt(json_obj['M-E_H_3-21']) #screw rpm
                                                dic['Extruder3_40'] = fixedInt(json_obj['M-E_H_3-22']) #line speed
                                                dic['Extruder3_41'] = fixedInt(json_obj['M-E_H_3-25']) #batches used
                                                dic['Extruder3_42'] = fixedInt(json_obj['M-E_H_3-43']) #extruder qty
                                                dic['Extruder3_43'] = fixedInt(json_obj['M-E_H_3-26']) #temp head set
                                                dic['Extruder3_44'] = fixedInt(json_obj['M-E_H_3-51']) #temp head act
                                                dic['Extruder3_45'] = fixedInt(json_obj['M-E_H_3-28']) #temp zone1 set
                                                dic['Extruder3_46'] = fixedInt(json_obj['M-E_H_3-27']) #temp zone1 act
                                                dic['Extruder3_47'] = fixedInt(json_obj['M-E_H_3-30']) #temp zone2 set 
                                                dic['Extruder3_48'] = fixedInt(json_obj['M-E_H_3-29']) #temp zone2 act
                                                dic['Extruder3_49'] = fixedInt(json_obj['M-E_H_3-52']) #tempo zone3 set
                                                dic['Extruder3_50'] = fixedInt(json_obj['M-E_H_3-31']) #temp zone3 act
                                                dic['Extruder3_51'] = fixedInt(json_obj['M-E_H_3-33']) #temp zone4 set
                                                dic['Extruder3_52'] = fixedInt(json_obj['M-E_H_3-32']) #temp zone4 act
                                                dic['Extruder3_53'] = fixedInt(json_obj['M-E_H_3-34']) #temp zone5 set
                                                dic['Extruder3_54'] = fixedInt(json_obj['M-E_H_3-35']) #temp zone5 act
                                                dic['Extruder3_55'] = fixedInt(json_obj['M-E_H_3-36']) #vaccumn set value
                                                dic['Extruder3_56'] = fixedInt(json_obj['M-E_H_3-37']) #vaccum act value
                                                dic['Extruder3_57'] = fixedInt(json_obj['M-E_H_3-38']) #wall thick spec
                                                dic['Extruder3_58'] = fixedInt(json_obj['M-E_H_3-39']) #wall thick act
                                                dic['Extruder3_59'] = fixedInt(json_obj['M-E_H_3-40']) #ecc set value
                                                dic['Extruder3_60'] = fixedInt(json_obj['M-E_H_3-41']) #ecc act value
                                                dic['Extruder3_61'] = fixedInt(json_obj['M-E_H_3-42']) #qa approval
                                                dic['Extruder3_1'] = fixedInt(json_obj['M-E_R_3-0']) #PIR
                                                dic['Extruder3_2'] = fixedInt(json_obj['M-E_R_3-1']) #OPERATOR NAME
                                                dic['Extruder3_3'] = fixedInt(json_obj['M-E_R_3-2']) #LINE RUN FEEDBACK
                                                dic['Extruder3_4'] = fixedInt(json_obj['M-E_R_3-3']) #OD SETPOINT
                                                dic['Extruder3_5'] = fixedInt(json_obj['M-E_R_3-4']) #OD ACTUAL
                                                dic['Extruder3_6'] = fixedInt(json_obj['M-E_R_3-5']) #ID SETPOINT
                                                dic['Extruder3_7'] = fixedInt(json_obj['M-E_R_3-6']) #ID ACTUAL
                                                dic['Extruder3_8'] = fixedInt(json_obj['M-E_R_3-7']) #THICKNESS SET
                                                dic['Extruder3_9'] = fixedInt(json_obj['M-E_R_3-8']) #THICKNESS ACT
                                                dic['Extruder3_10'] = fixedInt(json_obj['M-E_R_3-9'] )#EXTRUDER RPM SET
                                                dic['Extruder3_11'] = fixedInt(json_obj['M-E_R_3-10']) #EXTRUDER RPM ACT
                                                dic['Extruder3_12'] = fixedInt(json_obj['M-E_R_3-11']) #EXTRUDER CURRENT SET
                                                dic['Extruder3_13'] = fixedInt(json_obj['M-E_R_3-12']) #EXTRUDER CURRENT ACT
                                                dic['Extruder3_14'] = fixedInt(json_obj['M-E_R_3-13']) #EXTRUDER PRESSURE SET
                                                dic['Extruder3_15'] = fixedInt(json_obj['M-E_R_3-14']) #EXTRUDER PRESSURE ACT
                                                dic['Extruder3_16'] = fixedInt(json_obj['M-E_R_3-15']) #LINE MPM SET
                                                dic['Extruder3_17'] = fixedInt(json_obj['M-E_R_3-16']) #LINE MPM ACT
                                                dic['Extruder3_18'] = fixedInt(json_obj['M-E_R_3-17']) #PRODUCTION METER
                                                dic['Extruder3_19'] = fixedInt(json_obj['M-E_R_3-18']) #HEAD TEMP SETPOINT
                                                dic['Extruder3_20'] = fixedInt(json_obj['M-E_R_3-19']) #HEAD TEMP ACTUAL
                                                dic['Extruder3_21'] = fixedInt(json_obj['M-E_R_3-20']) #SCREW TEMP SETPOINT
                                                dic['Extruder3_22'] = fixedInt(json_obj['M-E_R_3-21']) #SCREW TEMP ACTUAL
                                                dic['Extruder3_23'] = fixedInt(json_obj['M-E_R_3-22']) #ZONE2 TEMP SETPOINT
                                                dic['Extruder3_24'] = fixedInt(json_obj['M-E_R_3-23']) #ZONE2 TEMP ACTUAL
                                                dic['Extruder3_25'] = fixedInt(json_obj['M-E_R_3-24']) #ZONE3 TEMP SETPOINT
                                                dic['Extruder3_26'] = fixedInt(json_obj['M-E_R_3-25']) #ZONE3 TEMP ACTUAL
                                                
                                                dic['Vulcanizer1_1'] = fixedInt(json_obj['M-V_R_1-0']) #PIR
                                                dic['Vulcanizer1_2'] = fixedInt(json_obj['M-V_R_1-1']) #OPERATOR NAME
                                                dic['Vulcanizer1_3'] = fixedInt(json_obj['M-V_R_1-2']) #PROGRAM NAME
                                                dic['Vulcanizer1_4'] = fixedInt(json_obj['M-V_R_1-3']) #RAMPUP1_SETPOINT TEMP // Curing Set Point
                                                dic['Vulcanizer1_5'] = fixedInt(json_obj['M-V_R_1-4']) #CURING1_SETPOINT TEMP
                                                dic['Vulcanizer1_6'] = fixedInt(json_obj['M-V_R_1-5']) #RAMPUP2 SETPOINT TEMP
                                                dic['Vulcanizer1_7'] = fixedInt(json_obj['M-V_R_1-6']) #CURING2 SETPOINT TEMP
                                                dic['Vulcanizer1_8'] = fixedInt(json_obj['M-V_R_1-7']) #ACTUAL TEMPERATURE // Curing Temp
                                                dic['Vulcanizer1_9'] = fixedInt(json_obj['M-V_R_1-8']) #ACTUAL PRESSURE
                                                dic['Vulcanizer1_10'] = fixedInt(json_obj['M-V_R_1-9'] )#ACTUAL RAPUP1 TIME IN MIN
                                                dic['Vulcanizer1_11'] = fixedInt(json_obj['M-V_R_1-10']) #ACTUAL CURING1 TIME IN MIN
                                                dic['Vulcanizer1_12'] = fixedInt(json_obj['M-V_R_1-11']) #ACTUAL RAPUP2 TIME IN MIN
                                                dic['Vulcanizer1_13'] = fixedInt(json_obj['M-V_R_1-12']) #ACTUAL CURING2 TIME IN MIN
                                                
                                                dic['Testing1_1'] = fixedInt(json_obj['M-T_R_1-0']) #PIR
                                                dic['Testing1_2'] = fixedInt(json_obj['M-T_R_1-1']) #OPERATOR NAME
                                                dic['Testing1_3'] = fixedInt(json_obj['M-T_R_1-2']) #TEST ID
                                                dic['Testing1_4'] = fixedInt(json_obj['M-T_R_1-3']) #HOSE DIAMETER
                                                dic['Testing1_5'] = fixedInt(json_obj['M-T_R_1-4']) #SET TEST PRESSURE // Testing pres spec
                                                dic['Testing1_6'] = fixedInt(json_obj['M-T_R_1-5']) #ACTUAL TEST PRESSURE
                                                dic['Testing1_7'] = fixedInt(json_obj['M-T_R_1-6']) #SET EXTRACTION PRESSURE
                                                dic['Testing1_8'] = fixedInt(json_obj['M-T_R_1-7']) #ACTUAL EXTRACTION PRESSURE
                                                dic['Testing1_9'] = fixedInt(json_obj['M-T_R_1-8']) #TEST PRESSURE TIME
                                                dic['Testing1_10'] = fixedInt(json_obj['M-T_R_1-9'] )#TEST HOSE FROM
                                                dic['Testing1_11'] = fixedInt(json_obj['M-T_R_1-10']) #TEST HOSE TO
                                                dic['Testing1_12'] = fixedInt(json_obj['M-T_R_1-11']) #TEST RESULT PASS
                                                dic['Testing1_13'] = fixedInt(json_obj['M-T_R_1-12']) #TEST RESULT FAIL
                                                
                                                dic['Testing2_1'] = fixedInt(json_obj['M-T_R_2-0']) #PIR
                                                dic['Testing2_2'] = fixedInt(json_obj['M-T_R_2-1']) #OPERATOR NAME
                                                dic['Testing2_3'] = fixedInt(json_obj['M-T_R_2-2']) #TEST ID
                                                dic['Testing2_4'] = fixedInt(json_obj['M-T_R_2-3']) #HOSE DIAMETER
                                                dic['Testing2_5'] = fixedInt(json_obj['M-T_R_2-4']) #SET TEST PRESSURE
                                                dic['Testing2_6'] = fixedInt(json_obj['M-T_R_2-5']) #ACTUAL TEST PRESSURE
                                                dic['Testing2_7'] = fixedInt(json_obj['M-T_R_2-6']) #SET EXTRACTION PRESSURE
                                                dic['Testing2_8'] = fixedInt(json_obj['M-T_R_2-7']) #ACTUAL EXTRACTION PRESSURE
                                                dic['Testing2_9'] = fixedInt(json_obj['M-T_R_2-8']) #TEST PRESSURE TIME
                                                dic['Testing2_10'] = fixedInt(json_obj['M-T_R_2-9'] )#TEST HOSE FROM
                                                dic['Testing2_11'] = fixedInt(json_obj['M-T_R_2-10']) #TEST HOSE TO
                                                dic['Testing2_12'] = fixedInt(json_obj['M-T_R_2-11']) #TEST RESULT PASS
                                                dic['Testing2_13'] = fixedInt(json_obj['M-T_R_2-12']) #TEST RESULT FAIL
                                                
                                                dic['Testing3_1'] = fixedInt(json_obj['M-T_R_3-0']) #PIR
                                                dic['Testing3_2'] = fixedInt(json_obj['M-T_R_3-1']) #OPERATOR NAME
                                                dic['Testing3_3'] = fixedInt(json_obj['M-T_R_3-2']) #TEST ID
                                                dic['Testing3_4'] = fixedInt(json_obj['M-T_R_3-3']) #HOSE DIAMETER
                                                dic['Testing3_5'] = fixedInt(json_obj['M-T_R_3-4']) #SET TEST PRESSURE
                                                dic['Testing3_6'] = fixedInt(json_obj['M-T_R_3-5']) #ACTUAL TEST PRESSURE
                                                dic['Testing3_7'] = fixedInt(json_obj['M-T_R_3-6']) #SET EXTRACTION PRESSURE
                                                dic['Testing3_8'] = fixedInt(json_obj['M-T_R_3-7']) #ACTUAL EXTRACTION PRESSURE
                                                dic['Testing3_9'] = fixedInt(json_obj['M-T_R_3-8']) #TEST PRESSURE TIME
                                                dic['Testing3_10'] = fixedInt(json_obj['M-T_R_3-9'] )#TEST HOSE FROM
                                                dic['Testing3_11'] = fixedInt(json_obj['M-T_R_3-10']) #TEST HOSE TO
                                                dic['Testing3_12'] = fixedInt(json_obj['M-T_R_3-11']) #TEST RESULT PASS
                                                dic['Testing3_13'] = fixedInt(json_obj['M-T_R_3-12']) #TEST RESULT FAIL
                                                
                                                dic['ManPims1_1'] = fixedInt(json_obj['M-M_P_1-0']) #DRUM IN
                                                dic['ManPims1_2'] = fixedInt(json_obj['M-M_P_1-1']) #DRUM OUT
                                                
                                                dic['ManPims2_1'] = fixedInt(json_obj['M-M_P_2-0']) #DRUM IN
                                                dic['ManPims2_2'] = fixedInt(json_obj['M-M_P_2-1']) #DRUM OUT
                                                '''
                                                dic['ManPims3_1'] = json_obj['tags']['M-M_P_3-0'] #DRUM IN
                                                dic['ManPims3_2'] = json_obj['tags']['M-M_P_3-1'] #DRUM OUT
                                                '''
                                                # Extruder PIMS1 Tags
                                                '''
                                                dic['ExtPims1_1'] = fixedInt(json_obj['M-E_P_1-0']) #drum in
                                                dic['ExtPims1_2'] = fixedInt(json_obj['M-E_P_1-1']) #drum out
                                                dic['ExtPims1_3'] = fixedInt(json_obj['M-E_P_1-2']) #RED TAPE METER 3
                                                dic['ExtPims1_4'] = fixedInt(json_obj['M-E_P_1-3']) #RED TAPE METER 4
                                                dic['ExtPims1_5'] = fixedInt(json_obj['M-E_P_1-4']) #RED TAPE METER 5
                                                dic['ExtPims1_6'] = fixedInt(json_obj['M-E_P_1-5']) #RED TAPE METER 6
                                                dic['ExtPims1_7'] = fixedInt(json_obj['M-E_P_1-6']) #RED TAPE METER 7
                                                dic['ExtPims1_8'] = fixedInt(json_obj['M-E_P_1-7']) #RED TAPE METER 8
                                                dic['ExtPims1_9'] = fixedInt(json_obj['M-E_P_1-8']) #RED TAPE METER 9
                                                dic['ExtPims1_10'] = fixedInt(json_obj['M-E_P_1-9'] )#RED TAPE METER 10
                                                dic['ExtPims1_11'] = fixedInt(json_obj['M-E_P_1-10']) #RED TAPE METER 11
                                                dic['ExtPims1_12'] = fixedInt(json_obj['M-E_P_1-11']) #RED TAPE METER 12
                                                dic['ExtPims1_13'] = fixedInt(json_obj['M-E_P_1-12']) #RED TAPE METER 13
                                                dic['ExtPims1_14'] = fixedInt(json_obj['M-E_P_1-13']) #RED TAPE METER 14
                                                dic['ExtPims1_15'] = fixedInt(json_obj['M-E_P_1-14']) #RED TAPE METER 15
                                                dic['ExtPims1_16'] = fixedInt(json_obj['M-E_P_1-15']) #RED TAPE METER 16
                                                dic['ExtPims1_17'] = fixedInt(json_obj['M-E_P_1-16']) #RED TAPE METER 15
                                                dic['ExtPims1_18'] = fixedInt(json_obj['M-E_P_1-17']) #RED TAPE METER 16
                                                dic['ExtPims1_19'] = fixedInt(json_obj['M-E_P_1-18']) #RED TAPE METER 17
                                                dic['ExtPims1_20'] = fixedInt(json_obj['M-E_P_1-19']) #RED TAPE METER 18
                                                dic['ExtPims1_21'] = fixedInt(json_obj['M-E_P_1-20']) #RED TAPE METER 19
                                                dic['ExtPims1_22'] = fixedInt(json_obj['M-E_P_1-21']) #RED TAPE METER 20
                                                dic['ExtPims1_23'] = fixedInt(json_obj['M-E_P_1-22']) #RED TAPE METER 21
                                                dic['ExtPims1_24'] = fixedInt(json_obj['M-E_P_1-23']) #RED TAPE METER 22
                                                dic['ExtPims1_25'] = fixedInt(json_obj['M-E_P_1-24']) #RED TAPE METER 23
                                                dic['ExtPims1_26'] = fixedInt(json_obj['M-E_P_1-25']) #RED TAPE METER 24
                                                dic['ExtPims1_27'] = fixedInt(json_obj['M-E_P_1-26']) #RED TAPE METER 25
                                                dic['ExtPims1_28'] = fixedInt(json_obj['M-E_P_1-27']) #RED TAPE METER 26
                                                dic['ExtPims1_29'] = fixedInt(json_obj['M-E_P_1-28']) #RED TAPE METER 27
                                                dic['ExtPims1_30'] = fixedInt(json_obj['M-E_P_1-29']) #RED TAPE METER 28
                                                dic['ExtPims1_31'] = fixedInt(json_obj['M-E_P_1-30']) #RED TAPE METER 29
                                                dic['ExtPims1_32'] = fixedInt(json_obj['M-E_P_1-31'])#RED TAPE METER 30
                                                dic['ExtPims1_33'] = fixedInt(json_obj['M-E_P_1-32']) #RED TAPE METER 31
                                                dic['ExtPims1_34'] = fixedInt(json_obj['M-E_P_1-33']) #RED TAPE METER 32
                                                dic['ExtPims1_35'] = fixedInt(json_obj['M-E_P_1-34']) #RED TAPE METER 33
                                                dic['ExtPims1_36'] = fixedInt(json_obj['M-E_P_1-35']) #RED TAPE METER 34
                                                dic['ExtPims1_37'] = fixedInt(json_obj['M-E_P_1-36']) #RED TAPE METER 35
                                                dic['ExtPims1_38'] = fixedInt(json_obj['M-E_P_1-37']) #RED TAPE METER 36
                                                dic['ExtPims1_39'] = fixedInt(json_obj['M-E_P_1-38']) #RED TAPE METER 37
                                                dic['ExtPims1_40'] = fixedInt(json_obj['M-E_P_1-39']) #RED TAPE METER 38
                                                dic['ExtPims1_41'] = fixedInt(json_obj['M-E_P_1-40']) #RED TAPE METER 39
                                                dic['ExtPims1_42'] = fixedInt(json_obj['M-E_P_1-41']) #RED TAPE METER 40
                                                dic['ExtPims1_43'] = fixedInt(json_obj['M-E_P_1-42']) #RED TAPE METER 41
                                                dic['ExtPims1_44'] = fixedInt(json_obj['M-E_P_1-43']) #RED TAPE METER 42
                                                dic['ExtPims1_45'] = fixedInt(json_obj['M-E_P_1-44']) #RED TAPE METER 43
                                                dic['ExtPims1_46'] = fixedInt(json_obj['M-E_P_1-45']) #RED TAPE METER 44
                                                dic['ExtPims1_47'] = fixedInt(json_obj['M-E_P_1-46']) #RED TAPE METER 45
                                                dic['ExtPims1_48'] = fixedInt(json_obj['M-E_P_1-47']) #RED TAPE METER 46
                                                dic['ExtPims1_49'] = fixedInt(json_obj['M-E_P_1-48']) #RED TAPE METER 47
                                                dic['ExtPims1_50'] = fixedInt(json_obj['M-E_P_1-49']) #RED TAPE METER 48
                                                dic['ExtPims1_51'] = fixedInt(json_obj['M-E_P_1-50']) #RED TAPE METER 49
                                                dic['ExtPims1_52'] = fixedInt(json_obj['M-E_P_1-51']) #RED TAPE METER 50
                                                dic['ExtPims1_53'] = fixedInt(json_obj['M-E_P_1-52']) #RED TAPE METER 51
                                                dic['ExtPims1_54'] = fixedInt(json_obj['M-E_P_1-53']) #RED TAPE METER 52
                                                dic['ExtPims1_55'] = fixedInt(json_obj['M-E_P_1-54']) #RED TAPE METER 53
                                                dic['ExtPims1_56'] = fixedInt(json_obj['M-E_P_1-55']) #RED TAPE METER 54
                                                dic['ExtPims1_57'] = fixedInt(json_obj['M-E_P_1-56']) #RED TAPE METER 55
                                                dic['ExtPims1_58'] = fixedInt(json_obj['M-E_P_1-57']) #RED TAPE METER 56
                                                dic['ExtPims1_59'] = fixedInt(json_obj['M-E_P_1-58']) #RED TAPE METER 57
                                                dic['ExtPims1_60'] = fixedInt(json_obj['M-E_P_1-59']) #RED TAPE METER 58
                                                dic['ExtPims1_61'] = fixedInt(json_obj['M-E_P_1-60']) #RED TAPE METER 59
                                                dic['ExtPims1_62'] = fixedInt(json_obj['M-E_P_1-61']) #RED TAPE METER 60
                                                dic['ExtPims1_63'] = fixedInt(json_obj['M-E_P_1-62']) #RED TAPE METER 61
                                                dic['ExtPims1_64'] = fixedInt(json_obj['M-E_P_1-63']) #RED TAPE METER 62
                                                dic['ExtPims1_65'] = fixedInt(json_obj['M-E_P_1-64']) #RED TAPE METER 63
                                                dic['ExtPims1_66'] = fixedInt(json_obj['M-E_P_1-65']) #RED TAPE METER 64
                                                dic['ExtPims1_67'] = fixedInt(json_obj['M-E_P_1-66']) #RED TAPE METER 65
                                                dic['ExtPims1_68'] = fixedInt(json_obj['M-E_P_1-67'])#RED TAPE METER 66
                                                dic['ExtPims1_69'] = fixedInt(json_obj['M-E_P_1-68']) #RED TAPE METER 67
                                                dic['ExtPims1_70'] = fixedInt(json_obj['M-E_P_1-69']) #RED TAPE METER 68
                                                dic['ExtPims1_71'] = fixedInt(json_obj['M-E_P_1-70']) #RED TAPE METER 69
                                                dic['ExtPims1_72'] = fixedInt(json_obj['M-E_P_1-71']) #RED TAPE METER 70
                                                dic['ExtPims1_73'] = fixedInt(json_obj['M-E_P_1-72']) #RED TAPE METER 71
                                                dic['ExtPims1_74'] = fixedInt(json_obj['M-E_P_1-73']) #RED TAPE METER 72
                                                dic['ExtPims1_75'] = fixedInt(json_obj['M-E_P_1-74']) #RED TAPE METER 73
                                                dic['ExtPims1_76'] = fixedInt(json_obj['M-E_P_1-75']) #RED TAPE METER 74
                                                dic['ExtPims1_77'] = fixedInt(json_obj['M-E_P_1-76']) #RED TAPE METER 75
                                                dic['ExtPims1_78'] = fixedInt(json_obj['M-E_P_1-77']) #RED TAPE METER 76
                                                dic['ExtPims1_79'] = fixedInt(json_obj['M-E_P_1-78']) #RED TAPE METER 77
                                                dic['ExtPims1_80'] = fixedInt(json_obj['M-E_P_1-79']) #RED TAPE METER 78
                                                dic['ExtPims1_81'] = fixedInt(json_obj['M-E_P_1-80']) #DRUM IN
                                                dic['ExtPims1_82'] = fixedInt(json_obj['M-E_P_1-81']) #DRUM OUT
                                                
                                                dic['ExtPims3_1'] = fixedInt(json_obj['M-E_P_3-0']) #drum in
                                                dic['ExtPims3_2'] = fixedInt(json_obj['M-E_P_3-1']) #drum out
                                                dic['ExtPims3_3'] = fixedInt(json_obj['M-E_P_3-2']) #RED TAPE METER 3
                                                dic['ExtPims3_4'] = fixedInt(json_obj['M-E_P_3-3']) #RED TAPE METER 4
                                                dic['ExtPims3_5'] = fixedInt(json_obj['M-E_P_3-4']) #RED TAPE METER 5
                                                dic['ExtPims3_6'] = fixedInt(json_obj['M-E_P_3-5']) #RED TAPE METER 6
                                                dic['ExtPims3_7'] = fixedInt(json_obj['M-E_P_3-6']) #RED TAPE METER 7
                                                dic['ExtPims3_8'] = fixedInt(json_obj['M-E_P_3-7']) #RED TAPE METER 8
                                                dic['ExtPims3_9'] = fixedInt(json_obj['M-E_P_3-8']) #RED TAPE METER 9
                                                dic['ExtPims3_10'] = fixedInt(json_obj['M-E_P_3-9'] )#RED TAPE METER 10
                                                dic['ExtPims3_11'] = fixedInt(json_obj['M-E_P_3-10']) #RED TAPE METER 11
                                                dic['ExtPims3_12'] = fixedInt(json_obj['M-E_P_3-11']) #RED TAPE METER 12
                                                dic['ExtPims3_13'] = fixedInt(json_obj['M-E_P_3-12']) #RED TAPE METER 13
                                                dic['ExtPims3_14'] = fixedInt(json_obj['M-E_P_3-13']) #RED TAPE METER 14
                                                dic['ExtPims3_15'] = fixedInt(json_obj['M-E_P_3-14']) #RED TAPE METER 15
                                                dic['ExtPims3_16'] = fixedInt(json_obj['M-E_P_3-15']) #RED TAPE METER 16
                                                dic['ExtPims3_17'] = fixedInt(json_obj['M-E_P_3-16']) #RED TAPE METER 15
                                                dic['ExtPims3_18'] = fixedInt(json_obj['M-E_P_3-17']) #RED TAPE METER 16
                                                dic['ExtPims3_19'] = fixedInt(json_obj['M-E_P_3-18']) #RED TAPE METER 17
                                                dic['ExtPims3_20'] = fixedInt(json_obj['M-E_P_3-19']) #RED TAPE METER 18
                                                dic['ExtPims3_21'] = fixedInt(json_obj['M-E_P_3-20']) #RED TAPE METER 19
                                                dic['ExtPims3_22'] = fixedInt(json_obj['M-E_P_3-21']) #RED TAPE METER 20
                                                dic['ExtPims3_23'] = fixedInt(json_obj['M-E_P_3-22']) #RED TAPE METER 21
                                                dic['ExtPims3_24'] = fixedInt(json_obj['M-E_P_3-23']) #RED TAPE METER 22
                                                dic['ExtPims3_25'] = fixedInt(json_obj['M-E_P_3-24']) #RED TAPE METER 23
                                                dic['ExtPims3_26'] = fixedInt(json_obj['M-E_P_3-25']) #RED TAPE METER 24
                                                dic['ExtPims3_27'] = fixedInt(json_obj['M-E_P_3-26']) #RED TAPE METER 25
                                                dic['ExtPims3_28'] = fixedInt(json_obj['M-E_P_3-27']) #RED TAPE METER 26
                                                dic['ExtPims3_29'] = fixedInt(json_obj['M-E_P_3-28']) #RED TAPE METER 27
                                                dic['ExtPims3_30'] = fixedInt(json_obj['M-E_P_3-29']) #RED TAPE METER 28
                                                dic['ExtPims3_31'] = fixedInt(json_obj['M-E_P_3-30']) #RED TAPE METER 29
                                                dic['ExtPims3_32'] = fixedInt(json_obj['M-E_P_3-31'])#RED TAPE METER 30
                                                dic['ExtPims3_33'] = fixedInt(json_obj['M-E_P_3-32']) #RED TAPE METER 31
                                                dic['ExtPims3_34'] = fixedInt(json_obj['M-E_P_3-33']) #RED TAPE METER 32
                                                dic['ExtPims3_35'] = fixedInt(json_obj['M-E_P_3-34']) #RED TAPE METER 33
                                                dic['ExtPims3_36'] = fixedInt(json_obj['M-E_P_3-35']) #RED TAPE METER 34
                                                dic['ExtPims3_37'] = fixedInt(json_obj['M-E_P_3-36']) #RED TAPE METER 35
                                                dic['ExtPims3_38'] = fixedInt(json_obj['M-E_P_3-37']) #RED TAPE METER 36
                                                dic['ExtPims3_39'] = fixedInt(json_obj['M-E_P_3-38']) #RED TAPE METER 37
                                                dic['ExtPims3_40'] = fixedInt(json_obj['M-E_P_3-39']) #RED TAPE METER 38
                                                dic['ExtPims3_41'] = fixedInt(json_obj['M-E_P_3-40']) #RED TAPE METER 39
                                                dic['ExtPims3_42'] = fixedInt(json_obj['M-E_P_3-41']) #RED TAPE METER 40
                                                dic['ExtPims3_43'] = fixedInt(json_obj['M-E_P_3-42']) #RED TAPE METER 41
                                                dic['ExtPims3_44'] = fixedInt(json_obj['M-E_P_3-43']) #RED TAPE METER 42
                                                dic['ExtPims3_45'] = fixedInt(json_obj['M-E_P_3-44']) #RED TAPE METER 43
                                                dic['ExtPims3_46'] = fixedInt(json_obj['M-E_P_3-45']) #RED TAPE METER 44
                                                dic['ExtPims3_47'] = fixedInt(json_obj['M-E_P_3-46']) #RED TAPE METER 45
                                                dic['ExtPims3_48'] = fixedInt(json_obj['M-E_P_3-47']) #RED TAPE METER 46
                                                dic['ExtPims3_49'] = fixedInt(json_obj['M-E_P_3-48']) #RED TAPE METER 47
                                                dic['ExtPims3_50'] = fixedInt(json_obj['M-E_P_3-49']) #RED TAPE METER 48
                                                dic['ExtPims3_51'] = fixedInt(json_obj['M-E_P_3-50']) #RED TAPE METER 49
                                                dic['ExtPims3_52'] = fixedInt(json_obj['M-E_P_3-51']) #RED TAPE METER 50
                                                dic['ExtPims3_53'] = fixedInt(json_obj['M-E_P_3-52']) #RED TAPE METER 51
                                                dic['ExtPims3_54'] = fixedInt(json_obj['M-E_P_3-53']) #RED TAPE METER 52
                                                dic['ExtPims3_55'] = fixedInt(json_obj['M-E_P_3-54']) #RED TAPE METER 53
                                                dic['ExtPims3_56'] = fixedInt(json_obj['M-E_P_3-55']) #RED TAPE METER 54
                                                dic['ExtPims3_57'] = fixedInt(json_obj['M-E_P_3-56']) #RED TAPE METER 55
                                                dic['ExtPims3_58'] = fixedInt(json_obj['M-E_P_3-57']) #RED TAPE METER 56
                                                dic['ExtPims3_59'] = fixedInt(json_obj['M-E_P_3-58']) #RED TAPE METER 57
                                                dic['ExtPims3_60'] = fixedInt(json_obj['M-E_P_3-59']) #RED TAPE METER 58
                                                dic['ExtPims3_61'] = fixedInt(json_obj['M-E_P_3-60']) #RED TAPE METER 59
                                                dic['ExtPims3_62'] = fixedInt(json_obj['M-E_P_3-61']) #RED TAPE METER 60
                                                dic['ExtPims3_63'] = fixedInt(json_obj['M-E_P_3-62']) #RED TAPE METER 61
                                                dic['ExtPims3_64'] = fixedInt(json_obj['M-E_P_3-63']) #RED TAPE METER 62
                                                dic['ExtPims3_65'] = fixedInt(json_obj['M-E_P_3-64']) #RED TAPE METER 63
                                                dic['ExtPims3_66'] = fixedInt(json_obj['M-E_P_3-65']) #RED TAPE METER 64
                                                dic['ExtPims3_67'] = fixedInt(json_obj['M-E_P_3-66']) #RED TAPE METER 65
                                                dic['ExtPims3_68'] = fixedInt(json_obj['M-E_P_3-67']) #RED TAPE METER 66
                                                dic['ExtPims3_69'] = fixedInt(json_obj['M-E_P_3-68']) #RED TAPE METER 67
                                                dic['ExtPims3_70'] = fixedInt(json_obj['M-E_P_3-69']) #RED TAPE METER 68
                                                dic['ExtPims3_71'] = fixedInt(json_obj['M-E_P_3-70']) #RED TAPE METER 69
                                                dic['ExtPims3_72'] = fixedInt(json_obj['M-E_P_3-71']) #RED TAPE METER 70
                                                dic['ExtPims3_73'] = fixedInt(json_obj['M-E_P_3-72']) #RED TAPE METER 71
                                                dic['ExtPims3_74'] = fixedInt(json_obj['M-E_P_3-73']) #RED TAPE METER 72
                                                dic['ExtPims3_75'] = fixedInt(json_obj['M-E_P_3-74']) #RED TAPE METER 73
                                                dic['ExtPims3_76'] = fixedInt(json_obj['M-E_P_3-75']) #RED TAPE METER 74
                                                dic['ExtPims3_77'] = fixedInt(json_obj['M-E_P_3-76']) #RED TAPE METER 75
                                                dic['ExtPims3_78'] = fixedInt(json_obj['M-E_P_3-77']) #RED TAPE METER 76
                                                dic['ExtPims3_79'] = fixedInt(json_obj['M-E_P_3-78']) #RED TAPE METER 77
                                                dic['ExtPims3_80'] = fixedInt(json_obj['M-E_P_3-79']) #RED TAPE METER 78
                                                dic['ExtPims3_81'] = fixedInt(json_obj['M-E_P_3-80']) #DRUM IN
                                                dic['ExtPims3_82'] = fixedInt(json_obj['M-E_P_3-81']) #DRUM OUT
                                                dic['VulPims1_1'] = fixedInt(json_obj['M-V_P_1-0']) #DRUM IN
                                                dic['VulPims1_2'] = fixedInt(json_obj['M-V_P_1-1']) #DRUM OUT
                                                '''
                                                #Testing PIMS Tags
                                                '''
                                                dic['TestPims1_1'] = fixedInt(json_obj['M-T_P_1-0']) #DRUM IN
                                                dic['TestPims1_2'] = fixedInt(json_obj['M-T_P_1-1']) #DRUM OUT
                                                dic['TestPims1_3'] = fixedInt(json_obj['M-T_P_1-2']) #RED TAPE METER 1
                                                dic['TestPims1_4'] = fixedInt(json_obj['M-T_P_1-3']) #RED TAPE METER 2
                                                dic['TestPims1_5'] = fixedInt(json_obj['M-T_P_1-4']) #RED TAPE METER 3
                                                dic['TestPims1_6'] = fixedInt(json_obj['M-T_P_1-5']) #RED TAPE METER 4
                                                dic['TestPims1_7'] = fixedInt(json_obj['M-T_P_1-6']) #RED TAPE METER 5
                                                dic['TestPims1_8'] = fixedInt(json_obj['M-T_P_1-7']) #RED TAPE METER 6
                                                dic['TestPims1_9'] = fixedInt(json_obj['M-T_P_1-8']) #RED TAPE METER 7
                                                dic['TestPims1_10'] = fixedInt(json_obj['M-T_P_1-9'] )#RED TAPE METER 8
                                                dic['TestPims1_11'] = fixedInt(json_obj['M-T_P_1-10']) #RED TAPE METER 9
                                                dic['TestPims1_12'] = fixedInt(json_obj['M-T_P_1-11']) #RED TAPE METER 10
                                                dic['TestPims1_13'] = fixedInt(json_obj['M-T_P_1-12']) #RED TAPE METER 11
                                                dic['TestPims1_14'] = fixedInt(json_obj['M-T_P_1-13']) #RED TAPE METER 12
                                                dic['TestPims1_15'] = fixedInt(json_obj['M-T_P_1-14']) #RED TAPE METER 13
                                                dic['TestPims1_16'] = fixedInt(json_obj['M-T_P_1-15'])#RED TAPE METER 14
                                                dic['TestPims1_17'] = fixedInt(json_obj['M-T_P_1-16']) #RED TAPE METER 15
                                                dic['TestPims1_18'] = fixedInt(json_obj['M-T_P_1-17']) #RED TAPE METER 16
                                                dic['TestPims1_19'] = fixedInt(json_obj['M-T_P_1-18']) #RED TAPE METER 17
                                                dic['TestPims1_20'] = fixedInt(json_obj['M-T_P_1-19']) #RED TAPE METER 18
                                                dic['TestPims1_21'] = fixedInt(json_obj['M-T_P_1-20']) #RED TAPE METER 19
                                                dic['TestPims1_22'] = fixedInt(json_obj['M-T_P_1-21']) #RED TAPE METER 20
                                                dic['TestPims1_23'] = fixedInt(json_obj['M-T_P_1-22']) #RED TAPE METER 21
                                                dic['TestPims1_24'] = fixedInt(json_obj['M-T_P_1-23']) #RED TAPE METER 22
                                                dic['TestPims1_25'] = fixedInt(json_obj['M-T_P_1-24']) #RED TAPE METER 23
                                                dic['TestPims1_26'] = fixedInt(json_obj['M-T_P_1-25']) #RED TAPE METER 24
                                                dic['TestPims1_27'] = fixedInt(json_obj['M-T_P_1-26']) #RED TAPE METER 25
                                                dic['TestPims1_28'] = fixedInt(json_obj['M-T_P_1-27']) #RED TAPE METER 26
                                                dic['TestPims1_29'] = fixedInt(json_obj['M-T_P_1-28']) #RED TAPE METER 27
                                                dic['TestPims1_30'] = fixedInt(json_obj['M-T_P_1-29']) #RED TAPE METER 28
                                                dic['TestPims1_31'] = fixedInt(json_obj['M-T_P_1-30']) #RED TAPE METER 29
                                                dic['TestPims1_32'] = fixedInt(json_obj['M-T_P_1-31'])#RED TAPE METER 30
                                                dic['TestPims1_33'] = fixedInt(json_obj['M-T_P_1-32']) #RED TAPE METER 31
                                                dic['TestPims1_34'] = fixedInt(json_obj['M-T_P_1-33']) #RED TAPE METER 32
                                                dic['TestPims1_35'] = fixedInt(json_obj['M-T_P_1-34']) #RED TAPE METER 33
                                                dic['TestPims1_36'] = fixedInt(json_obj['M-T_P_1-35']) #RED TAPE METER 34
                                                dic['TestPims1_37'] = fixedInt(json_obj['M-T_P_1-36']) #RED TAPE METER 35
                                                dic['TestPims1_38'] = fixedInt(json_obj['M-T_P_1-37']) #RED TAPE METER 36
                                                dic['TestPims1_39'] = fixedInt(json_obj['M-T_P_1-38']) #RED TAPE METER 37
                                                dic['TestPims1_40'] = fixedInt(json_obj['M-T_P_1-39']) #RED TAPE METER 38
                                                dic['TestPims1_41'] = fixedInt(json_obj['M-T_P_1-40']) #RED TAPE METER 39
                                                dic['TestPims1_42'] = fixedInt(json_obj['M-T_P_1-41']) #RED TAPE METER 40
                                                dic['TestPims1_43'] = fixedInt(json_obj['M-T_P_1-42']) #RED TAPE METER 41
                                                dic['TestPims1_44'] = fixedInt(json_obj['M-T_P_1-43']) #RED TAPE METER 42
                                                dic['TestPims1_45'] = fixedInt(json_obj['M-T_P_1-44']) #RED TAPE METER 43
                                                dic['TestPims1_46'] = fixedInt(json_obj['M-T_P_1-45']) #RED TAPE METER 44
                                                dic['TestPims1_47'] = fixedInt(json_obj['M-T_P_1-46']) #RED TAPE METER 45
                                                dic['TestPims1_48'] = fixedInt(json_obj['M-T_P_1-47']) #RED TAPE METER 46
                                                dic['TestPims1_49'] = fixedInt(json_obj['M-T_P_1-48']) #RED TAPE METER 47
                                                dic['TestPims1_50'] = fixedInt(json_obj['M-T_P_1-49']) #RED TAPE METER 48
                                                dic['TestPims1_51'] = fixedInt(json_obj['M-T_P_1-50']) #RED TAPE METER 49
                                                dic['TestPims1_52'] = fixedInt(json_obj['M-T_P_1-51'])#RED TAPE METER 50
                                                dic['TestPims1_53'] = fixedInt(json_obj['M-T_P_1-52']) #RED TAPE METER 51
                                                dic['TestPims1_54'] = fixedInt(json_obj['M-T_P_1-53']) #RED TAPE METER 52
                                                dic['TestPims1_55'] = fixedInt(json_obj['M-T_P_1-54']) #RED TAPE METER 53
                                                dic['TestPims1_56'] = fixedInt(json_obj['M-T_P_1-55']) #RED TAPE METER 54
                                                dic['TestPims1_57'] = fixedInt(json_obj['M-T_P_1-56']) #RED TAPE METER 55
                                                dic['TestPims1_58'] = fixedInt(json_obj['M-T_P_1-57']) #RED TAPE METER 56
                                                dic['TestPims1_59'] = fixedInt(json_obj['M-T_P_1-58']) #RED TAPE METER 57
                                                dic['TestPims1_60'] = fixedInt(json_obj['M-T_P_1-59']) #RED TAPE METER 58
                                                dic['TestPims1_61'] = fixedInt(json_obj['M-T_P_1-60']) #RED TAPE METER 59
                                                dic['TestPims1_62'] = fixedInt(json_obj['M-T_P_1-61']) #RED TAPE METER 60
                                                dic['TestPims1_63'] = fixedInt(json_obj['M-T_P_1-62']) #RED TAPE METER 61
                                                dic['TestPims1_64'] = fixedInt(json_obj['M-T_P_1-63']) #RED TAPE METER 62
                                                dic['TestPims1_65'] = fixedInt(json_obj['M-T_P_1-64']) #RED TAPE METER 63
                                                dic['TestPims1_66'] = fixedInt(json_obj['M-T_P_1-65']) #RED TAPE METER 64
                                                dic['TestPims1_67'] = fixedInt(json_obj['M-T_P_1-66']) #RED TAPE METER 65
                                                dic['TestPims1_68'] = fixedInt(json_obj['M-T_P_1-67'])#RED TAPE METER 66
                                                dic['TestPims1_69'] = fixedInt(json_obj['M-T_P_1-68']) #RED TAPE METER 67
                                                dic['TestPims1_70'] = fixedInt(json_obj['M-T_P_1-69']) #RED TAPE METER 68
                                                dic['TestPims1_71'] = fixedInt(json_obj['M-T_P_1-70']) #RED TAPE METER 69
                                                dic['TestPims1_72'] = fixedInt(json_obj['M-T_P_1-71']) #RED TAPE METER 70
                                                dic['TestPims1_73'] = fixedInt(json_obj['M-T_P_1-72']) #RED TAPE METER 71
                                                dic['TestPims1_74'] = fixedInt(json_obj['M-T_P_1-73']) #RED TAPE METER 72
                                                dic['TestPims1_75'] = fixedInt(json_obj['M-T_P_1-74']) #RED TAPE METER 73
                                                dic['TestPims1_76'] = fixedInt(json_obj['M-T_P_1-75']) #RED TAPE METER 74
                                                dic['TestPims1_77'] = fixedInt(json_obj['M-T_P_1-76']) #RED TAPE METER 75
                                                dic['TestPims1_78'] = fixedInt(json_obj['M-T_P_1-77']) #RED TAPE METER 76
                                                dic['TestPims1_79'] = fixedInt(json_obj['M-T_P_1-78']) #RED TAPE METER 77
                                                dic['TestPims1_80'] = fixedInt(json_obj['M-T_P_1-79']) #RED TAPE METER 78
                                                dic['TestPims1_81'] = fixedInt(json_obj['M-T_P_1-80']) #RED TAPE METER 79
                                                dic['TestPims1_82'] = fixedInt(json_obj['M-T_P_1-81']) #RED TAPE METER 80
                                                
                                                dic['TestPims2_1'] = fixedInt(json_obj['M-T_P_2-0']) #DRUM IN
                                                dic['TestPims2_2'] = fixedInt(json_obj['M-T_P_2-1']) #DRUM OUT
                                                dic['TestPims2_3'] = fixedInt(json_obj['M-T_P_2-2']) #RED TAPE METER 1
                                                dic['TestPims2_4'] = fixedInt(json_obj['M-T_P_2-3']) #RED TAPE METER 2
                                                dic['TestPims2_5'] = fixedInt(json_obj['M-T_P_2-4']) #RED TAPE METER 3
                                                dic['TestPims2_6'] = fixedInt(json_obj['M-T_P_2-5']) #RED TAPE METER 4
                                                dic['TestPims2_7'] = fixedInt(json_obj['M-T_P_2-6']) #RED TAPE METER 5
                                                dic['TestPims2_8'] = fixedInt(json_obj['M-T_P_2-7']) #RED TAPE METER 6
                                                dic['TestPims2_9'] = fixedInt(json_obj['M-T_P_2-8']) #RED TAPE METER 7
                                                dic['TestPims2_10'] = fixedInt(json_obj['M-T_P_2-9'] )#RED TAPE METER 8
                                                dic['TestPims2_11'] = fixedInt(json_obj['M-T_P_2-10']) #RED TAPE METER 9
                                                dic['TestPims2_12'] = fixedInt(json_obj['M-T_P_2-11']) #RED TAPE METER 10
                                                dic['TestPims2_13'] = fixedInt(json_obj['M-T_P_2-12']) #RED TAPE METER 11
                                                dic['TestPims2_14'] = fixedInt(json_obj['M-T_P_2-13']) #RED TAPE METER 12
                                                dic['TestPims2_15'] = fixedInt(json_obj['M-T_P_2-14']) #RED TAPE METER 13
                                                dic['TestPims2_16'] = fixedInt(json_obj['M-T_P_2-15'])#RED TAPE METER 14
                                                dic['TestPims2_17'] = fixedInt(json_obj['M-T_P_2-16']) #RED TAPE METER 15
                                                dic['TestPims2_18'] = fixedInt(json_obj['M-T_P_2-17']) #RED TAPE METER 16
                                                dic['TestPims2_19'] = fixedInt(json_obj['M-T_P_2-18']) #RED TAPE METER 17
                                                dic['TestPims2_20'] = fixedInt(json_obj['M-T_P_2-19']) #RED TAPE METER 18
                                                dic['TestPims2_21'] = fixedInt(json_obj['M-T_P_2-20']) #RED TAPE METER 19
                                                dic['TestPims2_22'] = fixedInt(json_obj['M-T_P_2-21']) #RED TAPE METER 20
                                                dic['TestPims2_23'] = fixedInt(json_obj['M-T_P_2-22']) #RED TAPE METER 21
                                                dic['TestPims2_24'] = fixedInt(json_obj['M-T_P_2-23']) #RED TAPE METER 22
                                                dic['TestPims2_25'] = fixedInt(json_obj['M-T_P_2-24']) #RED TAPE METER 23
                                                dic['TestPims2_26'] = fixedInt(json_obj['M-T_P_2-25']) #RED TAPE METER 24
                                                dic['TestPims2_27'] = fixedInt(json_obj['M-T_P_2-26']) #RED TAPE METER 25
                                                dic['TestPims2_28'] = fixedInt(json_obj['M-T_P_2-27']) #RED TAPE METER 26
                                                dic['TestPims2_29'] = fixedInt(json_obj['M-T_P_2-28']) #RED TAPE METER 27
                                                dic['TestPims2_30'] = fixedInt(json_obj['M-T_P_2-29']) #RED TAPE METER 28
                                                dic['TestPims2_31'] = fixedInt(json_obj['M-T_P_2-30']) #RED TAPE METER 29
                                                dic['TestPims2_32'] = fixedInt(json_obj['M-T_P_2-31'])#RED TAPE METER 30
                                                dic['TestPims2_33'] = fixedInt(json_obj['M-T_P_2-32']) #RED TAPE METER 31
                                                dic['TestPims2_34'] = fixedInt(json_obj['M-T_P_2-33']) #RED TAPE METER 32
                                                dic['TestPims2_35'] = fixedInt(json_obj['M-T_P_2-34']) #RED TAPE METER 33
                                                dic['TestPims2_36'] = fixedInt(json_obj['M-T_P_2-35']) #RED TAPE METER 34
                                                dic['TestPims2_37'] = fixedInt(json_obj['M-T_P_2-36']) #RED TAPE METER 35
                                                dic['TestPims2_38'] = fixedInt(json_obj['M-T_P_2-37']) #RED TAPE METER 36
                                                dic['TestPims2_39'] = fixedInt(json_obj['M-T_P_2-38']) #RED TAPE METER 37
                                                dic['TestPims2_40'] = fixedInt(json_obj['M-T_P_2-39']) #RED TAPE METER 38
                                                dic['TestPims2_41'] = fixedInt(json_obj['M-T_P_2-40']) #RED TAPE METER 39
                                                dic['TestPims2_42'] = fixedInt(json_obj['M-T_P_2-41']) #RED TAPE METER 40
                                                dic['TestPims2_43'] = fixedInt(json_obj['M-T_P_2-42']) #RED TAPE METER 41
                                                dic['TestPims2_44'] = fixedInt(json_obj['M-T_P_2-43']) #RED TAPE METER 42
                                                dic['TestPims2_45'] = fixedInt(json_obj['M-T_P_2-44']) #RED TAPE METER 43
                                                dic['TestPims2_46'] = fixedInt(json_obj['M-T_P_2-45']) #RED TAPE METER 44
                                                dic['TestPims2_47'] = fixedInt(json_obj['M-T_P_2-46']) #RED TAPE METER 45
                                                dic['TestPims2_48'] = fixedInt(json_obj['M-T_P_2-47']) #RED TAPE METER 46
                                                dic['TestPims2_49'] = fixedInt(json_obj['M-T_P_2-48']) #RED TAPE METER 47
                                                dic['TestPims2_50'] = fixedInt(json_obj['M-T_P_2-49']) #RED TAPE METER 48
                                                dic['TestPims2_51'] = fixedInt(json_obj['M-T_P_2-50']) #RED TAPE METER 49
                                                dic['TestPims2_52'] = fixedInt(json_obj['M-T_P_2-51'])#RED TAPE METER 50
                                                dic['TestPims2_53'] = fixedInt(json_obj['M-T_P_2-52']) #RED TAPE METER 51
                                                dic['TestPims2_54'] = fixedInt(json_obj['M-T_P_2-53']) #RED TAPE METER 52
                                                dic['TestPims2_55'] = fixedInt(json_obj['M-T_P_2-54']) #RED TAPE METER 53
                                                dic['TestPims2_56'] = fixedInt(json_obj['M-T_P_2-55']) #RED TAPE METER 54
                                                dic['TestPims2_57'] = fixedInt(json_obj['M-T_P_2-56']) #RED TAPE METER 55
                                                dic['TestPims2_58'] = fixedInt(json_obj['M-T_P_2-57']) #RED TAPE METER 56
                                                dic['TestPims2_59'] = fixedInt(json_obj['M-T_P_2-58']) #RED TAPE METER 57
                                                dic['TestPims2_60'] = fixedInt(json_obj['M-T_P_2-59']) #RED TAPE METER 58
                                                dic['TestPims2_61'] = fixedInt(json_obj['M-T_P_2-60']) #RED TAPE METER 59
                                                dic['TestPims2_62'] = fixedInt(json_obj['M-T_P_2-61']) #RED TAPE METER 60
                                                dic['TestPims2_63'] = fixedInt(json_obj['M-T_P_2-62']) #RED TAPE METER 61
                                                dic['TestPims2_64'] = fixedInt(json_obj['M-T_P_2-63']) #RED TAPE METER 62
                                                dic['TestPims2_65'] = fixedInt(json_obj['M-T_P_2-64']) #RED TAPE METER 63
                                                dic['TestPims2_66'] = fixedInt(json_obj['M-T_P_2-65']) #RED TAPE METER 64
                                                dic['TestPims2_67'] = fixedInt(json_obj['M-T_P_2-66']) #RED TAPE METER 65
                                                dic['TestPims2_68'] = fixedInt(json_obj['M-T_P_2-67'])#RED TAPE METER 66
                                                dic['TestPims2_69'] = fixedInt(json_obj['M-T_P_2-68']) #RED TAPE METER 67
                                                dic['TestPims2_70'] = fixedInt(json_obj['M-T_P_2-69']) #RED TAPE METER 68
                                                dic['TestPims2_71'] = fixedInt(json_obj['M-T_P_2-70']) #RED TAPE METER 69
                                                dic['TestPims2_72'] = fixedInt(json_obj['M-T_P_2-71']) #RED TAPE METER 70
                                                dic['TestPims2_73'] = fixedInt(json_obj['M-T_P_2-72']) #RED TAPE METER 71
                                                dic['TestPims2_74'] = fixedInt(json_obj['M-T_P_2-73']) #RED TAPE METER 72
                                                dic['TestPims2_75'] = fixedInt(json_obj['M-T_P_2-74']) #RED TAPE METER 73
                                                dic['TestPims2_76'] = fixedInt(json_obj['M-T_P_2-75']) #RED TAPE METER 74
                                                dic['TestPims2_77'] = fixedInt(json_obj['M-T_P_2-76']) #RED TAPE METER 75
                                                dic['TestPims2_78'] = fixedInt(json_obj['M-T_P_2-77']) #RED TAPE METER 76
                                                dic['TestPims2_79'] = fixedInt(json_obj['M-T_P_2-78']) #RED TAPE METER 77
                                                dic['TestPims2_80'] = fixedInt(json_obj['M-T_P_2-79']) #RED TAPE METER 78
                                                dic['TestPims2_81'] = fixedInt(json_obj['M-T_P_2-80']) #RED TAPE METER 79
                                                dic['TestPims2_82'] = fixedInt(json_obj['M-T_P_2-81']) #RED TAPE METER 80
                                                
                                                dic['TestPims3_1'] = fixedInt(json_obj['M-T_P_3-0']) #DRUM IN
                                                dic['TestPims3_2'] = fixedInt(json_obj['M-T_P_3-1']) #DRUM OUT
                                                dic['TestPims3_3'] = fixedInt(json_obj['M-T_P_3-2']) #RED TAPE METER 1
                                                dic['TestPims3_4'] = fixedInt(json_obj['M-T_P_3-3']) #RED TAPE METER 2
                                                dic['TestPims3_5'] = fixedInt(json_obj['M-T_P_3-4']) #RED TAPE METER 3
                                                dic['TestPims3_6'] = fixedInt(json_obj['M-T_P_3-5']) #RED TAPE METER 4
                                                dic['TestPims3_7'] = fixedInt(json_obj['M-T_P_3-6']) #RED TAPE METER 5
                                                dic['TestPims3_8'] = fixedInt(json_obj['M-T_P_3-7']) #RED TAPE METER 6
                                                dic['TestPims3_9'] = fixedInt(json_obj['M-T_P_3-8']) #RED TAPE METER 7
                                                dic['TestPims3_10'] = fixedInt(json_obj['M-T_P_3-9'] )#RED TAPE METER 8
                                                dic['TestPims3_11'] = fixedInt(json_obj['M-T_P_3-10']) #RED TAPE METER 9
                                                dic['TestPims3_12'] = fixedInt(json_obj['M-T_P_3-11']) #RED TAPE METER 10
                                                dic['TestPims3_13'] = fixedInt(json_obj['M-T_P_3-12']) #RED TAPE METER 11
                                                dic['TestPims3_14'] = fixedInt(json_obj['M-T_P_3-13']) #RED TAPE METER 12
                                                dic['TestPims3_15'] = fixedInt(json_obj['M-T_P_3-14']) #RED TAPE METER 13
                                                dic['TestPims3_16'] = fixedInt(json_obj['M-T_P_3-15'])#RED TAPE METER 14
                                                dic['TestPims3_17'] = fixedInt(json_obj['M-T_P_3-16']) #RED TAPE METER 15
                                                dic['TestPims3_18'] = fixedInt(json_obj['M-T_P_3-17']) #RED TAPE METER 16
                                                dic['TestPims3_19'] = fixedInt(json_obj['M-T_P_3-18']) #RED TAPE METER 17
                                                dic['TestPims3_20'] = fixedInt(json_obj['M-T_P_3-19']) #RED TAPE METER 18
                                                dic['TestPims3_21'] = fixedInt(json_obj['M-T_P_3-20']) #RED TAPE METER 19
                                                dic['TestPims3_22'] = fixedInt(json_obj['M-T_P_3-21']) #RED TAPE METER 20
                                                dic['TestPims3_23'] = fixedInt(json_obj['M-T_P_3-22']) #RED TAPE METER 21
                                                dic['TestPims3_24'] = fixedInt(json_obj['M-T_P_3-23']) #RED TAPE METER 22
                                                dic['TestPims3_25'] = fixedInt(json_obj['M-T_P_3-24']) #RED TAPE METER 23
                                                dic['TestPims3_26'] = fixedInt(json_obj['M-T_P_3-25']) #RED TAPE METER 24
                                                dic['TestPims3_27'] = fixedInt(json_obj['M-T_P_3-26']) #RED TAPE METER 25
                                                dic['TestPims3_28'] = fixedInt(json_obj['M-T_P_3-27']) #RED TAPE METER 26
                                                dic['TestPims3_29'] = fixedInt(json_obj['M-T_P_3-28']) #RED TAPE METER 27
                                                dic['TestPims3_30'] = fixedInt(json_obj['M-T_P_3-29']) #RED TAPE METER 28
                                                dic['TestPims3_31'] = fixedInt(json_obj['M-T_P_3-30']) #RED TAPE METER 29
                                                dic['TestPims3_32'] = fixedInt(json_obj['M-T_P_3-31'])#RED TAPE METER 30
                                                dic['TestPims3_33'] = fixedInt(json_obj['M-T_P_3-32']) #RED TAPE METER 31
                                                dic['TestPims3_34'] = fixedInt(json_obj['M-T_P_3-33']) #RED TAPE METER 32
                                                dic['TestPims3_35'] = fixedInt(json_obj['M-T_P_3-34']) #RED TAPE METER 33
                                                dic['TestPims3_36'] = fixedInt(json_obj['M-T_P_3-35']) #RED TAPE METER 34
                                                dic['TestPims3_37'] = fixedInt(json_obj['M-T_P_3-36']) #RED TAPE METER 35
                                                dic['TestPims3_38'] = fixedInt(json_obj['M-T_P_3-37']) #RED TAPE METER 36
                                                dic['TestPims3_39'] = fixedInt(json_obj['M-T_P_3-38']) #RED TAPE METER 37
                                                dic['TestPims3_40'] = fixedInt(json_obj['M-T_P_3-39']) #RED TAPE METER 38
                                                dic['TestPims3_41'] = fixedInt(json_obj['M-T_P_3-40']) #RED TAPE METER 39
                                                dic['TestPims3_42'] = fixedInt(json_obj['M-T_P_3-41']) #RED TAPE METER 40
                                                dic['TestPims3_43'] = fixedInt(json_obj['M-T_P_3-42']) #RED TAPE METER 41
                                                dic['TestPims3_44'] = fixedInt(json_obj['M-T_P_3-43']) #RED TAPE METER 42
                                                dic['TestPims3_45'] = fixedInt(json_obj['M-T_P_3-44']) #RED TAPE METER 43
                                                dic['TestPims3_46'] = fixedInt(json_obj['M-T_P_3-45']) #RED TAPE METER 44
                                                dic['TestPims3_47'] = fixedInt(json_obj['M-T_P_3-46']) #RED TAPE METER 45
                                                dic['TestPims3_48'] = fixedInt(json_obj['M-T_P_3-47']) #RED TAPE METER 46
                                                dic['TestPims3_49'] = fixedInt(json_obj['M-T_P_3-48']) #RED TAPE METER 47
                                                dic['TestPims3_50'] = fixedInt(json_obj['M-T_P_3-49']) #RED TAPE METER 48
                                                dic['TestPims3_51'] = fixedInt(json_obj['M-T_P_3-50']) #RED TAPE METER 49
                                                dic['TestPims3_52'] = fixedInt(json_obj['M-T_P_3-51'])#RED TAPE METER 50
                                                dic['TestPims3_53'] = fixedInt(json_obj['M-T_P_3-52']) #RED TAPE METER 51
                                                dic['TestPims3_54'] = fixedInt(json_obj['M-T_P_3-53']) #RED TAPE METER 52
                                                dic['TestPims3_55'] = fixedInt(json_obj['M-T_P_3-54']) #RED TAPE METER 53
                                                dic['TestPims3_56'] = fixedInt(json_obj['M-T_P_3-55']) #RED TAPE METER 54
                                                dic['TestPims3_57'] = fixedInt(json_obj['M-T_P_3-56']) #RED TAPE METER 55
                                                dic['TestPims3_58'] = fixedInt(json_obj['M-T_P_3-57']) #RED TAPE METER 56
                                                dic['TestPims3_59'] = fixedInt(json_obj['M-T_P_3-58']) #RED TAPE METER 57
                                                dic['TestPims3_60'] = fixedInt(json_obj['M-T_P_3-59']) #RED TAPE METER 58
                                                dic['TestPims3_61'] = fixedInt(json_obj['M-T_P_3-60']) #RED TAPE METER 59
                                                dic['TestPims3_62'] = fixedInt(json_obj['M-T_P_3-61']) #RED TAPE METER 60
                                                dic['TestPims3_63'] = fixedInt(json_obj['M-T_P_3-62']) #RED TAPE METER 61
                                                dic['TestPims3_64'] = fixedInt(json_obj['M-T_P_3-63']) #RED TAPE METER 62
                                                dic['TestPims3_65'] = fixedInt(json_obj['M-T_P_3-64']) #RED TAPE METER 63
                                                dic['TestPims3_66'] = fixedInt(json_obj['M-T_P_3-65']) #RED TAPE METER 64
                                                dic['TestPims3_67'] = fixedInt(json_obj['M-T_P_3-66']) #RED TAPE METER 65
                                                dic['TestPims3_68'] = fixedInt(json_obj['M-T_P_3-67'])#RED TAPE METER 66
                                                dic['TestPims3_69'] = fixedInt(json_obj['M-T_P_3-68']) #RED TAPE METER 67
                                                dic['TestPims3_70'] = fixedInt(json_obj['M-T_P_3-69']) #RED TAPE METER 68
                                                dic['TestPims3_71'] = fixedInt(json_obj['M-T_P_3-70']) #RED TAPE METER 69
                                                dic['TestPims3_72'] = fixedInt(json_obj['M-T_P_3-71']) #RED TAPE METER 70
                                                dic['TestPims3_73'] = fixedInt(json_obj['M-T_P_3-72']) #RED TAPE METER 71
                                                dic['TestPims3_74'] = fixedInt(json_obj['M-T_P_3-73']) #RED TAPE METER 72
                                                dic['TestPims3_75'] = fixedInt(json_obj['M-T_P_3-74']) #RED TAPE METER 73
                                                dic['TestPims3_76'] = fixedInt(json_obj['M-T_P_3-75']) #RED TAPE METER 74
                                                dic['TestPims3_77'] = fixedInt(json_obj['M-T_P_3-76']) #RED TAPE METER 75
                                                dic['TestPims3_78'] = fixedInt(json_obj['M-T_P_3-77']) #RED TAPE METER 76
                                                dic['TestPims3_79'] = fixedInt(json_obj['M-T_P_3-78']) #RED TAPE METER 77
                                                dic['TestPims3_80'] = fixedInt(json_obj['M-T_P_3-79']) #RED TAPE METER 78
                                                dic['TestPims3_81'] = fixedInt(json_obj['M-T_P_3-80']) #RED TAPE METER 79
                                                dic['TestPims3_82'] = fixedInt(json_obj['M-T_P_3-81']) #RED TAPE METER 80
                                                '''
                                                dic['ExtStop1_1'] = fixedInt(json_obj['M-E_S_1-0']) #Int value containing 1-20 value's
                                                dic['ExtStop1_2'] = json_obj['M-E_S_1-1'] #Boolean value containing on off status
                                                dic['ExtStopMessage1'] = ""
                                            
                                                dic['ExtStop3_1'] = fixedInt(json_obj['M-E_S_3-0']) #Int value containing 1-20 value's
                                                dic['ExtStop3_2'] = json_obj['M-E_S_3-1'] #Boolean value containing on off status
                                                dic['ExtStopMessage3'] = ""
                                             
                                                dic['ManStop1_1'] = fixedInt(json_obj['M-M_S_1-0']) #Int value containing 1-20 value's
                                                dic['ManStop1_2'] = json_obj['M-M_S_1-1'] #Boolean value containing on off status
                                                dic['ManStopMessage1'] = ""
                                                
                                                dic['ManStop2_1'] = fixedInt(json_obj['M-M_S_2-0']) #Int value containing 1-20 value's
                                                dic['ManStop2_2'] = json_obj['M-M_S_2-1'] #Boolean value containing on off status
                                                dic['ManStopMessage2'] = ""
                                             
                                                dic['VulStop1_1'] = fixedInt(json_obj['M-V_S_1-0']) #Int value containing 1-20 value's
                                                dic['VulStop1_2'] = json_obj['M-V_S_1-1'] #Boolean value containing on off status
                                                dic['VulStopMessage1'] = ""
                                                
                                                dic['TestStop1_1'] = fixedInt(json_obj['M-T_S_1-0']) #Int value containing 1-20 value's
                                                dic['TestStop1_2'] = json_obj['M-T_S_1-1'] #Boolean value containing on off status
                                                dic['TestStopMessage1'] = ""
                                                
                                                dic['TestStop2_1'] = fixedInt(json_obj['M-T_S_2-0']) #Int value containing 1-20 value's
                                                dic['TestStop2_2'] = json_obj['M-T_S_2-1'] #Boolean value containing on off status
                                                dic['TestStopMessage2'] = ""
                                                
                                                dic['TestStop3_1'] = fixedInt(json_obj['M-T_S_3-0']) #Int value containing 1-20 value's
                                                dic['TestStop3_2'] = json_obj['M-T_S_3-1'] #Boolean value containing on off status
                                                dic['TestStopMessage3'] = ""
                                                

                                                
                                                sql2()
        except(error):
                print("Error ::", error)
                #continue


def findBool(val):
    return val.lower() in ['1', 'true', 't']

def on_disconnect(client, userdata, rc=0):
    print("disconnect")
    client.loop_stop()



def polling_thread2():
    print("Thread2:PushedClient Initialized")
    client = mqttClient.Client("MQTT3890778965")
    client.username_pw_set("", "")
    client.on_message=on_message2
    #client.on_log=on_log
    #client.on_disconnect=on_disconnect
    client.connect('localhost', 1883)
    client.loop_start()
    client.subscribe('polyhose2/')
    print("Thread2: subscribed")
    #client.disconnect()


def sql2():
    try:
        if(int(dic['Mandrel1_1']) != 0 and int(dic['Mandrel1_1']) != 1) :   
                sql = "INSERT INTO mandrelreport1 ( pir , mpir, operator_name , program_name , mandrel_id , actual_od , minimum_od , maximum_od, fixed_block_st, movable_block_st, fixed_block_at, movable_block_at) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = ( str(dic['Mandrel1_1']), str(dic['Mandrel1_12']), str(dic['Mandrel1_2']),
                        str(dic['Mandrel1_3']), findFloat(float(dic['Mandrel1_4'])),
                        findFloat(float(dic['Mandrel1_5'])), findFloat(float(dic['Mandrel1_6'])), 
                        findFloat(float(dic['Mandrel1_7'])), findFloat(float(dic['Mandrel1_8'])), 
                        findFloat(float(dic['Mandrel1_9'])), findFloat(float(dic['Mandrel1_10'])), 
                        findFloat(float(dic['Mandrel1_11'])))
                mycursor.execute(sql, val)
        

        if(int(dic['Mandrel2_1']) != 0 and int(dic['Mandrel2_1']) != 1) :
                sql = "INSERT INTO mandrelreport2 ( pir , mpir, operator_name , program_name , mandrel_id , actual_od , minimum_od , maximum_od, fixed_block_st, movable_block_st, fixed_block_at, movable_block_at) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = ( str(dic['Mandrel2_1']), str(dic['Mandrel2_12']), str(dic['Mandrel2_2']),
                        str(dic['Mandrel2_3']), findFloat(float(dic['Mandrel2_4'])),
                        findFloat(float(dic['Mandrel2_5'])), findFloat(float(dic['Mandrel2_6'])), 
                        findFloat(float(dic['Mandrel2_7'])), findFloat(float(dic['Mandrel2_8'])), 
                        findFloat(float(dic['Mandrel2_9'])), findFloat(float(dic['Mandrel2_10'])), 
                        findFloat(float(dic['Mandrel2_11'])))
                mycursor.execute(sql, val)
        
       
        if (int(dic['Extruder1_1']) != 0 and int(dic['Extruder1_1']) != 1):
                sql = "INSERT INTO extruderreport1 ( pir , lmpir, operator_name , line_run_feedback , od_setpoint , od_actual , id_setpoint , id_actual, thickness_set, thickness_act, ext_rpm_set, ext_rpm_act, ext_cur_set, ext_cur_act, ext_pre_set, ext_pre_act, line_mpm_set, line_mpm_act, prod_meter, head_temp_sp, head_temp_act, screw_temp_sp, screw_temp_act, zone2_temp_sp, zone2_temp_act, zone3_temp_sp, zone3_temp_act, mesh, linear_cut, tube_hot_od_set, tube_hot_od_act, tube_cold_od_set, tube_cold_od_act, pin_set_value, pin_act_value, die_set_value, die_act_value, drum_out_no, amps, screw_rpm, line_speed, batches_used, ext_qty, temp_head_set, temp_head_act, temp_zone1_set, temp_zone1_act, temp_zone2_set, temp_zone2_act, temp_zone3_set, temp_zone3_act, temp_zone4_set, temp_zone4_act, temp_zone5_set, temp_zone5_act, vaccum_set_value, vaccum_act_value, wall_thick_spec, wall_thick_act, ecc_set_value, ecc_act_value, qa_approval) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = ( str(dic['Extruder1_1']), str(dic['Extruder1_27']), str(dic['Extruder1_2']),
                        findBool(dic['Extruder1_3']), findFloat(float(dic['Extruder1_4'])),
                        findFloat(float(dic['Extruder1_5'])), findFloat(float(dic['Extruder1_6'])), 
                        findFloat(float(dic['Extruder1_7'])), findFloat(float(dic['Extruder1_8'])), 
                        findFloat(float(dic['Extruder1_9'])), findFloat(float(dic['Extruder1_10'])), 
                        findFloat(float(dic['Extruder1_11'])),findFloat(float(dic['Extruder1_12'])),
                        findFloat(float(dic['Extruder1_13'])),findFloat(float(dic['Extruder1_14'])),
                        findFloat(float(dic['Extruder1_15'])),findFloat(float(dic['Extruder1_16'])),
                        findFloat(float(dic['Extruder1_17'])),findFloat(float(dic['Extruder1_18'])),
                        findFloat(float(dic['Extruder1_19'])),findFloat(float(dic['Extruder1_20'])),
                        findFloat(float(dic['Extruder1_21'])),findFloat(float(dic['Extruder1_22'])),
                        findFloat(float(dic['Extruder1_23'])),findFloat(float(dic['Extruder1_24'])),
                        findFloat(float(dic['Extruder1_25'])),findFloat(float(dic['Extruder1_26'])),
                        str(dic['Extruder1_27']),str(dic['Extruder1_28']),
                        findFloat(float(dic['Extruder1_29'])),findFloat(float(dic['Extruder1_30'])),
                        findFloat(float(dic['Extruder1_31'])),findFloat(float(dic['Extruder1_32'])),
                        findFloat(float(dic['Extruder1_33'])),findFloat(float(dic['Extruder1_34'])),
                        findFloat(float(dic['Extruder1_35'])),findFloat(float(dic['Extruder1_36'])),
                        str(dic['Extruder1_37']),findFloat(float(dic['Extruder1_38'])),
                        findFloat(float(dic['Extruder1_39'])),findFloat(float(dic['Extruder1_40'])),
                        str(dic['Extruder1_41']),str(dic['Extruder1_42']),
                        findFloat(float(dic['Extruder1_43'])),findFloat(float(dic['Extruder1_44'])),
                        findFloat(float(dic['Extruder1_45'])),findFloat(float(dic['Extruder1_46'])),
                        findFloat(float(dic['Extruder1_47'])),findFloat(float(dic['Extruder1_48'])),
                        findFloat(float(dic['Extruder1_49'])),findFloat(float(dic['Extruder1_50'])),
                        findFloat(float(dic['Extruder1_51'])),findFloat(float(dic['Extruder1_52'])),
                        findFloat(float(dic['Extruder1_53'])),findFloat(float(dic['Extruder1_54'])),
                        findFloat(float(dic['Extruder1_55'])),findFloat(float(dic['Extruder1_56'])),
                        findFloat(float(dic['Extruder1_57'])),findFloat(float(dic['Extruder1_58'])),
                        findFloat(float(dic['Extruder1_59'])),findFloat(float(dic['Extruder1_60'])),
                        str(dic['Extruder1_61']))
                mycursor.execute(sql, val)
        
        if(int(dic['Extruder3_1']) != 0 and int(dic['Extruder3_1']) != 1):
                sql = "INSERT INTO extruderreport3 ( pir , operator_name , line_run_feedback , od_setpoint , od_actual , id_setpoint , id_actual, thickness_set, thickness_act, ext_rpm_set, ext_rpm_act, ext_cur_set, ext_cur_act, ext_pre_set, ext_pre_act, line_mpm_set, line_mpm_act, prod_meter, head_temp_sp, head_temp_act, screw_temp_sp, screw_temp_act, zone2_temp_sp, zone2_temp_act, zone3_temp_sp, zone3_temp_act, mesh, linear_cut, tube_hot_od_set, tube_hot_od_act, tube_cold_od_set, tube_cold_od_act, pin_set_value, pin_act_value, die_set_value, die_act_value, drum_out_no, amps, screw_rpm, line_speed, batches_used, ext_qty, temp_head_set, temp_head_act, temp_zone1_set, temp_zone1_act, temp_zone2_set, temp_zone2_act, temp_zone3_set, temp_zone3_act, temp_zone4_set, temp_zone4_act, temp_zone5_set, temp_zone5_act, vaccum_set_value, vaccum_act_value, wall_thick_spec, wall_thick_act, ecc_set_value, ecc_act_value, qa_approval) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = ( str(dic['Extruder3_1']), str(dic['Extruder3_2']),
                        findBool(dic['Extruder3_3']), findFloat(float(dic['Extruder3_4'])),
                        findFloat(float(dic['Extruder3_5'])), findFloat(float(dic['Extruder3_6'])), 
                        findFloat(float(dic['Extruder3_7'])), findFloat(float(dic['Extruder3_8'])), 
                        findFloat(float(dic['Extruder3_9'])), findFloat(float(dic['Extruder3_10'])), 
                        findFloat(float(dic['Extruder3_11'])),findFloat(float(dic['Extruder3_12'])),
                        findFloat(float(dic['Extruder3_13'])),findFloat(float(dic['Extruder3_14'])),
                        findFloat(float(dic['Extruder3_15'])),findFloat(float(dic['Extruder3_16'])),
                        findFloat(float(dic['Extruder3_17'])),findFloat(float(dic['Extruder3_18'])),
                        findFloat(float(dic['Extruder3_19'])),findFloat(float(dic['Extruder3_20'])),
                        findFloat(float(dic['Extruder3_21'])),findFloat(float(dic['Extruder3_22'])),
                        findFloat(float(dic['Extruder3_23'])),findFloat(float(dic['Extruder3_24'])),
                        findFloat(float(dic['Extruder3_25'])),findFloat(float(dic['Extruder3_26'])),
                        str(dic['Extruder3_27']),str(dic['Extruder3_28']),
                        findFloat(float(dic['Extruder3_29'])),findFloat(float(dic['Extruder3_30'])),
                        findFloat(float(dic['Extruder3_31'])),findFloat(float(dic['Extruder3_32'])),
                        findFloat(float(dic['Extruder3_33'])),findFloat(float(dic['Extruder3_34'])),
                        findFloat(float(dic['Extruder3_35'])),findFloat(float(dic['Extruder3_36'])),
                        str(dic['Extruder3_37']),findFloat(float(dic['Extruder3_38'])),
                        findFloat(float(dic['Extruder3_39'])),findFloat(float(dic['Extruder3_40'])),
                        str(dic['Extruder3_41']),str(dic['Extruder3_42']),
                        findFloat(float(dic['Extruder3_43'])),findFloat(float(dic['Extruder3_44'])),
                        findFloat(float(dic['Extruder3_45'])),findFloat(float(dic['Extruder3_46'])),
                        findFloat(float(dic['Extruder3_47'])),findFloat(float(dic['Extruder3_48'])),
                        findFloat(float(dic['Extruder3_49'])),findFloat(float(dic['Extruder3_50'])),
                        findFloat(float(dic['Extruder3_51'])),findFloat(float(dic['Extruder3_52'])),
                        findFloat(float(dic['Extruder3_53'])),findFloat(float(dic['Extruder3_54'])),
                        findFloat(float(dic['Extruder3_55'])),findFloat(float(dic['Extruder3_56'])),
                        findFloat(float(dic['Extruder3_57'])),findFloat(float(dic['Extruder3_58'])),
                        findFloat(float(dic['Extruder3_59'])),findFloat(float(dic['Extruder3_60'])),
                        str(dic['Extruder3_61']))
                mycursor.execute(sql, val)
                
               
        if(int(dic['Vulcanizer1_1']) != 0 and int(dic['Vulcanizer1_1']) != 1):
                sql = "INSERT INTO vulcanizerreport1 ( pir , operator_name , program_name , rampup1_st , curing1_st , rampup2_st , curing2_st, actual_temp, actual_pres, actual_rapup1_tim, actual_curing1_tim, actual_rapup2_tim, actual_curing2_tim) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = ( str(dic['Vulcanizer1_1']), str(dic['Vulcanizer1_2']),
                        str(dic['Vulcanizer1_3']), findFloat(float(dic['Vulcanizer1_4'])),
                        findFloat(float(dic['Vulcanizer1_5'])), findFloat(float(dic['Vulcanizer1_6'])), 
                        findFloat(float(dic['Vulcanizer1_7'])), findFloat(float(dic['Vulcanizer1_8'])),
                        findFloat(float(dic['Vulcanizer1_9'])), findFloat(float(dic['Vulcanizer1_10'])),
                        findFloat(float(dic['Vulcanizer1_11'])), findFloat(float(dic['Vulcanizer1_12'])),
                        findFloat(float(dic['Vulcanizer1_13'])))
                mycursor.execute(sql, val)
        
        if(int(dic['Testing1_1']) != 0 and int(dic['Testing1_1']) != 1): 
                sql = "INSERT INTO testingreport1 ( pir , operator_name , test_id , hose_diameter , set_test_pres , actual_test_pres , set_ext_pres, act_ext_pres, test_pres_time, test_hose_from, test_hose_to, test_result_pass, test_result_fail) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = ( str(dic['Testing1_1']), str(dic['Testing1_2']),
                        int(dic['Testing1_3']), findFloat(float(dic['Testing1_4'])),
                        findFloat(float(dic['Testing1_5'])), findFloat(float(dic['Testing1_6'])), 
                        findFloat(float(dic['Testing1_7'])), findFloat(float(dic['Testing1_8'])),
                        int(dic['Testing1_9']), int(dic['Testing1_10']),
                        int(dic['Testing1_11']), findBool(dic['Testing1_12']),
                        findBool(dic['Testing1_13']))
                mycursor.execute(sql, val)
        
        if(int(dic['Testing2_1']) != 0 and int(dic['Testing2_1']) != 1):   
                sql = "INSERT INTO testingreport2 ( pir , operator_name , test_id , hose_diameter , set_test_pres , actual_test_pres , set_ext_pres, act_ext_pres, test_pres_time, test_hose_from, test_hose_to, test_result_pass, test_result_fail) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = ( str(dic['Testing2_1']), str(dic['Testing2_2']),
                        int(dic['Testing2_3']), findFloat(float(dic['Testing2_4'])),
                        findFloat(float(dic['Testing2_5'])), findFloat(float(dic['Testing2_6'])), 
                        findFloat(float(dic['Testing2_7'])), findFloat(float(dic['Testing2_8'])),
                        int(dic['Testing2_9']), int(dic['Testing2_10']),
                        int(dic['Testing2_11']), findBool(dic['Testing2_12']),
                        findBool(dic['Testing2_13']))
                mycursor.execute(sql, val)
        
        if(int(dic['Testing3_1']) != 0 and int(dic['Testing3_1']) != 1): 
                sql = "INSERT INTO testingreport3 ( pir , operator_name , test_id , hose_diameter , set_test_pres , actual_test_pres , set_ext_pres, act_ext_pres, test_pres_time, test_hose_from, test_hose_to, test_result_pass, test_result_fail) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = ( str(dic['Testing3_1']), str(dic['Testing3_2']),
                        int(dic['Testing3_3']), findFloat(float(dic['Testing3_4'])),
                        findFloat(float(dic['Testing3_5'])), findFloat(float(dic['Testing3_6'])), 
                        findFloat(float(dic['Testing3_7'])), findFloat(float(dic['Testing3_8'])),
                        int(dic['Testing3_9']), int(dic['Testing3_10']),
                        int(dic['Testing3_11']), findBool(dic['Testing3_12']),
                        findBool(dic['Testing3_13']))
                mycursor.execute(sql, val)
               

                           
        
        '''
        
        #Ext downtime
        # Here i have to add logic for "Option not selected"
        '''
        if(int(dic['ExtStop1_1']) == '0'): #reason no. will come here
                globalBS.tempExtOpt1 = True
        else:
                globalBS.tempExtOpt1 = False
        '''
        if(int(dic['ExtStop1_1']) == '23'): #reason no. will come here
                globalBS.tempExtSetup1 = True
        else:
                globalBS.tempExtSetup1 = False
        if(int(dic['ExtStop1_1']) == '24'): #reason no. will come here
                globalBS.tempExtClean1 = True
        else:
                globalBS.tempExtClean1 = False
        sql = "INSERT INTO extdowntime1 ( pir, status, setup, machine_clean ) VALUES (%s,%s,%s,%s)"
        val = (str(dic['ExtProd1_1']), findBool(dic['ExtProd1_13']), globalBS.tempExtSetup1, globalBS.tempExtClean1 )
        mycursor.execute(sql, val)
        

        if(int(dic['ExtStop3_1']) == '23'): #reason no. will come here
                globalBS.tempExtSetup3 = True
        else:
                globalBS.tempExtSetup3 = False
        if(int(dic['ExtStop3_1']) == '24'): #reason no. will come here
                globalBS.tempExtClean3 = True
        else:
                globalBS.tempExtClean3 = False
        sql = "INSERT INTO extdowntime3 ( pir, status, setup, machine_clean ) VALUES (%s,%s,%s,%s)"
        val = (str(dic['ExtProd3_1']), findBool(dic['ExtProd3_13']), globalBS.tempExtSetup3, globalBS.tempExtClean3 )
        mycursor.execute(sql, val)
        
        
        
        sql = "INSERT INTO vuldowntime1 ( pir, status) VALUES (%s,%s)"
        val = (str(dic['VulProd1_1']), findBool(dic['VulProd1_10']))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO testdowntime1 ( pir, status) VALUES (%s,%s)"
        val = (str(dic['TestProd1_1']), findBool(dic['TestProd1_9']))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO testdowntime2 ( pir, status) VALUES (%s,%s)"
        val = (str(dic['TestProd2_1']), findBool(dic['TestProd2_9']))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO testdowntime3 ( pir, status) VALUES (%s,%s)"
        val = (str(dic['TestProd3_1']), findBool(dic['TestProd3_9']))
        mycursor.execute(sql, val)
        '''
             
        
        ''' 
        sql = "INSERT INTO manpims1 ( drum_in, drum_out ) VALUES (%s,%s)"
        val = (str(dic['ManPims1_1']),str(dic['ManPims1_2']))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO manpims2 ( drum_in, drum_out ) VALUES (%s,%s)"
        val = (str(dic['ManPims2_1']),str(dic['ManPims2_2']))
        mycursor.execute(sql, val)
        
     
        
        sql = "INSERT INTO vulpims1 ( drum_in, drum_out ) VALUES (%s,%s)"
        val = (str(dic['VulPims1_1']),str(dic['VulPims1_2']))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO extpims1 ( rtm_1 , rtm_2 , rtm_3 , rtm_4 , rtm_5, rtm_6, rtm_7, rtm_8, rtm_9, rtm_10, rtm_11 , rtm_12 , rtm_13 , rtm_14 , rtm_15, rtm_16, rtm_17, rtm_18, rtm_19, rtm_20, rtm_21 , rtm_22 , rtm_23 , rtm_24 , rtm_25, rtm_26, rtm_27, rtm_28, rtm_29, rtm_30, rtm_31 , rtm_32 , rtm_33 , rtm_34 , rtm_35, rtm_36, rtm_37, rtm_38, rtm_39, rtm_40, rtm_41 , rtm_42 , rtm_43 , rtm_44 , rtm_45, rtm_46, rtm_47, rtm_48, rtm_49, rtm_50, rtm_51 , rtm_52 , rtm_53 , rtm_54 , rtm_55, rtm_56, rtm_57, rtm_58, rtm_59, rtm_60, rtm_61 , rtm_62 , rtm_63 , rtm_64 , rtm_65, rtm_66, rtm_67, rtm_68, rtm_69, rtm_70, rtm_71 , rtm_72 , rtm_73 , rtm_74 , rtm_75, rtm_76, rtm_77, rtm_78, rtm_79, rtm_80, drum_in, drum_out) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( findFloat(float(dic['ExtPims1_3'])), findFloat(float(dic['ExtPims1_4'])), 
                findFloat(float(dic['ExtPims1_5'])), findFloat(float(dic['ExtPims1_6'])), 
                findFloat(float(dic['ExtPims1_7'])), findFloat(float(dic['ExtPims1_8'])), 
                findFloat(float(dic['ExtPims1_9'])), findFloat(float(dic['ExtPims1_10'])),  
                findFloat(float(dic['ExtPims1_11'])), findFloat(float(dic['ExtPims1_12'])), 
                findFloat(float(dic['ExtPims1_13'])), findFloat(float(dic['ExtPims1_14'])), 
                findFloat(float(dic['ExtPims1_15'])), findFloat(float(dic['ExtPims1_16'])), 
                findFloat(float(dic['ExtPims1_17'])), findFloat(float(dic['ExtPims1_18'])), 
                findFloat(float(dic['ExtPims1_19'])), findFloat(float(dic['ExtPims1_20'])), 
                findFloat(float(dic['ExtPims1_21'])), findFloat(float(dic['ExtPims1_22'])), 
                findFloat(float(dic['ExtPims1_23'])), findFloat(float(dic['ExtPims1_24'])), 
                findFloat(float(dic['ExtPims1_25'])), findFloat(float(dic['ExtPims1_26'])), 
                findFloat(float(dic['ExtPims1_27'])), findFloat(float(dic['ExtPims1_28'])), 
                findFloat(float(dic['ExtPims1_29'])), findFloat(float(dic['ExtPims1_30'])),
                findFloat(float(dic['ExtPims1_31'])), findFloat(float(dic['ExtPims1_32'])), 
                findFloat(float(dic['ExtPims1_33'])), findFloat(float(dic['ExtPims1_34'])), 
                findFloat(float(dic['ExtPims1_35'])), findFloat(float(dic['ExtPims1_36'])), 
                findFloat(float(dic['ExtPims1_37'])), findFloat(float(dic['ExtPims1_38'])), 
                findFloat(float(dic['ExtPims1_39'])), findFloat(float(dic['ExtPims1_40'])), 
                findFloat(float(dic['ExtPims1_41'])), findFloat(float(dic['ExtPims1_42'])), 
                findFloat(float(dic['ExtPims1_43'])), findFloat(float(dic['ExtPims1_44'])), 
                findFloat(float(dic['ExtPims1_45'])), findFloat(float(dic['ExtPims1_46'])), 
                findFloat(float(dic['ExtPims1_47'])), findFloat(float(dic['ExtPims1_48'])), 
                findFloat(float(dic['ExtPims1_49'])), findFloat(float(dic['ExtPims1_50'])), 
                findFloat(float(dic['ExtPims1_51'])), findFloat(float(dic['ExtPims1_52'])), 
                findFloat(float(dic['ExtPims1_53'])), findFloat(float(dic['ExtPims1_54'])), 
                findFloat(float(dic['ExtPims1_55'])), findFloat(float(dic['ExtPims1_56'])), 
                findFloat(float(dic['ExtPims1_57'])), findFloat(float(dic['ExtPims1_58'])), 
                findFloat(float(dic['ExtPims1_59'])), findFloat(float(dic['ExtPims1_60'])), 
                findFloat(float(dic['ExtPims1_61'])), findFloat(float(dic['ExtPims1_62'])), 
                findFloat(float(dic['ExtPims1_63'])), findFloat(float(dic['ExtPims1_64'])), 
                findFloat(float(dic['ExtPims1_65'])), findFloat(float(dic['ExtPims1_66'])), 
                findFloat(float(dic['ExtPims1_67'])), findFloat(float(dic['ExtPims1_68'])), 
                findFloat(float(dic['ExtPims1_69'])), findFloat(float(dic['ExtPims1_70'])), 
                findFloat(float(dic['ExtPims1_71'])), findFloat(float(dic['ExtPims1_72'])), 
                findFloat(float(dic['ExtPims1_73'])), findFloat(float(dic['ExtPims1_74'])), 
                findFloat(float(dic['ExtPims1_75'])), findFloat(float(dic['ExtPims1_76'])), 
                findFloat(float(dic['ExtPims1_77'])), findFloat(float(dic['ExtPims1_78'])),
                findFloat(float(dic['ExtPims1_79'])), findFloat(float(dic['ExtPims1_80'])),
                findFloat(float(dic['ExtPims1_81'])), findFloat(float(dic['ExtPims1_82'])),
                str(dic['ExtPims1_1']), str(dic['ExtPims1_2']))
        mycursor.execute(sql, val)
        
       
        
        sql = "INSERT INTO extpims3 ( rtm_1 , rtm_2 , rtm_3 , rtm_4 , rtm_5, rtm_6, rtm_7, rtm_8, rtm_9, rtm_10, rtm_11 , rtm_12 , rtm_13 , rtm_14 , rtm_15, rtm_16, rtm_17, rtm_18, rtm_19, rtm_20, rtm_21 , rtm_22 , rtm_23 , rtm_24 , rtm_25, rtm_26, rtm_27, rtm_28, rtm_29, rtm_30, rtm_31 , rtm_32 , rtm_33 , rtm_34 , rtm_35, rtm_36, rtm_37, rtm_38, rtm_39, rtm_40, rtm_41 , rtm_42 , rtm_43 , rtm_44 , rtm_45, rtm_46, rtm_47, rtm_48, rtm_49, rtm_50, rtm_51 , rtm_52 , rtm_53 , rtm_54 , rtm_55, rtm_56, rtm_57, rtm_58, rtm_59, rtm_60, rtm_61 , rtm_62 , rtm_63 , rtm_64 , rtm_65, rtm_66, rtm_67, rtm_68, rtm_69, rtm_70, rtm_71 , rtm_72 , rtm_73 , rtm_74 , rtm_75, rtm_76, rtm_77, rtm_78, rtm_79, rtm_80, drum_in, drum_out) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( findFloat(float(dic['ExtPims3_3'])), findFloat(float(dic['ExtPims3_4'])), 
                findFloat(float(dic['ExtPims3_5'])), findFloat(float(dic['ExtPims3_6'])), 
                findFloat(float(dic['ExtPims3_7'])), findFloat(float(dic['ExtPims3_8'])), 
                findFloat(float(dic['ExtPims3_9'])), findFloat(float(dic['ExtPims3_10'])),  
                findFloat(float(dic['ExtPims3_11'])), findFloat(float(dic['ExtPims3_12'])), 
                findFloat(float(dic['ExtPims3_13'])), findFloat(float(dic['ExtPims3_14'])), 
                findFloat(float(dic['ExtPims3_15'])), findFloat(float(dic['ExtPims3_16'])), 
                findFloat(float(dic['ExtPims3_17'])), findFloat(float(dic['ExtPims3_18'])), 
                findFloat(float(dic['ExtPims3_19'])), findFloat(float(dic['ExtPims3_20'])), 
                findFloat(float(dic['ExtPims3_21'])), findFloat(float(dic['ExtPims3_22'])), 
                findFloat(float(dic['ExtPims3_23'])), findFloat(float(dic['ExtPims3_24'])), 
                findFloat(float(dic['ExtPims3_25'])), findFloat(float(dic['ExtPims3_26'])), 
                findFloat(float(dic['ExtPims3_27'])), findFloat(float(dic['ExtPims3_28'])), 
                findFloat(float(dic['ExtPims3_29'])), findFloat(float(dic['ExtPims3_30'])),
                findFloat(float(dic['ExtPims3_31'])), findFloat(float(dic['ExtPims3_32'])), 
                findFloat(float(dic['ExtPims3_33'])), findFloat(float(dic['ExtPims3_34'])), 
                findFloat(float(dic['ExtPims3_35'])), findFloat(float(dic['ExtPims3_36'])), 
                findFloat(float(dic['ExtPims3_37'])), findFloat(float(dic['ExtPims3_38'])), 
                findFloat(float(dic['ExtPims3_39'])), findFloat(float(dic['ExtPims3_40'])), 
                findFloat(float(dic['ExtPims3_41'])), findFloat(float(dic['ExtPims3_42'])), 
                findFloat(float(dic['ExtPims3_43'])), findFloat(float(dic['ExtPims3_44'])), 
                findFloat(float(dic['ExtPims3_45'])), findFloat(float(dic['ExtPims3_46'])), 
                findFloat(float(dic['ExtPims3_47'])), findFloat(float(dic['ExtPims3_48'])), 
                findFloat(float(dic['ExtPims3_49'])), findFloat(float(dic['ExtPims3_50'])), 
                findFloat(float(dic['ExtPims3_51'])), findFloat(float(dic['ExtPims3_52'])), 
                findFloat(float(dic['ExtPims3_53'])), findFloat(float(dic['ExtPims3_54'])), 
                findFloat(float(dic['ExtPims3_55'])), findFloat(float(dic['ExtPims3_56'])), 
                findFloat(float(dic['ExtPims3_57'])), findFloat(float(dic['ExtPims3_58'])), 
                findFloat(float(dic['ExtPims3_59'])), findFloat(float(dic['ExtPims3_60'])), 
                findFloat(float(dic['ExtPims3_61'])), findFloat(float(dic['ExtPims3_62'])), 
                findFloat(float(dic['ExtPims3_63'])), findFloat(float(dic['ExtPims3_64'])), 
                findFloat(float(dic['ExtPims3_65'])), findFloat(float(dic['ExtPims3_66'])), 
                findFloat(float(dic['ExtPims3_67'])), findFloat(float(dic['ExtPims3_68'])), 
                findFloat(float(dic['ExtPims3_69'])), findFloat(float(dic['ExtPims3_70'])), 
                findFloat(float(dic['ExtPims3_71'])), findFloat(float(dic['ExtPims3_72'])), 
                findFloat(float(dic['ExtPims3_73'])), findFloat(float(dic['ExtPims3_74'])), 
                findFloat(float(dic['ExtPims3_75'])), findFloat(float(dic['ExtPims3_76'])), 
                findFloat(float(dic['ExtPims3_77'])), findFloat(float(dic['ExtPims3_78'])),
                findFloat(float(dic['ExtPims3_79'])), findFloat(float(dic['ExtPims3_80'])),
                findFloat(float(dic['ExtPims3_81'])), findFloat(float(dic['ExtPims3_82'])),
                str(dic['ExtPims3_1']), str(dic['ExtPims3_2']))
        mycursor.execute(sql, val)
        
        
        sql = "INSERT INTO testpims1 ( drum_in, drum_out, rtm_1 , rtm_2 , rtm_3 , rtm_4 , rtm_5, rtm_6, rtm_7, rtm_8, rtm_9, rtm_10, rtm_11 , rtm_12 , rtm_13 , rtm_14 , rtm_15, rtm_16, rtm_17, rtm_18, rtm_19, rtm_20, rtm_21 , rtm_22 , rtm_23 , rtm_24 , rtm_25, rtm_26, rtm_27, rtm_28, rtm_29, rtm_30, rtm_31 , rtm_32 , rtm_33 , rtm_34 , rtm_35, rtm_36, rtm_37, rtm_38, rtm_39, rtm_40, rtm_41 , rtm_42 , rtm_43 , rtm_44 , rtm_45, rtm_46, rtm_47, rtm_48, rtm_49, rtm_50, rtm_51 , rtm_52 , rtm_53 , rtm_54 , rtm_55, rtm_56, rtm_57, rtm_58, rtm_59, rtm_60, rtm_61 , rtm_62 , rtm_63 , rtm_64 , rtm_65, rtm_66, rtm_67, rtm_68, rtm_69, rtm_70, rtm_71 , rtm_72 , rtm_73 , rtm_74 , rtm_75, rtm_76, rtm_77, rtm_78, rtm_79, rtm_80) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( str(dic['TestPims1_1']), str(dic['TestPims1_2']),
                findFloat(float(dic['TestPims1_3'])), findFloat(float(dic['TestPims1_4'])),
                findFloat(float(dic['TestPims1_5'])), findFloat(float(dic['TestPims1_6'])), 
                findFloat(float(dic['TestPims1_7'])), findFloat(float(dic['TestPims1_8'])), 
                findFloat(float(dic['TestPims1_9'])), findFloat(float(dic['TestPims1_10'])), 
                findFloat(float(dic['TestPims1_11'])), findFloat(float(dic['TestPims1_12'])),  
                findFloat(float(dic['TestPims1_13'])), findFloat(float(dic['TestPims1_14'])), 
                findFloat(float(dic['TestPims1_15'])), findFloat(float(dic['TestPims1_16'])), 
                findFloat(float(dic['TestPims1_17'])), findFloat(float(dic['TestPims1_18'])), 
                findFloat(float(dic['TestPims1_19'])), findFloat(float(dic['TestPims1_20'])), 
                findFloat(float(dic['TestPims1_21'])), findFloat(float(dic['TestPims1_22'])), 
                findFloat(float(dic['TestPims1_23'])), findFloat(float(dic['TestPims1_24'])), 
                findFloat(float(dic['TestPims1_25'])), findFloat(float(dic['TestPims1_26'])), 
                findFloat(float(dic['TestPims1_27'])), findFloat(float(dic['TestPims1_28'])), 
                findFloat(float(dic['TestPims1_29'])), findFloat(float(dic['TestPims1_30'])), 
                findFloat(float(dic['TestPims1_31'])), findFloat(float(dic['TestPims1_32'])),
                findFloat(float(dic['TestPims1_33'])), findFloat(float(dic['TestPims1_34'])), 
                findFloat(float(dic['TestPims1_35'])), findFloat(float(dic['TestPims1_36'])), 
                findFloat(float(dic['TestPims1_37'])), findFloat(float(dic['TestPims1_38'])), 
                findFloat(float(dic['TestPims1_39'])), findFloat(float(dic['TestPims1_40'])), 
                findFloat(float(dic['TestPims1_41'])), findFloat(float(dic['TestPims1_42'])), 
                findFloat(float(dic['TestPims1_43'])), findFloat(float(dic['TestPims1_44'])), 
                findFloat(float(dic['TestPims1_45'])), findFloat(float(dic['TestPims1_46'])), 
                findFloat(float(dic['TestPims1_47'])), findFloat(float(dic['TestPims1_48'])), 
                findFloat(float(dic['TestPims1_49'])), findFloat(float(dic['TestPims1_50'])), 
                findFloat(float(dic['TestPims1_51'])), findFloat(float(dic['TestPims1_52'])), 
                findFloat(float(dic['TestPims1_53'])), findFloat(float(dic['TestPims1_54'])), 
                findFloat(float(dic['TestPims1_55'])), findFloat(float(dic['TestPims1_56'])), 
                findFloat(float(dic['TestPims1_57'])), findFloat(float(dic['TestPims1_58'])), 
                findFloat(float(dic['TestPims1_59'])), findFloat(float(dic['TestPims1_60'])), 
                findFloat(float(dic['TestPims1_61'])), findFloat(float(dic['TestPims1_62'])), 
                findFloat(float(dic['TestPims1_63'])), findFloat(float(dic['TestPims1_64'])), 
                findFloat(float(dic['TestPims1_65'])), findFloat(float(dic['TestPims1_66'])), 
                findFloat(float(dic['TestPims1_67'])), findFloat(float(dic['TestPims1_68'])), 
                findFloat(float(dic['TestPims1_69'])), findFloat(float(dic['TestPims1_70'])), 
                findFloat(float(dic['TestPims1_71'])), findFloat(float(dic['TestPims1_72'])), 
                findFloat(float(dic['TestPims1_73'])), findFloat(float(dic['TestPims1_74'])), 
                findFloat(float(dic['TestPims1_75'])), findFloat(float(dic['TestPims1_76'])), 
                findFloat(float(dic['TestPims1_77'])), findFloat(float(dic['TestPims1_78'])), 
                findFloat(float(dic['TestPims1_79'])), findFloat(float(dic['TestPims1_80'])),
                findFloat(float(dic['TestPims1_81'])), findFloat(float(dic['TestPims1_82'])))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO testpims2 ( drum_in, drum_out, rtm_1 , rtm_2 , rtm_3 , rtm_4 , rtm_5, rtm_6, rtm_7, rtm_8, rtm_9, rtm_10, rtm_11 , rtm_12 , rtm_13 , rtm_14 , rtm_15, rtm_16, rtm_17, rtm_18, rtm_19, rtm_20, rtm_21 , rtm_22 , rtm_23 , rtm_24 , rtm_25, rtm_26, rtm_27, rtm_28, rtm_29, rtm_30, rtm_31 , rtm_32 , rtm_33 , rtm_34 , rtm_35, rtm_36, rtm_37, rtm_38, rtm_39, rtm_40, rtm_41 , rtm_42 , rtm_43 , rtm_44 , rtm_45, rtm_46, rtm_47, rtm_48, rtm_49, rtm_50, rtm_51 , rtm_52 , rtm_53 , rtm_54 , rtm_55, rtm_56, rtm_57, rtm_58, rtm_59, rtm_60, rtm_61 , rtm_62 , rtm_63 , rtm_64 , rtm_65, rtm_66, rtm_67, rtm_68, rtm_69, rtm_70, rtm_71 , rtm_72 , rtm_73 , rtm_74 , rtm_75, rtm_76, rtm_77, rtm_78, rtm_79, rtm_80) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( str(dic['TestPims2_1']), str(dic['TestPims2_2']),
                findFloat(float(dic['TestPims2_3'])), findFloat(float(dic['TestPims2_4'])),
                findFloat(float(dic['TestPims2_5'])), findFloat(float(dic['TestPims2_6'])), 
                findFloat(float(dic['TestPims2_7'])), findFloat(float(dic['TestPims2_8'])), 
                findFloat(float(dic['TestPims2_9'])), findFloat(float(dic['TestPims2_10'])), 
                findFloat(float(dic['TestPims2_11'])), findFloat(float(dic['TestPims2_12'])),  
                findFloat(float(dic['TestPims2_13'])), findFloat(float(dic['TestPims2_14'])), 
                findFloat(float(dic['TestPims2_15'])), findFloat(float(dic['TestPims2_16'])), 
                findFloat(float(dic['TestPims2_17'])), findFloat(float(dic['TestPims2_18'])), 
                findFloat(float(dic['TestPims2_19'])), findFloat(float(dic['TestPims2_20'])), 
                findFloat(float(dic['TestPims2_21'])), findFloat(float(dic['TestPims2_22'])), 
                findFloat(float(dic['TestPims2_23'])), findFloat(float(dic['TestPims2_24'])), 
                findFloat(float(dic['TestPims2_25'])), findFloat(float(dic['TestPims2_26'])), 
                findFloat(float(dic['TestPims2_27'])), findFloat(float(dic['TestPims2_28'])), 
                findFloat(float(dic['TestPims2_29'])), findFloat(float(dic['TestPims2_30'])), 
                findFloat(float(dic['TestPims2_31'])), findFloat(float(dic['TestPims2_32'])),
                findFloat(float(dic['TestPims2_33'])), findFloat(float(dic['TestPims2_34'])), 
                findFloat(float(dic['TestPims2_35'])), findFloat(float(dic['TestPims2_36'])), 
                findFloat(float(dic['TestPims2_37'])), findFloat(float(dic['TestPims2_38'])), 
                findFloat(float(dic['TestPims2_39'])), findFloat(float(dic['TestPims2_40'])), 
                findFloat(float(dic['TestPims2_41'])), findFloat(float(dic['TestPims2_42'])), 
                findFloat(float(dic['TestPims2_43'])), findFloat(float(dic['TestPims2_44'])), 
                findFloat(float(dic['TestPims2_45'])), findFloat(float(dic['TestPims2_46'])), 
                findFloat(float(dic['TestPims2_47'])), findFloat(float(dic['TestPims2_48'])), 
                findFloat(float(dic['TestPims2_49'])), findFloat(float(dic['TestPims2_50'])), 
                findFloat(float(dic['TestPims2_51'])), findFloat(float(dic['TestPims2_52'])), 
                findFloat(float(dic['TestPims2_53'])), findFloat(float(dic['TestPims2_54'])), 
                findFloat(float(dic['TestPims2_55'])), findFloat(float(dic['TestPims2_56'])), 
                findFloat(float(dic['TestPims2_57'])), findFloat(float(dic['TestPims2_58'])), 
                findFloat(float(dic['TestPims2_59'])), findFloat(float(dic['TestPims2_60'])), 
                findFloat(float(dic['TestPims2_61'])), findFloat(float(dic['TestPims2_62'])), 
                findFloat(float(dic['TestPims2_63'])), findFloat(float(dic['TestPims2_64'])), 
                findFloat(float(dic['TestPims2_65'])), findFloat(float(dic['TestPims2_66'])), 
                findFloat(float(dic['TestPims2_67'])), findFloat(float(dic['TestPims2_68'])), 
                findFloat(float(dic['TestPims2_69'])), findFloat(float(dic['TestPims2_70'])), 
                findFloat(float(dic['TestPims2_71'])), findFloat(float(dic['TestPims2_72'])), 
                findFloat(float(dic['TestPims2_73'])), findFloat(float(dic['TestPims2_74'])), 
                findFloat(float(dic['TestPims2_75'])), findFloat(float(dic['TestPims2_76'])), 
                findFloat(float(dic['TestPims2_77'])), findFloat(float(dic['TestPims2_78'])), 
                findFloat(float(dic['TestPims2_79'])), findFloat(float(dic['TestPims2_80'])),
                findFloat(float(dic['TestPims2_81'])), findFloat(float(dic['TestPims2_82'])))
        mycursor.execute(sql, val)
        

        sql = "INSERT INTO testpims3 ( drum_in, drum_out, rtm_1 , rtm_2 , rtm_3 , rtm_4 , rtm_5, rtm_6, rtm_7, rtm_8, rtm_9, rtm_10, rtm_11 , rtm_12 , rtm_13 , rtm_14 , rtm_15, rtm_16, rtm_17, rtm_18, rtm_19, rtm_20, rtm_21 , rtm_22 , rtm_23 , rtm_24 , rtm_25, rtm_26, rtm_27, rtm_28, rtm_29, rtm_30, rtm_31 , rtm_32 , rtm_33 , rtm_34 , rtm_35, rtm_36, rtm_37, rtm_38, rtm_39, rtm_40, rtm_41 , rtm_42 , rtm_43 , rtm_44 , rtm_45, rtm_46, rtm_47, rtm_48, rtm_49, rtm_50, rtm_51 , rtm_52 , rtm_53 , rtm_54 , rtm_55, rtm_56, rtm_57, rtm_58, rtm_59, rtm_60, rtm_61 , rtm_62 , rtm_63 , rtm_64 , rtm_65, rtm_66, rtm_67, rtm_68, rtm_69, rtm_70, rtm_71 , rtm_72 , rtm_73 , rtm_74 , rtm_75, rtm_76, rtm_77, rtm_78, rtm_79, rtm_80) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( str(dic['TestPims3_1']), str(dic['TestPims3_2']),
                findFloat(float(dic['TestPims3_3'])), findFloat(float(dic['TestPims3_4'])),
                findFloat(float(dic['TestPims3_5'])), findFloat(float(dic['TestPims3_6'])), 
                findFloat(float(dic['TestPims3_7'])), findFloat(float(dic['TestPims3_8'])), 
                findFloat(float(dic['TestPims3_9'])), findFloat(float(dic['TestPims3_10'])), 
                findFloat(float(dic['TestPims3_11'])), findFloat(float(dic['TestPims3_12'])),  
                findFloat(float(dic['TestPims3_13'])), findFloat(float(dic['TestPims3_14'])), 
                findFloat(float(dic['TestPims3_15'])), findFloat(float(dic['TestPims3_16'])), 
                findFloat(float(dic['TestPims3_17'])), findFloat(float(dic['TestPims3_18'])), 
                findFloat(float(dic['TestPims3_19'])), findFloat(float(dic['TestPims3_20'])), 
                findFloat(float(dic['TestPims3_21'])), findFloat(float(dic['TestPims3_22'])), 
                findFloat(float(dic['TestPims3_23'])), findFloat(float(dic['TestPims3_24'])), 
                findFloat(float(dic['TestPims3_25'])), findFloat(float(dic['TestPims3_26'])), 
                findFloat(float(dic['TestPims3_27'])), findFloat(float(dic['TestPims3_28'])), 
                findFloat(float(dic['TestPims3_29'])), findFloat(float(dic['TestPims3_30'])), 
                findFloat(float(dic['TestPims3_31'])), findFloat(float(dic['TestPims3_32'])),
                findFloat(float(dic['TestPims3_33'])), findFloat(float(dic['TestPims3_34'])), 
                findFloat(float(dic['TestPims3_35'])), findFloat(float(dic['TestPims3_36'])), 
                findFloat(float(dic['TestPims3_37'])), findFloat(float(dic['TestPims3_38'])), 
                findFloat(float(dic['TestPims3_39'])), findFloat(float(dic['TestPims3_40'])), 
                findFloat(float(dic['TestPims3_41'])), findFloat(float(dic['TestPims3_42'])), 
                findFloat(float(dic['TestPims3_43'])), findFloat(float(dic['TestPims3_44'])), 
                findFloat(float(dic['TestPims3_45'])), findFloat(float(dic['TestPims3_46'])), 
                findFloat(float(dic['TestPims3_47'])), findFloat(float(dic['TestPims3_48'])), 
                findFloat(float(dic['TestPims3_49'])), findFloat(float(dic['TestPims3_50'])), 
                findFloat(float(dic['TestPims3_51'])), findFloat(float(dic['TestPims3_52'])), 
                findFloat(float(dic['TestPims3_53'])), findFloat(float(dic['TestPims3_54'])), 
                findFloat(float(dic['TestPims3_55'])), findFloat(float(dic['TestPims3_56'])), 
                findFloat(float(dic['TestPims3_57'])), findFloat(float(dic['TestPims3_58'])), 
                findFloat(float(dic['TestPims3_59'])), findFloat(float(dic['TestPims3_60'])), 
                findFloat(float(dic['TestPims3_61'])), findFloat(float(dic['TestPims3_62'])), 
                findFloat(float(dic['TestPims3_63'])), findFloat(float(dic['TestPims3_64'])), 
                findFloat(float(dic['TestPims3_65'])), findFloat(float(dic['TestPims3_66'])), 
                findFloat(float(dic['TestPims3_67'])), findFloat(float(dic['TestPims3_68'])), 
                findFloat(float(dic['TestPims3_69'])), findFloat(float(dic['TestPims3_70'])), 
                findFloat(float(dic['TestPims3_71'])), findFloat(float(dic['TestPims3_72'])), 
                findFloat(float(dic['TestPims3_73'])), findFloat(float(dic['TestPims3_74'])), 
                findFloat(float(dic['TestPims3_75'])), findFloat(float(dic['TestPims3_76'])), 
                findFloat(float(dic['TestPims3_77'])), findFloat(float(dic['TestPims3_78'])), 
                findFloat(float(dic['TestPims3_79'])), findFloat(float(dic['TestPims3_80'])),
                findFloat(float(dic['TestPims3_81'])), findFloat(float(dic['TestPims3_82'])))
        mycursor.execute(sql, val)
        '''
        print("Thread2: Data Dumped")
        
    except(error):
        print("Error ::", error)
        #continue


def update():
    pass




# display loop (in main thread)
if __name__ == "__main__":
        try:
                print("Thread2:PushedClient Initialized")
                client = mqttClient.Client("MQTT3890778965")
                client.username_pw_set("", "")
                client.on_message=on_message2
                client.on_connect=on_connect2
                #client.on_log=on_log
                client.on_disconnect=on_disconnect
                client.connect('localhost', 1883)
                client.loop_forever()
        except KeyboardInterrupt:
                client.disconnect()
