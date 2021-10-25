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
        
        tempExtStop = tempExtStart = False
        tempLastBit = False
        tempMessage = ''
        
 
regs = []
dic = {}

#count = 0


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

def findResultOk(val):
        if(val):
                return 'PASS'
        else:
                return 'FAIL'

def findResultNOk(val):
        if(val):
                return 'FAIL'
        else:
                return 'PASS'

def on_connect2(client, userdata, flags, rc):
    client.subscribe('saf/')
    print("Thread3: subscribed")


def on_message2(client, userdata, message):
        try:    
                #global count
                connection.ping(reconnect=True)
                if message.topic == 'saf/':
                        #count2 += 1
                        json_data = str(message.payload.decode("utf-8","ignore"))
                        if(is_valid_json(json_data)):
                                json_obj = json.loads(json_data)
                                if(findBool(json_obj['connected'])):
                                        if(findBool(json_obj['T2-11']) and not globalBS.tempExtStart):
                                                globalBS.tempExtStart = True
                                                globalBS.tempExtStop = False
                                                try:
                                                        sql = "INSERT INTO extentries ( pir_no , status) VALUES ( %s,%s)"
                                                        val = ( str(fixedInt(json_obj['T2-15'])), True)
                                                        mycursor.execute(sql, val)

                                                        print("Entry: Started")

                                                except(error):
                                                        print("Error ::", error)
                                        if(not findBool(json_obj['T2-11']) and not globalBS.tempExtStop):
                                                globalBS.tempExtStop = True
                                                globalBS.tempExtStart = False
                                                try:
                                                        sql = "INSERT INTO extentries ( pir_no , status) VALUES ( %s,%s)"
                                                        val = ( str(fixedInt(json_obj['T2-15'])), False)
                                                        mycursor.execute(sql, val)

                                                        print("Entry: Stopped")

                                                except(error):
                                                        print("Error ::", error)

                                        if(findBool(json_obj['T2-10'])):  #or (not findBool(json_obj['T2-8']) and not findBool(json_obj['T2-9']))
                                                #New tags added from here
                                                #print("Thread2:Data Processing")
                                                dic['TestLivePres'] = fixedInt(json_obj['T2-0']) #DT-String MQTT Addr:- T2[0]
                                                dic['TestActPres'] = fixedInt(json_obj['T2-1']) #DT-String MQTT Addr:- T2[1]
                                                dic['TestSetPres'] = fixedInt(json_obj['T2-2']) #DT-String MQTT Addr:- T2[2]
                                                dic['HoseFrom'] = fixedInt(json_obj['T2-3']) #DT-String MQTT Addr:- T2[3]
                                                dic['HoseTo'] = fixedInt(json_obj['T2-4']) #DT-String MQTT Addr:- T2[4]
                                                dic['TestId'] = fixedInt(json_obj['T2-5']) #DT-String MQTT Addr:- T2[5]
                                                dic['SetTestTime'] = fixedInt(json_obj['T2-6']) #DT-String MQTT Addr:- T2[6]
                                                dic['ActTestTime'] = fixedInt(json_obj['T2-7']) #DT-String MQTT Addr:- T2[7]
                                                dic['TestResultOk'] = fixedInt(json_obj['T2-8']) #DT-String MQTT Addr:- T2[8]
                                                dic['TestResultNotOk'] = fixedInt(json_obj['T2-9']) #DT-String MQTT Addr:- T2[9]
                                                dic['TestStarted'] = fixedInt(json_obj['T2-10']) #DT-String MQTT Addr:- T2[10]
                                                dic['ExtStarted'] = fixedInt(json_obj['T2-11']) #DT-String MQTT Addr:- T2[11]
                                                dic['ExtLivePres'] = fixedInt(json_obj['T2-12']) #DT-String MQTT Addr:- T2[12]
                                                dic['ExtActPres'] = fixedInt(json_obj['T2-13']) #DT-String MQTT Addr:- T2[13]
                                                dic['ExtSetPres'] = fixedInt(json_obj['T2-14']) #DT-String MQTT Addr:- T2[14]
                                                dic['PirNo'] = fixedInt(json_obj['T2-15']) #DT-String MQTT Addr:- T2[15]
                                                dic['HoseType'] = fixedInt(json_obj['T2-16']) #DT-String MQTT Addr:- T2[16]
                                                dic['PeakPressure'] = fixedInt(json_obj['T2-17']) #DT-String MQTT Addr:- T2[17]
                                                dic['TestingTolerance'] = fixedInt(json_obj['T2-18']) #DT-String MQTT Addr:- T2[18]
                                                dic['Tolerance1'] = fixedInt(json_obj['T2-19']) #DT-String MQTT Addr:- T2[19]
                                                dic['Tolerance2'] = fixedInt(json_obj['T2-20']) #DT-String MQTT Addr:- T2[20]
                                                dic['TestingPeakPress'] = fixedInt(json_obj['T2-21']) #DT-String MQTT Addr:- T2[20]
                                                globalBS.tempLastBit = False
                                                sql3()
                                        
                                        if(not findBool(json_obj['T2-10']) and not globalBS.tempLastBit):
                                                dic['TestLivePres'] = fixedInt(json_obj['T2-0']) #DT-String MQTT Addr:- T2[0]
                                                dic['TestActPres'] = fixedInt(json_obj['T2-1']) #DT-String MQTT Addr:- T2[1]
                                                dic['TestSetPres'] = fixedInt(json_obj['T2-2']) #DT-String MQTT Addr:- T2[2]
                                                dic['HoseFrom'] = fixedInt(json_obj['T2-3']) #DT-String MQTT Addr:- T2[3]
                                                dic['HoseTo'] = fixedInt(json_obj['T2-4']) #DT-String MQTT Addr:- T2[4]
                                                dic['TestId'] = fixedInt(json_obj['T2-5']) #DT-String MQTT Addr:- T2[5]
                                                dic['SetTestTime'] = fixedInt(json_obj['T2-6']) #DT-String MQTT Addr:- T2[6]
                                                dic['ActTestTime'] = fixedInt(json_obj['T2-7']) #DT-String MQTT Addr:- T2[7]
                                                dic['TestResultOk'] = fixedInt(json_obj['T2-8']) #DT-String MQTT Addr:- T2[8]
                                                dic['TestResultNotOk'] = fixedInt(json_obj['T2-9']) #DT-String MQTT Addr:- T2[9]
                                                dic['TestStarted'] = fixedInt(json_obj['T2-10']) #DT-String MQTT Addr:- T2[10]
                                                dic['ExtStarted'] = fixedInt(json_obj['T2-11']) #DT-String MQTT Addr:- T2[11]
                                                dic['ExtLivePres'] = fixedInt(json_obj['T2-12']) #DT-String MQTT Addr:- T2[12]
                                                dic['ExtActPres'] = fixedInt(json_obj['T2-13']) #DT-String MQTT Addr:- T2[13]
                                                dic['ExtSetPres'] = fixedInt(json_obj['T2-14']) #DT-String MQTT Addr:- T2[14]
                                                dic['PirNo'] = fixedInt(json_obj['T2-15']) #DT-String MQTT Addr:- T2[15]
                                                dic['HoseType'] = fixedInt(json_obj['T2-16']) #DT-String MQTT Addr:- T2[16]
                                                dic['PeakPressure'] = fixedInt(json_obj['T2-17']) #DT-String MQTT Addr:- T2[17]
                                                dic['TestingTolerance'] = fixedInt(json_obj['T2-18']) #DT-String MQTT Addr:- T2[18]
                                                dic['Tolerance1'] = fixedInt(json_obj['T2-19']) #DT-String MQTT Addr:- T2[19]
                                                dic['Tolerance2'] = fixedInt(json_obj['T2-20']) #DT-String MQTT Addr:- T2[20]
                                                dic['TestingPeakPress'] = fixedInt(json_obj['T2-21']) #DT-String MQTT Addr:- T2[20]
                                                if (not findBool(json_obj['T2-8']) and not findBool(json_obj['T2-9'])):
                                                        globalBS.tempMessage = "Interrupt"
                                                        globalBS.tempLastBit = True
                                                elif(findBool(json_obj['T2-8']) and findBool(json_obj['T2-9'])):
                                                        globalBS.tempMessage = 'Invalid'
                                                        globalBS.tempLastBit = True
                                                elif(findBool(json_obj['T2-8'])):
                                                        globalBS.tempMessage = 'PASS'
                                                        globalBS.tempLastBit = True
                                                elif(findBool(json_obj['T2-9'])):
                                                        globalBS.tempMessage = 'FAIL'
                                                        globalBS.tempLastBit = True
                                                
                                                sql5(globalBS.tempMessage)




                                        if(findBool(json_obj['T2-11'])):
                                                #New tags added from here
                                                #print("Thread2:Data Processing")
                                                dic['TestLivePres'] = fixedInt(json_obj['T2-0']) #DT-String MQTT Addr:- T2[0]
                                                dic['TestActPres'] = fixedInt(json_obj['T2-1']) #DT-String MQTT Addr:- T2[1]
                                                dic['TestSetPres'] = fixedInt(json_obj['T2-2']) #DT-String MQTT Addr:- T2[2]
                                                dic['HoseFrom'] = fixedInt(json_obj['T2-3']) #DT-String MQTT Addr:- T2[3]
                                                dic['HoseTo'] = fixedInt(json_obj['T2-4']) #DT-String MQTT Addr:- T2[4]
                                                dic['TestId'] = fixedInt(json_obj['T2-5']) #DT-String MQTT Addr:- T2[5]
                                                dic['SetTestTime'] = fixedInt(json_obj['T2-6']) #DT-String MQTT Addr:- T2[6]
                                                dic['ActTestTime'] = fixedInt(json_obj['T2-7']) #DT-String MQTT Addr:- T2[7]
                                                dic['TestResultOk'] = fixedInt(json_obj['T2-8']) #DT-String MQTT Addr:- T2[8]
                                                dic['TestResultNotOk'] = fixedInt(json_obj['T2-9']) #DT-String MQTT Addr:- T2[9]
                                                dic['TestStarted'] = fixedInt(json_obj['T2-10']) #DT-String MQTT Addr:- T2[10]
                                                dic['ExtStarted'] = fixedInt(json_obj['T2-11']) #DT-String MQTT Addr:- T2[11]
                                                dic['ExtLivePres'] = fixedInt(json_obj['T2-12']) #DT-String MQTT Addr:- T2[12]
                                                dic['ExtActPres'] = fixedInt(json_obj['T2-13']) #DT-String MQTT Addr:- T2[13]
                                                dic['ExtSetPres'] = fixedInt(json_obj['T2-14']) #DT-String MQTT Addr:- T2[14]
                                                dic['PirNo'] = fixedInt(json_obj['T2-15']) #DT-String MQTT Addr:- T2[15]
                                                dic['HoseType'] = fixedInt(json_obj['T2-16']) #DT-String MQTT Addr:- T2[16]
                                                dic['PeakPressure'] = fixedInt(json_obj['T2-17']) #DT-String MQTT Addr:- T2[17]
                                                dic['TestingTolerance'] = fixedInt(json_obj['T2-18']) #DT-String MQTT Addr:- T2[18]
                                                dic['Tolerance1'] = fixedInt(json_obj['T2-19']) #DT-String MQTT Addr:- T2[19]
                                                dic['Tolerance2'] = fixedInt(json_obj['T2-20']) #DT-String MQTT Addr:- T2[20]
                                                dic['TestingPeakPress'] = fixedInt(json_obj['T2-21']) #DT-String MQTT Addr:- T2[20]


                                                sql4()
                                                        
                        '''
                        if(count2 >= 130): #dumping like counting
                                count2 = 0;
                                #updateLang('english')
                                print("Thread3:Data Processing")
                                json_data = str(message.payload.decode("utf-8","ignore"))
                                if(is_valid_json(json_data)):
                                        json_obj = json.loads(json_data)
                                        if(findBool(json_obj['connected'])):
                                                #print(type(json_obj))
                        '''                        
                                        
        except(error):
                print("Error ::", error)
                #continue




def on_disconnect(client, userdata, rc=0):
    print("disconnect")
    client.loop_stop()



def sql3():
    try:
        sql = "INSERT INTO testparameter ( pir_no , test_id, test_tolerance, hose_from, hose_to , set_test_time, live_pres, set_pres , act_pres , test_result_bit, peak_pressure, testing_tolerance, tolerance, result_not_ok, testing_peak_press, hose_type, tolerance2) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( str(dic['PirNo']), int(dic['TestId']), findFloat(float(dic['TestingTolerance'])),
                str(dic['HoseFrom']), str(dic['HoseTo']),
                findFloat(float(dic['SetTestTime'])), findFloat(float(dic['TestLivePres'])),
                findFloat(float(dic['TestSetPres'])), findFloat(float(dic['TestActPres'])),
                findResultOk(findBool(dic['TestResultOk'])),findFloat(float(dic['PeakPressure'])),
                findFloat(float(dic['TestingTolerance'])),findFloat(float(dic['Tolerance1'])),
                findResultNOk(findBool(dic['TestResultNotOk'])),findFloat(float(dic['TestingPeakPress'])),
                str(dic['HoseType']), findFloat(float(dic['Tolerance2'])))
        mycursor.execute(sql, val)
        
        print("Thread3: (Test) Data Dumped")
        
    except(error):
        print("Error ::", error)
        #continue


def sql4():
    try:
        sql = "INSERT INTO extparameter ( pir_no , test_id, test_tolerance, hose_from, hose_to , set_test_time, live_pres, set_pres , act_pres , test_result_bit, peak_pressure, testing_tolerance, tolerance, result_not_ok, testing_peak_press, hose_type) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( str(dic['PirNo']), int(dic['TestId']), findFloat(float(dic['TestingTolerance'])),
                str(dic['HoseFrom']), str(dic['HoseTo']),
                findFloat(float(dic['SetTestTime'])), findFloat(float(dic['ExtLivePres'])),
                findFloat(float(dic['ExtSetPres'])), findFloat(float(dic['ExtActPres'])),
                findBool(dic['TestResultOk']),findFloat(float(dic['PeakPressure'])),
                findFloat(float(dic['TestingTolerance'])),findFloat(float(dic['Tolerance2'])),
                findBool(dic['TestResultNotOk']),findFloat(float(dic['TestingPeakPress'])),
                str(dic['HoseType']))
        mycursor.execute(sql, val)
        
        print("Thread3: (Ext) Data Dumped")
        
    except(error):
        print("Error ::", error)
        #continue

def sql5(status):
    try:
        sql = "INSERT INTO testparameter ( pir_no , test_id, test_tolerance, hose_from, hose_to , set_test_time, live_pres, set_pres , act_pres , test_result_bit, peak_pressure, testing_tolerance, tolerance, result_not_ok, testing_peak_press, hose_type, tolerance2) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = ( str(dic['PirNo']), int(dic['TestId']), findFloat(float(dic['TestingTolerance'])),
                str(dic['HoseFrom']), str(dic['HoseTo']),
                findFloat(float(dic['SetTestTime'])), findFloat(float(dic['TestLivePres'])),
                findFloat(float(dic['TestSetPres'])), findFloat(float(dic['TestActPres'])),
                status,findFloat(float(dic['PeakPressure'])),
                findFloat(float(dic['TestingTolerance'])),findFloat(float(dic['Tolerance1'])),
                status,findFloat(float(dic['TestingPeakPress'])),
                str(dic['HoseType']), findFloat(float(dic['Tolerance2'])))
        mycursor.execute(sql, val)
        
        print("Thread3: (Test) Data Dumped after Stop")
        
    except(error):
        print("Error ::", error)
        #continue

def updateTable(status):
    try:
        sql = "UPDATE testparameter SET test_result_bit = %s WHERE id = LAST_INSERT_ID()"
        val = (status)
        mycursor.execute(sql, val)
        
        print("Thread3: (Test) Data Updated")
        
    except(error):
        print("Error ::", error)
        #continue


def update():
    pass




# display loop (in main thread)
if __name__ == "__main__":
        try:
                print("Thread3:PushedClient Initialized")
                client = mqttClient.Client("MQTT3890787345")
                client.username_pw_set("", "")
                client.on_message=on_message2
                client.on_connect=on_connect2
                #client.on_log=on_log
                client.on_disconnect=on_disconnect
                client.connect('localhost', 1883)
                client.loop_forever()
        except KeyboardInterrupt:
                client.disconnect()
