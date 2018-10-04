
import blescan
import sys
from firebase import firebase
import bluetooth._bluetooth as bluez
import sqlite3
import datetime
from pyfcm import FCMNotification

#firebase

api_key="AAAA_4CCsfU:APA91bFyBB2Rm4JDT4rHez2lgxgmqun1AytQH0VIZ7ux_WQnhlFs6T68HniZSrr22i4m1KfaNZcSktUWbkjN-aj0sodI74NC5ifHaacMhT6v651WCOc-l3-8_wY5cFFb_iyiLCxM-oC-"
push_service = FCMNotification(api_key=api_key)

#sqlite
conn = sqlite3.connect('db/bl_log.db')


def insert_log(bl_log_data):
    sql = ''' INSERT INTO Log(CustomerName,MacAdress,InsertDate)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, bl_log_data)

def insert_anon_log(bl_log_data):
    sql = ''' INSERT INTO Log_Anonymus(Mac,InsertedDate)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, bl_log_data)




#firebase
firebase = firebase.FirebaseApplication(
    'https://beacon-5d432.firebaseio.com/', None)  # database
customers = firebase.get('/', None)  # tum macler
for k, v in customers.iteritems():
    print k, v


#bluetooth
dev_id = 0  # varsayilan bl modulu
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "ERROR BLUETOOTH MODULE NOT FOUND!"
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)
print "--------------------------------------------"
while True:
	now = datetime.datetime.now()
	returnedList = blescan.parse_events(sock, 10)
	print "--BULUNAN CIHAZLAR:"
	for beacon in returnedList:
		print beacon
		bl_data = beacon.split(',')
		mac = bl_data[0]
		insert_anon_data=(mac,now.isoformat())
		insert_anon_log(insert_anon_data)

	print "--TANIMLANAN KISILER:"
	for beacon in returnedList:
		for key, value in customers.iteritems():
    			mac_api=value.split("#");
				dv_mac = mac_api[0]
				registration_id = mac_api[1]

			if beacon.find(str(dv_mac)) != -1:
        			ad = "Adi:" + str(key)
				mac=" - Mac Adresi:" + str(dv_mac)
				print ad, mac
				insert_user_data=(str(key),str(value),now.isoformat())
				insert_log(insert_user_data)
				message_title = "Hosgeldiniz"
				message_body = "Merhaba "+str(key)+" Sıra Almak Ister misiniz?"
				result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
